# 2528. 最大化城市的最小电量

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>stations</code>&nbsp;，其中&nbsp;<code>stations[i]</code>&nbsp;表示第 <code>i</code>&nbsp;座城市的供电站数目。</p>

<p>每个供电站可以在一定 <strong>范围</strong>&nbsp;内给所有城市提供电力。换句话说，如果给定的范围是&nbsp;<code>r</code>&nbsp;，在城市&nbsp;<code>i</code>&nbsp;处的供电站可以给所有满足&nbsp;<code>|i - j| &lt;= r</code> 且&nbsp;<code>0 &lt;= i, j &lt;= n - 1</code>&nbsp;的城市&nbsp;<code>j</code>&nbsp;供电。</p>

<ul>
	<li><code>|x|</code>&nbsp;表示 <code>x</code>&nbsp;的 <strong>绝对值</strong>&nbsp;。比方说，<code>|7 - 5| = 2</code>&nbsp;，<code>|3 - 10| = 7</code>&nbsp;。</li>
</ul>

<p>一座城市的 <strong>电量</strong>&nbsp;是所有能给它供电的供电站数目。</p>

<p>政府批准了可以额外建造 <code>k</code>&nbsp;座供电站，你需要决定这些供电站分别应该建在哪里，这些供电站与已经存在的供电站有相同的供电范围。</p>

<p>给你两个整数&nbsp;<code>r</code> 和&nbsp;<code>k</code>&nbsp;，如果以最优策略建造额外的发电站，返回所有城市中，最小电量的最大值是多少。</p>

<p>这 <code>k</code>&nbsp;座供电站可以建在多个城市。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>stations = [1,2,4,5,0], r = 1, k = 2
<b>输出：</b>5
<b>解释：</b>
最优方案之一是把 2 座供电站都建在城市 1 。
每座城市的供电站数目分别为 [1,4,4,5,0] 。
- 城市 0 的供电站数目为 1 + 4 = 5 。
- 城市 1 的供电站数目为 1 + 4 + 4 = 9 。
- 城市 2 的供电站数目为 4 + 4 + 5 = 13 。
- 城市 3 的供电站数目为 5 + 4 = 9 。
- 城市 4 的供电站数目为 5 + 0 = 5 。
供电站数目最少是 5 。
无法得到更优解，所以我们返回 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>stations = [4,4,4,4], r = 0, k = 3
<b>输出：</b>4
<b>解释：</b>
无论如何安排，总有一座城市的供电站数目是 4 ，所以最优解是 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == stations.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= stations[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= r&nbsp;&lt;= n - 1</code></li>
	<li><code>0 &lt;= k&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 队列
- 数组
- 二分查找
- 前缀和
- 滑动窗口

## 提示

1. Pre calculate the number of stations on each city using Line Sweep.
2. Use binary search to maximize the minimum.

## 示例

```
[1,2,4,5,0]
1
2
[4,4,4,4]
0
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxPower(vector<int>& stations, int r, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxPower(int[] stations, int r, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPower(self, stations, r, k):
        """
        :type stations: List[int]
        :type r: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        
```

### C

```c
long long maxPower(int* stations, int stationsSize, int r, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxPower(int[] stations, int r, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stations
 * @param {number} r
 * @param {number} k
 * @return {number}
 */
var maxPower = function(stations, r, k) {
    
};
```

### TypeScript

```typescript
function maxPower(stations: number[], r: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stations
     * @param Integer $r
     * @param Integer $k
     * @return Integer
     */
    function maxPower($stations, $r, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPower(_ stations: [Int], _ r: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPower(stations: IntArray, r: Int, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPower(List<int> stations, int r, int k) {
    
  }
}
```

### Go

```golang
func maxPower(stations []int, r int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stations
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def max_power(stations, r, k)
    
end
```

### Scala

```scala
object Solution {
    def maxPower(stations: Array[Int], r: Int, k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_power(stations: Vec<i32>, r: i32, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-power stations r k)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_power(Stations :: [integer()], R :: integer(), K :: integer()) -> integer().
max_power(Stations, R, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_power(stations :: [integer], r :: integer, k :: integer) :: integer
  def max_power(stations, r, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPower(stations: Array<Int64>, r: Int64, k: Int64): Int64 {

    }
}
```

