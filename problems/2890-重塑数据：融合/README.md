# 2890. 重塑数据：融合

## 题目描述

<pre>
DataFrame <code>report</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| product     | object |
| quarter_1   | int    |
| quarter_2   | int    |
| quarter_3   | int    |
| quarter_4   | int    |
+-------------+--------+
</pre>

<p>编写一个解决方案，将数据 <strong>重塑</strong> 成每一行表示特定季度产品销售数据的形式。</p>

<p>结果格式如下例所示：</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：
</strong>+-------------+-----------+-----------+-----------+-----------+
| product     | quarter_1 | quarter_2 | quarter_3 | quarter_4 |
+-------------+-----------+-----------+-----------+-----------+
| Umbrella    | 417       | 224       | 379       | 611       |
| SleepingBag | 800       | 936       | 93        | 875       |
+-------------+-----------+-----------+-----------+-----------+
<strong>输出：</strong>
+-------------+-----------+-------+
| product     | quarter   | sales |
+-------------+-----------+-------+
| Umbrella    | quarter_1 | 417   |
| SleepingBag | quarter_1 | 800   |
| Umbrella    | quarter_2 | 224   |
| SleepingBag | quarter_2 | 936   |
| Umbrella    | quarter_3 | 379   |
| SleepingBag | quarter_3 | 93    |
| Umbrella    | quarter_4 | 611   |
| SleepingBag | quarter_4 | 875   |
+-------------+-----------+-------+
<strong>解释：</strong>
DataFrame 已从宽格式重塑为长格式。每一行表示一个季度内产品的销售情况。
</pre>


## 难度

Easy

## 提示

1. Consider using a built-in function in pandas library to transform the data

## 示例

```
{"headers":{"report":["product","quarter_1","quarter_2","quarter_3","quarter_4"]},"rows":{"report":[["Umbrella",417,224,379,611],["SleepingBag",800,936,93,875]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    
```

