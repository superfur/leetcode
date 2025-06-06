# 1587. 银行账户概要 II

## 题目描述

<p>表: <code>Users</code></p>

<pre>
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account 是该表的主键(具有唯一值的列)。
该表的每一行都包含银行中每个用户的帐号。
表中不会有两个用户具有相同的名称。
</pre>

<p>&nbsp;</p>

<p>表: <code>Transactions</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id 是该表主键(具有唯一值的列)。
该表的每一行包含了所有账户的交易改变情况。
如果用户收到了钱, 那么金额是正的; 如果用户转了钱, 那么金额是负的。
所有账户的起始余额为 0。
</pre>

<p>&nbsp;</p>

<p>编写解决方案,&nbsp;&nbsp;报告余额高于 10000 的所有用户的名字和余额.&nbsp;账户的余额等于包含该账户的所有交易的总和。</p>

<p>返回结果表单 <strong>无顺序要求</strong> 。</p>

<p>查询结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<code><strong>输入：</strong>
Users</code> table:
+------------+--------------+
| account    | name         |
+------------+--------------+
| 900001     | Alice        |
| 900002     | Bob          |
| 900003     | Charlie      |
+------------+--------------+

<code>Transactions</code> table:
+------------+------------+------------+---------------+
| trans_id   | account    | amount     | transacted_on |
+------------+------------+------------+---------------+
| 1          | 900001     | 7000       |  2020-08-01   |
| 2          | 900001     | 7000       |  2020-09-01   |
| 3          | 900001     | -3000      |  2020-09-02   |
| 4          | 900002     | 1000       |  2020-09-12   |
| 5          | 900003     | 6000       |  2020-08-07   |
| 6          | 900003     | 6000       |  2020-09-07   |
| 7          | 900003     | -4000      |  2020-09-11   |
+------------+------------+------------+---------------+
<strong>输出：</strong>
+------------+------------+
| <code>name    </code>   | <code>balance  </code>  |
+------------+------------+
| Alice      | 11000      |
+------------+------------+
<strong>解释：</strong>
Alice 的余额为(7000 + 7000 - 3000) = 11000.
Bob 的余额为1000.
Charlie 的余额为(6000 + 6000 - 4000) = 8000.
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers": {"Users": ["account", "name"], "Transactions": ["trans_id", "account", "amount", "transacted_on"]}, "rows": {"Users": [[900001, "Alice"], [900002, "Bob"], [900003, "Charlie"]], "Transactions": [[1, 900001, 7000, "2020-08-01"], [2, 900001, 7000, "2020-09-01"], [3, 900001, -3000, "2020-09-02"], [4, 900002, 1000, "2020-09-12"], [5, 900003, 6000, "2020-08-07"], [6, 900003, 6000, "2020-09-07"], [7, 900003, -4000, "2020-09-11"]]}}
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

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

