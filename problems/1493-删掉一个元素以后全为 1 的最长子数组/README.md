# 1493. 删掉一个元素以后全为 1 的最长子数组

## 题目描述

<p>给你一个二进制数组&nbsp;<code>nums</code>&nbsp;，你需要从中删掉一个元素。</p>

<p>请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。</p>

<p>如果不存在这样的子数组，请返回 0 。</p>

<p>&nbsp;</p>

<p><strong>提示 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,0,1]
<strong>输出：</strong>3
<strong>解释：</strong>删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,1,1,0,1,1,0,1]
<strong>输出：</strong>5
<strong>解释：</strong>删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1]
<strong>输出：</strong>2
<strong>解释：</strong>你必须要删除一个元素。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code>&nbsp;要么是&nbsp;<code>0</code>&nbsp;要么是&nbsp;<code>1</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 滑动窗口

## 提示

1. Maintain a sliding window where there is at most one zero in it.

## 示例

```
[1,1,0,1]
[0,1,1,1,0,1,1,0,1]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int longestSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function longestSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func longestSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def longestSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_subarray(Nums :: [integer()]) -> integer().
longest_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_subarray(nums :: [integer]) :: integer
  def longest_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubarray(nums: Array<Int64>): Int64 {

    }
}
```

