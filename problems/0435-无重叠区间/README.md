# 435. 无重叠区间

## 题目描述

<p>给定一个区间的集合&nbsp;<code>intervals</code>&nbsp;，其中 <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;。返回 <em>需要移除区间的最小数量，使剩余区间互不重叠&nbsp;</em>。</p>

<p><strong>注意</strong>&nbsp;只在一点上接触的区间是&nbsp;<strong>不重叠的</strong>。例如&nbsp;<code>[1, 2]</code>&nbsp;和&nbsp;<code>[2, 3]</code>&nbsp;是不重叠的。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> intervals = [[1,2],[2,3],[3,4],[1,3]]
<strong>输出:</strong> 1
<strong>解释:</strong> 移除 [1,3] 后，剩下的区间没有重叠。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> intervals = [ [1,2], [1,2], [1,2] ]
<strong>输出:</strong> 2
<strong>解释:</strong> 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> intervals = [ [1,2], [2,3] ]
<strong>输出:</strong> 0
<strong>解释:</strong> 你不需要移除任何区间，因为它们已经是无重叠的了。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-5 * 10<sup>4</sup>&nbsp;&lt;= start<sub>i</sub>&nbsp;&lt; end<sub>i</sub>&nbsp;&lt;= 5 * 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划
- 排序

## 示例

```
[[1,2],[2,3],[3,4],[1,3]]
[[1,2],[1,2],[1,2]]
[[1,2],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        
    }
};
```

### Java

```java
class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
```

### C

```c
int eraseOverlapIntervals(int** intervals, int intervalsSize, int* intervalsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EraseOverlapIntervals(int[][] intervals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var eraseOverlapIntervals = function(intervals) {
    
};
```

### TypeScript

```typescript
function eraseOverlapIntervals(intervals: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function eraseOverlapIntervals($intervals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun eraseOverlapIntervals(intervals: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int eraseOverlapIntervals(List<List<int>> intervals) {
    
  }
}
```

### Go

```golang
func eraseOverlapIntervals(intervals [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer}
def erase_overlap_intervals(intervals)
    
end
```

### Scala

```scala
object Solution {
    def eraseOverlapIntervals(intervals: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (erase-overlap-intervals intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec erase_overlap_intervals(Intervals :: [[integer()]]) -> integer().
erase_overlap_intervals(Intervals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec erase_overlap_intervals(intervals :: [[integer]]) :: integer
  def erase_overlap_intervals(intervals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func eraseOverlapIntervals(intervals: Array<Array<Int64>>): Int64 {

    }
}
```

