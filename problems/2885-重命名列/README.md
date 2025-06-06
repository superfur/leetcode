# 2885. 重命名列

## 题目描述

<pre>
DataFrame <code>students</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
</pre>

<p>编写一个解决方案，按以下方式重命名列：</p>

<ul>
	<li><code>id</code>&nbsp;重命名为&nbsp;<code>student_id</code></li>
	<li><code>first</code>&nbsp;重命名为&nbsp;<code>first_name</code></li>
	<li><code>last</code>&nbsp;重命名为&nbsp;<code>last_name</code></li>
	<li><code>age</code>&nbsp;重命名为&nbsp;<code>age_in_years</code></li>
</ul>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：
</strong>+----+---------+----------+-----+
| id | first   | last     | age |
+----+---------+----------+-----+
| 1  | Mason   | King     | 6   |
| 2  | Ava     | Wright   | 7   |
| 3  | Taylor  | Hall     | 16  |
| 4  | Georgia | Thompson | 18  |
| 5  | Thomas  | Moore    | 10  |
+----+---------+----------+-----+
<b>输出：</b>
+------------+------------+-----------+--------------+
| student_id | first_name | last_name | age_in_years |
+------------+------------+-----------+--------------+
| 1          | Mason      | King      | 6            |
| 2          | Ava        | Wright    | 7            |
| 3          | Taylor     | Hall      | 16           |
| 4          | Georgia    | Thompson  | 18           |
| 5          | Thomas     | Moore     | 10           |
+------------+------------+-----------+--------------+
<b>解释：</b>
列名已相应更换。</pre>


## 难度

Easy

## 提示

1. Consider using a build-in function in pandas library with a dictionary to rename the columns as specified.

## 示例

```
{"headers":{"students":["id","first","last","age"]},"rows":{"employees":[],"students":[[1,"Mason","King",6],[2,"Ava","Wright",7],[3,"Taylor","Hall",16],[4,"Georgia","Thompson",18],[5,"Thomas","Moore",10]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    
```

