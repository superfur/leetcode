# 2980. 检查按位或是否存在尾随零

## 题目描述

<p>给你一个<strong> 正整数 </strong>数组 <code>nums</code> 。</p>

<p>你需要检查是否可以从数组中选出 <strong>两个或更多 </strong>元素，满足这些元素的按位或运算（ <code>OR</code>）结果的二进制表示中 <strong>至少</strong><strong> </strong>存在一个尾随零。</p>

<p>例如，数字 <code>5</code> 的二进制表示是 <code>"101"</code>，不存在尾随零，而数字 <code>4</code> 的二进制表示是 <code>"100"</code>，存在两个尾随零。</p>

<p>如果可以选择两个或更多元素，其按位或运算结果存在尾随零，返回 <code>true</code>；否则，返回<em> </em><code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5]
<strong>输出：</strong>true
<strong>解释：</strong>如果选择元素 2 和 4，按位或运算结果是 6，二进制表示为 "110" ，存在一个尾随零。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,8,16]
<strong>输出：</strong>true
<strong>解释：</strong>如果选择元素 2 和 4，按位或运算结果是 6，二进制表示为 "110"，存在一个尾随零。
其他按位或运算结果存在尾随零的可能选择方案包括：(2, 8), (2, 16), (4, 8), (4, 16), (8, 16), (2, 4, 8), (2, 4, 16), (2, 8, 16), (4, 8, 16), 以及 (2, 4, 8, 16) 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,5,7,9]
<strong>输出：</strong>false
<strong>解释：</strong>不存在按位或运算结果存在尾随零的选择方案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组

## 提示

1. Bitwise <code>OR</code> can never unset a bit. If there is a solution, there must be a solution with only a pair of elements.
2. We can brute force the solution: enumerate all the pairs.
3. As the least significant bit must stay unset, the question is whether the array has at least two even elements.

## 示例

```
[1,2,3,4,5]
[2,4,8,16]
[1,3,5,7,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool hasTrailingZeros(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean hasTrailingZeros(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        
```

### C

```c
bool hasTrailingZeros(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool HasTrailingZeros(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var hasTrailingZeros = function(nums) {
    
};
```

### TypeScript

```typescript
function hasTrailingZeros(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function hasTrailingZeros($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func hasTrailingZeros(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun hasTrailingZeros(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool hasTrailingZeros(List<int> nums) {
    
  }
}
```

### Go

```golang
func hasTrailingZeros(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def has_trailing_zeros(nums)
    
end
```

### Scala

```scala
object Solution {
    def hasTrailingZeros(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn has_trailing_zeros(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (has-trailing-zeros nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec has_trailing_zeros(Nums :: [integer()]) -> boolean().
has_trailing_zeros(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec has_trailing_zeros(nums :: [integer]) :: boolean
  def has_trailing_zeros(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func hasTrailingZeros(nums: Array<Int64>): Bool {

    }
}
```

