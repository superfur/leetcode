# 2087. 网格图中机器人回家的最小代价

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的网格图，其中&nbsp;<code>(0, 0)</code>&nbsp;是最左上角的格子，<code>(m - 1, n - 1)</code>&nbsp;是最右下角的格子。给你一个整数数组&nbsp;<code>startPos</code>&nbsp;，<code>startPos = [start<sub>row</sub>, start<sub>col</sub>]</code>&nbsp;表示 <strong>初始</strong>&nbsp;有一个 <strong>机器人</strong>&nbsp;在格子&nbsp;<code>(start<sub>row</sub>, start<sub>col</sub>)</code>&nbsp;处。同时给你一个整数数组&nbsp;<code>homePos</code>&nbsp;，<code>homePos = [home<sub>row</sub>, home<sub>col</sub>]</code>&nbsp;表示机器人的 <strong>家</strong>&nbsp;在格子&nbsp;<code>(home<sub>row</sub>, home<sub>col</sub>)</code>&nbsp;处。</p>

<p>机器人需要回家。每一步它可以往四个方向移动：<strong>上</strong>，<strong>下</strong>，<strong>左</strong>，<strong>右</strong>，同时机器人不能移出边界。每一步移动都有一定代价。再给你两个下标从&nbsp;<strong>0</strong>&nbsp;开始的额整数数组：长度为&nbsp;<code>m</code>&nbsp;的数组&nbsp;<code>rowCosts</code> &nbsp;和长度为 <code>n</code>&nbsp;的数组&nbsp;<code>colCosts</code>&nbsp;。</p>

<ul>
	<li>如果机器人往 <strong>上</strong>&nbsp;或者往 <strong>下</strong>&nbsp;移动到第 <code>r</code>&nbsp;<strong>行</strong>&nbsp;的格子，那么代价为&nbsp;<code>rowCosts[r]</code>&nbsp;。</li>
	<li>如果机器人往 <strong>左</strong>&nbsp;或者往 <strong>右</strong>&nbsp;移动到第 <code>c</code>&nbsp;<strong>列</strong> 的格子，那么代价为&nbsp;<code>colCosts[c]</code>&nbsp;。</li>
</ul>

<p>请你返回机器人回家需要的 <strong>最小总代价</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/10/11/eg-1.png" style="width: 282px; height: 217px;"></p>

<pre><strong>输入：</strong>startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]
<b>输出：</b>18
<b>解释：</b>一个最优路径为：
从 (1, 0) 开始
-&gt; 往下走到 (<em><strong>2</strong></em>, 0) 。代价为 rowCosts[2] = 3 。
-&gt; 往右走到 (2, <em><strong>1</strong></em>) 。代价为 colCosts[1] = 2 。
-&gt; 往右走到 (2, <em><strong>2</strong></em>) 。代价为 colCosts[2] = 6 。
-&gt; 往右走到 (2, <em><strong>3</strong></em>) 。代价为 colCosts[3] = 7 。
总代价为 3 + 2 + 6 + 7 = 18</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]
<b>输出：</b>0
<b>解释：</b>机器人已经在家了，所以不需要移动。总代价为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == rowCosts.length</code></li>
	<li><code>n == colCosts.length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= rowCosts[r], colCosts[c] &lt;= 10<sup>4</sup></code></li>
	<li><code>startPos.length == 2</code></li>
	<li><code>homePos.length == 2</code></li>
	<li><code>0 &lt;= start<sub>row</sub>, home<sub>row</sub> &lt; m</code></li>
	<li><code>0 &lt;= start<sub>col</sub>, home<sub>col</sub> &lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Irrespective of what path the robot takes, it will have to traverse all the rows between startRow and homeRow and all the columns between startCol and homeCol.
2. Hence, making any other move other than traversing the required rows and columns will potentially incur more cost which can be avoided.

## 示例

```
[1,0]
[2,3]
[5,4,3]
[8,2,6,7]
[0,0]
[0,0]
[5]
[26]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
```

### C

```c
int minCost(int* startPos, int startPosSize, int* homePos, int homePosSize, int* rowCosts, int rowCostsSize, int* colCosts, int colCostsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} startPos
 * @param {number[]} homePos
 * @param {number[]} rowCosts
 * @param {number[]} colCosts
 * @return {number}
 */
var minCost = function(startPos, homePos, rowCosts, colCosts) {
    
};
```

### TypeScript

```typescript
function minCost(startPos: number[], homePos: number[], rowCosts: number[], colCosts: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $startPos
     * @param Integer[] $homePos
     * @param Integer[] $rowCosts
     * @param Integer[] $colCosts
     * @return Integer
     */
    function minCost($startPos, $homePos, $rowCosts, $colCosts) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ startPos: [Int], _ homePos: [Int], _ rowCosts: [Int], _ colCosts: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(startPos: IntArray, homePos: IntArray, rowCosts: IntArray, colCosts: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<int> startPos, List<int> homePos, List<int> rowCosts, List<int> colCosts) {
    
  }
}
```

### Go

```golang
func minCost(startPos []int, homePos []int, rowCosts []int, colCosts []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} start_pos
# @param {Integer[]} home_pos
# @param {Integer[]} row_costs
# @param {Integer[]} col_costs
# @return {Integer}
def min_cost(start_pos, home_pos, row_costs, col_costs)
    
end
```

### Scala

```scala
object Solution {
    def minCost(startPos: Array[Int], homePos: Array[Int], rowCosts: Array[Int], colCosts: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(start_pos: Vec<i32>, home_pos: Vec<i32>, row_costs: Vec<i32>, col_costs: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost startPos homePos rowCosts colCosts)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(StartPos :: [integer()], HomePos :: [integer()], RowCosts :: [integer()], ColCosts :: [integer()]) -> integer().
min_cost(StartPos, HomePos, RowCosts, ColCosts) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(start_pos :: [integer], home_pos :: [integer], row_costs :: [integer], col_costs :: [integer]) :: integer
  def min_cost(start_pos, home_pos, row_costs, col_costs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(startPos: Array<Int64>, homePos: Array<Int64>, rowCosts: Array<Int64>, colCosts: Array<Int64>): Int64 {

    }
}
```

