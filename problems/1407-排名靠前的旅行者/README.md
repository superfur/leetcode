# 1407. 排名靠前的旅行者

## 题目描述

<p>表：<code>Users</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id 是该表中具有唯一值的列。
name 是用户名字。</pre>

<p>&nbsp;</p>

<p>表：<code>Rides</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id 是该表中具有唯一值的列。
user_id 是本次行程的用户的 id, 而该用户此次行程距离为 distance 。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，报告每个用户的旅行距离。</p>

<p>返回的结果表单，以&nbsp;<code>travelled_distance</code>&nbsp;<strong>降序排列</strong> ，如果有两个或者更多的用户旅行了相同的距离,&nbsp;那么再以&nbsp;<code>name</code>&nbsp;<strong>升序排列</strong> 。</p>

<p>返回结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Users 表：
+------+-----------+
| id   | name      |
+------+-----------+
| 1    | Alice     |
| 2    | Bob       |
| 3    | Alex      |
| 4    | Donald    |
| 7    | Lee       |
| 13   | Jonathan  |
| 19   | Elvis     |
+------+-----------+

Rides 表：
+------+----------+----------+
| id   | user_id  | distance |
+------+----------+----------+
| 1    | 1        | 120      |
| 2    | 2        | 317      |
| 3    | 3        | 222      |
| 4    | 7        | 100      |
| 5    | 13       | 312      |
| 6    | 19       | 50       |
| 7    | 7        | 120      |
| 8    | 19       | 400      |
| 9    | 7        | 230      |
+------+----------+----------+
<strong>输出：</strong>
+----------+--------------------+
| name     | travelled_distance |
+----------+--------------------+
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
+----------+--------------------+
<strong>解释：</strong>
Elvis 和 Lee 旅行了 450 英里，Elvis 是排名靠前的旅行者，因为他的名字在字母表上的排序比 Lee 更小。
Bob, Jonathan, Alex 和 Alice 只有一次行程，我们只按此次行程的全部距离对他们排序。
Donald 没有任何行程, 他的旅行距离为 0。
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Users":["id","name"],"Rides":["id","user_id","distance"]},"rows":{"Users":[[1,"Alice"],[2,"Bob"],[3,"Alex"],[4,"Donald"],[7,"Lee"],[13,"Jonathan"],[19,"Elvis"]],"Rides":[[1,1,120],[2,2,317],[3,3,222],[4,7,100],[5,13,312],[6,19,50],[7,7,120],[8,19,400],[9,7,230]]}}
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

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

