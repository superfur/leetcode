# LCR 091. 粉刷房子

## 题目描述

<p>假如有一排房子，共 <code>n</code> 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。</p>

<p>当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个&nbsp;<code>n x 3</code><em>&nbsp;</em>的正整数矩阵 <code>costs</code> 来表示的。</p>

<p>例如，<code>costs[0][0]</code> 表示第 0 号房子粉刷成红色的成本花费；<code>costs[1][2]</code>&nbsp;表示第 1 号房子粉刷成绿色的花费，以此类推。</p>

<p>请计算出粉刷完所有房子最少的花费成本。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>costs = [[17,2,17],[16,16,5],[14,3,19]]
<strong>输出: </strong>10
<strong>解释: </strong>将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色<strong>。</strong>
&nbsp;    最少花费: 2 + 5 + 3 = 10。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>costs = [[7,6,2]]
<strong>输出: 2</strong>
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>costs.length == n</code></li>
	<li><code>costs[i].length == 3</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= costs[i][j] &lt;= 20</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 256&nbsp;题相同：<a href="https://leetcode-cn.com/problems/paint-house/">https://leetcode-cn.com/problems/paint-house/</a></p>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[[17,2,17],[16,16,5],[14,3,19]]
[[7,6,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {

    }
};
```

### Java

```java
class Solution {
    public int minCost(int[][] costs) {

    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
```

### C

```c


int minCost(int** costs, int costsSize, int* costsColSize){

}
```

### C#

```csharp
public class Solution {
    public int MinCost(int[][] costs) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} costs
 * @return {number}
 */
var minCost = function(costs) {

};
```

### TypeScript

```typescript
function minCost(costs: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $costs
     * @return Integer
     */
    function minCost($costs) {

    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ costs: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(costs: Array<IntArray>): Int {

    }
}
```

### Go

```golang
func minCost(costs [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} costs
# @return {Integer}
def min_cost(costs)

end
```

### Scala

```scala
object Solution {
    def minCost(costs: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(costs: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (min-cost costs)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec min_cost(Costs :: [[integer()]]) -> integer().
min_cost(Costs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(costs :: [[integer]]) :: integer
  def min_cost(costs) do

  end
end
```

