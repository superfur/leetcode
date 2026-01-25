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

使用 `python3 scripts/sync_and_test.py` 脚本连接 LeetCode，支持同步数据、远程测试和提交代码。

#### 1. 登录配置

```bash
# 配置 leetcode.com 登录信息
python3 scripts/sync_and_test.py login --site leetcode.com
```

按照提示从浏览器复制 `csrftoken` 和 `LEETCODE_SESSION`：

1. 登录 leetcode.com
2. 打开开发者工具 (F12) -> Application/存储
3. 复制 Cookies 中的 `csrftoken` 和 `LEETCODE_SESSION`

#### 2. 查看状态

```bash
# 查看登录状态
python3 scripts/sync_and_test.py status

# 查看提交历史
python3 scripts/sync_and_test.py submissions
```

#### 3. 同步数据

```bash
# 同步题目列表和解决状态
python3 scripts/sync_and_test.py sync
```

#### 4. 测试和提交

```bash
# 本地测试 (使用 test_cases.json)
python3 scripts/sync_and_test.py test "两数之和" --python

# 远程测试 (使用 LeetCode 服务器)
python3 scripts/sync_and_test.py remote-test "两数之和" --python

# 提交代码到 LeetCode
python3 scripts/sync_and_test.py submit "两数之和" --python
```

**支持的编程语言：**
| 语言 | `--language` 值 |
|------|----------------|
| Python | `python` |
| TypeScript | `typescript` |
| Go | `go` |
| Rust | `rust` |
| Java | `java` |

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