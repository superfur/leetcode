# 1965. 丢失信息的雇员

## 题目描述

<p>表: <code>Employees</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id 是该表中具有唯一值的列。
每一行表示雇员的 id 和他的姓名。
</pre>

<p>表: <code>Salaries</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id 是该表中具有唯一值的列。
每一行表示雇员的 id 和他的薪水。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，找到所有 <strong>丢失信息</strong> 的雇员 id。当满足下面一个条件时，就被认为是雇员的信息丢失：</p>

<ul>
	<li>雇员的 <strong>姓名</strong> 丢失了，或者</li>
	<li>雇员的 <strong>薪水信息</strong> 丢失了</li>
</ul>

<p>返回这些雇员的 id &nbsp;<code>employee_id</code>&nbsp;，&nbsp;<strong>从小到大排序&nbsp;</strong>。</p>

<p>查询结果格式如下面的例子所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Employees table:
+-------------+----------+
| employee_id | name     |
+-------------+----------+
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
+-------------+----------+
Salaries table:
+-------------+--------+
| employee_id | salary |
+-------------+--------+
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
+-------------+--------+
<strong>输出：</strong>
+-------------+
| employee_id |
+-------------+
| 1           |
| 2           |
+-------------+
<strong>解释：</strong>
雇员 1，2，4，5 都在这个公司工作。
1 号雇员的姓名丢失了。
2 号雇员的薪水信息丢失了。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Employees":["employee_id","name"],"Salaries":["employee_id","salary"]},"rows":{"Employees":[[2,"Crew"],[4,"Haven"],[5,"Kristian"]],"Salaries":[[5,76071],[1,22517],[4,63539]]}}
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

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

