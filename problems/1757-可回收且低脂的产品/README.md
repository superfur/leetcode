# 1757. 可回收且低脂的产品

## 题目描述

<p>表：<code>Products</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
<code>product_id</code> 是该表的主键（具有唯一值的列）。
low_fats 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品是低脂产品，'N' 表示不是低脂产品。
recyclable 是枚举类型，取值为以下两种 ('Y', 'N')，其中 'Y' 表示该产品可回收，而 'N' 表示不可回收。</pre>

<p>&nbsp;</p>

<p>编写解决方案找出既是低脂又是可回收的产品编号。</p>

<p>返回结果 <strong>无顺序要求</strong> 。</p>

<p>返回结果格式如下例所示：</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Products 表：
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
<strong>输出：</strong>
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
<strong>解释：</strong>
只有产品 id 为 1 和 3 的产品，既是低脂又是可回收的产品。
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Products":["product_id","low_fats","recyclable"]},"rows":{"Products":[["0","Y","N"],["1","Y","Y"],["2","N","Y"],["3","Y","Y"],["4","N","N"]]}}
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

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

