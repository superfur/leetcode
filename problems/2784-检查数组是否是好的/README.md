# 2784. 检查数组是否是好的

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，如果它是数组&nbsp;<code>base[n]</code>&nbsp;的一个排列，我们称它是个&nbsp;<strong>好</strong>&nbsp;数组。</p>

<p><code>base[n] = [1, 2, ..., n - 1, n, n]</code>&nbsp;（换句话说，它是一个长度为 <code>n + 1</code>&nbsp;且包含&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;恰好各一次，包含 <code>n</code>&nbsp; 两次的一个数组）。比方说，<code>base[1] = [1, 1]</code>&nbsp;，<code>base[3] = [1, 2, 3, 3]</code>&nbsp;。</p>

<p>如果数组是一个好数组，请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p><strong>注意：</strong>数组的排列是这些数字按任意顺序排布后重新得到的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2, 1, 3]
<b>输出：</b>false
<b>解释：</b>因为数组的最大元素是 3 ，唯一可以构成这个数组的 base[n] 对应的 n = 3 。但是 base[3] 有 4 个元素，但数组 nums 只有 3 个元素，所以无法得到 base[3] = [1, 2, 3, 3] 的排列，所以答案为 false 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1, 3, 3, 2]
<b>输出：</b>true
<b>解释：因为</b>数组的最大元素是 3 ，唯一可以构成这个数组的 base[n] 对应的 n = 3 ，可以看出数组是 base[3] = [1, 2, 3, 3] 的一个排列（交换 nums 中第二个和第四个元素）。所以答案为 true 。</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [1, 1]
<b>输出：</b>true
<b>解释：</b>因为数组的最大元素是 1 ，唯一可以构成这个数组的 base[n] 对应的 n = 1，可以看出数组是 base[1] = [1, 1] 的一个排列。所以答案为 true 。</pre>

<p><strong>示例 4：</strong></p>

<pre><b>输入：</b>nums = [3, 4, 4, 1, 2, 1]
<b>输出：</b>false
<b>解释：</b>因为数组的最大元素是 4 ，唯一可以构成这个数组的 base[n] 对应的 n = 4 。但是 base[n] 有 5 个元素而 nums 有 6 个元素。所以答案为 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= num[i] &lt;= 200</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. Find the maximum element of the array.

## 示例

```
[2, 1, 3]
[1, 3, 3, 2]
[1, 1]
[3, 4, 4, 1, 2, 1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isGood(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isGood(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
```

### C

```c
bool isGood(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsGood(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isGood = function(nums) {
    
};
```

### TypeScript

```typescript
function isGood(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isGood($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isGood(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isGood(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isGood(List<int> nums) {
    
  }
}
```

### Go

```golang
func isGood(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def is_good(nums)
    
end
```

### Scala

```scala
object Solution {
    def isGood(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_good(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-good nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_good(Nums :: [integer()]) -> boolean().
is_good(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_good(nums :: [integer]) :: boolean
  def is_good(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isGood(nums: Array<Int64>): Bool {

    }
}
```

