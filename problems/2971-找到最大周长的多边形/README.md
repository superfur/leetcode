# 2971. 找到最大周长的多边形

## 题目描述

<p>给你一个长度为&nbsp;<code>n</code>&nbsp;的&nbsp;<strong>正</strong>&nbsp;整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p><strong>多边形</strong>&nbsp;指的是一个至少有 <code>3</code>&nbsp;条边的封闭二维图形。多边形的 <strong>最长边</strong>&nbsp;一定 <strong>小于</strong>&nbsp;所有其他边长度之和。</p>

<p>如果你有&nbsp;<code>k</code>&nbsp;（<code>k &gt;= 3</code>）个&nbsp;<strong>正</strong>&nbsp;数&nbsp;<code>a<sub>1</sub></code>，<code>a<sub>2</sub></code>，<code>a<sub>3</sub></code>, ...，<code>a<sub>k</sub></code> 满足&nbsp;<code>a<sub>1</sub> &lt;= a<sub>2</sub> &lt;= a<sub>3</sub> &lt;= ... &lt;= a<sub>k</sub></code> <strong>且</strong> <code>a<sub>1</sub> + a<sub>2</sub> + a<sub>3</sub> + ... + a<sub>k-1</sub> &gt; a<sub>k</sub></code><sub>&nbsp;</sub>，那么 <strong>一定</strong>&nbsp;存在一个&nbsp;<code>k</code>&nbsp;条边的多边形，每条边的长度分别为&nbsp;<code>a<sub>1</sub></code>&nbsp;，<code>a<sub>2</sub></code>&nbsp;，<code>a<sub>3</sub></code>&nbsp;，&nbsp;...，<code>a<sub>k</sub></code>&nbsp;。</p>

<p>一个多边形的 <strong>周长</strong>&nbsp;指的是它所有边之和。</p>

<p>请你返回从 <code>nums</code>&nbsp;中可以构造的 <strong>多边形&nbsp;</strong>的 <strong>最大周长</strong>&nbsp;。如果不能构造出任何多边形，请你返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [5,5,5]
<b>输出：</b>15
<b>解释：</b>nums 中唯一可以构造的多边形为三角形，每条边的长度分别为 5 ，5 和 5 ，周长为 5 + 5 + 5 = 15 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,12,1,2,5,50,3]
<b>输出：</b>12
<b>解释：</b>最大周长多边形为五边形，每条边的长度分别为 1 ，1 ，2 ，3 和 5 ，周长为 1 + 1 + 2 + 3 + 5 = 12 。
我们无法构造一个包含变长为 12 或者 50 的多边形，因为其他边之和没法大于两者中的任何一个。
所以最大周长为 12 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [5,5,50]
<b>输出：</b>-1
<b>解释：</b>无法构造任何多边形，因为多边形至少要有 3 条边且 50 &gt; 5 + 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 前缀和
- 排序

## 提示

1. Sort the array.
2. Use greedy algorithm. If we select an edge as the longest side, it is always better to pick up all the edges with length no longer than this longest edge.
3. Note that the number of edges should not be less than 3.

## 示例

```
[5,5,5]
[1,12,1,2,5,50,3]
[5,5,50]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long largestPerimeter(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long largestPerimeter(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
```

### C

```c
long long largestPerimeter(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long LargestPerimeter(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var largestPerimeter = function(nums) {
    
};
```

### TypeScript

```typescript
function largestPerimeter(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestPerimeter($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestPerimeter(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestPerimeter(List<int> nums) {
    
  }
}
```

### Go

```golang
func largestPerimeter(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def largest_perimeter(nums)
    
end
```

### Scala

```scala
object Solution {
    def largestPerimeter(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_perimeter(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-perimeter nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_perimeter(Nums :: [integer()]) -> integer().
largest_perimeter(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_perimeter(nums :: [integer]) :: integer
  def largest_perimeter(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestPerimeter(nums: Array<Int64>): Int64 {

    }
}
```

