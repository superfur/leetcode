# 57. 插入区间

## 题目描述

<p>给你一个<strong> 无重叠的</strong><em> ，</em>按照区间起始端点排序的区间列表 <code>intervals</code>，其中&nbsp;<code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个区间的开始和结束，并且&nbsp;<code>intervals</code>&nbsp;按照&nbsp;<code>start<sub>i</sub></code>&nbsp;升序排列。同样给定一个区间&nbsp;<code>newInterval = [start, end]</code>&nbsp;表示另一个区间的开始和结束。</p>

<p>在&nbsp;<code>intervals</code> 中插入区间&nbsp;<code>newInterval</code>，使得&nbsp;<code>intervals</code>&nbsp;依然按照&nbsp;<code>start<sub>i</sub></code>&nbsp;升序排列，且区间之间不重叠（如果有必要的话，可以合并区间）。</p>

<p>返回插入之后的&nbsp;<code>intervals</code>。</p>

<p><strong>注意</strong> 你不需要原地修改&nbsp;<code>intervals</code>。你可以创建一个新数组然后返回它。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>输出：</strong>[[1,5],[6,9]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>输出：</strong>[[1,2],[3,10],[12,16]]
<strong>解释：</strong>这是因为新的区间 <code>[4,8]</code> 与 <code>[3,5],[6,7],[8,10]</code>&nbsp;重叠。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;=&nbsp;start<sub>i</sub> &lt;=&nbsp;end<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals</code> 根据 <code>start<sub>i</sub></code> 按 <strong>升序</strong> 排列</li>
	<li><code>newInterval.length == 2</code></li>
	<li><code>0 &lt;=&nbsp;start &lt;=&nbsp;end &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 提示

1. Intervals Array is sorted. Can you use Binary Search to find the correct position to insert the new Interval.?
2. Can you try merging the overlapping intervals while inserting the new interval?
3. This can be done by comparing the end of the last interval with the start of the new interval and vice versa.

## 示例

```
[[1,3],[6,9]]
[2,5]
[[1,2],[3,5],[6,7],[8,10],[12,16]]
[4,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
    }
}
```

### Python

```python
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** insert(int** intervals, int intervalsSize, int* intervalsColSize, int* newInterval, int newIntervalSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] Insert(int[][] intervals, int[] newInterval) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */
var insert = function(intervals, newInterval) {
    
};
```

### TypeScript

```typescript
function insert(intervals: number[][], newInterval: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @param Integer[] $newInterval
     * @return Integer[][]
     */
    function insert($intervals, $newInterval) {
        
    }
}
```

### Swift

```swift
class Solution {
    func insert(_ intervals: [[Int]], _ newInterval: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun insert(intervals: Array<IntArray>, newInterval: IntArray): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> insert(List<List<int>> intervals, List<int> newInterval) {
    
  }
}
```

### Go

```golang
func insert(intervals [][]int, newInterval []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @param {Integer[]} new_interval
# @return {Integer[][]}
def insert(intervals, new_interval)
    
end
```

### Scala

```scala
object Solution {
    def insert(intervals: Array[Array[Int]], newInterval: Array[Int]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (insert intervals newInterval)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec insert(Intervals :: [[integer()]], NewInterval :: [integer()]) -> [[integer()]].
insert(Intervals, NewInterval) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec insert(intervals :: [[integer]], new_interval :: [integer]) :: [[integer]]
  def insert(intervals, new_interval) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func insert(intervals: Array<Array<Int64>>, newInterval: Array<Int64>): Array<Array<Int64>> {

    }
}
```

