---
description: 本地测试题目代码（弱校验，只确认代码能跑，不代表通过）
argument-hint: <题号|中文名|slug> [--python|--typescript|--go|--rust|--java]
---

如果 `$ARGUMENTS` 里带了 `--python`/`--typescript`/`--go`/`--rust`/`--java` 或 `--language`，只跑那一个：

```bash
python scripts/sync_and_test.py test $ARGUMENTS
```

**如果没带任何语言参数，默认对全部 5 种语言各跑一次**（哪个语言还没生成代码文件，脚本会提示"代码文件不存在"，跳过即可，不算错误）：

```bash
python scripts/sync_and_test.py test $ARGUMENTS --python
python scripts/sync_and_test.py test $ARGUMENTS --typescript
python scripts/sync_and_test.py test $ARGUMENTS --go
python scripts/sync_and_test.py test $ARGUMENTS --rust
python scripts/sync_and_test.py test $ARGUMENTS --java
```

汇总每种语言的结果用中文回复，并提醒用户：这只是本地烟雾测试（不会真正灌入 test_cases.json 的输入做比对），要验证正确性请用 `/lc:remote-test`。
