# 1907. 按分类统计薪水

## 题目描述

<p>表: <code>Accounts</code></p>

<pre>
+-------------+------+
| 列名        | 类型  |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
在 SQL 中，account_id&nbsp;是这个表的主键。
每一行都包含一个银行帐户的月收入的信息。
</pre>

<p>&nbsp;</p>

<p>查询每个工资类别的银行账户数量。&nbsp;工资类别如下：</p>

<ul>
	<li><code>"Low Salary"</code>：所有工资 <strong>严格低于</strong> <code>20000</code> 美元。</li>
	<li><code>"Average Salary"</code>： <strong>包含</strong> 范围内的所有工资&nbsp;<code>[$20000,&nbsp;$50000]</code> 。</li>
	<li>
	<p><code>"High Salary"</code>：所有工资 <strong>严格大于</strong> <code>50000</code> 美元。</p>
	</li>
</ul>

<p>结果表 <strong>必须</strong> 包含所有三个类别。&nbsp;如果某个类别中没有帐户，则报告&nbsp;<code>0</code> 。</p>

<p>按 <strong>任意顺序</strong> 返回结果表。</p>

<p>查询结果格式如下示例。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>
Accounts 表:
+------------+--------+
| account_id | income |
+------------+--------+
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
+------------+--------+
<strong>输出：</strong>
+----------------+----------------+
| category       | accounts_count |
+----------------+----------------+
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
+----------------+----------------+
<strong>解释：</strong>
低薪: 有一个账户 2.
中等薪水: 没有.
高薪: 有三个账户，他们是 3, 6和 8.</pre>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Accounts":["account_id","income"]},"rows":{"Accounts":[[3,108939],[2,12747],[8,87709],[6,91796]]}}
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

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

