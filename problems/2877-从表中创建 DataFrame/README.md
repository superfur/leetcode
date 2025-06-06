# 2877. 从表中创建 DataFrame

## 题目描述

<p>编写一个解决方案，基于名为&nbsp;&nbsp;<code>student_data</code>&nbsp;的二维列表&nbsp;<b>创建 </b>一个 DataFrame 。这个二维列表包含一些学生的 ID 和年龄信息。</p>

<p>DataFrame 应该有两列，&nbsp;<code>student_id</code>&nbsp;和&nbsp;<code>age</code>，并且与原始二维列表的顺序相同。</p>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：
</strong>student_data:<strong>
</strong><code>[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]</code>
<b>输出：</b>
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
<b>解释：</b>
基于 student_data 创建了一个 DataFrame，包含 student_id 和 age 两列。
</pre>


## 难度

Easy

## 提示

1. Consider using a built-in function in pandas library and specifying the column names within it.

## 示例

```
[[1,15],[2,11],[3,11],[4,20]]
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    
```

