# 2601. 质数减法运算

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，数组长度为 <code>n</code> 。</p>

<p>你可以执行无限次下述运算：</p>

<ul>
	<li>选择一个之前未选过的下标 <code>i</code> ，并选择一个 <strong>严格小于</strong> <code>nums[i]</code> 的质数 <code>p</code> ，从 <code>nums[i]</code> 中减去 <code>p</code> 。</li>
</ul>

<p>如果你能通过上述运算使得 <code>nums</code> 成为严格递增数组，则返回 <code>true</code> ；否则返回 <code>false</code> 。</p>

<p><strong>严格递增数组</strong> 中的每个元素都严格大于其前面的元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,9,6,10]
<strong>输出：</strong>true
<strong>解释：</strong>
在第一次运算中：选择 i = 0 和 p = 3 ，然后从 nums[0] 减去 3 ，nums 变为 [1,9,6,10] 。
在第二次运算中：选择 i = 1 和 p = 7 ，然后从 nums[1] 减去 7 ，nums 变为 [1,2,6,10] 。
第二次运算后，nums 按严格递增顺序排序，因此答案为 true 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [6,8,11,12]
<strong>输出：</strong>true
<strong>解释：</strong>nums 从一开始就按严格递增顺序排序，因此不需要执行任何运算。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,8,3]
<strong>输出：</strong>false
<strong>解释：</strong>可以证明，执行运算无法使 nums 按严格递增顺序排序，因此答案是 false 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums.length == n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 二分查找
- 数论

## 提示

1. Think about if we have many primes to subtract from nums[i]. Which prime is more optimal?
2. The most optimal prime to subtract from nums[i] is the one that makes nums[i] the smallest as possible and greater than nums[i-1].

## 示例

```
[4,9,6,10]
[6,8,11,12]
[5,8,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool primeSubOperation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean primeSubOperation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
```

### C

```c
bool primeSubOperation(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PrimeSubOperation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var primeSubOperation = function(nums) {
    
};
```

### TypeScript

```typescript
function primeSubOperation(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function primeSubOperation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func primeSubOperation(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun primeSubOperation(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool primeSubOperation(List<int> nums) {
    
  }
}
```

### Go

```golang
func primeSubOperation(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def prime_sub_operation(nums)
    
end
```

### Scala

```scala
object Solution {
    def primeSubOperation(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn prime_sub_operation(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (prime-sub-operation nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec prime_sub_operation(Nums :: [integer()]) -> boolean().
prime_sub_operation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec prime_sub_operation(nums :: [integer]) :: boolean
  def prime_sub_operation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func primeSubOperation(nums: Array<Int64>): Bool {

    }
}
```

