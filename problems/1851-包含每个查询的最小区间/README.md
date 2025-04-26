# 1851. 包含每个查询的最小区间

## 题目描述

<p>给你一个二维整数数组 <code>intervals</code> ，其中 <code>intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> 表示第 <code>i</code> 个区间开始于 <code>left<sub>i</sub></code> 、结束于 <code>right<sub>i</sub></code>（包含两侧取值，<strong>闭区间</strong>）。区间的 <strong>长度</strong> 定义为区间中包含的整数数目，更正式地表达是 <code>right<sub>i</sub> - left<sub>i</sub> + 1</code> 。</p>

<p>再给你一个整数数组 <code>queries</code> 。第 <code>j</code> 个查询的答案是满足&nbsp;<code>left<sub>i</sub> &lt;= queries[j] &lt;= right<sub>i</sub></code> 的 <strong>长度最小区间 <code>i</code> 的长度</strong> 。如果不存在这样的区间，那么答案是 <code>-1</code> 。</p>

<p>以数组形式返回对应查询的所有答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
<strong>输出：</strong>[3,3,1,4]
<strong>解释：</strong>查询处理如下：
- Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
- Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
<strong>输出：</strong>[2,-1,4,6]
<strong>解释：</strong>查询处理如下：
- Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
- Query = 19：不存在包含 19 的区间，答案为 -1 。
- Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
- Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= queries[j] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 排序
- 扫描线
- 堆（优先队列）

## 提示

1. Is there a way to order the intervals and queries such that it takes less time to query?
2. Is there a way to add and remove intervals by going from the smallest query to the largest query to find the minimum size?

## 示例

```
[[1,4],[2,4],[3,6],[4,4]]
[2,3,4,5]
[[2,3],[2,5],[1,8],[20,25]]
[2,19,5,22]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] minInterval(int[][] intervals, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MinInterval(int[][] intervals, int[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @param {number[]} queries
 * @return {number[]}
 */
var minInterval = function(intervals, queries) {
    
};
```

### TypeScript

```typescript
function minInterval(intervals: number[][], queries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @param Integer[] $queries
     * @return Integer[]
     */
    function minInterval($intervals, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minInterval(_ intervals: [[Int]], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minInterval(intervals: Array<IntArray>, queries: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minInterval(List<List<int>> intervals, List<int> queries) {
    
  }
}
```

### Go

```golang
func minInterval(intervals [][]int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @param {Integer[]} queries
# @return {Integer[]}
def min_interval(intervals, queries)
    
end
```

### Scala

```scala
object Solution {
    def minInterval(intervals: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_interval(intervals: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (min-interval intervals queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_interval(Intervals :: [[integer()]], Queries :: [integer()]) -> [integer()].
min_interval(Intervals, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_interval(intervals :: [[integer]], queries :: [integer]) :: [integer]
  def min_interval(intervals, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minInterval(intervals: Array<Array<Int64>>, queries: Array<Int64>): Array<Int64> {

    }
}
```

