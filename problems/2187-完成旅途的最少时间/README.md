# 2187. 完成旅途的最少时间

## 题目描述

<p>给你一个数组&nbsp;<code>time</code>&nbsp;，其中&nbsp;<code>time[i]</code>&nbsp;表示第 <code>i</code>&nbsp;辆公交车完成 <strong>一趟</strong><strong>旅途</strong>&nbsp;所需要花费的时间。</p>

<p>每辆公交车可以 <strong>连续</strong> 完成多趟旅途，也就是说，一辆公交车当前旅途完成后，可以 <strong>立马开始</strong>&nbsp;下一趟旅途。每辆公交车 <strong>独立</strong>&nbsp;运行，也就是说可以同时有多辆公交车在运行且互不影响。</p>

<p>给你一个整数&nbsp;<code>totalTrips</code>&nbsp;，表示所有公交车&nbsp;<strong>总共</strong>&nbsp;需要完成的旅途数目。请你返回完成 <strong>至少</strong>&nbsp;<code>totalTrips</code>&nbsp;趟旅途需要花费的 <strong>最少</strong>&nbsp;时间。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>time = [1,2,3], totalTrips = 5
<b>输出：</b>3
<strong>解释：</strong>
- 时刻 t = 1 ，每辆公交车完成的旅途数分别为 [1,0,0] 。
  已完成的总旅途数为 1 + 0 + 0 = 1 。
- 时刻 t = 2 ，每辆公交车完成的旅途数分别为 [2,1,0] 。
  已完成的总旅途数为 2 + 1 + 0 = 3 。
- 时刻 t = 3 ，每辆公交车完成的旅途数分别为 [3,1,1] 。
  已完成的总旅途数为 3 + 1 + 1 = 5 。
所以总共完成至少 5 趟旅途的最少时间为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>time = [2], totalTrips = 1
<b>输出：</b>2
<strong>解释：</strong>
只有一辆公交车，它将在时刻 t = 2 完成第一趟旅途。
所以完成 1 趟旅途的最少时间为 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= time[i], totalTrips &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. For a given amount of time, how can we count the total number of trips completed by all buses within that time?
2. Consider using binary search.

## 示例

```
[1,2,3]
5
[2]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumTime(vector<int>& time, int totalTrips) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumTime(int[] time, int totalTrips) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTime(self, time, totalTrips):
        """
        :type time: List[int]
        :type totalTrips: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
```

### C

```c
long long minimumTime(int* time, int timeSize, int totalTrips) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumTime(int[] time, int totalTrips) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number} totalTrips
 * @return {number}
 */
var minimumTime = function(time, totalTrips) {
    
};
```

### TypeScript

```typescript
function minimumTime(time: number[], totalTrips: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer $totalTrips
     * @return Integer
     */
    function minimumTime($time, $totalTrips) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTime(_ time: [Int], _ totalTrips: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTime(time: IntArray, totalTrips: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTime(List<int> time, int totalTrips) {
    
  }
}
```

### Go

```golang
func minimumTime(time []int, totalTrips int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} time
# @param {Integer} total_trips
# @return {Integer}
def minimum_time(time, total_trips)
    
end
```

### Scala

```scala
object Solution {
    def minimumTime(time: Array[Int], totalTrips: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_time(time: Vec<i32>, total_trips: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-time time totalTrips)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_time(Time :: [integer()], TotalTrips :: integer()) -> integer().
minimum_time(Time, TotalTrips) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_time(time :: [integer], total_trips :: integer) :: integer
  def minimum_time(time, total_trips) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTime(time: Array<Int64>, totalTrips: Int64): Int64 {

    }
}
```

