# 586. 订单最多的客户

## 题目描述

<p>表:&nbsp;<code>Orders</code></p>

<pre>
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
在 SQL 中，Order_number是该表的主键。
此表包含关于订单ID和客户ID的信息。
</pre>

<p>&nbsp;</p>

<p>查找下了 <strong>最多订单</strong>&nbsp;的客户的 <code>customer_number</code> 。</p>

<p>测试用例生成后， <strong>恰好有一个客户</strong> 比任何其他客户下了更多的订单。</p>

<p>查询结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
Orders 表:
+--------------+-----------------+
| order_number | customer_number |
+--------------+-----------------+
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
+--------------+-----------------+
<strong>输出:</strong> 
+-----------------+
| customer_number |
+-----------------+
| 3               |
+-----------------+
<strong>解释:</strong> 
customer_number 为 '3' 的顾客有两个订单，比顾客 '1' 或者 '2' 都要多，因为他们只有一个订单。
所以结果是该顾客的 customer_number ，也就是 3 。
</pre>

<p>&nbsp;</p>

<p><strong>进阶：</strong> 如果有多位顾客订单数并列最多，你能找到他们所有的 <code>customer_number</code> 吗？</p>


## 难度

Easy

## 标签

- 数据库

## 提示

1. MySQL uses a different expression to get the first records other than MSSQL's TOP expression.

## 示例

```
{"headers":{"orders":["order_number","customer_number"]},"rows":{"orders":[[1,1],[2,2],[3,3],[4,3]]}}
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

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

