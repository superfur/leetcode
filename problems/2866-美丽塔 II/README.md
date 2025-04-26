# 2866. 美丽塔 II

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>maxHeights</code>&nbsp;。</p>

<p>你的任务是在坐标轴上建 <code>n</code>&nbsp;座塔。第&nbsp;<code>i</code>&nbsp;座塔的下标为 <code>i</code>&nbsp;，高度为&nbsp;<code>heights[i]</code>&nbsp;。</p>

<p>如果以下条件满足，我们称这些塔是 <strong>美丽</strong>&nbsp;的：</p>

<ol>
	<li><code>1 &lt;= heights[i] &lt;= maxHeights[i]</code></li>
	<li><code>heights</code>&nbsp;是一个 <strong>山脉</strong> 数组。</li>
</ol>

<p>如果存在下标 <code>i</code>&nbsp;满足以下条件，那么我们称数组&nbsp;<code>heights</code>&nbsp;是一个 <strong>山脉</strong> 数组：</p>

<ul>
	<li>对于所有&nbsp;<code>0 &lt; j &lt;= i</code>&nbsp;，都有&nbsp;<code>heights[j - 1] &lt;= heights[j]</code></li>
	<li>对于所有&nbsp;<code>i &lt;= k &lt; n - 1</code>&nbsp;，都有&nbsp;<code>heights[k + 1] &lt;= heights[k]</code></li>
</ul>

<p>请你返回满足 <b>美丽塔</b>&nbsp;要求的方案中，<strong>高度和的最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>maxHeights = [5,3,4,1,1]
<b>输出：</b>13
<b>解释：</b>和最大的美丽塔方案为 heights = [5,3,3,1,1] ，这是一个美丽塔方案，因为：
- 1 &lt;= heights[i] &lt;= maxHeights[i]  
- heights 是个山脉数组，峰值在 i = 0 处。
13 是所有美丽塔方案中的最大高度和。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>maxHeights = [6,5,3,9,2,7]
<b>输出：</b>22
<strong>解释：</strong> 和最大的美丽塔方案为 heights = [3,3,3,9,2,2] ，这是一个美丽塔方案，因为：
- 1 &lt;= heights[i] &lt;= maxHeights[i]
- heights 是个山脉数组，峰值在 i = 3 处。
22 是所有美丽塔方案中的最大高度和。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>maxHeights = [3,2,5,5,2,3]
<b>输出：</b>18
<strong>解释：</strong>和最大的美丽塔方案为 heights = [2,2,5,5,2,2] ，这是一个美丽塔方案，因为：
- 1 &lt;= heights[i] &lt;= maxHeights[i]
- heights 是个山脉数组，最大值在 i = 2 处。
注意，在这个方案中，i = 3 也是一个峰值。
18 是所有美丽塔方案中的最大高度和。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == maxHeights&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= maxHeights[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 单调栈

## 提示

1. Try all the possible indices <code>i</code> as the peak.
2. Let <code>left[i]</code> be the maximum sum of heights for the prefix <code>0, …, i</code> when index <code>i</code> is the peak.
3. Let <code>right[i]</code> be the maximum sum of heights for suffix <code>i, …, (n - 1)</code> when <code>i</code> is the peak
4. Compute values of <code>left[i]</code> from left to right using DP.
For each <code>i</code> from <code>0</code> to <code>n - 1</code>, <code>left[i] = maxHeights * (i - j) + answer[j]</code>, where <code>j</code> is the rightmost index to the left of <code>i</code> such that <code>maxHeights[j] < maxHeights[i] </code>.
5. For each <code>i</code> from <code>n - 1</code> to <code>0</code>, <code>right[i] = maxHeights * (j - i) + answer[j]</code>, where <code>j</code> is the leftmost index to the right of <code>i</code> such that <code>maxHeights[j] < maxHeights[i] </code>.

## 示例

```
[5,3,4,1,1]
[6,5,3,9,2,7]
[3,2,5,5,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumSumOfHeights(vector<int>& maxHeights) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumSumOfHeights(List<Integer> maxHeights) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSumOfHeights(self, maxHeights):
        """
        :type maxHeights: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
```

### C

```c
long long maximumSumOfHeights(int* maxHeights, int maxHeightsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumSumOfHeights(IList<int> maxHeights) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} maxHeights
 * @return {number}
 */
var maximumSumOfHeights = function(maxHeights) {
    
};
```

### TypeScript

```typescript
function maximumSumOfHeights(maxHeights: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $maxHeights
     * @return Integer
     */
    function maximumSumOfHeights($maxHeights) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSumOfHeights(_ maxHeights: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSumOfHeights(maxHeights: List<Int>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSumOfHeights(List<int> maxHeights) {
    
  }
}
```

### Go

```golang
func maximumSumOfHeights(maxHeights []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} max_heights
# @return {Integer}
def maximum_sum_of_heights(max_heights)
    
end
```

### Scala

```scala
object Solution {
    def maximumSumOfHeights(maxHeights: List[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum_of_heights(max_heights: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum-of-heights maxHeights)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_sum_of_heights(MaxHeights :: [integer()]) -> integer().
maximum_sum_of_heights(MaxHeights) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum_of_heights(max_heights :: [integer]) :: integer
  def maximum_sum_of_heights(max_heights) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSumOfHeights(maxHeights: ArrayList<Int64>): Int64 {

    }
}
```

