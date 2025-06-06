# 1045. 买下所有产品的客户

## 题目描述

<p><code>Customer</code>&nbsp;表：</p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
该表可能包含重复的行。
customer_id 不为 NULL。
product_key 是 Product 表的外键(reference 列)。
</pre>

<p><code>Product</code>&nbsp;表：</p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key 是这张表的主键（具有唯一值的列）。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，报告&nbsp;<code>Customer</code> 表中购买了 <code>Product</code> 表中所有产品的客户的 id。</p>

<p>返回结果表 <strong>无顺序要求</strong> 。</p>

<p>返回结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Customer 表：
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product 表：
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
<strong>输出：</strong>
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
<strong>解释：</strong>
购买了所有产品（5 和 6）的客户的 id 是 1 和 3 。
</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Customer":["customer_id","product_key"],"Product":["product_key"]},"rows":{"Customer":[[1,5],[2,6],[3,5],[3,6],[1,6]],"Product":[[5],[6]]}}
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

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

