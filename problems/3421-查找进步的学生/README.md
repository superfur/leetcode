# 3421. 查找进步的学生

## 题目描述

<p>表：<code>Scores</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student_id  | int     |
| subject     | varchar |
| score       | int     |
| exam_date   | varchar |
+-------------+---------+
(student_id, subject, exam_date) 是这张表的主键。
每一行包含有关学生在特定考试日期特定科目成绩的信息。分数范围从 0 到 100（包括边界）。
</pre>

<p>编写一个解决方案来查找 <strong>进步的学生</strong>。如果 <strong>同时</strong> 满足以下两个条件，则该学生被认为是进步的：</p>

<ul>
	<li>在 <strong>同一科目</strong> 至少参加过两个不同日期的考试。</li>
	<li>他们在该学科<strong> 最近的分数 </strong>比他们 第一次该学科考试的分数更高。</li>
</ul>

<p>返回结果表以&nbsp;<code>student_id</code>，<code>subject</code> <strong>升序</strong>&nbsp;排序。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>Scores 表：</p>

<pre>
+------------+----------+-------+------------+
| student_id | subject  | score | exam_date  |
+------------+----------+-------+------------+
| 101        | Math     | 70    | 2023-01-15 |
| 101        | Math     | 85    | 2023-02-15 |
| 101        | Physics  | 65    | 2023-01-15 |
| 101        | Physics  | 60    | 2023-02-15 |
| 102        | Math     | 80    | 2023-01-15 |
| 102        | Math     | 85    | 2023-02-15 |
| 103        | Math     | 90    | 2023-01-15 |
| 104        | Physics  | 75    | 2023-01-15 |
| 104        | Physics  | 85    | 2023-02-15 |
+------------+----------+-------+------------+</pre>

<p><strong>出：</strong></p>

<pre class="example-io">
+------------+----------+-------------+--------------+
| student_id | subject  | first_score | latest_score |
+------------+----------+-------------+--------------+
| 101        | Math     | 70          | 85           |
| 102        | Math     | 80          | 85           |
| 104        | Physics  | 75          | 85           |
+------------+----------+-------------+--------------+
</pre>

<p><strong>解释：</strong></p>

<ul>
	<li>学生 101 的数学：从 70 分进步到 85 分。</li>
	<li>学生 101 的物理：没有进步（从 65 分退步到 60分）</li>
	<li>学生 102 的数学：从 80 进步到 85 分。</li>
	<li>学生 103 的数学：只有一次考试，不符合资格。</li>
	<li>学生 104 的物理：从 75 分进步到 85 分。</li>
</ul>

<p>结果表以 student_id，subject 升序排序。</p>
</div>


## 难度

Medium

## 标签

- 数据库

## 示例

```
{"headers":{"Scores":["student_id","subject","score","exam_date"]},"rows":{"Scores":[[101,"Math",70,"2023-01-15"],[101,"Math",85,"2023-02-15"],[101,"Physics",65,"2023-01-15"],[101,"Physics",60,"2023-02-15"],[102,"Math",80,"2023-01-15"],[102,"Math",85,"2023-02-15"],[103,"Math",90,"2023-01-15"],[104,"Physics",75,"2023-01-15"],[104,"Physics",85,"2023-02-15"]]}}
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

def find_students_who_improved(scores: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

