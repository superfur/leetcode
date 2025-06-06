# 1158. 市场分析 I

## 题目描述

<p>表：&nbsp;<code>Users</code></p>

<pre>
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id 是此表主键（具有唯一值的列）。
表中描述了购物网站的用户信息，用户可以在此网站上进行商品买卖。
</pre>

<p>&nbsp;</p>

<p>表：&nbsp;<code>Orders</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id 是此表主键（具有唯一值的列）。
item_id 是 Items 表的外键（reference 列）。
（buyer_id，seller_id）是 User 表的外键。
</pre>

<p>&nbsp;</p>

<p>表：<code>Items</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| item_id       | int     |
| item_brand    | varchar |
+---------------+---------+
item_id 是此表的主键（具有唯一值的列）。
</pre>

<p>&nbsp;</p>

<p>编写解决方案找出每个用户的注册日期和在 <strong><code>2019</code> </strong>年作为买家的订单总数。</p>

<p>以 <strong>任意顺序</strong> 返回结果表。</p>

<p>查询结果格式如下。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Users 表:
+---------+------------+----------------+
| user_id | join_date  | favorite_brand |
+---------+------------+----------------+
| 1       | 2018-01-01 | Lenovo         |
| 2       | 2018-02-09 | Samsung        |
| 3       | 2018-01-19 | LG             |
| 4       | 2018-05-21 | HP             |
+---------+------------+----------------+
Orders 表:
+----------+------------+---------+----------+-----------+
| order_id | order_date | item_id | buyer_id | seller_id |
+----------+------------+---------+----------+-----------+
| 1        | 2019-08-01 | 4       | 1        | 2         |
| 2        | 2018-08-02 | 2       | 1        | 3         |
| 3        | 2019-08-03 | 3       | 2        | 3         |
| 4        | 2018-08-04 | 1       | 4        | 2         |
| 5        | 2018-08-04 | 1       | 3        | 4         |
| 6        | 2019-08-05 | 2       | 2        | 4         |
+----------+------------+---------+----------+-----------+
Items 表:
+---------+------------+
| item_id | item_brand |
+---------+------------+
| 1       | Samsung    |
| 2       | Lenovo     |
| 3       | LG         |
| 4       | HP         |
+---------+------------+
<strong>输出：</strong>
+-----------+------------+----------------+
| buyer_id  | join_date  | orders_in_2019 |
+-----------+------------+----------------+
| 1         | 2018-01-01 | 1              |
| 2         | 2018-02-09 | 2              |
| 3         | 2018-01-19 | 0              |
| 4         | 2018-05-21 | 0              |
+-----------+------------+----------------+</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Users":["user_id","join_date","favorite_brand"],"Orders":["order_id","order_date","item_id","buyer_id","seller_id"],"Items":["item_id","item_brand"]},"rows":{"Users":[[1,"2018-01-01","Lenovo"],[2,"2018-02-09","Samsung"],[3,"2018-01-19","LG"],[4,"2018-05-21","HP"]],"Orders":[[1,"2019-08-01",4,1,2],[2,"2018-08-02",2,1,3],[3,"2019-08-03",3,2,3],[4,"2018-08-04",1,4,2],[5,"2018-08-04",1,3,4],[6,"2019-08-05",2,2,4]],"Items":[[1,"Samsung"],[2,"Lenovo"],[3,"LG"],[4,"HP"]]}}
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

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

