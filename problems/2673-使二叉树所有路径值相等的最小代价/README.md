# 2673. 使二叉树所有路径值相等的最小代价

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;表示一棵 <b>满二叉树</b>&nbsp;里面节点的数目，节点编号从 <code>1</code>&nbsp;到 <code>n</code>&nbsp;。根节点编号为 <code>1</code>&nbsp;，树中每个非叶子节点&nbsp;<code>i</code>&nbsp;都有两个孩子，分别是左孩子&nbsp;<code>2 * i</code>&nbsp;和右孩子&nbsp;<code>2 * i + 1</code>&nbsp;。</p>

<p>树中每个节点都有一个值，用下标从<b>&nbsp;0</b>&nbsp;开始、长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>cost</code>&nbsp;表示，其中&nbsp;<code>cost[i]</code>&nbsp;是第&nbsp;<code>i + 1</code>&nbsp;个节点的值。每次操作，你可以将树中&nbsp;<strong>任意</strong>&nbsp;节点的值&nbsp;<strong>增加</strong>&nbsp;<code>1</code>&nbsp;。你可以执行操作 <strong>任意</strong> 次。</p>

<p>你的目标是让根到每一个 <strong>叶子结点</strong>&nbsp;的路径值相等。请你返回 <strong>最少</strong>&nbsp;需要执行增加操作多少次。</p>

<p><b>注意：</b></p>

<ul>
	<li><strong>满二叉树</strong>&nbsp;指的是一棵树，它满足树中除了叶子节点外每个节点都恰好有 2 个子节点，且所有叶子节点距离根节点距离相同。</li>
	<li><strong>路径值</strong> 指的是路径上所有节点的值之和。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/04/04/binaryytreeedrawio-4.png" /></p>

<pre>
<b>输入：</b>n = 7, cost = [1,5,2,2,3,3,1]
<b>输出：</b>6
<b>解释：</b>我们执行以下的增加操作：
- 将节点 4 的值增加一次。
- 将节点 3 的值增加三次。
- 将节点 7 的值增加两次。
从根到叶子的每一条路径值都为 9 。
总共增加次数为 1 + 3 + 2 = 6 。
这是最小的答案。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/04/04/binaryytreee2drawio.png" style="width: 205px; height: 151px;" /></p>

<pre>
<b>输入：</b>n = 3, cost = [5,3,3]
<b>输出：</b>0
<b>解释：</b>两条路径已经有相等的路径值，所以不需要执行任何增加操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n + 1</code> 是&nbsp;<code>2</code>&nbsp;的幂</li>
	<li><code>cost.length == n</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 树
- 数组
- 动态规划
- 二叉树

## 提示

1. The path from the root to a leaf that has the maximum cost should not be modified.
2. The optimal way is to increase all other paths to make their costs equal to the path with maximum cost.

## 示例

```
7
[1,5,2,2,3,3,1]
3
[5,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minIncrements(int n, vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public int minIncrements(int n, int[] cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minIncrements(self, n, cost):
        """
        :type n: int
        :type cost: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
```

### C

```c
int minIncrements(int n, int* cost, int costSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinIncrements(int n, int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} cost
 * @return {number}
 */
var minIncrements = function(n, cost) {
    
};
```

### TypeScript

```typescript
function minIncrements(n: number, cost: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $cost
     * @return Integer
     */
    function minIncrements($n, $cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minIncrements(_ n: Int, _ cost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minIncrements(n: Int, cost: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minIncrements(int n, List<int> cost) {
    
  }
}
```

### Go

```golang
func minIncrements(n int, cost []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} cost
# @return {Integer}
def min_increments(n, cost)
    
end
```

### Scala

```scala
object Solution {
    def minIncrements(n: Int, cost: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_increments(n: i32, cost: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-increments n cost)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_increments(N :: integer(), Cost :: [integer()]) -> integer().
min_increments(N, Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_increments(n :: integer, cost :: [integer]) :: integer
  def min_increments(n, cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minIncrements(n: Int64, cost: Array<Int64>): Int64 {

    }
}
```

