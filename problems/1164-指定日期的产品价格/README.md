# 1164. 指定日期的产品价格

## 题目描述

<p>产品数据表: <code>Products</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) 是此表的主键（具有唯一值的列组合）。
这张表的每一行分别记录了 某产品 在某个日期 更改后 的新价格。</pre>

<p>&nbsp;</p>

<p>编写一个解决方案，找出在&nbsp;<code>2019-08-16</code><strong> </strong>时全部产品的价格，假设所有产品在修改前的价格都是&nbsp;<code>10</code><strong> 。</strong></p>

<p>以 <strong>任意顺序 </strong>返回结果表。</p>

<p>结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Products 表:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
<strong>输出：</strong>
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Products":["product_id","new_price","change_date"]},"rows":{"Products":[[1,20,"2019-08-14"],[2,50,"2019-08-14"],[1,30,"2019-08-15"],[1,35,"2019-08-16"],[2,65,"2019-08-17"],[3,20,"2019-08-18"]]}}
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

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

