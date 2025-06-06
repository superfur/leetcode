# 2886. 改变数据类型

## 题目描述

<pre>
DataFrame <code>students</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
| grade       | float  |
+-------------+--------+
</pre>

<p>编写一个解决方案来纠正以下错误：</p>

<p>&nbsp;<code>grade</code>&nbsp;列被存储为浮点数，将它转换为整数。</p>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：
</strong>DataFrame students:
+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73.0  |
| 2          | Kate | 15  | 87.0  |
+------------+------+-----+-------+
<strong>输出：
</strong>+------------+------+-----+-------+
| student_id | name | age | grade |
+------------+------+-----+-------+
| 1          | Ava  | 6   | 73    |
| 2          | Kate | 15  | 87    |
+------------+------+-----+-------+
<b>解释：</b>
grade 列的数据类型已转换为整数。</pre>


## 难度

Easy

## 提示

1. Consider using a build-in function in pandas library with a dictionary to convert the datatype of columns as specified.

## 示例

```
{"headers":{"students":["student_id","name","age","grade"]},"rows":{"students":[[1,"Ava",6,73.0],[2,"Kate",15,87.0]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    
```

