# 2888. 重塑数据：连结

## 题目描述

<pre>
DataFrame <code>df1</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame <code>df2</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

</pre>

<p>编写一个解决方案，将两个&nbsp;DataFrames <b>垂直 </b>连接成一个&nbsp;DataFrame。</p>

<p>结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：
df1</strong>
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
+------------+---------+-----+
<strong>df2
</strong>+------------+------+-----+
| student_id | name | age |
+------------+------+-----+
| 5          | Leo  | 7   |
| 6          | Alex | 7   |
+------------+------+-----+
<b>输出：</b>
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 1          | Mason   | 8   |
| 2          | Ava     | 6   |
| 3          | Taylor  | 15  |
| 4          | Georgia | 17  |
| 5          | Leo     | 7   |
| 6          | Alex    | 7   |
+------------+---------+-----+
<strong>解释：
</strong>两个 DataFrame 被垂直堆叠，它们的行被合并。</pre>


## 难度

Easy

## 提示

1. Consider using a built-in function in pandas library with the appropriate axis argument.

## 示例

```
{"headers":{"df1":["student_id","name","age"],"df2":["student_id","name","age"]},"rows":{"df1":[[1,"Mason",8],[2,"Ava",6],[3,"Taylor",15],[4,"Georgia",17]],"df2":[[5,"Leo",7],[6,"Alex",7]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    
```

