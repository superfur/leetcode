# 1962. 移除石子使总数最小

## 题目描述

<p>给你一个整数数组 <code>piles</code> ，数组 <strong>下标从 0 开始</strong> ，其中 <code>piles[i]</code> 表示第 <code>i</code> 堆石子中的石子数量。另给你一个整数 <code>k</code> ，请你执行下述操作 <strong>恰好</strong> <code>k</code> 次：</p>

<ul>
	<li>选出任一石子堆 <code>piles[i]</code> ，并从中 <strong>移除</strong> <code>floor(piles[i] / 2)</code> 颗石子。</li>
</ul>

<p><strong>注意：</strong>你可以对 <strong>同一堆</strong> 石子多次执行此操作。</p>

<p>返回执行 <code>k</code> 次操作后，剩下石子的 <strong>最小</strong> 总数。</p>

<p><code>floor(x)</code> 为 <strong>小于</strong> 或 <strong>等于</strong> <code>x</code> 的 <strong>最大</strong> 整数。（即，对 <code>x</code> 向下取整）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>piles = [5,4,9], k = 2
<strong>输出：</strong>12
<strong>解释：</strong>可能的执行情景如下：
- 对第 2 堆石子执行移除操作，石子分布情况变成 [5,4,<strong><em>5</em></strong>] 。
- 对第 0 堆石子执行移除操作，石子分布情况变成 [<strong><em>3</em></strong>,4,5] 。
剩下石子的总数为 12 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>piles = [4,3,6,7], k = 3
<strong>输出：</strong>12
<strong>解释：</strong>可能的执行情景如下：
- 对第 2 堆石子执行移除操作，石子分布情况变成 [4,3,<strong><em>3</em></strong>,7] 。
- 对第 3 堆石子执行移除操作，石子分布情况变成 [4,3,3,<strong><em>4</em></strong>] 。
- 对第 0 堆石子执行移除操作，石子分布情况变成 [<strong><em>2</em></strong>,3,3,4] 。
剩下石子的总数为 12 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= piles.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= piles[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. Choose the pile with the maximum number of stones each time.
2. Use a data structure that helps you find the mentioned pile each time efficiently.
3. One such data structure is a Priority Queue.

## 示例

```
[5,4,9]
2
[4,3,6,7]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minStoneSum(int[] piles, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
```

### C

```c
int minStoneSum(int* piles, int pilesSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinStoneSum(int[] piles, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} piles
 * @param {number} k
 * @return {number}
 */
var minStoneSum = function(piles, k) {
    
};
```

### TypeScript

```typescript
function minStoneSum(piles: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @param Integer $k
     * @return Integer
     */
    function minStoneSum($piles, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minStoneSum(_ piles: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minStoneSum(piles: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minStoneSum(List<int> piles, int k) {
    
  }
}
```

### Go

```golang
func minStoneSum(piles []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} piles
# @param {Integer} k
# @return {Integer}
def min_stone_sum(piles, k)
    
end
```

### Scala

```scala
object Solution {
    def minStoneSum(piles: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-stone-sum piles k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_stone_sum(Piles :: [integer()], K :: integer()) -> integer().
min_stone_sum(Piles, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_stone_sum(piles :: [integer], k :: integer) :: integer
  def min_stone_sum(piles, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minStoneSum(piles: Array<Int64>, k: Int64): Int64 {

    }
}
```

