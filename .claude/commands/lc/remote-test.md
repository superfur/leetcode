---
description: 提交代码到 LeetCode 判题服务器做远程测试（不计入提交记录）
argument-hint: <题号|中文名|slug> [--python|--typescript|--go|--rust|--java]
---

先确认登录状态（如不确定可先跑 `python scripts/sync_and_test.py status`；未登录则提示用户运行 `/lc:login`）。

如果 `$ARGUMENTS` 里带了具体语言 flag，只跑那一个：

```bash
python scripts/sync_and_test.py remote-test $ARGUMENTS
```

**如果没带任何语言参数，默认对该题目已存在代码的每种语言都跑一次远程判题**（`solutions/<语言>/` 下有对应文件的语言）：

```bash
python scripts/sync_and_test.py remote-test $ARGUMENTS --python
python scripts/sync_and_test.py remote-test $ARGUMENTS --typescript
python scripts/sync_and_test.py remote-test $ARGUMENTS --go
python scripts/sync_and_test.py remote-test $ARGUMENTS --rust
python scripts/sync_and_test.py remote-test $ARGUMENTS --java
```

哪种语言代码文件还不存在，脚本会提示并跳过，不算错误。把每种语言的判题结果（通过/未通过、失败的具体用例、报错信息、用时和内存）汇总成中文回复。如果没通过，基于返回的错误信息定位并修正代码，然后可以再次调用本命令复测。
