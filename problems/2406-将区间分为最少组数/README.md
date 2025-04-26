# 2406. 将区间分为最少组数

## 题目描述

<p>给你一个二维整数数组&nbsp;<code>intervals</code>&nbsp;，其中&nbsp;<code>intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;表示 <strong>闭</strong>&nbsp;区间&nbsp;<code>[left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;。</p>

<p>你需要将&nbsp;<code>intervals</code> 划分为一个或者多个区间&nbsp;<strong>组</strong>&nbsp;，每个区间 <b>只</b>&nbsp;属于一个组，且同一个组中任意两个区间 <strong>不相交</strong>&nbsp;。</p>

<p>请你返回 <strong>最少</strong>&nbsp;需要划分成多少个组。</p>

<p>如果两个区间覆盖的范围有重叠（即至少有一个公共数字），那么我们称这两个区间是 <strong>相交</strong>&nbsp;的。比方说区间&nbsp;<code>[1, 5]</code> 和&nbsp;<code>[5, 8]</code>&nbsp;相交。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
<b>输出：</b>3
<b>解释：</b>我们可以将区间划分为如下的区间组：
- 第 1 组：[1, 5] ，[6, 8] 。
- 第 2 组：[2, 3] ，[5, 10] 。
- 第 3 组：[1, 10] 。
可以证明无法将区间划分为少于 3 个组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>intervals = [[1,3],[5,6],[8,10],[11,13]]
<b>输出：</b>1
<b>解释：</b>所有区间互不相交，所以我们可以把它们全部放在一个组内。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 前缀和
- 排序
- 堆（优先队列）

## 提示

1. Can you find a different way to describe the question?
2. The minimum number of groups we need is equivalent to the maximum number of intervals that overlap at some point. How can you find that?

## 示例

```
[[5,10],[6,8],[1,5],[2,3],[1,10]]
[[1,3],[5,6],[8,10],[11,13]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minGroups(vector<vector<int>>& intervals) {
        
    }
};
```

### Java

```java
class Solution {
    public int minGroups(int[][] intervals) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
```

### C

```c
int minGroups(int** intervals, int intervalsSize, int* intervalsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinGroups(int[][] intervals) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} intervals
 * @return {number}
 */
var minGroups = function(intervals) {
    
};
```

### TypeScript

```typescript
function minGroups(intervals: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $intervals
     * @return Integer
     */
    function minGroups($intervals) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minGroups(_ intervals: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minGroups(intervals: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minGroups(List<List<int>> intervals) {
    
  }
}
```

### Go

```golang
func minGroups(intervals [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} intervals
# @return {Integer}
def min_groups(intervals)
    
end
```

### Scala

```scala
object Solution {
    def minGroups(intervals: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_groups(intervals: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-groups intervals)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_groups(Intervals :: [[integer()]]) -> integer().
min_groups(Intervals) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_groups(intervals :: [[integer]]) :: integer
  def min_groups(intervals) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minGroups(intervals: Array<Array<Int64>>): Int64 {

    }
}
```

