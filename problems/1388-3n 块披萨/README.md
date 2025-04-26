# 1388. 3n 块披萨

## 题目描述

<p>给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：</p>

<ul>
	<li>你挑选 <strong>任意</strong>&nbsp;一块披萨。</li>
	<li>Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。</li>
	<li>Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。</li>
	<li>重复上述过程直到没有披萨剩下。</li>
</ul>

<p>每一块披萨的大小按顺时针方向由循环数组 <code>slices</code>&nbsp;表示。</p>

<p>请你返回你可以获得的披萨大小总和的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/sample_3_1723.png" style="height: 240px; width: 475px;" /></p>

<pre>
<strong>输入：</strong>slices = [1,2,3,4,5,6]
<strong>输出：</strong>10
<strong>解释：</strong>选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/sample_4_1723.png" style="height: 250px; width: 475px;" /></strong></p>

<pre>
<strong>输入：</strong>slices = [8,9,8,6,1,1]
<strong>输出：</strong>16
<strong>解释：</strong>两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= slices.length &lt;= 500</code></li>
	<li><code>slices.length % 3 == 0</code></li>
	<li><code>1 &lt;= slices[i] &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 动态规划
- 堆（优先队列）

## 提示

1. By studying the pattern of the operations, we can find out that the problem is equivalent to: Given an integer array with size 3N, select N integers with maximum sum and any selected integers are not next to each other in the array.
2. The first one in the array is considered next to the last one in the array. Use Dynamic Programming to solve it.

## 示例

```
[1,2,3,4,5,6]
[8,9,8,6,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSizeSlices(vector<int>& slices) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSizeSlices(int[] slices) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSizeSlices(self, slices):
        """
        :type slices: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
```

### C

```c
int maxSizeSlices(int* slices, int slicesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSizeSlices(int[] slices) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} slices
 * @return {number}
 */
var maxSizeSlices = function(slices) {
    
};
```

### TypeScript

```typescript
function maxSizeSlices(slices: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $slices
     * @return Integer
     */
    function maxSizeSlices($slices) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSizeSlices(_ slices: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSizeSlices(slices: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSizeSlices(List<int> slices) {
    
  }
}
```

### Go

```golang
func maxSizeSlices(slices []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} slices
# @return {Integer}
def max_size_slices(slices)
    
end
```

### Scala

```scala
object Solution {
    def maxSizeSlices(slices: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_size_slices(slices: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-size-slices slices)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_size_slices(Slices :: [integer()]) -> integer().
max_size_slices(Slices) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_size_slices(slices :: [integer]) :: integer
  def max_size_slices(slices) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSizeSlices(slices: Array<Int64>): Int64 {

    }
}
```

