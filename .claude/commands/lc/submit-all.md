---
description: 一条命令把同一题的多种语言解法一次性提交（脚本自带确认）
argument-hint: <题号> [--langs python,go,...] [--site leetcode.com|leetcode.cn] [--wait 秒]
---

⚠️ 这会把该题目前所有指定语言的解法都提交一次，记入 LeetCode 提交历史。运行：

```bash
python scripts/submit_all.py $ARGUMENTS
```

脚本本身会有交互确认——除非用户明确要求跳过确认，否则不要额外加 `--yes`。运行结束后把每种语言的判题结果汇总成一个简短的中文列表回复用户（哪些 Accepted，哪些失败及原因）。
