# 1731. 每位经理的下属员工数量

## 题目描述

<p>表：<code>Employees</code></p>

<pre>
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id 是这个表中具有不同值的列。
该表包含员工以及需要听取他们汇报的上级经理的 ID 的信息。 有些员工不需要向任何人汇报（reports_to 为空）。
</pre>

<p>&nbsp;</p>

<p>对于此问题，我们将至少有一个其他员工需要向他汇报的员工，视为一个经理。</p>

<p>编写一个解决方案来返回需要听取汇报的所有经理的 ID、名称、直接向该经理汇报的员工人数，以及这些员工的平均年龄，其中该平均年龄需要四舍五入到最接近的整数。</p>

<p>返回的结果集需要按照&nbsp;<code>employee_id</code> 进行排序。</p>

<p>结果的格式如下：</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Employees 表：
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
<strong>输出：</strong>
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
<strong>解释：
</strong>Hercy 有两个需要向他汇报的员工, 他们是 Alice and Bob. 他们的平均年龄是 (41+36)/2 = 38.5, 四舍五入的结果是 39.
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong> 
Employees 表：
+-------------+---------+------------+-----+ 
| employee_id | name &nbsp; &nbsp;| reports_to | age |
|-------------|---------|------------|-----|
| 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Michael | null &nbsp; &nbsp; &nbsp; | 45 &nbsp;|
| 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Alice &nbsp; | 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 38 &nbsp;|
| 3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Bob &nbsp; &nbsp; | 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 42 &nbsp;|
| 4 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Charlie | 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 34 &nbsp;|
| 5 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | David &nbsp; | 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 40 &nbsp;|
| 6 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Eve &nbsp; &nbsp; | 3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;| 37 &nbsp;|
| 7 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Frank &nbsp; | null &nbsp; &nbsp; &nbsp; | 50 &nbsp;|
| 8 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Grace &nbsp; | null &nbsp; &nbsp; &nbsp; | 48 &nbsp;|
+-------------+---------+------------+-----+ 
<strong>输出：</strong> 
+-------------+---------+---------------+-------------+
| employee_id | name &nbsp; &nbsp;| reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Michael | 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 40 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
| 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Alice &nbsp; | 2 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 37 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
| 3 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Bob &nbsp; &nbsp; | 1 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | 37 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;|
+-------------+---------+---------------+-------------+</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Employees":["employee_id","name","reports_to","age"]},"rows":{"Employees":[[9,"Hercy",null,43],[6,"Alice",9,41],[4,"Bob",9,36],[2,"Winston",null,37]]}}
{"headers":{"Employees":["employee_id","name","reports_to","age"]},"rows":{"Employees":[[1,"Michael",null,45],[2,"Alice",1,38],[3,"Bob",1,42],[4,"Charlie",2,34],[5,"David",2,40],[6,"Eve",3,37],[7,"Frank",null,50],[8,"Grace",null,48]]}}
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

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

