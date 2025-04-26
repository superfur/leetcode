# 2332. 坐上公交的最晚时间

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>buses</code>&nbsp;，其中&nbsp;<code>buses[i]</code>&nbsp;表示第 <code>i</code>&nbsp;辆公交车的出发时间。同时给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>m</code>&nbsp;的整数数组&nbsp;<code>passengers</code>&nbsp;，其中&nbsp;<code>passengers[j]</code>&nbsp;表示第&nbsp;<code>j</code>&nbsp;位乘客的到达时间。所有公交车出发的时间互不相同，所有乘客到达的时间也互不相同。</p>

<p>给你一个整数&nbsp;<code>capacity</code>&nbsp;，表示每辆公交车&nbsp;<strong>最多</strong>&nbsp;能容纳的乘客数目。</p>

<p>每位乘客都会排队搭乘下一辆有座位的公交车。如果你在 <code>y</code>&nbsp;时刻到达，公交在&nbsp;<code>x</code>&nbsp;时刻出发，满足&nbsp;<code>y &lt;= x</code>&nbsp;&nbsp;且公交没有满，那么你可以搭乘这一辆公交。<strong>最早</strong>&nbsp;到达的乘客优先上车。</p>

<p>返回你可以搭乘公交车的最晚到达公交站时间。你 <strong>不能</strong>&nbsp;跟别的乘客同时刻到达。</p>

<p><strong>注意：</strong>数组&nbsp;<code>buses</code> 和&nbsp;<code>passengers</code>&nbsp;不一定是有序的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>buses = [10,20], passengers = [2,17,18,19], capacity = 2
<b>输出：</b>16
<strong>解释：</strong>
第 1 辆公交车载着第 1 位乘客。
第 2 辆公交车载着你和第 2 位乘客。
注意你不能跟其他乘客同一时间到达，所以你必须在第二位乘客之前到达。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
<b>输出：</b>20
<b>解释：</b>
第 1 辆公交车载着第 4 位乘客。
第 2 辆公交车载着第 6 位和第 2 位乘客。
第 3 辆公交车载着第 1 位乘客和你。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == buses.length</code></li>
	<li><code>m == passengers.length</code></li>
	<li><code>1 &lt;= n, m, capacity &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= buses[i], passengers[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>buses</code>&nbsp;中的元素 <strong>互不相同&nbsp;</strong>。</li>
	<li><code>passengers</code>&nbsp;中的元素 <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. Sort the buses and passengers arrays.
2. Use 2 pointers to traverse buses and passengers with a simulation of passengers getting on a particular bus.

## 示例

```
[10,20]
[2,17,18,19]
2
[20,30,10]
[19,13,26,4,25,11,21]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int latestTimeCatchTheBus(vector<int>& buses, vector<int>& passengers, int capacity) {
        
    }
};
```

### Java

```java
class Solution {
    public int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        
    }
}
```

### Python

```python
class Solution(object):
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        """
        :type buses: List[int]
        :type passengers: List[int]
        :type capacity: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        
```

### C

```c
int latestTimeCatchTheBus(int* buses, int busesSize, int* passengers, int passengersSize, int capacity) {
    
}
```

### C#

```csharp
public class Solution {
    public int LatestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} buses
 * @param {number[]} passengers
 * @param {number} capacity
 * @return {number}
 */
var latestTimeCatchTheBus = function(buses, passengers, capacity) {
    
};
```

### TypeScript

```typescript
function latestTimeCatchTheBus(buses: number[], passengers: number[], capacity: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $buses
     * @param Integer[] $passengers
     * @param Integer $capacity
     * @return Integer
     */
    function latestTimeCatchTheBus($buses, $passengers, $capacity) {
        
    }
}
```

### Swift

```swift
class Solution {
    func latestTimeCatchTheBus(_ buses: [Int], _ passengers: [Int], _ capacity: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun latestTimeCatchTheBus(buses: IntArray, passengers: IntArray, capacity: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int latestTimeCatchTheBus(List<int> buses, List<int> passengers, int capacity) {
    
  }
}
```

### Go

```golang
func latestTimeCatchTheBus(buses []int, passengers []int, capacity int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} buses
# @param {Integer[]} passengers
# @param {Integer} capacity
# @return {Integer}
def latest_time_catch_the_bus(buses, passengers, capacity)
    
end
```

### Scala

```scala
object Solution {
    def latestTimeCatchTheBus(buses: Array[Int], passengers: Array[Int], capacity: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn latest_time_catch_the_bus(buses: Vec<i32>, passengers: Vec<i32>, capacity: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (latest-time-catch-the-bus buses passengers capacity)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec latest_time_catch_the_bus(Buses :: [integer()], Passengers :: [integer()], Capacity :: integer()) -> integer().
latest_time_catch_the_bus(Buses, Passengers, Capacity) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec latest_time_catch_the_bus(buses :: [integer], passengers :: [integer], capacity :: integer) :: integer
  def latest_time_catch_the_bus(buses, passengers, capacity) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func latestTimeCatchTheBus(buses: Array<Int64>, passengers: Array<Int64>, capacity: Int64): Int64 {

    }
}
```

