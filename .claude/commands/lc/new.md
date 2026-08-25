---
description: 生成 LeetCode 题目的解法模板文件（Python/TypeScript/Go/Rust/Java）
argument-hint: <题号|中文名|slug> [--all | --python --typescript --go --rust --java] [-f]
---

如果 `$ARGUMENTS` 里已经带了语言 flag（`--python`/`--typescript`/`--go`/`--rust`/`--java`/`--all`），原样使用；**如果没带任何语言 flag，默认补上 `--all`（生成全部 5 种语言）**，而不是让脚本退回到只生成 Python：

```bash
python3 scripts/new_solution.py $ARGUMENTS --all
```

（若 `$ARGUMENTS` 已包含语言 flag 则不要重复追加 `--all`，直接原样运行。）

然后用中文简要汇报生成/跳过了哪些文件。如果脚本提示文件已存在而用户没有传 `-f`，不要自动补上 `-f` 重跑——先询问用户是否真的要覆盖已有解法代码。
