# 2206. 将数组划分成相等数对

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，它包含&nbsp;<code>2 * n</code>&nbsp;个整数。</p>

<p>你需要将&nbsp;<code>nums</code> 划分成&nbsp;<code>n</code>&nbsp;个数对，满足：</p>

<ul>
	<li>每个元素 <strong>只属于一个 </strong>数对。</li>
	<li>同一数对中的元素 <strong>相等</strong>&nbsp;。</li>
</ul>

<p>如果可以将 <code>nums</code>&nbsp;划分成 <code>n</code>&nbsp;个数对，请你返回 <code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,3,2,2,2]
<b>输出：</b>true
<b>解释：</b>
nums<code>&nbsp;中总共有 6 个元素，所以它们应该被划分成</code> 6 / 2 = 3 个数对。
nums 可以划分成 (2, 2) ，(3, 3) 和 (2, 2) ，满足所有要求。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>false
<b>解释：</b>
无法将 nums 划分成 4 / 2 = 2 个数对且满足所有要求。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 500</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表
- 计数

## 提示

1. For any number x in the range [1, 500], count the number of elements in nums whose values are equal to x.
2. The elements with equal value can be divided completely into pairs if and only if their count is even.

## 示例

```
[3,2,3,2,2,2]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool divideArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean divideArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
```

### C

```c
bool divideArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool DivideArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var divideArray = function(nums) {
    
};
```

### TypeScript

```typescript
function divideArray(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function divideArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func divideArray(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divideArray(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool divideArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func divideArray(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def divide_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def divideArray(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (divide-array nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec divide_array(Nums :: [integer()]) -> boolean().
divide_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divide_array(nums :: [integer]) :: boolean
  def divide_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func divideArray(nums: Array<Int64>): Bool {

    }
}
```

