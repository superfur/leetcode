# 1450. 在既定时间做作业的学生人数

## 题目描述

<p>给你两个整数数组 <code>startTime</code>（开始时间）和 <code>endTime</code>（结束时间），并指定一个整数 <code>queryTime</code> 作为查询时间。</p>

<p>已知，第 <code>i</code> 名学生在 <code>startTime[i]</code> 时开始写作业并于 <code>endTime[i]</code> 时完成作业。</p>

<p>请返回在查询时间 <code>queryTime</code> 时正在做作业的学生人数。形式上，返回能够使 <code>queryTime</code> 处于区间 <code>[startTime[i], endTime[i]]</code>（含）的学生人数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
<strong>输出：</strong>1
<strong>解释：</strong>一共有 3 名学生。
第一名学生在时间 1 开始写作业，并于时间 3 完成作业，在时间 4 没有处于做作业的状态。
第二名学生在时间 2 开始写作业，并于时间 2 完成作业，在时间 4 没有处于做作业的状态。
第三名学生在时间 3 开始写作业，预计于时间 7 完成作业，这是是唯一一名在时间 4 时正在做作业的学生。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>startTime = [4], endTime = [4], queryTime = 4
<strong>输出：</strong>1
<strong>解释：</strong>在查询时间只有一名学生在做作业。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>startTime = [4], endTime = [4], queryTime = 5
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
<strong>输出：</strong>0
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>startTime.length == endTime.length</code></li>
	<li><code>1 &lt;= startTime.length &lt;= 100</code></li>
	<li><code>1 &lt;= startTime[i] &lt;= endTime[i] &lt;= 1000</code></li>
	<li><code>1 &lt;=&nbsp;queryTime &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Imagine that startTime[i] and endTime[i] form an interval (i.e. [startTime[i], endTime[i]]).
2. The answer is how many times the queryTime laid in those mentioned intervals.

## 示例

```
[1,2,3]
[3,2,7]
4
[4]
[4]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int busyStudent(int[] startTime, int[] endTime, int queryTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        
```

### C

```c
int busyStudent(int* startTime, int startTimeSize, int* endTime, int endTimeSize, int queryTime) {
    
}
```

### C#

```csharp
public class Solution {
    public int BusyStudent(int[] startTime, int[] endTime, int queryTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} startTime
 * @param {number[]} endTime
 * @param {number} queryTime
 * @return {number}
 */
var busyStudent = function(startTime, endTime, queryTime) {
    
};
```

### TypeScript

```typescript
function busyStudent(startTime: number[], endTime: number[], queryTime: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $startTime
     * @param Integer[] $endTime
     * @param Integer $queryTime
     * @return Integer
     */
    function busyStudent($startTime, $endTime, $queryTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func busyStudent(_ startTime: [Int], _ endTime: [Int], _ queryTime: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun busyStudent(startTime: IntArray, endTime: IntArray, queryTime: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int busyStudent(List<int> startTime, List<int> endTime, int queryTime) {
    
  }
}
```

### Go

```golang
func busyStudent(startTime []int, endTime []int, queryTime int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} start_time
# @param {Integer[]} end_time
# @param {Integer} query_time
# @return {Integer}
def busy_student(start_time, end_time, query_time)
    
end
```

### Scala

```scala
object Solution {
    def busyStudent(startTime: Array[Int], endTime: Array[Int], queryTime: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn busy_student(start_time: Vec<i32>, end_time: Vec<i32>, query_time: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (busy-student startTime endTime queryTime)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec busy_student(StartTime :: [integer()], EndTime :: [integer()], QueryTime :: integer()) -> integer().
busy_student(StartTime, EndTime, QueryTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec busy_student(start_time :: [integer], end_time :: [integer], query_time :: integer) :: integer
  def busy_student(start_time, end_time, query_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func busyStudent(startTime: Array<Int64>, endTime: Array<Int64>, queryTime: Int64): Int64 {

    }
}
```

