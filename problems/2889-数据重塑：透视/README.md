# 2889. 数据重塑：透视

## 题目描述

<pre>
DataFrame <code>weather</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| city        | object |
| month       | object |
| temperature | int    |
+-------------+--------+
</pre>

<p>编写一个解决方案，以便将数据&nbsp;<strong>旋转</strong>，使得每一行代表特定月份的温度，而每个城市都是一个单独的列。</p>

<p>输出结果格式如下示例所示。</p>

<p>&nbsp;</p>
<b>示例 1:</b>

<pre>
<b>输入：</b>
+--------------+----------+-------------+
| city         | month    | temperature |
+--------------+----------+-------------+
| Jacksonville | January  | 13          |
| Jacksonville | February | 23          |
| Jacksonville | March    | 38          |
| Jacksonville | April    | 5           |
| Jacksonville | May      | 34          |
| ElPaso       | January  | 20          |
| ElPaso       | February | 6           |
| ElPaso       | March    | 26          |
| ElPaso       | April    | 2           |
| ElPaso       | May      | 43          |
+--------------+----------+-------------+
<code><b>输出：</b>
+----------+--------+--------------+
| month    | ElPaso | Jacksonville |
+----------+--------+--------------+
| April    | 2      | 5            |
| February | 6      | 23           |
| January  | 20     | 13           |
| March    | 26     | 38           |
| May      | 43     | 34           |
+----------+--------+--------------+</code>
<strong>解释：
</strong>表格被旋转，每一列代表一个城市，每一行代表特定的月份。</pre>


## 难度

Easy

## 提示

1. Consider using a built-in function in pandas library to transform the data

## 示例

```
{"headers":{"weather":["city","month","temperature"]},"rows":{"weather":[["Jacksonville","January",13],["Jacksonville","February",23],["Jacksonville","March",38],["Jacksonville","April",5],["Jacksonville","May",34],["ElPaso","January",20],["ElPaso","February",6],["ElPaso","March",26],["ElPaso","April",2],["ElPaso","May",43]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    
```

