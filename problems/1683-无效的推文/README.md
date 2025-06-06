# 1683. 无效的推文

## 题目描述

<p>表：<code>Tweets</code></p>

<pre>
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
在 SQL 中，tweet_id 是这个表的主键。
content 只包含字母数字字符，'!'，' '，不包含其它特殊字符。
这个表包含某社交媒体 App 中所有的推文。</pre>

<p>&nbsp;</p>

<p>查询所有无效推文的编号（ID）。当推文内容中的字符数<strong>严格大于</strong> <code>15</code> 时，该推文是无效的。</p>

<p>以<strong>任意顺序</strong>返回结果表。</p>

<p>查询结果格式如下所示：</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Tweets 表：
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+

<strong>输出：</strong>
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
<strong>解释：</strong>
推文 1 的长度 length = 14。该推文是有效的。
推文 2 的长度 length = 32。该推文是无效的。
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Tweets":["tweet_id","content"]},"rows":{"Tweets":[[1,"Let us Code"],[2,"More than fifteen chars are here!"]]}}
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

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

