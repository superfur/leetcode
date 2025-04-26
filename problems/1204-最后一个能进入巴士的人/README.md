# 1204. 最后一个能进入巴士的人

## 题目描述

<p>表: <code>Queue</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id 是这个表具有唯一值的列。
该表展示了所有候车乘客的信息。
表中 person_id 和 turn 列将包含从 1 到 n 的所有数字，其中 n 是表中的行数。
turn 决定了候车乘客上巴士的顺序，其中 turn=1 表示第一个上巴士，turn=n 表示最后一个上巴士。
weight 表示候车乘客的体重，以千克为单位。
</pre>

<p>&nbsp;</p>

<p>有一队乘客在等着上巴士。然而，巴士有<code>1000</code>&nbsp; <strong>千克</strong> 的重量限制，所以其中一部分乘客可能无法上巴士。</p>

<p>编写解决方案找出 <strong>最后一个</strong> 上巴士且不超过重量限制的乘客，并报告 <code>person_name</code> 。题目测试用例确保顺位第一的人可以上巴士且不会超重。</p>

<p>返回结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Queue 表
+-----------+-------------+--------+------+
| person_id | person_name | weight | turn |
+-----------+-------------+--------+------+
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
+-----------+-------------+--------+------+
<strong>输出：</strong>
+-------------+
| person_name |
+-------------+
| John Cena   |
+-------------+
<strong>解释：</strong>
为了简化，Queue 表按 turn 列由小到大排序。
+------+----+-----------+--------+--------------+
| Turn | ID | Name      | Weight | Total Weight |
+------+----+-----------+--------+--------------+
| 1    | 5  | Alice     | 250    | 250          |
| 2    | 3  | Alex      | 350    | 600          |
| 3    | 6  | John Cena | 400    | 1000         | (最后一个上巴士)
| 4    | 2  | Marie     | 200    | 1200         | (无法上巴士)
| 5    | 4  | Bob       | 175    | ___          |
| 6    | 1  | Winston   | 500    | ___          |
+------+----+-----------+--------+--------------+</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Queue":["person_id","person_name","weight","turn"]},"rows":{"Queue":[[5,"Alice",250,1],[4,"Bob",175,5],[3,"Alex",350,2],[6,"John Cena",400,3],[1,"Winston",500,6],[2,"Marie",200,4]]}}
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

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

