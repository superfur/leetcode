# 1326. 灌溉花园的最少水龙头数目

## 题目描述

<p>在 x 轴上有一个一维的花园。花园长度为&nbsp;<code>n</code>，从点&nbsp;<code>0</code>&nbsp;开始，到点&nbsp;<code>n</code>&nbsp;结束。</p>

<p>花园里总共有&nbsp;<code>n + 1</code> 个水龙头，分别位于&nbsp;<code>[0, 1, ..., n]</code> 。</p>

<p>给你一个整数&nbsp;<code>n</code>&nbsp;和一个长度为&nbsp;<code>n + 1</code> 的整数数组&nbsp;<code>ranges</code>&nbsp;，其中&nbsp;<code>ranges[i]</code> （下标从 0 开始）表示：如果打开点&nbsp;<code>i</code>&nbsp;处的水龙头，可以灌溉的区域为&nbsp;<code>[i -&nbsp; ranges[i], i + ranges[i]]</code>&nbsp;。</p>

<p>请你返回可以灌溉整个花园的&nbsp;<strong>最少水龙头数目</strong>&nbsp;。如果花园始终存在无法灌溉到的地方，请你返回&nbsp;<strong>-1</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/19/1685_example_1.png" /></p>

<pre>
<strong>输入：</strong>n = 5, ranges = [3,4,1,1,0,0]
<strong>输出：</strong>1
<strong>解释：
</strong>点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, ranges = [0,0,0,0]
<strong>输出：</strong>-1
<strong>解释：</strong>即使打开所有水龙头，你也无法灌溉整个花园。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>ranges.length == n + 1</code></li>
	<li><code>0 &lt;= ranges[i] &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. Create intervals of the area covered by each tap, sort intervals by the left end.
2. We need to cover the interval [0, n]. we can start with the first interval and out of all intervals that intersect with it we choose the one that covers the farthest point to the right.
3. What if there is a gap between intervals that is not covered ? we should stop and return -1 as there is some interval that cannot be covered.

## 示例

```
5
[3,4,1,1,0,0]
3
[0,0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minTaps(int n, vector<int>& ranges) {
        
    }
};
```

### Java

```java
class Solution {
    public int minTaps(int n, int[] ranges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
```

### C

```c
int minTaps(int n, int* ranges, int rangesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinTaps(int n, int[] ranges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} ranges
 * @return {number}
 */
var minTaps = function(n, ranges) {
    
};
```

### TypeScript

```typescript
function minTaps(n: number, ranges: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $ranges
     * @return Integer
     */
    function minTaps($n, $ranges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minTaps(_ n: Int, _ ranges: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minTaps(n: Int, ranges: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minTaps(int n, List<int> ranges) {
    
  }
}
```

### Go

```golang
func minTaps(n int, ranges []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} ranges
# @return {Integer}
def min_taps(n, ranges)
    
end
```

### Scala

```scala
object Solution {
    def minTaps(n: Int, ranges: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_taps(n: i32, ranges: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-taps n ranges)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_taps(N :: integer(), Ranges :: [integer()]) -> integer().
min_taps(N, Ranges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_taps(n :: integer, ranges :: [integer]) :: integer
  def min_taps(n, ranges) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minTaps(n: Int64, ranges: Array<Int64>): Int64 {

    }
}
```

