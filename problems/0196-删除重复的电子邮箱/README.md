# 196. 删除重复的电子邮箱

## 题目描述

<p>表:&nbsp;<code>Person</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id 是该表的主键列(具有唯一值的列)。
该表的每一行包含一封电子邮件。电子邮件将不包含大写字母。
</pre>

<p>&nbsp;</p>

<p>编写解决方案<strong> 删除</strong> 所有重复的电子邮件，只保留一个具有最小 <code>id</code> 的唯一电子邮件。</p>

<p>（对于 SQL 用户，请注意你应该编写一个 <code>DELETE</code> 语句而不是 <code>SELECT</code> 语句。）</p>

<p>（对于 Pandas 用户，请注意你应该直接修改 <code>Person</code> 表。）</p>

<p>运行脚本后，显示的答案是 <code>Person</code> 表。驱动程序将首先编译并运行您的代码片段，然后再显示 <code>Person</code> 表。<code>Person</code> 表的最终顺序 <strong>无关紧要</strong> 。</p>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<pre>
<strong>输入:</strong> 
Person 表:
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
<strong>输出:</strong> 
+----+------------------+
| id | email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
<strong>解释:</strong> john@example.com重复两次。我们保留最小的Id = 1。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers": {"Person": ["id", "email"]}, "rows": {"Person": [[1, "john@example.com"], [2, "bob@example.com"], [3, "john@example.com"]]}}
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

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

