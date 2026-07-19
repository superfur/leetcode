# LeetCode 解题仓库

这是一个包含多种编程语言解法的 LeetCode 解题仓库。目前包含前 1000 道题的解法。

## 项目结构

```
leetcode/
├── problems/                # 问题描述和测试用例
│   └── [problem_number]-*/  # 每个问题的独立目录
│       ├── README.md        # 问题描述
│       └── test_cases.json  # 测试用例
├── solutions/               # 解法代码
│   ├── typescript/         # TypeScript 解法
│   ├── rust/               # Rust 解法
│   ├── python/             # Python 解法
│   ├── go/                 # Go 解法
│   └── java/               # Java 解法
├── scripts/                 # 工具脚本
│   └── new_solution.py     # 快速生成题目解法
└── tests/                  # 测试文件
    ├── typescript/         # TypeScript 测试
    ├── rust/               # Rust 测试
    ├── python/             # Python 测试
    ├── go/                 # Go 测试
    └── java/               # Java 测试
```

## 快速开始

### 生成新题目解法

使用 `python3 scripts/new_solution.py` 快速生成题目解法模板：

```bash
# 通过中文名称生成 Python 解法
python3 scripts/new_solution.py "两数之和"

# 通过编号生成所有语言解法
python3 scripts/new_solution.py 1 --all

# 通过 slug 生成指定语言
python3 scripts/new_solution.py two-sum --python --typescript --go

# 强制覆盖已存在的文件
python3 scripts/new_solution.py "两数之和" -f

# 查看帮助信息
python3 scripts/new_solution.py --help
```

**支持多种查询方式：**
- 题目编号：`python3 scripts/new_solution.py 1`
- 中文名称：`python3 scripts/new_solution.py "两数之和"`
- 题目 slug：`python3 scripts/new_solution.py two-sum`

**常用选项：**
| 选项 | 说明 |
|------|------|
| `--all` | 生成所有语言的解法 |
| `-f` | 强制覆盖已存在的文件 |
| `--python` | 只生成 Python 解法 |
| `--typescript` | 只生成 TypeScript 解法 |
| `--go` | 只生成 Go 解法 |
| `--rust` | 只生成 Rust 解法 |
| `--java` | 只生成 Java 解法 |

### 运行测试

```bash
# 运行所有测试
npm test

# 监听模式运行测试
npm run test:watch
```

### 连接 LeetCode

使用 `python scripts/sync_and_test.py` 脚本连接 LeetCode，支持同步数据、远程测试和提交代码。
**默认对接 leetcode.cn**（可在命令中用 `--site leetcode.com` 切换到国际站）。

#### 0. 安装依赖

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 安装浏览器自动化所需的 chromium（用于浏览器登录）
python -m playwright install chromium
```

> 如果只打算用 cookie 方式登录，可跳过 `playwright install chromium`，但 `requests` 仍需安装。

#### 1. 登录

**方式 A：浏览器登录（推荐，支持扫码 / 短信 / 账号密码 / 第三方）**

```bash
python scripts/sync_and_test.py login
```

脚本会弹出一个浏览器窗口，你在里面用任意方式登录 leetcode.cn，登录成功后脚本自动捕获 cookie 并保存，无需手动复制。约 30 秒内未登录会提示继续等待，最长 5 分钟。

**方式 B：手动粘贴 Cookie**

```bash
python scripts/sync_and_test.py login --method cookie
```

按提示从浏览器开发者工具 (F12) → Application → Cookies 复制 `csrftoken` 和 `LEETCODE_SESSION` 的值。

> 登录其它站点：`--site leetcode.com`。

#### 2. 查看状态

```bash
# 查看登录状态
python scripts/sync_and_test.py status

# 查看提交历史
python scripts/sync_and_test.py submissions
```

#### 3. 同步数据

```bash
# 同步题目列表和解决状态
python scripts/sync_and_test.py sync
```

#### 4. 测试和提交

```bash
# 本地测试 (使用 test_cases.json)
python scripts/sync_and_test.py test "两数之和" --python

# 远程测试 (使用 LeetCode 服务器，不计入提交)
python scripts/sync_and_test.py remote-test "两数之和" --python

# 提交代码到 LeetCode (计入提交记录)
python scripts/sync_and_test.py submit "两数之和" --python
```

**支持的编程语言：**
| 语言 | `--language` 值 |
|------|----------------|
| Python | `python` |
| TypeScript | `typescript` |
| Go | `go` |
| Rust | `rust` |
| Java | `java` |

> 说明：提交/远程测试会自动拉取题目的真实 `questionId`、按站点映射语言 slug（leetcode.cn 上 `python → python3`、`go → golang`），并使用 GraphQL 查询判题结果。

## 编程语言版本要求

- TypeScript: ^4.9.0
- Rust: ^1.70.0
- Python: ^3.8
- Go: ^1.20
- Java: ^17

## 贡献指南

欢迎提交新的解法或改进现有解法。请确保：
1. 代码符合相应语言的编码规范
2. 包含必要的注释说明
3. 通过所有测试用例 