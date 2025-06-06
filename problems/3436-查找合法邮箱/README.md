# 3436. 查找合法邮箱

## 题目描述

<p>表：<code>Users</code></p>

<pre>
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| user_id         | int     |
| email           | varchar |
+-----------------+---------+
(user_id) 是这张表的唯一主键。
每一行包含用户的唯一 ID 和邮箱地址。
</pre>

<p>编写一个解决方案来查找所有 <b>合法邮箱地址</b>。一个合法的邮箱地址符合下述条件：</p>

<ul>
	<li>只包含一个&nbsp;<code>@</code>&nbsp;符号。</li>
	<li>以&nbsp;<code>.com</code>&nbsp;结尾。</li>
	<li><code>@</code>&nbsp;符号前面的部分只包含&nbsp;<strong>字母数字</strong>&nbsp;字符和&nbsp;<strong>下划线</strong>。</li>
	<li><code>@</code>&nbsp;符号后面与&nbsp;<code>.com</code>&nbsp;前面的部分 包含 <strong>只有字母&nbsp;</strong>的域名。</li>
</ul>

<p>返回结果表以&nbsp;<code>user_id</code> <strong>升序</strong>&nbsp;排序。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>Users 表：</p>

<pre class="example-io">
+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+
</pre>

<p><strong>输出：</strong></p>

<pre class="example-io">
+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+
</pre>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>alice@example.com</strong>&nbsp;是合法的因为它包含一个&nbsp;<code>@</code>，alice 是只有字母数字的，并且&nbsp;example.com 以字母开始并以 .com&nbsp;结束。</li>
	<li><strong>bob_at_example.com</strong>&nbsp;是不合法的因为它包含下划线但没有&nbsp;<code>@</code>。</li>
	<li><strong>charlie@example.net</strong>&nbsp;是不合法的因为域名没有以&nbsp;<code>.com</code>&nbsp;结尾。</li>
	<li><strong>david@domain.com</strong>&nbsp;是合法的因为它满足所有条件。</li>
	<li><strong>eve@invalid</strong>&nbsp;是不合法的因为域名没有以&nbsp;<code>.com</code>&nbsp;结尾。</li>
</ul>

<p>结果表以 user_id 升序排序。</p>
</div>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Users":["user_id","email"]},"rows":{"Users":[[1,"alice@example.com"],[2,"bob_at_example.com"],[3,"charlie@example.net"],[4,"david@domain.com"],[5,"eve@invalid"]]}}
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

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

