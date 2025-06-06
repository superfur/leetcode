# 1873. 计算特殊奖金

## 题目描述

<p>表: <code>Employees</code></p>

<pre>
+-------------+---------+
| 列名        | 类型     |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id 是这个表的主键(具有唯一值的列)。
此表的每一行给出了雇员id ，名字和薪水。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，计算每个雇员的奖金。如果一个雇员的 id 是 <strong>奇数</strong> 并且他的名字不是以 <code>'M'</code> <strong>开头</strong>，那么他的奖金是他工资的 <code>100%</code> ，否则奖金为 <code>0</code> 。</p>

<p>返回的结果按照&nbsp;<code>employee_id</code>&nbsp;排序。</p>

<p>返回结果格式如下面的例子所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Employees 表:
+-------------+---------+--------+
| employee_id | name    | salary |
+-------------+---------+--------+
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
+-------------+---------+--------+
<strong>输出：</strong>
+-------------+-------+
| employee_id | bonus |
+-------------+-------+
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
+-------------+-------+
<strong>解释：</strong>
因为雇员id是偶数，所以雇员id 是2和8的两个雇员得到的奖金是0。
雇员id为3的因为他的名字以'M'开头，所以，奖金是0。
其他的雇员得到了百分之百的奖金。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Employees":["employee_id","name","salary"]},"rows":{"Employees":[[2,"Meir",3000],[3,"Michael",3800],[7,"Addilyn",7400],[8,"Juan",6100],[9,"Kannon",7700]]}}
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

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

