# 775. 全局倒置与局部倒置

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> ，表示由范围 <code>[0, n - 1]</code> 内所有整数组成的一个排列。</p>

<p><strong>全局倒置</strong> 的数目等于满足下述条件不同下标对 <code>(i, j)</code> 的数目：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; n</code></li>
	<li><code>nums[i] &gt; nums[j]</code></li>
</ul>

<p><strong>局部倒置</strong> 的数目等于满足下述条件的下标 <code>i</code> 的数目：</p>

<ul>
	<li><code>0 &lt;= i &lt; n - 1</code></li>
	<li><code>nums[i] &gt; nums[i + 1]</code></li>
</ul>

<p>当数组 <code>nums</code> 中 <strong>全局倒置</strong> 的数量等于 <strong>局部倒置</strong> 的数量时，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,0,2]
<strong>输出：</strong>true
<strong>解释：</strong>有 1 个全局倒置，和 1 个局部倒置。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,0]
<strong>输出：</strong>false
<strong>解释：</strong>有 2 个全局倒置，和 1 个局部倒置。
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; n</code></li>
	<li><code>nums</code> 中的所有整数 <strong>互不相同</strong></li>
	<li><code>nums</code> 是范围 <code>[0, n - 1]</code> 内所有数字组成的一个排列</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. Where can the 0 be placed in an ideal permutation?  What about the 1?

## 示例

```
[1,0,2]
[1,2,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isIdealPermutation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isIdealPermutation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isIdealPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        
```

### C

```c
bool isIdealPermutation(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsIdealPermutation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isIdealPermutation = function(nums) {
    
};
```

### TypeScript

```typescript
function isIdealPermutation(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isIdealPermutation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isIdealPermutation(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isIdealPermutation(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isIdealPermutation(List<int> nums) {
    
  }
}
```

### Go

```golang
func isIdealPermutation(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def is_ideal_permutation(nums)
    
end
```

### Scala

```scala
object Solution {
    def isIdealPermutation(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_ideal_permutation(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-ideal-permutation nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_ideal_permutation(Nums :: [integer()]) -> boolean().
is_ideal_permutation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_ideal_permutation(nums :: [integer]) :: boolean
  def is_ideal_permutation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isIdealPermutation(nums: Array<Int64>): Bool {

    }
}
```

