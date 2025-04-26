# 2149. 按符号重排数组

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，数组长度为 <strong>偶数</strong> ，由数目 <strong>相等</strong> 的正整数和负整数组成。</p>

<p>你需要返回满足下述条件的数组&nbsp;<code>nums</code>：</p>

<ol>
	<li>任意&nbsp;<strong>连续</strong> 的两个整数 <strong>符号相反</strong></li>
	<li>对于符号相同的所有整数，<strong>保留</strong> 它们在 <code>nums</code> 中的 <strong>顺序</strong> 。</li>
	<li>重排后数组以正整数开头。</li>
</ol>

<p>重排元素满足上述条件后，返回修改后的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,-2,-5,2,-4]
<strong>输出：</strong>[3,-2,1,-5,2,-4]
<strong>解释：</strong>
nums 中的正整数是 [3,1,2] ，负整数是 [-2,-5,-4] 。
重排的唯一可行方案是 [3,-2,1,-5,2,-4]，能满足所有条件。
像 [1,-2,2,-5,3,-4]、[3,1,2,-2,-5,-4]、[-2,3,-5,1,-4,2] 这样的其他方案是不正确的，因为不满足一个或者多个条件。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,1]
<strong>输出：</strong>[1,-1]
<strong>解释：</strong>
1 是 nums 中唯一一个正整数，-1 是 nums 中唯一一个负整数。
所以 nums 重排为 [1,-1] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>nums.length</code> 是 <strong>偶数</strong></li>
	<li><code>1 &lt;= |nums[i]| &lt;= 10<sup>5</sup></code></li>
	<li><code>nums</code> 由 <strong>相等</strong> 数量的正整数和负整数组成</li>
</ul>

<p>&nbsp;</p>

<p>不需要原地进行修改。</p>


## 难度

Medium

## 标签

- 数组
- 双指针
- 模拟

## 提示

1. Divide the array into two parts- one comprising of only positive integers and the other of negative integers.
2. Merge the two parts to get the resultant array.

## 示例

```
[3,1,-2,-5,2,-4]
[-1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] rearrangeArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeArray(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RearrangeArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var rearrangeArray = function(nums) {
    
};
```

### TypeScript

```typescript
function rearrangeArray(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function rearrangeArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rearrangeArray(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rearrangeArray(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> rearrangeArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func rearrangeArray(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def rearrange_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def rearrangeArray(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rearrange_array(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (rearrange-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec rearrange_array(Nums :: [integer()]) -> [integer()].
rearrange_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rearrange_array(nums :: [integer]) :: [integer]
  def rearrange_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rearrangeArray(nums: Array<Int64>): Array<Int64> {

    }
}
```

