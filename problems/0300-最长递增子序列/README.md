# 300. 最长递增子序列

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，找到其中最长严格递增子序列的长度。</p>

<p><strong>子序列&nbsp;</strong>是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，<code>[3,6,2,7]</code> 是数组 <code>[0,3,1,6,2,2,7]</code> 的<span data-keyword="subsequence-array">子序列</span>。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,9,2,5,3,7,101,18]
<strong>输出：</strong>4
<strong>解释：</strong>最长递增子序列是 [2,3,7,101]，因此长度为 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,0,3,2,3]
<strong>输出：</strong>4
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,7,7,7,7,7,7]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2500</code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><b>进阶：</b></p>

<ul>
	<li>你能将算法的时间复杂度降低到&nbsp;<code>O(n log(n))</code> 吗?</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 动态规划

## 示例

```
[10,9,2,5,3,7,101,18]
[0,1,0,3,2,3]
[7,7,7,7,7,7,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int lengthOfLIS(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
```

### C

```c
int lengthOfLIS(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LengthOfLIS(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    
};
```

### TypeScript

```typescript
function lengthOfLIS(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function lengthOfLIS($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lengthOfLIS(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lengthOfLIS(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lengthOfLIS(List<int> nums) {
    
  }
}
```

### Go

```golang
func lengthOfLIS(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def length_of_lis(nums)
    
end
```

### Scala

```scala
object Solution {
    def lengthOfLIS(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (length-of-lis nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec length_of_lis(Nums :: [integer()]) -> integer().
length_of_lis(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec length_of_lis(nums :: [integer]) :: integer
  def length_of_lis(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lengthOfLIS(nums: Array<Int64>): Int64 {

    }
}
```

