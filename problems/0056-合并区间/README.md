# 56. 合并区间

## 题目描述

<p>以数组 <code>intervals</code> 表示若干个区间的集合，其中单个区间为 <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 。请你合并所有重叠的区间，并返回&nbsp;<em>一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[2,6],[8,10],[15,18]]
<strong>输出：</strong>[[1,6],[8,10],[15,18]]
<strong>解释：</strong>区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[4,5]]
<strong>输出：</strong>[[1,5]]
<strong>解释：</strong>区间 [1,4] 和 [4,5] 可被视为重叠区间。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序

## 示例

```
[[1,3],[2,6],[8,10],[15,18]]
[[1,4],[4,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] merge(int[][] intervals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** merge(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] Merge(int[][] intervals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {
    
};
```

### TypeScript

```typescript
function merge(intervals: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer[][]
     */
    function merge($intervals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func merge(_ intervals: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun merge(intervals: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> merge(List<List<int>> intervals) {
    
  }
}
```

### Go

```golang
func merge(intervals [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer[][]}
def merge(intervals)
    
end
```

### Scala

```scala
object Solution {
    def merge(intervals: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (merge intervals)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec merge(Intervals :: [[integer()]]) -> [[integer()]].
merge(Intervals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec merge(intervals :: [[integer]]) :: [[integer]]
  def merge(intervals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func merge(intervals: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

