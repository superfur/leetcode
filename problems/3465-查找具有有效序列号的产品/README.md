# 3465. 查找具有有效序列号的产品

## 题目描述

<p>表：<code>products</code></p>

<pre>
+--------------+------------+
| Column Name  | Type       |
+--------------+------------+
| product_id   | int        |
| product_name | varchar    |
| description  | varchar    |
+--------------+------------+
(product_id) 是这张表的唯一主键。
这张表的每一行表示一个产品的唯一 ID，名字和描述。
</pre>

<p>编写一个解决方案来找到所有描述中 <strong>包含一个有效序列号</strong>&nbsp;模式的产品。一个有效序列号符合下述规则：</p>

<ul>
	<li>以 <strong>SN </strong>字母开头（区分大小写）。</li>
	<li>后面有恰好&nbsp;<code>4</code>&nbsp;位数字。</li>
	<li>接着是一个短横（-）， 短横后面还有另一组 <code>4</code> <strong>位数字</strong></li>
	<li>序列号必须在描述内（可能不在描述的开头）</li>
</ul>

<p>返回结果表以&nbsp;<code>product_id</code> <strong>升序</strong>&nbsp;排序。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>products 表：</p>

<pre class="example-io">
+------------+--------------+------------------------------------------------------+
| product_id | product_name | description                                          |
+------------+--------------+------------------------------------------------------+
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 3          | Widget C     | Product SN1234-56789 is available now                |
| 4          | Widget D     | No serial number here                                |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
+------------+--------------+------------------------------------------------------+
    </pre>

<p><strong>输出：</strong></p>

<pre class="example-io">
+------------+--------------+------------------------------------------------------+
| product_id | product_name | description                                          |
+------------+--------------+------------------------------------------------------+
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
+------------+--------------+------------------------------------------------------+
    </pre>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>产品 1：</strong>有效的序列号&nbsp;SN1234-5678</li>
	<li><strong>产品 2：</strong>有效的序列号 SN9876-1234</li>
	<li><strong>产品 3：</strong>无效的序列号&nbsp;SN1234-56789（短横后包含 5 位数字）</li>
	<li><strong>产品 4：</strong>描述中没有序列号</li>
	<li><strong>产品 5：</strong>有效的序列号 SN4321-8765</li>
</ul>

<p>结果表以 product_id 升序排序。</p>
</div>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"products":["product_id","product_name","description"]},"rows":{"products":[[1,"Widget A","This is a sample product with SN1234-5678"],[2,"Widget B","A product with serial SN9876-1234 in the description"],[3,"Widget C","Product SN1234-56789 is available now"],[4,"Widget D","No serial number here"],[5,"Widget E","Check out SN4321-8765 in this description"]]}}
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

def find_valid_serial_products(products: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

