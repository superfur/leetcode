---
description: 提交代码到 LeetCode（会计入提交记录，请谨慎）
argument-hint: <题号|中文名|slug> [--python|--typescript|--go|--rust|--java]
---

⚠️ 这个操作会被记录进用户的 LeetCode 提交历史，不可撤销。如果 `$ARGUMENTS` 里题目不明确，先跟用户确认清楚要提交哪道题。

- 如果 `$ARGUMENTS` 里带了具体语言 flag，只提交那一种：
  ```bash
  python scripts/sync_and_test.py submit $ARGUMENTS
  ```
- **如果没带任何语言参数，默认对该题目已有代码的全部语言各提交一次**——直接委托给 `submit_all.py`（它内部默认就是 python/typescript/go/rust/java 全部 5 种）：
  ```bash
  python scripts/submit_all.py $ARGUMENTS
  ```
  这个脚本自带交互确认，除非用户明确要求跳过，否则不要额外加 `--yes`。

执行后如实汇报每种语言的判题结果（Accepted / Wrong Answer / TLE / 编译错误等，以及用时和内存百分位）。如果某个语言失败，把失败原因讲清楚，不要自动重复提交——问用户是想先修代码用 `/lc:remote-test` 验证过再提交，还是直接重试。
