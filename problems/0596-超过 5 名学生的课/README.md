# 596. 超过 5 名学生的课

## 题目描述

<p>表:&nbsp;<code>Courses</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class)是该表的主键（不同值的列的组合）。
该表的每一行表示学生的名字和他们注册的班级。
</pre>

<p>&nbsp;</p>

<p>查询&nbsp;<strong>至少有 5 个学生</strong> 的所有班级。</p>

<p>以 <strong>任意顺序 </strong>返回结果表。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
<strong>输出:</strong> 
+---------+ 
| class &nbsp; | 
+---------+ 
| Math &nbsp; &nbsp;| 
+---------+
<strong>解释: </strong>
-数学课有 6 个学生，所以我们包括它。
-英语课有 1 名学生，所以我们不包括它。
-生物课有 1 名学生，所以我们不包括它。
-计算机课有 1 个学生，所以我们不包括它。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers": {"Courses": ["student", "class"]}, "rows": {"Courses": [["A", "Math"], ["B", "English"], ["C", "Math"], ["D", "Biology"], ["E", "Math"], ["F", "Computer"], ["G", "Math"], ["H", "Math"], ["I", "Math"]]}}
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

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

