# 1383. 最大的团队表现值

## 题目描述

<p>给定两个整数 <code>n</code> 和 <code>k</code>，以及两个长度为 <code>n</code> 的整数数组 <code>speed</code> 和<code> efficiency</code>。现有 <code>n</code> 名工程师，编号从 <code>1</code> 到 <code>n</code>。其中 <code>speed[i]</code>&nbsp;和 <code>efficiency[i]</code>&nbsp;分别代表第 <code>i</code>&nbsp;位工程师的速度和效率。</p>

<p>从这 <code>n</code> 名工程师中最多选择 <code>k</code> 名不同的工程师，使其组成的团队具有最大的团队表现值。</p>

<p><strong>团队表现值</strong>&nbsp;的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。</p>

<p>请你返回该团队的​​​​​​最大团队表现值，由于答案可能很大，请你返回结果对 <code>10^9 + 7</code> 取余后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
<strong>输出：</strong>60
<strong>解释：</strong>
我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
<strong>输出：</strong>68
<strong>解释：
</strong>此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
<strong>输出：</strong>72
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 10^5</code></li>
	<li><code>speed.length == n</code></li>
	<li><code>efficiency.length == n</code></li>
	<li><code>1 &lt;= speed[i] &lt;= 10^5</code></li>
	<li><code>1 &lt;= efficiency[i] &lt;= 10^8</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. Keep track of the engineers by their efficiency in decreasing order.
2. Starting from one engineer, to build a team, it suffices to bring K-1 more engineers who have higher efficiencies as well as high speeds.

## 示例

```
6
[2,10,3,1,5,8]
[5,4,3,9,7,2]
2
6
[2,10,3,1,5,8]
[5,4,3,9,7,2]
3
6
[2,10,3,1,5,8]
[5,4,3,9,7,2]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPerformance(int n, vector<int>& speed, vector<int>& efficiency, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPerformance(self, n, speed, efficiency, k):
        """
        :type n: int
        :type speed: List[int]
        :type efficiency: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
```

### C

```c
int maxPerformance(int n, int* speed, int speedSize, int* efficiency, int efficiencySize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPerformance(int n, int[] speed, int[] efficiency, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} speed
 * @param {number[]} efficiency
 * @param {number} k
 * @return {number}
 */
var maxPerformance = function(n, speed, efficiency, k) {
    
};
```

### TypeScript

```typescript
function maxPerformance(n: number, speed: number[], efficiency: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $speed
     * @param Integer[] $efficiency
     * @param Integer $k
     * @return Integer
     */
    function maxPerformance($n, $speed, $efficiency, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPerformance(_ n: Int, _ speed: [Int], _ efficiency: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPerformance(n: Int, speed: IntArray, efficiency: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPerformance(int n, List<int> speed, List<int> efficiency, int k) {
    
  }
}
```

### Go

```golang
func maxPerformance(n int, speed []int, efficiency []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} speed
# @param {Integer[]} efficiency
# @param {Integer} k
# @return {Integer}
def max_performance(n, speed, efficiency, k)
    
end
```

### Scala

```scala
object Solution {
    def maxPerformance(n: Int, speed: Array[Int], efficiency: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_performance(n: i32, speed: Vec<i32>, efficiency: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-performance n speed efficiency k)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_performance(N :: integer(), Speed :: [integer()], Efficiency :: [integer()], K :: integer()) -> integer().
max_performance(N, Speed, Efficiency, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_performance(n :: integer, speed :: [integer], efficiency :: [integer], k :: integer) :: integer
  def max_performance(n, speed, efficiency, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPerformance(n: Int64, speed: Array<Int64>, efficiency: Array<Int64>, k: Int64): Int64 {

    }
}
```

