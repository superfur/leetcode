---
description: 一键 git add + commit + push（自动识别本次新增/修改的 LeetCode 题解并生成规范的 commit message）
argument-hint: [自定义 commit message，可选]
---

用户已经通过调用这个命令明确要求提交并推送，不需要再额外确认——直接执行，不用像 `/lc:submit` 那样先问一遍。

1. 运行 `git status --short` 看清楚有哪些改动（staged / unstaged / untracked）。如果什么都没有，直说"没有改动可提交"，不要创建空提交。

2. **分组**：
   - 如果改动集中在 `solutions/<语言>/<编号>*` 这种题解文件（可能有多个不同题号混在一起），按题号分组，**每个题号单独一个 commit**，消息格式严格照抄仓库现有风格：
     ```
     feat: 完成 <编号> 号题目<题目中文名>（去掉编号前缀，从 problems/<编号>-<中文名>/ 目录名取）(Python/TypeScript/Go/Rust/Java，按实际涉及的语言列出)

     Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
     ```
     语言列表只列这次改动里实际出现的语言，不要照抄全部 5 个如果其中缺了某个。
   - 如果改动是非题解文件（配置、文档、脚本等），用一条中文 commit message 概括这次改动的动机（why），同样带上 `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` 尾注。如果 `$ARGUMENTS` 里用户给了自定义消息，就用那条（仍要加上 Co-Authored-By 尾注），不要自己编。
   - 题解改动和非题解改动混在一起时，分开成不同的 commit，不要揉进一条。

3. 用 `git add <具体文件路径>`（不要用 `git add -A`/`git add .`，避免误把不相关的文件带进去）逐组暂存并 `git commit`。

4. 全部 commit 完成后，跑一次 `git push origin main`（或当前分支对应的远程分支）。

5. 用简短中文汇报：提交了几个 commit、每个的题号/摘要、push 是否成功（把 commit hash 带出来）。如果 push 失败（比如远程有新提交），说明原因，不要自动 force push 或者其他破坏性操作，问用户想怎么处理。
