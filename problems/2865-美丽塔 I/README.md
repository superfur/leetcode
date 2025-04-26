# 2865. 美丽塔 I

## 题目描述

<p>给定一个包含&nbsp;<code>n</code>&nbsp;个整数的数组&nbsp;<code>heights</code>&nbsp;表示&nbsp;<code>n</code>&nbsp;座连续的塔中砖块的数量。你的任务是移除一些砖块来形成一个 <strong>山脉状</strong> 的塔排列。在这种布置中，塔高度先是非递减，有一个或多个连续塔达到最大峰值，然后非递增排列。</p>

<p>返回满足山脉状塔排列的方案中，<strong>高度和的最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>maxHeights = [5,3,4,1,1]
<b>输出：</b>13
<b>解释：</b>我们移除一些砖块来形成 heights = [5,3,3,1,1]，峰值位于下标 0。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>maxHeights = [6,5,3,9,2,7]
<b>输出：</b>22
<strong>解释：</strong>我们移除一些砖块来形成 heights = [3,3,3,9,2,2]，峰值位于下标 3。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>maxHeights = [3,2,5,5,2,3]
<b>输出：</b>18
<strong>解释：</strong>我们移除一些砖块来形成 heights = [2,2,5,5,2,2]，峰值位于下标 2 或 3。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == heights.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= heights[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 单调栈

## 提示

1. Try all the possible indices <code>i</code> as the peak.
2. If <code>i</code> is the peak, <code>i-1<sup>th</sup></code> element, and <code>heights[j] = min(heights[j], heights[j + 1])</code> for <code>0 <= j < i </code>
3. If <code>i</code> is the peak, start from <code>i+1<sup>th</sup></code> element, heights[j] = min(heights[j], heights[j - 1]) for <code>i < j < heights.size()</code>

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
    long long maximumSumOfHeights(vector<int>& heights) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumSumOfHeights(int[] heights) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSumOfHeights(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        
```

### C

```c
long long maximumSumOfHeights(int* heights, int heightsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumSumOfHeights(int[] heights) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} heights
 * @return {number}
 */
var maximumSumOfHeights = function(heights) {
    
};
```

### TypeScript

```typescript
function maximumSumOfHeights(heights: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $heights
     * @return Integer
     */
    function maximumSumOfHeights($heights) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSumOfHeights(_ heights: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSumOfHeights(heights: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSumOfHeights(List<int> heights) {
    
  }
}
```

### Go

```golang
func maximumSumOfHeights(heights []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} heights
# @return {Integer}
def maximum_sum_of_heights(heights)
    
end
```

### Scala

```scala
object Solution {
    def maximumSumOfHeights(heights: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum_of_heights(heights: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum-of-heights heights)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_sum_of_heights(Heights :: [integer()]) -> integer().
maximum_sum_of_heights(Heights) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum_of_heights(heights :: [integer]) :: integer
  def maximum_sum_of_heights(heights) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSumOfHeights(heights: Array<Int64>): Int64 {

    }
}
```

