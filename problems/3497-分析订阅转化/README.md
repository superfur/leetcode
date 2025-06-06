# 3497. 分析订阅转化

## 题目描述

<p>表：<code>UserActivity</code></p>

<pre>
+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| user_id          | int     |
| activity_date    | date    |
| activity_type    | varchar |
| activity_duration| int     |
+------------------+---------+
(user_id, activity_date, activity_type) 是这张表的唯一主键。
activity_type 是('free_trial', 'paid', 'cancelled')中的一个。
activity_duration 是用户当天在平台上花费的分钟数。
每一行表示一个用户在特定日期的活动。
</pre>

<p>订阅服务想要分析用户行为模式。公司提供7天免费试用，试用结束后，用户可以选择订阅 <strong>付费计划</strong> 或 <strong>取消</strong>。编写解决方案：</p>

<ol>
	<li>查找从免费试用转为付费订阅的用户</li>
	<li>计算每位用户在 <strong>免费试用</strong> 期间的 <strong>平均每日活动时长</strong>（四舍五入至小数点后 <code>2</code> 位）</li>
	<li>计算每位用户在 <strong>付费</strong> 订阅期间的 <strong>平均每日活动时长</strong>（四舍五入到小数点后&nbsp;<code>2</code> 位）</li>
</ol>

<p>返回结果表以<em>&nbsp;</em><code>user_id</code><em> </em><strong>升序&nbsp;</strong>排序。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>UserActivity 表：</p>

<pre class="example-io">
+---------+---------------+---------------+-------------------+
| user_id | activity_date | activity_type | activity_duration |
+---------+---------------+---------------+-------------------+
| 1       | 2023-01-01    | free_trial    | 45                |
| 1       | 2023-01-02    | free_trial    | 30                |
| 1       | 2023-01-05    | free_trial    | 60                |
| 1       | 2023-01-10    | paid          | 75                |
| 1       | 2023-01-12    | paid          | 90                |
| 1       | 2023-01-15    | paid          | 65                |
| 2       | 2023-02-01    | free_trial    | 55                |
| 2       | 2023-02-03    | free_trial    | 25                |
| 2       | 2023-02-07    | free_trial    | 50                |
| 2       | 2023-02-10    | cancelled     | 0                 |
| 3       | 2023-03-05    | free_trial    | 70                |
| 3       | 2023-03-06    | free_trial    | 60                |
| 3       | 2023-03-08    | free_trial    | 80                |
| 3       | 2023-03-12    | paid          | 50                |
| 3       | 2023-03-15    | paid          | 55                |
| 3       | 2023-03-20    | paid          | 85                |
| 4       | 2023-04-01    | free_trial    | 40                |
| 4       | 2023-04-03    | free_trial    | 35                |
| 4       | 2023-04-05    | paid          | 45                |
| 4       | 2023-04-07    | cancelled     | 0                 |
+---------+---------------+---------------+-------------------+
</pre>

<p><strong>输出：</strong></p>

<pre class="example-io">
+---------+--------------------+-------------------+
| user_id | trial_avg_duration | paid_avg_duration |
+---------+--------------------+-------------------+
| 1       | 45.00              | 76.67             |
| 3       | 70.00              | 63.33             |
| 4       | 37.50              | 45.00             |
+---------+--------------------+-------------------+
</pre>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>用户 1:</strong>

	<ul>
		<li>体验了 3 天免费试用，时长分别为 45，30 和 60 分钟。</li>
		<li>平均试用时长：(45 + 30 + 60) / 3 = 45.00 分钟。</li>
		<li>拥有 3 天付费订阅，时长分别为 75，90 和 65分钟。</li>
		<li>平均花费时长：(75 + 90 + 65) / 3 = 76.67 分钟。</li>
	</ul>
	</li>
	<li><strong>用户 2:</strong>
	<ul>
		<li>体验了 3 天免费试用，时长分别为 55，25 和 50 分钟。</li>
		<li>平均试用时长：(55 + 25 + 50) / 3 = 43.33 分钟。</li>
		<li>没有转为付费订阅（只有&nbsp;free_trial 和 cancelled 活动）。</li>
		<li>未包含在输出中，因为他未转换为付费用户。</li>
	</ul>
	</li>
	<li><strong>用户 3:</strong>
	<ul>
		<li>体验了 3 天免费试用，时长分别为 70，60 和 80 分钟。</li>
		<li>平均试用时长：(70 + 60 + 80) / 3 = 70.00 分钟。</li>
		<li>拥有 3 天付费订阅，时长分别为 50，55 和 85 分钟。</li>
		<li>平均花费时长：(50 + 55 + 85) / 3 = 63.33 分钟。</li>
	</ul>
	</li>
	<li><strong>用户 4:</strong>
	<ul>
		<li>体验了 2 天免费试用，时长分别为 40 和 35 分钟。</li>
		<li>平均试用时长：(40 + 35) / 2 = 37.50 分钟。</li>
		<li>在取消前有 1 天的付费订阅，时长为45分钟。</li>
		<li>平均花费时长：45.00 分钟。</li>
	</ul>
	</li>
</ul>

<p>结果表仅包括从免费试用转为付费订阅的用户（用户 1，3 和 4），并且以&nbsp;user_id 升序排序。</p>
</div>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"UserActivity":["user_id","activity_date","activity_type","activity_duration"]},"rows":{"UserActivity":[[1,"2023-01-01","free_trial",45],[1,"2023-01-02","free_trial",30],[1,"2023-01-05","free_trial",60],[1,"2023-01-10","paid",75],[1,"2023-01-12","paid",90],[1,"2023-01-15","paid",65],[2,"2023-02-01","free_trial",55],[2,"2023-02-03","free_trial",25],[2,"2023-02-07","free_trial",50],[2,"2023-02-10","cancelled",0],[3,"2023-03-05","free_trial",70],[3,"2023-03-06","free_trial",60],[3,"2023-03-08","free_trial",80],[3,"2023-03-12","paid",50],[3,"2023-03-15","paid",55],[3,"2023-03-20","paid",85],[4,"2023-04-01","free_trial",40],[4,"2023-04-03","free_trial",35],[4,"2023-04-05","paid",45],[4,"2023-04-07","cancelled",0]]}}
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

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

