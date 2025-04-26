# 1729. 求关注者的数量

## 题目描述

<p>表：&nbsp;<code>Followers</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) 是这个表的主键（具有唯一值的列的组合）。
该表包含一个关注关系中关注者和用户的编号，其中关注者关注用户。</pre>

<p>&nbsp;</p>

<p>编写解决方案，对于每一个用户，返回该用户的关注者数量。</p>

<p>按&nbsp;<code>user_id</code>&nbsp;的顺序返回结果表。</p>

<p>查询结果的格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Followers 表：
+---------+-------------+
| user_id | follower_id |
+---------+-------------+
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
+---------+-------------+
<strong>输出：</strong>
+---------+----------------+
| user_id | followers_count|
+---------+----------------+
| 0       | 1              |
| 1       | 1              |
| 2       | 2              |
+---------+----------------+
<strong>解释：</strong>
0 的关注者有 {1}
1 的关注者有 {0}
2 的关注者有 {0,1}</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Followers":["user_id","follower_id"]},"rows":{"Followers":[["0","1"],["1","0"],["2","0"],["2","1"]]}}
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

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

