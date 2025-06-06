# 1484. 按日期分组销售产品

## 题目描述

<p>表&nbsp;<code>Activities</code>：</p>

<pre>
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
该表没有主键(具有唯一值的列)。它可能包含重复项。
此表的每一行都包含产品名称和在市场上销售的日期。
</pre>

<p>&nbsp;</p>

<p>编写解决方案找出每个日期、销售的不同产品的数量及其名称。<br />
每个日期的销售产品名称应按词典序排列。<br />
返回按&nbsp;<code>sell_date</code> 排序的结果表。<br />
结果表结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<code><strong>输入：</strong>
Activities</code> 表：
+------------+-------------+
| sell_date  | product     |
+------------+-------------+
| 2020-05-30 | Headphone   |
| 2020-06-01 | Pencil      |
| 2020-06-02 | Mask        |
| 2020-05-30 | Basketball  |
| 2020-06-01 | Bible       |
| 2020-06-02 | Mask        |
| 2020-05-30 | T-Shirt     |
+------------+-------------+
<strong>输出：</strong>
+------------+----------+------------------------------+
| sell_date  | num_sold | products                     |
+------------+----------+------------------------------+
| 2020-05-30 | 3        | Basketball,Headphone,T-shirt |
| 2020-06-01 | 2        | Bible,Pencil                 |
| 2020-06-02 | 1        | Mask                         |
+------------+----------+------------------------------+
<strong>解释：</strong>
对于2020-05-30，出售的物品是 (Headphone, Basketball, T-shirt)，按词典序排列，并用逗号 ',' 分隔。
对于2020-06-01，出售的物品是 (Pencil, Bible)，按词典序排列，并用逗号分隔。
对于2020-06-02，出售的物品是 (Mask)，只需返回该物品名。
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Activities":["sell_date","product"]},"rows":{"Activities":[["2020-05-30","Headphone"],["2020-06-01","Pencil"],["2020-06-02","Mask"],["2020-05-30","Basketball"],["2020-06-01","Bible"],["2020-06-02","Mask"],["2020-05-30","T-Shirt"]]}}
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

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

