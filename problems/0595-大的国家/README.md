# 595. 大的国家

## 题目描述

<p><code>World</code> 表：</p>

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
<code>name</code> 是该表的主键（具有唯一值的列）。
这张表的每一行提供：国家名称、所属大陆、面积、人口和 GDP 值。
</pre>

<p>&nbsp;</p>

<p>如果一个国家满足下述两个条件之一，则认为该国是 <strong>大国</strong> ：</p>

<ul>
	<li>面积至少为 300 万平方公里（即，<code>3000000 km<sup>2</sup></code>），或者</li>
	<li>人口至少为 2500 万（即 <code>25000000</code>）</li>
</ul>

<p>编写解决方案找出&nbsp;<strong>大国</strong> 的国家名称、人口和面积。</p>

<p>按 <strong>任意顺序</strong> 返回结果表。</p>

<p>返回结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<pre>
<strong>输入：</strong>
World 表：
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
<strong>输出：</strong>
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
</pre>
</div>
</div>
</div>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers": {"World": ["name", "continent",	"area",	"population", "gdp"]}, "rows": {"World": [["Afghanistan", "Asia", 652230, 25500100, 20343000000], ["Albania", "Europe", 28748, 2831741, 12960000000], ["Algeria", "Africa", 2381741, 37100000, 188681000000], ["Andorra", "Europe", 468, 78115,	3712000000], ["Angola", "Africa", 1246700, 20609294, 100990000000]]}}
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

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

