Agent eval on 20 held-out IR questions (agent `claude-sonnet-5-5`, judge `claude-opus-5-5`), evidence-only tools, record locations stripped from questions.

| Metric | Value |
|---|---|
| Citation accuracy, section/schedule level (n=20) | 90.0% |
| Citation accuracy, exhibit level (cites an exhibit the utility cited) | 95.0% |
| Judge: correct | 10.0% |
| Judge: correct or partially correct | 95.0% |
| Verdicts (correct / partial / incorrect / abstained / error) | 2 / 17 / 0 / 1 / 0 |
| Citations to pages the agent never saw | 0.0% |
| Median tool calls / seconds per question | 8 / 35.2 |
