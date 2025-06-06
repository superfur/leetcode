# 2861. 最大合金数

## 题目描述

<p>假设你是一家合金制造公司的老板，你的公司使用多种金属来制造合金。现在共有 <code>n</code> 种不同类型的金属可以使用，并且你可以使用 <code>k</code> 台机器来制造合金。每台机器都需要特定数量的每种金属来创建合金。</p>

<p>对于第 <code>i</code> 台机器而言，创建合金需要 <code>composition[i][j]</code> 份 <code>j</code> 类型金属。最初，你拥有 <code>stock[i]</code> 份 <code>i</code> 类型金属，而每购入一份 <code>i</code> 类型金属需要花费 <code>cost[i]</code> 的金钱。</p>

<p>给你整数 <code>n</code>、<code>k</code>、<code>budget</code>，下标从 <strong>1</strong> 开始的二维数组 <code>composition</code>，两个下标从 <strong>1</strong> 开始的数组 <code>stock</code> 和 <code>cost</code>，请你在预算不超过 <code>budget</code> 金钱的前提下，<strong>最大化</strong> 公司制造合金的数量。</p>

<p><strong>所有合金都需要由同一台机器制造。</strong></p>

<p>返回公司可以制造的最大合金数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,0], cost = [1,2,3]
<strong>输出：</strong>2
<strong>解释：</strong>最优的方法是使用第 1 台机器来制造合金。
要想制造 2 份合金，我们需要购买：
- 2 份第 1 类金属。
- 2 份第 2 类金属。
- 2 份第 3 类金属。
总共需要 2 * 1 + 2 * 2 + 2 * 3 = 12 的金钱，小于等于预算 15 。
注意，我们最开始时候没有任何一类金属，所以必须买齐所有需要的金属。
可以证明在示例条件下最多可以制造 2 份合金。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 2, budget = 15, composition = [[1,1,1],[1,1,10]], stock = [0,0,100], cost = [1,2,3]
<strong>输出：</strong>5
<strong>解释：</strong>最优的方法是使用第 2 台机器来制造合金。 
要想制造 5 份合金，我们需要购买： 
- 5 份第 1 类金属。
- 5 份第 2 类金属。 
- 0 份第 3 类金属。 
总共需要 5 * 1 + 5 * 2 + 0 * 3 = 15 的金钱，小于等于预算 15 。 
可以证明在示例条件下最多可以制造 5 份合金。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 3, budget = 10, composition = [[2,1],[1,2],[1,1]], stock = [1,1], cost = [5,5]
<strong>输出：</strong>2
<strong>解释：</strong>最优的方法是使用第 3 台机器来制造合金。
要想制造 2 份合金，我们需要购买：
- 1 份第 1 类金属。
- 1 份第 2 类金属。
总共需要 1 * 5 + 1 * 5 = 10 的金钱，小于等于预算 10 。
可以证明在示例条件下最多可以制造 2 份合金。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 100</code></li>
	<li><code>0 &lt;= budget &lt;= 10<sup>8</sup></code></li>
	<li><code>composition.length == k</code></li>
	<li><code>composition[i].length == n</code></li>
	<li><code>1 &lt;= composition[i][j] &lt;= 100</code></li>
	<li><code>stock.length == cost.length == n</code></li>
	<li><code>0 &lt;= stock[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= cost[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Use binary search to find the answer.

## 示例

```
3
2
15
[[1,1,1],[1,1,10]]
[0,0,0]
[1,2,3]
3
2
15
[[1,1,1],[1,1,10]]
[0,0,100]
[1,2,3]
2
3
10
[[2,1],[1,2],[1,1]]
[1,1]
[5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxNumberOfAlloys(int n, int k, int budget, vector<vector<int>>& composition, vector<int>& stock, vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxNumberOfAlloys(int n, int k, int budget, List<List<Integer>> composition, List<Integer> stock, List<Integer> cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
```

### C

```c
int maxNumberOfAlloys(int n, int k, int budget, int** composition, int compositionSize, int* compositionColSize, int* stock, int stockSize, int* cost, int costSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxNumberOfAlloys(int n, int k, int budget, IList<IList<int>> composition, IList<int> stock, IList<int> cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @param {number} budget
 * @param {number[][]} composition
 * @param {number[]} stock
 * @param {number[]} cost
 * @return {number}
 */
var maxNumberOfAlloys = function(n, k, budget, composition, stock, cost) {
    
};
```

### TypeScript

```typescript
function maxNumberOfAlloys(n: number, k: number, budget: number, composition: number[][], stock: number[], cost: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @param Integer $budget
     * @param Integer[][] $composition
     * @param Integer[] $stock
     * @param Integer[] $cost
     * @return Integer
     */
    function maxNumberOfAlloys($n, $k, $budget, $composition, $stock, $cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNumberOfAlloys(_ n: Int, _ k: Int, _ budget: Int, _ composition: [[Int]], _ stock: [Int], _ cost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNumberOfAlloys(n: Int, k: Int, budget: Int, composition: List<List<Int>>, stock: List<Int>, cost: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxNumberOfAlloys(int n, int k, int budget, List<List<int>> composition, List<int> stock, List<int> cost) {
    
  }
}
```

### Go

```golang
func maxNumberOfAlloys(n int, k int, budget int, composition [][]int, stock []int, cost []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @param {Integer} budget
# @param {Integer[][]} composition
# @param {Integer[]} stock
# @param {Integer[]} cost
# @return {Integer}
def max_number_of_alloys(n, k, budget, composition, stock, cost)
    
end
```

### Scala

```scala
object Solution {
    def maxNumberOfAlloys(n: Int, k: Int, budget: Int, composition: List[List[Int]], stock: List[Int], cost: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_number_of_alloys(n: i32, k: i32, budget: i32, composition: Vec<Vec<i32>>, stock: Vec<i32>, cost: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-number-of-alloys n k budget composition stock cost)
  (-> exact-integer? exact-integer? exact-integer? (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_number_of_alloys(N :: integer(), K :: integer(), Budget :: integer(), Composition :: [[integer()]], Stock :: [integer()], Cost :: [integer()]) -> integer().
max_number_of_alloys(N, K, Budget, Composition, Stock, Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_number_of_alloys(n :: integer, k :: integer, budget :: integer, composition :: [[integer]], stock :: [integer], cost :: [integer]) :: integer
  def max_number_of_alloys(n, k, budget, composition, stock, cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNumberOfAlloys(n: Int64, k: Int64, budget: Int64, composition: ArrayList<ArrayList<Int64>>, stock: ArrayList<Int64>, cost: ArrayList<Int64>): Int64 {

    }
}
```

