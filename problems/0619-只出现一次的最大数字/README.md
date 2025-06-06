# 619. 只出现一次的最大数字

## 题目描述

<p><code>MyNumbers</code> 表：</p>

<div class="original__bRMd">
<div>
<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
该表可能包含重复项（换句话说，在SQL中，该表没有主键）。
这张表的每一行都含有一个整数。
</pre>

<p>&nbsp;</p>

<p><strong>单一数字</strong> 是在 <code>MyNumbers</code> 表中只出现一次的数字。</p>

<p>找出最大的 <strong>单一数字</strong> 。如果不存在 <strong>单一数字</strong> ，则返回&nbsp;<code>null</code> 。</p>

<p>查询结果如下例所示。</p>
<ptable> </ptable>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
MyNumbers 表：
+-----+
| num |
+-----+
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
+-----+
<strong>输出：</strong>
+-----+
| num |
+-----+
| 6   |
+-----+
<strong>解释：</strong>单一数字有 1、4、5 和 6 。
6 是最大的单一数字，返回 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>
MyNumbers table:
+-----+
| num |
+-----+
| 8   |
| 8   |
| 7   |
| 7   |
| 3   |
| 3   |
| 3   |
+-----+
<strong>输出：</strong>
+------+
| num  |
+------+
| null |
+------+
<strong>解释：</strong>输入的表中不存在单一数字，所以返回 null 。
</pre>
</div>
</div>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers": {"MyNumbers": ["num"]}, "rows": {"MyNumbers": [[8],[8],[3],[3],[1],[4],[5],[6]]}}
{"headers": {"MyNumbers": ["num"]}, "rows": {"MyNumbers": [[8],[8],[7],[7],[3],[3],[3]]}}
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

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

