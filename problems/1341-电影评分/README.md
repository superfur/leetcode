# 1341. 电影评分

## 题目描述

<p>表：<code>Movies</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id 是这个表的主键(具有唯一值的列)。
title 是电影的名字。
</pre>

<p>表：<code>Users</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id 是表的主键(具有唯一值的列)。
'name' 列具有唯一值。</pre>

<p>表：<code>MovieRating</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) 是这个表的主键(具有唯一值的列的组合)。
这个表包含用户在其评论中对电影的评分 rating 。
created_at 是用户的点评日期。 
</pre>

<p>&nbsp;</p>

<p>请你编写一个解决方案：</p>

<ul>
	<li>查找评论电影数量最多的用户名。如果出现平局，返回字典序较小的用户名。</li>
	<li>查找在 <code>February 2020</code><strong> 平均评分最高</strong> 的电影名称。如果出现平局，返回字典序较小的电影名称。</li>
</ul>

<p><strong>字典序</strong> ，即按字母在字典中出现顺序对字符串排序，字典序较小则意味着排序靠前。</p>

<p>返回结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Movies 表：
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users 表：
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating 表：
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
<strong>输出：</strong>
Result 表：
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
<strong>解释：</strong>
Daniel 和 Monica 都点评了 3 部电影（"Avengers", "Frozen 2" 和 "Joker"） 但是 Daniel 字典序比较小。
Frozen 2 和 Joker 在 2 月的评分都是 3.5，但是 Frozen 2 的字典序比较小。
</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers": {"Movies": ["movie_id", "title"], "Users": ["user_id", "name"], "MovieRating": ["movie_id", "user_id", "rating", "created_at"]}, "rows": {"Movies": [[1, "Avengers"], [2, "Frozen 2"], [3, "Joker"]], "Users": [[1, "Daniel"], [2, "Monica"], [3, "Maria"], [4, "James"]], "MovieRating": [[1, 1, 3, "2020-01-12"], [1, 2, 4, "2020-02-11"], [1, 3, 2, "2020-02-12"], [1, 4, 1, "2020-01-01"], [2, 1, 5, "2020-02-17"], [2, 2, 2, "2020-02-01"], [2, 3, 2, "2020-03-01"], [3, 1, 3, "2020-02-22"], [3, 2, 4, "2020-02-25"]]}}
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

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

