Agent eval on 20 held-out IR questions (agent `claude-sonnet-5-5`, judge `claude-opus-5-5`), evidence-only tools, record locations stripped from questions.

| Metric | Value |
|---|---|
| Citation accuracy, section/schedule level (n=20) | 75.0% |
| Citation accuracy, exhibit level (cites an exhibit the utility cited) | 90.0% |
| Judge: correct | 35.0% |
| Judge: correct or partially correct | 75.0% |
| Verdicts (correct / partial / incorrect / abstained / error) | 7 / 8 / 1 / 4 / 0 |
| Citations to pages the agent never saw | 0.0% |
| Median tool calls / seconds per question | 6 / 26.7 |
