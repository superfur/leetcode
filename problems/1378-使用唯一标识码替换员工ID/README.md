# 1378. 使用唯一标识码替换员工ID

## 题目描述

<p><code>Employees</code> 表：</p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
在 SQL 中，id 是这张表的主键。
这张表的每一行分别代表了某公司其中一位员工的名字和 ID 。
</pre>

<p>&nbsp;</p>

<p><code>EmployeeUNI</code>&nbsp;表：</p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
在 SQL 中，(id, unique_id) 是这张表的主键。
这张表的每一行包含了该公司某位员工的 ID 和他的唯一标识码（unique ID）。
</pre>

<p>&nbsp;</p>

<p>展示每位用户的<strong> 唯一标识码（unique ID ）</strong>；如果某位员工没有唯一标识码，使用 null 填充即可。</p>

<p>你可以以<strong> 任意</strong> 顺序返回结果表。</p>

<p>返回结果的格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<code><strong>输入：</strong>
Employees</code> 表:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
<code>EmployeeUNI</code> 表:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
<strong>输出：</strong>
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
<strong>解释：</strong>
Alice and Bob 没有唯一标识码, 因此我们使用 null 替代。
Meir 的唯一标识码是 2 。
Winston 的唯一标识码是 3 。
Jonathan 唯一标识码是 1 。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Employees":["id","name"],"EmployeeUNI":["id","unique_id"]},"rows":{"Employees":[[1,"Alice"],[7,"Bob"],[11,"Meir"],[90,"Winston"],[3,"Jonathan"]],"EmployeeUNI":[[3,1],[11,2],[90,3]]}}
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

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

