---
description: 端到端完成一道 LeetCode 题目：定位题目 → 生成模板 → 实现代码 → 本地/远程测试
argument-hint: <题号|中文名|slug> [语言...，默认 python，可写多个如 python go]
---

按照 `leetcode` skill 里描述的标准流程，完成这道题：

$ARGUMENTS

第一个词是题目查询（编号 / 中文名 / slug），之后的词是目标语言（python/typescript/go/rust/java 中的若干个）。**没写语言就默认做全部 5 种**，不要缩小成只做 Python。

依次执行：读题（`problems/` 下对应 README.md）→ 缺模板则用 `scripts/new_solution.py` 生成 → 实现代码（保持函数签名不变）→ `scripts/sync_and_test.py test` 做本地烟雾测试 → `scripts/sync_and_test.py remote-test` 做真正的远程判题并据结果修正代码。**不要**自动执行 submit——除非用户在这次请求里明确写了"提交"/"submit"。完成后用简短中文汇报结果。
