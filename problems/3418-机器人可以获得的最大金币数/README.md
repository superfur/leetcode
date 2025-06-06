# 3418. 机器人可以获得的最大金币数

## 题目描述

<p>给你一个 <code>m x n</code> 的网格。一个机器人从网格的左上角 <code>(0, 0)</code> 出发，目标是到达网格的右下角 <code>(m - 1, n - 1)</code>。在任意时刻，机器人只能向右或向下移动。</p>

<p>网格中的每个单元格包含一个值 <code>coins[i][j]</code>：</p>

<ul>
	<li>如果 <code>coins[i][j] &gt;= 0</code>，机器人可以获得该单元格的金币。</li>
	<li>如果 <code>coins[i][j] &lt; 0</code>，机器人会遇到一个强盗，强盗会抢走该单元格数值的&nbsp;<strong>绝对值</strong> 的金币。</li>
</ul>

<p>机器人有一项特殊能力，可以在行程中&nbsp;<strong>最多感化&nbsp;</strong>2个单元格的强盗，从而防止这些单元格的金币被抢走。</p>

<p><strong>注意：</strong>机器人的总金币数可以是负数。</p>

<p>返回机器人在路径上可以获得的&nbsp;<strong>最大金币数&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">coins = [[0,1,-1],[1,-2,3],[2,-3,4]]</span></p>

<p><strong>输出：</strong> <span class="example-io">8</span></p>

<p><strong>解释：</strong></p>

<p>一个获得最多金币的最优路径如下：</p>

<ol>
	<li>从 <code>(0, 0)</code> 出发，初始金币为 <code>0</code>（总金币 = <code>0</code>）。</li>
	<li>移动到 <code>(0, 1)</code>，获得 <code>1</code> 枚金币（总金币 = <code>0 + 1 = 1</code>）。</li>
	<li>移动到 <code>(1, 1)</code>，遇到强盗抢走 <code>2</code> 枚金币。机器人在此处使用一次感化能力，避免被抢（总金币 = <code>1</code>）。</li>
	<li>移动到 <code>(1, 2)</code>，获得 <code>3</code> 枚金币（总金币 = <code>1 + 3 = 4</code>）。</li>
	<li>移动到 <code>(2, 2)</code>，获得 <code>4</code> 枚金币（总金币 = <code>4 + 4 = 8</code>）。</li>
</ol>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">coins = [[10,10,10],[10,10,10]]</span></p>

<p><strong>输出：</strong> <span class="example-io">40</span></p>

<p><strong>解释：</strong></p>

<p>一个获得最多金币的最优路径如下：</p>

<ol>
	<li>从 <code>(0, 0)</code> 出发，初始金币为 <code>10</code>（总金币 = <code>10</code>）。</li>
	<li>移动到 <code>(0, 1)</code>，获得 <code>10</code> 枚金币（总金币 = <code>10 + 10 = 20</code>）。</li>
	<li>移动到 <code>(0, 2)</code>，再获得 <code>10</code> 枚金币（总金币 = <code>20 + 10 = 30</code>）。</li>
	<li>移动到 <code>(1, 2)</code>，获得 <code>10</code> 枚金币（总金币 = <code>30 + 10 = 40</code>）。</li>
</ol>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == coins.length</code></li>
	<li><code>n == coins[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>-1000 &lt;= coins[i][j] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Use Dynamic Programming.
2. Let <code>dp[i][j][k]</code> denote the maximum amount of money a robot can earn by starting at cell <code>(i,j)</code> and having neutralized <code>k</code> robbers.

## 示例

```
[[0,1,-1],[1,-2,3],[2,-3,4]]
[[10,10,10],[10,10,10]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumAmount(int[][] coins) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumAmount(self, coins):
        """
        :type coins: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        
```

### C

```c
int maximumAmount(int** coins, int coinsSize, int* coinsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumAmount(int[][] coins) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} coins
 * @return {number}
 */
var maximumAmount = function(coins) {
    
};
```

### TypeScript

```typescript
function maximumAmount(coins: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $coins
     * @return Integer
     */
    function maximumAmount($coins) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumAmount(_ coins: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumAmount(coins: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumAmount(List<List<int>> coins) {
    
  }
}
```

### Go

```golang
func maximumAmount(coins [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} coins
# @return {Integer}
def maximum_amount(coins)
    
end
```

### Scala

```scala
object Solution {
    def maximumAmount(coins: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_amount(coins: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-amount coins)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_amount(Coins :: [[integer()]]) -> integer().
maximum_amount(Coins) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_amount(coins :: [[integer]]) :: integer
  def maximum_amount(coins) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumAmount(coins: Array<Array<Int64>>): Int64 {

    }
}
```

