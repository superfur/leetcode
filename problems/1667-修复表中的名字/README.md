# 1667. 修复表中的名字

## 题目描述

<p>表： <code>Users</code></p>

<pre>
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id 是该表的主键(具有唯一值的列)。
该表包含用户的 ID 和名字。名字仅由小写和大写字符组成。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，修复名字，使得只有第一个字符是大写的，其余都是小写的。</p>

<p>返回按 <code>user_id</code> 排序的结果表。</p>

<p>返回结果格式示例如下。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Users table:
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | aLice |
| 2       | bOB   |
+---------+-------+
<strong>输出：</strong>
+---------+-------+
| user_id | name  |
+---------+-------+
| 1       | Alice |
| 2       | Bob   |
+---------+-------+</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Users":["user_id","name"]},"rows":{"Users":[[1,"aLice"],[2,"bOB"]]}}
```

## 示例代码

### MySQL

```mysql
# Write your MySQL query statement below
```

### MS SQL Server

```mssql
/* Write your T-SQL query statement below */
```

### Oracle

```oraclesql
/* Write your PL/SQL query statement below */
```

### Pandas

```pythondata
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

