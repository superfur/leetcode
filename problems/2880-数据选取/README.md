# 2880. 数据选取

## 题目描述

<pre>
DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

</pre>

<p>编写一个解决方案，选择&nbsp;<code>student_id = 101</code>&nbsp;的学生的 name 和 age 并输出。</p>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<b>输入：</b>
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
<b>输出：</b>
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
<strong>解释：
</strong>学生 Ulysses 的 student_id = 101，所以我们输出了他的 name 和 age。</pre>


## 难度

Easy

## 提示

1. Consider applying both row and column filtering to select the desired data.

## 示例

```
{"headers":{"students":["student_id","name","age"]},"rows":{"students":[[101,"Ulysses",13],[53,"William",10],[128,"Henry",6],[3,"Henry",11]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    
```

