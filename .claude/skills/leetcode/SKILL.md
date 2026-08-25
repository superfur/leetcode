---
name: leetcode
description: 在本仓库中端到端完成一道 LeetCode 题目——定位题目、生成多语言模板、实现代码、本地/远程测试，以及在用户明确要求时提交到 LeetCode。当用户说"帮我做/刷/写一下 LeetCode 第 N 题"、"实现 XX 题的 Go/Python 解法"、"测试这道题"、"提交这道题"等时触发。
---

# LeetCode 刷题工作流

本仓库结构：`problems/<编号>-<中文名>/`（题目描述 README.md + test_cases.json），
`solutions/<语言>/<编号>*.<ext>`（解法代码，语言为 python/typescript/go/rust/java），
`scripts/` 下有三个核心脚本，均通过 `python3`/`python` 调用（无需额外包装，直接用 Bash 运行）：

- `scripts/new_solution.py` — 生成解法模板
- `scripts/sync_and_test.py` — 登录/同步/本地测试/远程测试/提交（子命令：login/status/sync/test/remote-test/submit/submissions）
- `scripts/submit_all.py` — 单题一次性按多语言提交

对应的快捷命令：`/lc:new` `/lc:solve` `/lc:test` `/lc:remote-test` `/lc:submit` `/lc:submit-all` `/lc:sync` `/lc:status` `/lc:login` `/lc:submissions`。

## 做一道题目的标准步骤

1. **解析请求**：从用户描述中提取题目查询词（编号 / 中文名 / slug 均可）和目标语言。**未指定语言时默认做全部 5 种**（python/typescript/go/rust/java），不要缩小成只做 Python；用户明确只提到某一两种语言时才只做那些。

2. **定位题目**：题目已经在本地 `problems/` 目录下（无需先联网同步）。用 `ls problems/ | grep <编号或关键词>` 或直接按编号前缀 `<编号 4 位补零>-` 查找对应文件夹，然后完整读取该文件夹下的 `README.md`（题目描述、示例、约束）。这一步必须做，不要凭记忆猜题目要求。

3. **生成模板（如缺失）**：检查 `solutions/<语言>/<编号>*.<ext>` 是否已存在。缺哪些语言就一次性生成：
   ```
   python3 scripts/new_solution.py "<query>" --all
   ```
   （若只做部分语言，把 `--all` 换成对应的 `--python`/`--typescript`/...）。**不要**在文件已存在时自动加 `-f` 强制覆盖——那会覆盖用户已有的解法代码，除非用户明确要求重写。

4. **实现代码**：对每种目标语言，编辑生成的解法文件，保持函数/类签名不变（LeetCode 判题是按签名调用的），只根据第 2 步读到的题目描述和约束实现逻辑，不要臆造签名或输入格式。同一道题在不同语言里的算法思路应该一致。

5. **本地测试（弱校验）**：对每种目标语言各跑一次：
   ```
   python scripts/sync_and_test.py test "<query>" --<language>
   ```
   注意：该本地测试只是"能否运行"的烟雾测试（不会真正灌入 test_cases.json 里的输入），**不能**当作正确性证明。如果是 TypeScript 且 `tests/typescript/<编号>-*.test.ts` 存在对应用例，可用 `npx jest <关键词>` 做更强的本地校验，但先确认该测试文件里的 import 路径与当前 `solutions/typescript/` 下的实际文件路径一致（仓库里部分旧测试文件路径已经过时，import 失败不代表解法错）。

6. **远程判题（不计入提交记录）**：确认已登录（`python scripts/sync_and_test.py status`，未登录则提示用户先跑 `/lc:login`），然后对每种目标语言各跑一次：
   ```
   python scripts/sync_and_test.py remote-test "<query>" --<language>
   ```
   这是判断解法是否真正正确的权威依据。哪种语言失败了，就根据返回的错误用例/报错信息定位问题、修改那种语言的代码、重新 remote-test，直至通过或已尝试合理次数后向用户反馈卡点——各语言互不影响，一种语言的失败不阻塞其他语言。

7. **提交**：**只有用户明确要求"提交"/"submit"时**才执行，因为这会记入 LeetCode 的提交历史（不可撤销）。提交前如果题目不明确，先跟用户确认。只提交某一种语言用 `python scripts/sync_and_test.py submit "<query>" --<language>`；**未指定语言则默认对该题已有代码的全部语言各提交一次**，直接用 `python scripts/submit_all.py "<query>"`（内部默认就是全部 5 种语言，也可用 `--langs` 收窄）。该脚本自带交互确认，除非用户要求跳过否则不要加 `--yes`。

8. 全部完成后用简短中文总结：做了哪道题、哪些语言、remote-test/submit 的结果（通过/未通过、用时和内存百分位等）。
