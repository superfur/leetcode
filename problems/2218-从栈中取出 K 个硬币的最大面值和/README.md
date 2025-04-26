# 2218. 从栈中取出 K 个硬币的最大面值和

## 题目描述

<p>一张桌子上总共有 <code>n</code>&nbsp;个硬币 <b>栈</b>&nbsp;。每个栈有 <strong>正整数</strong>&nbsp;个带面值的硬币。</p>

<p>每一次操作中，你可以从任意一个栈的 <strong>顶部</strong>&nbsp;取出 1 个硬币，从栈中移除它，并放入你的钱包里。</p>

<p>给你一个列表&nbsp;<code>piles</code>&nbsp;，其中&nbsp;<code>piles[i]</code>&nbsp;是一个整数数组，分别表示第 <code>i</code>&nbsp;个栈里 <strong>从顶到底</strong>&nbsp;的硬币面值。同时给你一个正整数&nbsp;<code>k</code>&nbsp;，请你返回在&nbsp;<strong>恰好</strong>&nbsp;进行&nbsp;<code>k</code>&nbsp;次操作的前提下，你钱包里硬币面值之和&nbsp;<strong>最大为多少</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/11/09/e1.png" style="width: 600px; height: 243px;" /></p>

<pre>
<b>输入：</b>piles = [[1,100,3],[7,8,9]], k = 2
<b>输出：</b>101
<strong>解释：</strong>
上图展示了几种选择 k 个硬币的不同方法。
我们可以得到的最大面值为 101 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
<b>输出：</b>706
<strong>解释：
</strong>如果我们所有硬币都从最后一个栈中取，可以得到最大面值和。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == piles.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= piles[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= sum(piles[i].length) &lt;= 2000</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 前缀和

## 提示

1. For each pile i, what will be the total value of coins we can collect if we choose the first j coins?
2. How can we use dynamic programming to combine the results from different piles to find the most optimal answer?

## 示例

```
[[1,100,3],[7,8,9]]
2
[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
```

### C

```c
int maxValueOfCoins(int** piles, int pilesSize, int* pilesColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxValueOfCoins(IList<IList<int>> piles, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} piles
 * @param {number} k
 * @return {number}
 */
var maxValueOfCoins = function(piles, k) {
    
};
```

### TypeScript

```typescript
function maxValueOfCoins(piles: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $piles
     * @param Integer $k
     * @return Integer
     */
    function maxValueOfCoins($piles, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxValueOfCoins(_ piles: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxValueOfCoins(piles: List<List<Int>>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxValueOfCoins(List<List<int>> piles, int k) {
    
  }
}
```

### Go

```golang
func maxValueOfCoins(piles [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} piles
# @param {Integer} k
# @return {Integer}
def max_value_of_coins(piles, k)
    
end
```

### Scala

```scala
object Solution {
    def maxValueOfCoins(piles: List[List[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_value_of_coins(piles: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-value-of-coins piles k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_value_of_coins(Piles :: [[integer()]], K :: integer()) -> integer().
max_value_of_coins(Piles, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_value_of_coins(piles :: [[integer]], k :: integer) :: integer
  def max_value_of_coins(piles, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxValueOfCoins(piles: ArrayList<ArrayList<Int64>>, k: Int64): Int64 {

    }
}
```

