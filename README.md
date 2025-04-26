# LeetCode 解题仓库

这是一个包含多种编程语言解法的 LeetCode 解题仓库。目前包含前 1000 道题的解法。

## 项目结构

```
leetcode/
├── problems/                # 问题描述和测试用例
│   └── [problem_number]/    # 每个问题的独立目录
│       ├── description.md   # 问题描述
│       └── test_cases.json  # 测试用例
├── solutions/               # 解法代码
│   ├── typescript/         # TypeScript 解法
│   ├── rust/               # Rust 解法
│   ├── python/             # Python 解法
│   ├── go/                 # Go 解法
│   └── java/               # Java 解法
└── tests/                  # 测试文件
    ├── typescript/         # TypeScript 测试
    ├── rust/               # Rust 测试
    ├── python/             # Python 测试
    ├── go/                 # Go 测试
    └── java/               # Java 测试
```

## 使用方法

1. 选择编程语言
2. 进入对应语言的解法目录
3. 运行测试

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