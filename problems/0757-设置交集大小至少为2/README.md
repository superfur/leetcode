# 757. 设置交集大小至少为2

## 题目描述

<p>给你一个二维整数数组 <code>intervals</code> ，其中 <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> 表示从 <code>start<sub>i</sub></code> 到 <code>end<sub>i</sub></code> 的所有整数，包括 <code>start<sub>i</sub></code> 和 <code>end<sub>i</sub></code> 。</p>

<p><strong>包含集合</strong> 是一个名为 <code>nums</code> 的数组，并满足 <code>intervals</code> 中的每个区间都 <strong>至少</strong> 有 <strong>两个</strong> 整数在 <code>nums</code> 中。</p>

<ul>
	<li>例如，如果 <code>intervals = [[1,3], [3,7], [8,9]]</code> ，那么 <code>[1,2,4,7,8,9]</code> 和 <code>[2,3,4,8,9]</code> 都符合 <strong>包含集合</strong> 的定义。</li>
</ul>

<p>返回包含集合可能的最小大小。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[3,7],[8,9]]
<strong>输出：</strong>5
<strong>解释：</strong>nums = [2, 3, 4, 8, 9].
可以证明不存在元素数量为 4 的包含集合。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,3],[1,4],[2,5],[3,5]]
<strong>输出：</strong>3
<strong>解释：</strong>nums = [2, 3, 4].
可以证明不存在元素数量为 2 的包含集合。 
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>intervals = [[1,2],[2,3],[2,4],[4,5]]
<strong>输出：</strong>5
<strong>解释：</strong>nums = [1, 2, 3, 4, 5].
可以证明不存在元素数量为 4 的包含集合。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 3000</code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 排序

## 示例

```
[[1,3],[3,7],[8,9]]
[[1,3],[1,4],[2,5],[3,5]]
[[1,2],[2,3],[2,4],[4,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        
    }
};
```

### Java

```java
class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
```

### C

```c
int intersectionSizeTwo(int** intervals, int intervalsSize, int* intervalsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int IntersectionSizeTwo(int[][] intervals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    
};
```

### TypeScript

```typescript
function intersectionSizeTwo(intervals: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function intersectionSizeTwo($intervals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func intersectionSizeTwo(_ intervals: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int intersectionSizeTwo(List<List<int>> intervals) {
    
  }
}
```

### Go

```golang
func intersectionSizeTwo(intervals [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer}
def intersection_size_two(intervals)
    
end
```

### Scala

```scala
object Solution {
    def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn intersection_size_two(intervals: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (intersection-size-two intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec intersection_size_two(Intervals :: [[integer()]]) -> integer().
intersection_size_two(Intervals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec intersection_size_two(intervals :: [[integer]]) :: integer
  def intersection_size_two(intervals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func intersectionSizeTwo(intervals: Array<Array<Int64>>): Int64 {

    }
}
```

