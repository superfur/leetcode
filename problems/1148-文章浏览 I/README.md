# 1148. 文章浏览 I

## 题目描述

<p><code>Views</code>&nbsp;表：</p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
此表可能会存在重复行。（换句话说，在 SQL 中这个表没有主键）
此表的每一行都表示某人在某天浏览了某位作者的某篇文章。
请注意，同一人的 author_id 和 viewer_id 是相同的。
</pre>

<p>&nbsp;</p>

<p>请查询出所有浏览过自己文章的作者。</p>

<p>结果按照作者的&nbsp;<code>id</code> 升序排列。</p>

<p>查询结果的格式如下所示：</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
Views 表：
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+

<strong>输出：</strong>
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Views":["article_id","author_id","viewer_id","view_date"]},"rows":{"Views":[[1,3,5,"2019-08-01"],[1,3,6,"2019-08-02"],[2,7,7,"2019-08-01"],[2,7,6,"2019-08-02"],[4,7,1,"2019-07-22"],[3,4,4,"2019-07-21"],[3,4,4,"2019-07-21"]]}}
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

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

