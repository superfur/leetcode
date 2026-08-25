---
description: 登录 LeetCode（浏览器登录或手动粘贴 Cookie）
argument-hint: [--method browser|cookie] [--site leetcode.com|leetcode.cn]
---

运行：

```bash
python scripts/sync_and_test.py login $ARGUMENTS
```

这一步是交互式的：
- 浏览器方式会弹出一个浏览器窗口，登录动作（扫码/短信/账号密码/第三方登录）需要用户自己在那个窗口里完成，不要代替用户输入账号密码。
- Cookie 方式脚本会在终端提示输入 `csrftoken` 和 `LEETCODE_SESSION`，提醒用户直接在终端粘贴，不要把这些值贴到聊天里。

命令跑完后汇报登录是否成功即可。
