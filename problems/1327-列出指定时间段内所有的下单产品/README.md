# 1327. 列出指定时间段内所有的下单产品

## 题目描述

<p>表: <code>Products</code></p>

<pre>
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id 是该表主键(具有唯一值的列)。
该表包含该公司产品的数据。
</pre>

<p>&nbsp;</p>

<p>表: <code>Orders</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
该表可能包含重复行。
product_id 是表单 Products 的外键（reference 列）。
unit 是在日期 order_date 内下单产品的数目。
</pre>

<p>&nbsp;</p>

<p>写一个解决方案，要求获取在 2020 年 2 月份下单的数量不少于 100 的产品的名字和数目。</p>

<p>返回结果表单的 <strong>顺序无要求 </strong>。</p>

<p>查询结果的格式如下。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Products 表:
+-------------+-----------------------+------------------+
| product_id  | product_name          | product_category |
+-------------+-----------------------+------------------+
| 1           | Leetcode Solutions    | Book             |
| 2           | Jewels of Stringology | Book             |
| 3           | HP                    | Laptop           |
| 4           | Lenovo                | Laptop           |
| 5           | Leetcode Kit          | T-shirt          |
+-------------+-----------------------+------------------+
Orders 表:
+--------------+--------------+----------+
| product_id   | order_date   | unit     |
+--------------+--------------+----------+
| 1            | 2020-02-05   | 60       |
| 1            | 2020-02-10   | 70       |
| 2            | 2020-01-18   | 30       |
| 2            | 2020-02-11   | 80       |
| 3            | 2020-02-17   | 2        |
| 3            | 2020-02-24   | 3        |
| 4            | 2020-03-01   | 20       |
| 4            | 2020-03-04   | 30       |
| 4            | 2020-03-04   | 60       |
| 5            | 2020-02-25   | 50       |
| 5            | 2020-02-27   | 50       |
| 5            | 2020-03-01   | 50       |
+--------------+--------------+----------+
<strong>输出：</strong>
+--------------------+---------+
| product_name       | unit    |
+--------------------+---------+
| Leetcode Solutions | 130     |
| Leetcode Kit       | 100     |
+--------------------+---------+
<strong>解释：</strong>
2020 年 2 月份下单 product_id = 1 的产品的数目总和为 (60 + 70) = 130 。
2020 年 2 月份下单 product_id = 2 的产品的数目总和为 80 。
2020 年 2 月份下单 product_id = 3 的产品的数目总和为 (2 + 3) = 5 。
2020 年 2 月份 product_id = 4 的产品并没有下单。
2020 年 2 月份下单 product_id = 5 的产品的数目总和为 (50 + 50) = 100 。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers": {"Products": ["product_id", "product_name", "product_category"], "Orders": ["product_id", "order_date", "unit"]}, "rows": {"Products": [[1, "Leetcode Solutions", "Book"], [2, "Jewels of Stringology", "Book"], [3, "HP", "Laptop"], [4, "Lenovo", "Laptop"], [5, "Leetcode Kit", "T-shirt"]], "Orders": [[1, "2020-02-05", 60], [1, "2020-02-10", 70], [2, "2020-01-18", 30], [2, "2020-02-11", 80], [3, "2020-02-17", 2], [3, "2020-02-24", 3], [4, "2020-03-01", 20], [4, "2020-03-04", 30], [4, "2020-03-04", 60], [5, "2020-02-25", 50], [5, "2020-02-27", 50], [5, "2020-03-01", 50]]}}
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

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

