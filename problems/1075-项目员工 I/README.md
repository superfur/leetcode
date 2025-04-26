# 1075. 项目员工 I

## 题目描述

<p>项目表&nbsp;<code>Project</code>：&nbsp;</p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| project_id  | int     |
| employee_id | int     |
+-------------+---------+
主键为 (project_id, employee_id)。
employee_id 是员工表 <code>Employee 表的外键。</code>
这张表的每一行表示 employee_id 的员工正在 project_id 的项目上工作。
</pre>

<p>&nbsp;</p>

<p>员工表&nbsp;<code>Employee</code>：</p>

<pre>
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| employee_id      | int     |
| name             | varchar |
| experience_years | int     |
+------------------+---------+
主键是 employee_id。数据保证 experience_years 非空。
这张表的每一行包含一个员工的信息。</pre>

<p>&nbsp;</p>

<p>请写一个 SQL&nbsp;语句，查询每一个项目中员工的&nbsp;<strong>平均&nbsp;</strong>工作年限，<strong>精确到小数点后两位</strong>。</p>

<p>以 <strong>任意</strong> 顺序返回结果表。</p>

<p>查询结果的格式如下。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Project 表：
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+

Employee 表：
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 1                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+

<strong>输出：</strong>
+-------------+---------------+
| project_id  | average_years |
+-------------+---------------+
| 1           | 2.00          |
| 2           | 2.50          |
+-------------+---------------+
<strong>解释：</strong>第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Project":["project_id","employee_id"],"Employee":["employee_id","name","experience_years"]},"rows":{"Project":[[1,1],[1,2],[1,3],[2,1],[2,4]],"Employee":[[1,"Khaled",3],[2,"Ali",2],[3,"John",1],[4,"Doe",2]]}}
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

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

