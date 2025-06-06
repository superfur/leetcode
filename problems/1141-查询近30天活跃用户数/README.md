# 1141. 查询近30天活跃用户数

## 题目描述

<p>表：<code>Activity</code></p>

<pre>
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| session_id    | int     |
| activity_date | date    |
| activity_type | enum    |
+---------------+---------+
该表没有包含重复数据。
activity_type 列是 ENUM(category) 类型， 从 ('open_session'， 'end_session'， 'scroll_down'， 'send_message') 取值。
该表记录社交媒体网站的用户活动。
注意，每个会话只属于一个用户。
</pre>

<p>&nbsp;</p>

<p>编写解决方案，统计截至&nbsp;<code>2019-07-27</code>（包含2019-07-27），近<strong>&nbsp;</strong><code>30</code> 天的每日活跃用户数（当天只要有一条活动记录，即为活跃用户）。</p>

<p>以 <strong>任意顺序</strong> 返回结果表。</p>

<p>结果示例如下。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>
Activity table:
+---------+------------+---------------+---------------+
| user_id | session_id | activity_date | activity_type |
+---------+------------+---------------+---------------+
| 1       | 1          | 2019-07-20    | open_session  |
| 1       | 1          | 2019-07-20    | scroll_down   |
| 1       | 1          | 2019-07-20    | end_session   |
| 2       | 4          | 2019-07-20    | open_session  |
| 2       | 4          | 2019-07-21    | send_message  |
| 2       | 4          | 2019-07-21    | end_session   |
| 3       | 2          | 2019-07-21    | open_session  |
| 3       | 2          | 2019-07-21    | send_message  |
| 3       | 2          | 2019-07-21    | end_session   |
| 4       | 3          | 2019-06-25    | open_session  |
| 4       | 3          | 2019-06-25    | end_session   |
+---------+------------+---------------+---------------+
<strong>输出：</strong>
+------------+--------------+ 
| day        | active_users |
+------------+--------------+ 
| 2019-07-20 | 2            |
| 2019-07-21 | 2            |
+------------+--------------+ <strong>
解释：</strong>注意非活跃用户的记录不需要展示。</pre>


## 难度

Easy

## 标签

- 数据库

## 示例

```
{"headers":{"Activity":["user_id","session_id","activity_date","activity_type"]},"rows":{"Activity":[[1,1,"2019-07-20","open_session"],[1,1,"2019-07-20","scroll_down"],[1,1,"2019-07-20","end_session"],[2,4,"2019-07-20","open_session"],[2,4,"2019-07-21","send_message"],[2,4,"2019-07-21","end_session"],[3,2,"2019-07-21","open_session"],[3,2,"2019-07-21","send_message"],[3,2,"2019-07-21","end_session"],[4,3,"2019-06-25","open_session"],[4,3,"2019-06-25","end_session"]]}}
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

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

