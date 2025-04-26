# 1870. 准时到达的列车最小时速

## 题目描述

<p>给你一个浮点数 <code>hour</code> ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 <code>n</code> 趟列车。另给你一个长度为 <code>n</code> 的整数数组 <code>dist</code> ，其中 <code>dist[i]</code> 表示第 <code>i</code> 趟列车的行驶距离（单位是千米）。</p>

<p>每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。</p>

<ul>
	<li>例如，第 <code>1</code> 趟列车需要 <code>1.5</code> 小时，那你必须再等待 <code>0.5</code> 小时，搭乘在第 2 小时发车的第 <code>2</code> 趟列车。</li>
</ul>

<p>返回能满足你在时限前到达办公室所要求全部列车的<strong> 最小正整数 </strong>时速（单位：千米每小时），如果无法准时到达，则返回 <code>-1</code> 。</p>

<p>生成的测试用例保证答案不超过 <code>10<sup>7</sup></code> ，且 <code>hour</code> 的 <strong>小数点后最多存在两位数字</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dist = [1,3,2], hour = 6
<strong>输出：</strong>1
<strong>解释：</strong>速度为 1 时：
- 第 1 趟列车运行需要 1/1 = 1 小时。
- 由于是在整数时间到达，可以立即换乘在第 1 小时发车的列车。第 2 趟列车运行需要 3/1 = 3 小时。
- 由于是在整数时间到达，可以立即换乘在第 4 小时发车的列车。第 3 趟列车运行需要 2/1 = 2 小时。
- 你将会恰好在第 6 小时到达。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>dist = [1,3,2], hour = 2.7
<strong>输出：</strong>3
<strong>解释：</strong>速度为 3 时：
- 第 1 趟列车运行需要 1/3 = 0.33333 小时。
- 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。
- 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。
- 你将会在第 2.66667 小时到达。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>dist = [1,3,2], hour = 1.9
<strong>输出：</strong>-1
<strong>解释：</strong>不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == dist.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= dist[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= hour &lt;= 10<sup>9</sup></code></li>
	<li><code>hours</code> 中，小数点后最多存在两位数字</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Given the speed the trains are traveling at, can you find the total time it takes for you to arrive?
2. Is there a cutoff where any speeds larger will always allow you to arrive on time?

## 示例

```
[1,3,2]
6
[1,3,2]
2.7
[1,3,2]
1.9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSpeedOnTime(vector<int>& dist, double hour) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSpeedOnTime(int[] dist, double hour) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
```

### C

```c
int minSpeedOnTime(int* dist, int distSize, double hour) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSpeedOnTime(int[] dist, double hour) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} dist
 * @param {number} hour
 * @return {number}
 */
var minSpeedOnTime = function(dist, hour) {
    
};
```

### TypeScript

```typescript
function minSpeedOnTime(dist: number[], hour: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $dist
     * @param Float $hour
     * @return Integer
     */
    function minSpeedOnTime($dist, $hour) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSpeedOnTime(_ dist: [Int], _ hour: Double) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSpeedOnTime(dist: IntArray, hour: Double): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSpeedOnTime(List<int> dist, double hour) {
    
  }
}
```

### Go

```golang
func minSpeedOnTime(dist []int, hour float64) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} dist
# @param {Float} hour
# @return {Integer}
def min_speed_on_time(dist, hour)
    
end
```

### Scala

```scala
object Solution {
    def minSpeedOnTime(dist: Array[Int], hour: Double): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_speed_on_time(dist: Vec<i32>, hour: f64) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-speed-on-time dist hour)
  (-> (listof exact-integer?) flonum? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_speed_on_time(Dist :: [integer()], Hour :: float()) -> integer().
min_speed_on_time(Dist, Hour) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_speed_on_time(dist :: [integer], hour :: float) :: integer
  def min_speed_on_time(dist, hour) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSpeedOnTime(dist: Array<Int64>, hour: Float64): Int64 {

    }
}
```

