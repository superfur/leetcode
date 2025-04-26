# 1288. 删除被覆盖区间

## 题目描述

<p>给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。</p>

<p>只有当&nbsp;<code>c &lt;= a</code>&nbsp;且&nbsp;<code>b &lt;= d</code>&nbsp;时，我们才认为区间&nbsp;<code>[a,b)</code> 被区间&nbsp;<code>[c,d)</code> 覆盖。</p>

<p>在完成所有删除操作后，请你返回列表中剩余区间的数目。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[3,6],[2,8]]
<strong>输出：</strong>2
<strong>解释：</strong>区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong>​​​​​​</p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 1000</code></li>
	<li><code>0 &lt;= intervals[i][0] &lt;&nbsp;intervals[i][1] &lt;= 10^5</code></li>
	<li>对于所有的&nbsp;<code>i != j</code>：<code>intervals[i] != intervals[j]</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序

## 提示

1. How to check if an interval is covered by another?
2. Compare each interval to all others and check if it is covered by any interval.

## 示例

```
[[1,4],[3,6],[2,8]]
[[1,4],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        
    }
};
```

### Java

```java
class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
```

### C

```c
int removeCoveredIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int RemoveCoveredIntervals(int[][] intervals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var removeCoveredIntervals = function(intervals) {
    
};
```

### TypeScript

```typescript
function removeCoveredIntervals(intervals: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function removeCoveredIntervals($intervals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeCoveredIntervals(_ intervals: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeCoveredIntervals(intervals: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int removeCoveredIntervals(List<List<int>> intervals) {
    
  }
}
```

### Go

```golang
func removeCoveredIntervals(intervals [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer}
def remove_covered_intervals(intervals)
    
end
```

### Scala

```scala
object Solution {
    def removeCoveredIntervals(intervals: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_covered_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (remove-covered-intervals intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec remove_covered_intervals(Intervals :: [[integer()]]) -> integer().
remove_covered_intervals(Intervals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_covered_intervals(intervals :: [[integer]]) :: integer
  def remove_covered_intervals(intervals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeCoveredIntervals(intervals: Array<Array<Int64>>): Int64 {

    }
}
```

