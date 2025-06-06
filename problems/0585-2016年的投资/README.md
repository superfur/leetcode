# 585. 2016年的投资

## 题目描述

<p><code>Insurance</code> 表：</p>

<div class="original__bRMd">
<div>
<pre>
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid 是这张表的主键(具有唯一值的列)。
表中的每一行都包含一条保险信息，其中：
pid 是投保人的投保编号。
tiv_2015 是该投保人在 2015 年的总投保金额，tiv_2016 是该投保人在 2016 年的总投保金额。
lat 是投保人所在城市的纬度。题目数据确保 lat 不为空。
lon 是投保人所在城市的经度。题目数据确保 lon 不为空。</pre>

<p>&nbsp;</p>

<p>编写解决方案报告 2016 年 (<code>tiv_2016</code>) 所有满足下述条件的投保人的投保金额之和：</p>

<ul>
	<li>他在 2015 年的投保额&nbsp;(<code>tiv_2015</code>) 至少跟一个其他投保人在 2015 年的投保额相同。</li>
	<li>他所在的城市必须与其他投保人都不同（也就是说&nbsp;(<code>lat, lon</code>) 不能跟其他任何一个投保人完全相同）。</li>
</ul>

<p><code>tiv_2016</code> 四舍五入的 <strong>两位小数</strong> 。</p>

<p>查询结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Insurance 表：
+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+
<strong>输出：</strong>
+----------+
| tiv_2016 |
+----------+
| 45.00    |
+----------+
<strong>解释：
</strong>表中的第一条记录和最后一条记录都满足两个条件。
tiv_2015 值为 10 与第三条和第四条记录相同，且其位置是唯一的。

第二条记录不符合任何一个条件。其 tiv_2015 与其他投保人不同，并且位置与第三条记录相同，这也导致了第三条记录不符合题目要求。
因此，结果是第一条记录和最后一条记录的 tiv_2016 之和，即 45 。</pre>
</div>
</div>


## 难度

Medium

## 标签

- 数据库

## 提示

1. Make the (LAT, LON) a pair to represent the location information

## 示例

```
{"headers":{"Insurance":["pid","tiv_2015","tiv_2016","lat","lon"]},"rows":{"Insurance":[[1,10,5,10,10],[2,20,20,20,20],[3,10,30,20,20],[4,10,40,40,40]]}}
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

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

