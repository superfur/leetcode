# 1179. 重新格式化部门表

## 题目描述

<p>表&nbsp;<code>Department</code>：</p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
在 SQL 中，(id, month) 是表的联合主键。
这个表格有关于每个部门每月收入的信息。
月份（month）可以取下列值 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]。
</pre>

<p>&nbsp;</p>

<p>重新格式化表格，使得&nbsp;<strong>每个月&nbsp;</strong>都有一个部门 id 列和一个收入列。</p>

<p>以 <strong>任意顺序</strong> 返回结果表。</p>

<p>结果格式如以下示例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>
Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+
<b>输出：</b>
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+
<b>解释：</b>四月到十二月的收入为空。 
请注意，结果表共有 13 列（1 列用于部门 ID，其余 12 列用于各个月份）。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Department":["id","revenue","month"]},"rows":{"Department":[[1,8000,"Jan"],[2,9000,"Jan"],[3,10000,"Feb"],[1,7000,"Feb"],[1,6000,"Mar"]]}}
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

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

