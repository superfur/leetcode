# 436. 寻找右区间

## 题目描述

<p>给你一个区间数组 <code>intervals</code> ，其中&nbsp;<code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> ，且每个&nbsp;<code>start<sub>i</sub></code> 都 <strong>不同</strong> 。</p>

<p>区间 <code>i</code> 的 <strong>右侧区间</strong>&nbsp;是满足 <code>start<sub>j</sub>&nbsp;&gt;= end<sub>i</sub></code>，且 <code>start<sub>j</sub></code> <strong>最小&nbsp;</strong>的区间 <code>j</code>。注意 <code>i</code> 可能等于 <code>j</code> 。</p>

<p>返回一个由每个区间 <code>i</code>&nbsp;对应的 <strong>右侧区间</strong> 下标组成的数组。如果某个区间 <code>i</code> 不存在对应的 <strong>右侧区间</strong> ，则下标 <code>i</code> 处的值设为 <code>-1</code> 。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,2]]
<strong>输出：</strong>[-1]
<strong>解释：</strong>集合中只有一个区间，所以输出-1。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[3,4],[2,3],[1,2]]
<strong>输出：</strong>[-1,0,1]
<strong>解释：</strong>对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,4],[2,3],[3,4]]
<strong>输出：</strong>[-1,2,-1]
<strong>解释：</strong>对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;intervals.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>-10<sup>6</sup> &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>每个间隔的起点都 <strong>不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 排序

## 示例

```
[[1,2]]
[[3,4],[2,3],[1,2]]
[[1,4],[2,3],[3,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findRightInterval(int[][] intervals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findRightInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindRightInterval(int[][] intervals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var findRightInterval = function(intervals) {
    
};
```

### TypeScript

```typescript
function findRightInterval(intervals: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer[]
     */
    function findRightInterval($intervals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findRightInterval(_ intervals: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findRightInterval(intervals: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findRightInterval(List<List<int>> intervals) {
    
  }
}
```

### Go

```golang
func findRightInterval(intervals [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer[]}
def find_right_interval(intervals)
    
end
```

### Scala

```scala
object Solution {
    def findRightInterval(intervals: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-right-interval intervals)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_right_interval(Intervals :: [[integer()]]) -> [integer()].
find_right_interval(Intervals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_right_interval(intervals :: [[integer]]) :: [integer]
  def find_right_interval(intervals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findRightInterval(intervals: Array<Array<Int64>>): Array<Int64> {

    }
}
```

