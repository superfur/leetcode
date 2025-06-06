# 2879. 显示前三行

## 题目描述

<pre>
DataFrame: <code>employees</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| employee_id | int    |
| name        | object |
| department  | object |
| salary      | int    |
+-------------+--------+
</pre>

<p>编写一个解决方案，显示这个 DataFrame 的<strong> 前&nbsp;&nbsp;<code>3</code>&nbsp;</strong>行。</p>

<p>&nbsp;</p>

<p><b>示例 1:</b></p>

<pre>
<strong>输入：
</strong>DataFrame employees
+-------------+-----------+-----------------------+--------+
| employee_id | name      | department            | salary |
+-------------+-----------+-----------------------+--------+
| 3           | Bob       | Operations            | 48675  |
| 90          | Alice     | Sales                 | 11096  |
| 9           | Tatiana   | Engineering           | 33805  |
| 60          | Annabelle | InformationTechnology | 37678  |
| 49          | Jonathan  | HumanResources        | 23793  |
| 43          | Khaled    | Administration        | 40454  |
+-------------+-----------+-----------------------+--------+
<b>输出：</b>
+-------------+---------+-------------+--------+
| employee_id | name    | department  | salary |
+-------------+---------+-------------+--------+
| 3           | Bob     | Operations  | 48675  |
| 90          | Alice   | Sales       | 11096  |
| 9           | Tatiana | Engineering | 33805  |
+-------------+---------+-------------+--------+
<b>解释：</b>
只有前 3 行被显示。</pre>


## 难度

Easy

## 提示

1. Consider using a built-in function in pandas library to retrieve the initial rows.

## 示例

```
{"headers":{"employees":["employee_id","name","department","salary"]},"rows":{"employees":[[3,"Bob","Operations",48675],[90,"Alice","Sales",11096],[9,"Tatiana","Engineering",33805],[60,"Annabelle","InformationTechnology",37678],[49,"Jonathan","HumanResources",23793],[43,"Khaled","Administration",40454]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    
```

