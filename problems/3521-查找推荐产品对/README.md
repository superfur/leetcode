# 3521. 查找推荐产品对

## 题目描述

<p>表：<code>ProductPurchases</code></p>

<pre>
+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) 是这张表的唯一主键。
每一行代表用户以特定数量购买的产品。
</pre>

<p>表：<code>ProductInfo</code></p>

<pre>
+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id 是这张表的唯一主键。
每一行表示一个产品的类别和价格。
</pre>

<p>亚马逊希望根据 <strong>共同购买模式</strong> 实现 “<strong>购买此商品的用户还购买了...</strong>” 功能。编写一个解决方案以实现：</p>

<ol>
	<li>识别 <strong>被同一客户一起频繁购买的</strong> <strong>不同</strong> 产品对（其中&nbsp;<code>product1_id</code> &lt; <code>product2_id</code>）</li>
	<li>对于 <strong>每个产品对</strong>，确定有多少客户购买了这两种产品</li>
</ol>

<p>如果 <strong>至少有</strong> <code>3</code> <strong>位不同的</strong> 客户同时购买了这两种产品，则认为该&nbsp;<strong>产品对&nbsp;</strong>适合推荐。</p>

<p>返回结果表以<em>&nbsp;</em><strong>customer_count</strong>&nbsp; <strong>降序&nbsp;</strong>排序，并且为了避免排序持平，以&nbsp;<code>product1_id</code><em> </em><strong>升序&nbsp;</strong>排序，并以<em>&nbsp;</em><code>product2_id</code><em> </em><strong>升序 </strong>排序。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>ProductPurchases 表：</p>

<pre class="example-io">
+---------+------------+----------+
| user_id | product_id | quantity |
+---------+------------+----------+
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 103        | 3        |
| 2       | 101        | 1        |
| 2       | 102        | 5        |
| 2       | 104        | 1        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 105        | 4        |
| 4       | 101        | 1        |
| 4       | 102        | 1        |
| 4       | 103        | 2        |
| 4       | 104        | 3        |
| 5       | 102        | 2        |
| 5       | 104        | 1        |
+---------+------------+----------+
</pre>

<p>ProductInfo 表：</p>

<pre class="example-io">
+------------+-------------+-------+
| product_id | category    | price |
+------------+-------------+-------+
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Clothing    | 35    |
| 104        | Kitchen     | 50    |
| 105        | Sports      | 75    |
+------------+-------------+-------+
</pre>

<p><strong>输出：</strong></p>

<pre class="example-io">
+-------------+-------------+-------------------+-------------------+----------------+
| product1_id | product2_id | product1_category | product2_category | customer_count |
+-------------+-------------+-------------------+-------------------+----------------+
| 101         | 102         | Electronics       | Books             | 3              |
| 101         | 103         | Electronics       | Clothing          | 3              |
| 102         | 104         | Books             | Kitchen           | 3              |
+-------------+-------------+-------------------+-------------------+----------------+
</pre>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>产品对 (101, 102)：</strong>

	<ul>
		<li>被用户 1，2 和 4 购买（3 个消费者）</li>
		<li>产品 101 属于电子商品类别</li>
		<li>产品 102 属于图书类别</li>
	</ul>
	</li>
	<li><strong>产品对 (101, 103)：</strong>
	<ul>
		<li>被用户 1，3 和 4 购买（3 个消费者）</li>
		<li>产品 101 属于电子商品类别</li>
		<li>产品 103 属于服装类别</li>
	</ul>
	</li>
	<li><strong>产品对 (102, 104)：</strong>
	<ul>
		<li>被用户 2，4 和 5 购买（3 个消费者）</li>
		<li>产品 102 属于图书类别</li>
		<li>产品 104 属于厨房用品类别</li>
	</ul>
	</li>
</ul>

<p>结果以 customer_count 降序排序。对于有相同&nbsp;customer_count 的产品对，将它们以&nbsp;product1_id 升序排序，然后以 product2_id 升序排序。</p>
</div>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"ProductPurchases":["user_id","product_id","quantity"],"ProductInfo":["product_id","category","price"]},"rows":{"ProductPurchases":[[1,101,2],[1,102,1],[1,103,3],[2,101,1],[2,102,5],[2,104,1],[3,101,2],[3,103,1],[3,105,4],[4,101,1],[4,102,1],[4,103,2],[4,104,3],[5,102,2],[5,104,1]],"ProductInfo":[[101,"Electronics",100],[102,"Books",20],[103,"Clothing",35],[104,"Kitchen",50],[105,"Sports",75]]}}
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

def find_product_recommendation_pairs(product_purchases: pd.DataFrame, product_info: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

