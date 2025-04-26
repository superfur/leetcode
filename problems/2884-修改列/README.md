# 2884. 修改列

## 题目描述

<pre>
DataFrame <code>employees</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| salary      | int    |
+-------------+--------+
</pre>

<p>一家公司决定增加员工的薪水。</p>

<p>编写一个解决方案，将每个员工的薪水乘以2来 <strong>修改</strong>&nbsp;<code>salary</code>&nbsp;列。</p>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><b>示例 1:</b></p>

<pre>
<strong>输入：
</strong>DataFrame employees
+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 19666  |
| Piper   | 74754  |
| Mia     | 62509  |
| Ulysses | 54866  |
+---------+--------+
<strong>输出：
</strong>+---------+--------+
| name    | salary |
+---------+--------+
| Jack    | 39332  |
| Piper   | 149508 |
| Mia     | 125018 |
| Ulysses | 109732 |
+---------+--------+
<strong>解释：
</strong>每个人的薪水都被加倍。</pre>


## 难度

Easy

## 提示

1. Considering multiplying each salary value by 2, using a simple assignment operation. The calculation of the value is done column-wise.

## 示例

```
{"headers":{"employees":["name","salary"]},"rows":{"employees":[["Jack",19666],["Piper",74754],["Mia",62509],["Ulysses",54866]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    
```

