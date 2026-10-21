CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS documents (
    doc_id         text PRIMARY KEY,          -- 'rds-<uri>' or 'ho-<slug>'
    source         text NOT NULL,             -- 'rds.oeb.ca' | 'hydroone.com'
    case_number    text NOT NULL,
    source_url     text NOT NULL,
    record_number  text,
    title          text NOT NULL,
    exhibit        text,                      -- normalized, e.g. '2B', 'B3'
    applicant      text,
    doc_type       text,                      -- RDS SIDocumentType
    doc_kind       text NOT NULL,             -- evidence | ir_response | ...
    date_received  date,
    ext            text,
    listed_size_bytes bigint,                 -- size the source reports; download must match
    size_bytes     bigint,                    -- bytes actually downloaded
    local_path     text,
    sha256         text,
    n_pages        int,
    status         text NOT NULL DEFAULT 'listed',
    error          text,
    timings        jsonb NOT NULL DEFAULT '{}'::jsonb,
    updated_at     timestamptz NOT NULL DEFAULT now()
);
CREATE INDEX IF NOT EXISTS documents_case_idx ON documents (case_number);
ALTER TABLE documents ADD COLUMN IF NOT EXISTS listed_size_bytes bigint;

CREATE TABLE IF NOT EXISTS pages (
    doc_id       text NOT NULL REFERENCES documents ON DELETE CASCADE,
    page_no      int  NOT NULL,               -- 1-based, matches PDF viewer #page=
    text         text NOT NULL,
    exhibit_ref  text,                        -- header ref, e.g. 'Exhibit 2B, Section E5'
    PRIMARY KEY (doc_id, page_no)
);

CREATE TABLE IF NOT EXISTS extracted_tables (
    table_id   bigserial PRIMARY KEY,
    doc_id     text NOT NULL REFERENCES documents ON DELETE CASCADE,
    page_no    int  NOT NULL,
    table_idx  int  NOT NULL,
    header     jsonb NOT NULL,
    rows       jsonb NOT NULL,
    UNIQUE (doc_id, page_no, table_idx)
);

CREATE TABLE IF NOT EXISTS table_cells (
    table_id    bigint NOT NULL REFERENCES extracted_tables ON DELETE CASCADE,
    row_idx     int NOT NULL,
    col_idx     int NOT NULL,
    col_name    text,
    value_text  text,
    value_num   double precision,
    PRIMARY KEY (table_id, row_idx, col_idx)
);

CREATE TABLE IF NOT EXISTS chunks (
    chunk_id     bigserial PRIMARY KEY,
    doc_id       text NOT NULL REFERENCES documents ON DELETE CASCADE,
    case_number  text NOT NULL,
    exhibit      text,
    doc_kind     text NOT NULL,
    page_start   int  NOT NULL,
    page_end     int  NOT NULL,
    heading      text,
    text         text NOT NULL,
    n_tokens     int  NOT NULL,
    tsv          tsvector GENERATED ALWAYS AS (
                   setweight(to_tsvector('english', coalesce(heading, '')), 'A') ||
                   setweight(to_tsvector('english', text), 'B')) STORED,
    embedding    vector(384)
);
-- Document frequency per lexeme, for IDF-style filtering of full-text queries.
-- Refreshed at the end of each ingestion workflow (oeb.pipeline.refresh_search_stats).
CREATE MATERIALIZED VIEW IF NOT EXISTS lexeme_df AS
    SELECT word, ndoc FROM ts_stat('SELECT tsv FROM chunks') WITH NO DATA;
CREATE UNIQUE INDEX IF NOT EXISTS lexeme_df_word_idx ON lexeme_df (word);

-- Read-only surface for the agent's query_table tool
CREATE OR REPLACE VIEW agent_tables AS
    SELECT t.table_id, t.doc_id, d.case_number, d.exhibit, d.doc_kind, d.title, t.page_no, t.header, t.rows
    FROM extracted_tables t JOIN documents d USING (doc_id);
CREATE OR REPLACE VIEW agent_table_cells AS
    SELECT c.table_id, t.doc_id, d.case_number, d.exhibit, d.doc_kind, t.page_no, c.row_idx, c.col_idx,
           c.col_name, c.value_text, c.value_num
    FROM table_cells c JOIN extracted_tables t USING (table_id) JOIN documents d USING (doc_id);

-- The agent's SQL runs as a role that can only read these two views (plus temp objects).
DO $$ BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'agent_ro') THEN
        CREATE ROLE agent_ro LOGIN PASSWORD 'agent_ro';
    END IF;
END $$;
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM agent_ro;
GRANT USAGE ON SCHEMA public TO agent_ro;
GRANT SELECT ON agent_tables, agent_table_cells TO agent_ro;

-- Utilities re-file updated exhibits, so many chunks are verbatim copies (16% in EB-2023-0195);
-- retrievers collapse them on this hash and keep the most recently filed copy.
ALTER TABLE chunks ADD COLUMN IF NOT EXISTS text_hash text
    GENERATED ALWAYS AS (md5(regexp_replace(text, '\s+', ' ', 'g'))) STORED;

CREATE INDEX IF NOT EXISTS chunks_doc_idx ON chunks (doc_id);
CREATE INDEX IF NOT EXISTS chunks_tsv_idx ON chunks USING gin (tsv);
CREATE INDEX IF NOT EXISTS chunks_emb_idx ON chunks USING hnsw (embedding vector_cosine_ops);
