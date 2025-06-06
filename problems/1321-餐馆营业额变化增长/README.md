# 1321. 餐馆营业额变化增长

## 题目描述

<p>表: <code>Customer</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
| visited_on    | date    |
| amount        | int     |
+---------------+---------+
在 SQL 中，(customer_id, visited_on) 是该表的主键。
该表包含一家餐馆的顾客交易数据。
visited_on 表示 (customer_id) 的顾客在 visited_on 那天访问了餐馆。
amount 是一个顾客某一天的消费总额。
</pre>

<p>&nbsp;</p>

<p>你是餐馆的老板，现在你想分析一下可能的营业额变化增长（每天至少有一位顾客）。</p>

<p>计算以 7 天（某日期 + 该日期前的 6 天）为一个时间段的顾客消费平均值。<code>average_amount</code>&nbsp;要 <strong>保留两位小数。</strong></p>

<p>结果按 <code>visited_on</code>&nbsp;<strong>升序排序</strong>。</p>

<p>返回结果格式的例子如下。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Customer 表:
+-------------+--------------+--------------+-------------+
| customer_id | name         | visited_on   | amount      |
+-------------+--------------+--------------+-------------+
| 1           | Jhon         | 2019-01-01   | 100         |
| 2           | Daniel       | 2019-01-02   | 110         |
| 3           | Jade         | 2019-01-03   | 120         |
| 4           | Khaled       | 2019-01-04   | 130         |
| 5           | Winston      | 2019-01-05   | 110         | 
| 6           | Elvis        | 2019-01-06   | 140         | 
| 7           | Anna         | 2019-01-07   | 150         |
| 8           | Maria        | 2019-01-08   | 80          |
| 9           | Jaze         | 2019-01-09   | 110         | 
| 1           | Jhon         | 2019-01-10   | 130         | 
| 3           | Jade         | 2019-01-10   | 150         | 
+-------------+--------------+--------------+-------------+
<strong>输出：</strong>
+--------------+--------------+----------------+
| visited_on   | amount       | average_amount |
+--------------+--------------+----------------+
| 2019-01-07   | 860          | 122.86         |
| 2019-01-08   | 840          | 120            |
| 2019-01-09   | 840          | 120            |
| 2019-01-10   | 1000         | 142.86         |
+--------------+--------------+----------------+
<strong>解释：</strong>
第一个七天消费平均值从 2019-01-01 到 2019-01-07 是restaurant-growth/restaurant-growth/ (100 + 110 + 120 + 130 + 110 + 140 + 150)/7 = 122.86
第二个七天消费平均值从 2019-01-02 到 2019-01-08 是 (110 + 120 + 130 + 110 + 140 + 150 + 80)/7 = 120
第三个七天消费平均值从 2019-01-03 到 2019-01-09 是 (120 + 130 + 110 + 140 + 150 + 80 + 110)/7 = 120
第四个七天消费平均值从 2019-01-04 到 2019-01-10 是 (130 + 110 + 140 + 150 + 80 + 110 + 130 + 150)/7 = 142.86</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Customer":["customer_id","name","visited_on","amount"]},"rows":{"Customer":[[1,"Jhon","2019-01-01",100],[2,"Daniel","2019-01-02",110],[3,"Jade","2019-01-03",120],[4,"Khaled","2019-01-04",130],[5,"Winston","2019-01-05",110],[6,"Elvis","2019-01-06",140],[7,"Anna","2019-01-07",150],[8,"Maria","2019-01-08",80],[9,"Jaze","2019-01-09",110],[1,"Jhon","2019-01-10",130],[3,"Jade","2019-01-10",150]]}}
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

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

