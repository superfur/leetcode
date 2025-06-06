# 1943. 描述绘画结果

## 题目描述

<p>给你一个细长的画，用数轴表示。这幅画由若干有重叠的线段表示，每个线段有 <strong>独一无二</strong>&nbsp;的颜色。给你二维整数数组&nbsp;<code>segments</code>&nbsp;，其中&nbsp;<code>segments[i] = [start<sub>i</sub>, end<sub>i</sub>, color<sub>i</sub>]</code>&nbsp;表示线段为&nbsp;<strong>半开区间</strong>&nbsp;<code>[start<sub>i</sub>, end<sub>i</sub>)</code> 且颜色为&nbsp;<code>color<sub>i</sub></code>&nbsp;。</p>

<p>线段间重叠部分的颜色会被 <strong>混合</strong>&nbsp;。如果有两种或者更多颜色混合时，它们会形成一种新的颜色，用一个 <strong>集合</strong>&nbsp;表示这个混合颜色。</p>

<ul>
	<li>比方说，如果颜色&nbsp;<code>2</code>&nbsp;，<code>4</code>&nbsp;和&nbsp;<code>6</code>&nbsp;被混合，那么结果颜色为&nbsp;<code>{2,4,6}</code>&nbsp;。</li>
</ul>

<p>为了简化题目，你不需要输出整个集合，只需要用集合中所有元素的 <strong>和</strong>&nbsp;来表示颜色集合。</p>

<p>你想要用 <strong>最少数目</strong>&nbsp;不重叠 <strong>半开区间</strong>&nbsp;来 <b>表示</b>&nbsp;这幅混合颜色的画。这些线段可以用二维数组&nbsp;<code>painting</code>&nbsp;表示，其中 <code>painting[j] = [left<sub>j</sub>, right<sub>j</sub>, mix<sub>j</sub>]</code>&nbsp;表示一个&nbsp;<strong>半开区间</strong><code>[left<sub>j</sub>, right<sub>j</sub>)</code>&nbsp;的颜色 <strong>和</strong>&nbsp;为&nbsp;<code>mix<sub>j</sub></code>&nbsp;。</p>

<ul>
	<li>比方说，这幅画由&nbsp;<code>segments = [[1,4,5],[1,7,7]]</code>&nbsp;组成，那么它可以表示为&nbsp;<code>painting = [[1,4,12],[4,7,7]]</code>&nbsp;，因为：

	<ul>
		<li><code>[1,4)</code>&nbsp;由颜色&nbsp;<code>{5,7}</code>&nbsp;组成（和为&nbsp;<code>12</code>），分别来自第一个线段和第二个线段。</li>
		<li><code>[4,7)</code>&nbsp;由颜色 <code>{7}</code>&nbsp;组成，来自第二个线段。</li>
	</ul>
	</li>
</ul>

<p>请你返回二维数组&nbsp;<code>painting</code>&nbsp;，它表示最终绘画的结果（<strong>没有</strong>&nbsp;被涂色的部分不出现在结果中）。你可以按 <strong>任意顺序</strong> 返回最终数组的结果。</p>

<p><strong>半开区间&nbsp;</strong><code>[a, b)</code>&nbsp;是数轴上点&nbsp;<code>a</code> 和点&nbsp;<code>b</code>&nbsp;之间的部分，<strong>包含 </strong>点&nbsp;<code>a</code>&nbsp;且 <strong>不包含</strong>&nbsp;点&nbsp;<code>b</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/18/1.png" style="width: 529px; height: 241px;" />
<pre>
<b>输入：</b>segments = [[1,4,5],[4,7,7],[1,7,9]]
<b>输出：</b>[[1,4,14],[4,7,16]]
<strong>解释：</strong>绘画结果可以表示为：
- [1,4) 颜色为 {5,9} （和为 14），分别来自第一和第二个线段。
- [4,7) 颜色为 {7,9} （和为 16），分别来自第二和第三个线段。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/18/2.png" style="width: 532px; height: 219px;" />
<pre>
<b>输入：</b>segments = [[1,7,9],[6,8,15],[8,10,7]]
<b>输出：</b>[[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
<b>解释：</b>绘画结果可以以表示为：
- [1,6) 颜色为 9 ，来自第一个线段。
- [6,7) 颜色为 {9,15} （和为 24），来自第一和第二个线段。
- [7,8) 颜色为 15 ，来自第二个线段。
- [8,10) 颜色为 7 ，来自第三个线段。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/04/c1.png" style="width: 529px; height: 289px;" />
<pre>
<b>输入：</b>segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
<b>输出：</b>[[1,4,12],[4,7,12]]
<strong>解释：</strong>绘画结果可以表示为：
- [1,4) 颜色为 {5,7} （和为 12），分别来自第一和第二个线段。
- [4,7) 颜色为 {1,11} （和为 12），分别来自第三和第四个线段。
注意，只返回一个单独的线段 [1,7) 是不正确的，因为混合颜色的集合不相同。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= segments.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>segments[i].length == 3</code></li>
	<li><code>1 &lt;= start<sub>i</sub> &lt; end<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= color<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li>每种颜色&nbsp;<code>color<sub>i</sub></code>&nbsp;互不相同。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和
- 排序

## 提示

1. Can we sort the segments in a way to help solve the problem?
2. How can we dynamically keep track of the sum of the current segment(s)?

## 示例

```
[[1,4,5],[4,7,7],[1,7,9]]
[[1,7,9],[6,8,15],[8,10,7]]
[[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<long long>> splitPainting(vector<vector<int>>& segments) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Long>> splitPainting(int[][] segments) {
        
    }
}
```

### Python

```python
class Solution(object):
    def splitPainting(self, segments):
        """
        :type segments: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
long long** splitPainting(int** segments, int segmentsSize, int* segmentsColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<long>> SplitPainting(int[][] segments) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} segments
 * @return {number[][]}
 */
var splitPainting = function(segments) {
    
};
```

### TypeScript

```typescript
function splitPainting(segments: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $segments
     * @return Integer[][]
     */
    function splitPainting($segments) {
        
    }
}
```

### Swift

```swift
class Solution {
    func splitPainting(_ segments: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitPainting(segments: Array<IntArray>): List<List<Long>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> splitPainting(List<List<int>> segments) {
    
  }
}
```

### Go

```golang
func splitPainting(segments [][]int) [][]int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} segments
# @return {Integer[][]}
def split_painting(segments)
    
end
```

### Scala

```scala
object Solution {
    def splitPainting(segments: Array[Array[Int]]): List[List[Long]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_painting(segments: Vec<Vec<i32>>) -> Vec<Vec<i64>> {
        
    }
}
```

### Racket

```racket
(define/contract (split-painting segments)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec split_painting(Segments :: [[integer()]]) -> [[integer()]].
split_painting(Segments) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec split_painting(segments :: [[integer]]) :: [[integer]]
  def split_painting(segments) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func splitPainting(segments: Array<Array<Int64>>): ArrayList<ArrayList<Int64>> {

    }
}
```

