# 602. 好友申请 II ：谁有最多的好友

## 题目描述

<p><code>RequestAccepted</code> 表：</p>

<div class="original__bRMd">
<div>
<pre>
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) 是这张表的主键(具有唯一值的列的组合)。
这张表包含发送好友请求的人的 ID ，接收好友请求的人的 ID ，以及好友请求通过的日期。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，找出拥有最多的好友的人和他拥有的好友数目。</p>

<p>生成的测试用例保证拥有最多好友数目的只有 1 个人。</p>

<p>查询结果格式如下例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>
RequestAccepted 表：
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
<strong>输出：</strong>
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
<strong>解释：</strong>
编号为 3 的人是编号为 1 ，2 和 4 的人的好友，所以他总共有 3 个好友，比其他人都多。</pre>

<p>&nbsp;</p>

<p><strong>进阶：</strong>在真实世界里，可能会有多个人拥有好友数相同且最多，你能找到所有这些人吗？</p>
</div>
</div>


## 难度

Medium

## 标签

- 数据库

## 提示

1. Being friends is bidirectional. If you accept someone's adding friend request, both you and the other person will have one more friend.

## 示例

```
{"headers":{"RequestAccepted":["requester_id","accepter_id","accept_date"]},"rows":{"RequestAccepted":[[1,2,"2016/06/03"],[1,3,"2016/06/08"],[2,3,"2016/06/08"],[3,4,"2016/06/09"]]}}
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

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

