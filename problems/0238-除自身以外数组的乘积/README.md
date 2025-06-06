# 238. 除自身以外数组的乘积

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，返回 数组&nbsp;<code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>&nbsp;等于&nbsp;<code>nums</code>&nbsp;中除&nbsp;<code>nums[i]</code>&nbsp;之外其余各元素的乘积&nbsp;。</p>

<p>题目数据 <strong>保证</strong> 数组&nbsp;<code>nums</code>之中任意元素的全部前缀元素和后缀的乘积都在&nbsp; <strong>32 位</strong> 整数范围内。</p>

<p>请&nbsp;<strong>不要使用除法，</strong>且在&nbsp;<code>O(n)</code> 时间复杂度内完成此题。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = <code>[1,2,3,4]</code>
<strong>输出:</strong> <code>[24,12,8,6]</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [-1,1,0,-3,3]
<strong>输出:</strong> [0,0,9,0,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>输入&nbsp;<strong>保证</strong> 数组&nbsp;<code>answer[i]</code>&nbsp;在&nbsp; <strong>32 位</strong> 整数范围内</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以在 <code>O(1)</code>&nbsp;的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组&nbsp;<strong>不被视为&nbsp;</strong>额外空间。）</p>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. Think how you can efficiently utilize prefix and suffix products to calculate the product of all elements except self for each index. Can you pre-compute the prefix and suffix products in linear time to avoid redundant calculations?
2. Can you minimize additional space usage by reusing memory or modifying the input array to store intermediate results?

## 示例

```
[1,2,3,4]
[-1,1,0,-3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] productExceptSelf(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    
};
```

### TypeScript

```typescript
function productExceptSelf(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function productExceptSelf($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> productExceptSelf(List<int> nums) {
    
  }
}
```

### Go

```golang
func productExceptSelf(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def product_except_self(nums)
    
end
```

### Scala

```scala
object Solution {
    def productExceptSelf(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (product-except-self nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec product_except_self(Nums :: [integer()]) -> [integer()].
product_except_self(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec product_except_self(nums :: [integer]) :: [integer]
  def product_except_self(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func productExceptSelf(nums: Array<Int64>): Array<Int64> {

    }
}
```

