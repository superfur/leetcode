# 2878. 获取 DataFrame 的大小

## 题目描述

<pre>
DataFrame <code>players:</code>
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| player_id   | int    |
| name        | object |
| age         | int    |
| position    | object |
| ...         | ...    |
+-------------+--------+
</pre>

<p>编写一个解决方案，计算并显示&nbsp;<code>players</code>&nbsp;的&nbsp;<strong>行数和列数</strong>。</p>

<p>将结果返回为一个数组：</p>

<p><code>[number of rows, number of columns]</code></p>

<p>返回结果格式如下示例所示。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<strong>输入：
</strong>+-----------+----------+-----+-------------+--------------------+
| player_id | name     | age | position    | team               |
+-----------+----------+-----+-------------+--------------------+
| 846       | Mason    | 21  | Forward     | RealMadrid         |
| 749       | Riley    | 30  | Winger      | Barcelona          |
| 155       | Bob      | 28  | Striker     | ManchesterUnited   |
| 583       | Isabella | 32  | Goalkeeper  | Liverpool          |
| 388       | Zachary  | 24  | Midfielder  | BayernMunich       |
| 883       | Ava      | 23  | Defender    | Chelsea            |
| 355       | Violet   | 18  | Striker     | Juventus           |
| 247       | Thomas   | 27  | Striker     | ParisSaint-Germain |
| 761       | Jack     | 33  | Midfielder  | ManchesterCity     |
| 642       | Charlie  | 36  | Center-back | Arsenal            |
+-----------+----------+-----+-------------+--------------------+<strong>
输出：
</strong>[10, 5]
<b>解释：</b>
这个 DataFrame 包含 10 行和 5 列。
</pre>


## 难度

Easy

## 提示

1. Consider using a built-in function in pandas library to get the size of a DataFrame.

## 示例

```
{"headers":{"players":["player_id","name","age","position","team"]},"rows":{"players":[[846,"Mason",21,"Forward","RealMadrid"],[749,"Riley",30,"Winger","Barcelona"],[155,"Bob",28,"Striker","ManchesterUnited"],[583,"Isabella",32,"Goalkeeper","Liverpool"],[388,"Zachary",24,"Midfielder","BayernMunich"],[883,"Ava",23,"Defender","Chelsea"],[355,"Violet",18,"Striker","Juventus"],[247,"Thomas",27,"Striker","ParisSaint-Germain"],[761,"Jack",33,"Midfielder","ManchesterCity"],[642,"Charlie",36,"Center-back","Arsenal"]]}}
```

## 示例代码

### Pandas

```pythondata
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    
```

