# 3020. 子集中元素的最大数量

## 题目描述

<p>给你一个<strong> 正整数 </strong>数组 <code>nums</code> 。</p>

<p>你需要从数组中选出一个满足下述条件的<span data-keyword="subset">子集</span>：</p>

<ul>
	<li>你可以将选中的元素放置在一个下标从 <strong>0</strong> 开始的数组中，并使其遵循以下模式：<code>[x, x<sup>2</sup>, x<sup>4</sup>, ..., x<sup>k/2</sup>, x<sup>k</sup>, x<sup>k/2</sup>, ..., x<sup>4</sup>, x<sup>2</sup>, x]</code>（<strong>注意</strong>，<code>k</code> 可以是任何 <strong>非负</strong> 的 2 的幂）。例如，<code>[2, 4, 16, 4, 2]</code> 和 <code>[3, 9, 3]</code> 都符合这一模式，而 <code>[2, 4, 8, 4, 2]</code> 则不符合。</li>
</ul>

<p>返回满足这些条件的子集中，元素数量的 <strong>最大值 </strong><em>。</em></p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,4,1,2,2]
<strong>输出：</strong>3
<strong>解释：</strong>选择子集 {4,2,2} ，将其放在数组 [2,4,2] 中，它遵循该模式，且 2<sup>2</sup> == 4 。因此答案是 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,2,4]
<strong>输出：</strong>1
<strong>解释：</strong>选择子集 {1}，将其放在数组 [1] 中，它遵循该模式。因此答案是 1 。注意我们也可以选择子集 {2} 、{4} 或 {3} ，可能存在多个子集都能得到相同的答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 枚举

## 提示

1. We can select an odd number of <code>1</code>’s.
2. Put all the values into a HashSet. We can start from each <code>x > 1</code> as the smallest chosen value and we can find the longest subset by checking the new values (which are the square of the previous value) in the set by brute force.
3. Note when <code>x > 1</code>, <code>x<sup>2</sup></code>, <code>x<sup>4</sup></code>, <code>x<sup>8</sup></code>, … increases very fast, the longest subset with smallest value x cannot be very long. (The length is <code>O(log(log(10<sup>9</sup>)))</code>.
4. Hence we can directly check all lengths less than <code>10</code> for all values of <code>x</code>.

## 示例

```
[5,4,1,2,2]
[1,3,2,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumLength = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_length(Nums :: [integer()]) -> integer().
maximum_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer]) :: integer
  def maximum_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumLength(nums: Array<Int64>): Int64 {

    }
}
```

