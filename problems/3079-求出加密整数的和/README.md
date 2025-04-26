# 3079. 求出加密整数的和

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，数组中的元素都是&nbsp;<strong>正</strong>&nbsp;整数。定义一个加密函数&nbsp;<code>encrypt</code>&nbsp;，<code>encrypt(x)</code>&nbsp;将一个整数 <code>x</code>&nbsp;中 <strong>每一个</strong>&nbsp;数位都用 <code>x</code>&nbsp;中的&nbsp;<strong>最大</strong>&nbsp;数位替换。比方说&nbsp;<code>encrypt(523) = 555</code> 且&nbsp;<code>encrypt(213) = 333</code>&nbsp;。</p>

<p>请你返回数组中所有元素加密后的 <strong>和</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [1,2,3]</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">6</span></p>

<p><b>解释：</b>加密后的元素位&nbsp;<code>[1,2,3]</code>&nbsp;。加密元素的和为&nbsp;<code>1 + 2 + 3 == 6</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [10,21,31]</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">66</span></p>

<p><b>解释：</b>加密后的元素为&nbsp;<code>[11,22,33]</code>&nbsp;。加密元素的和为&nbsp;<code>11 + 22 + 33 == 66</code> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. Encrypted numbers are of the form <code>11…1 * maxDigit</code>.

## 示例

```
[1,2,3]
[10,21,31]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfEncryptedInt(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfEncryptedInt(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfEncryptedInt(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
```

### C

```c
int sumOfEncryptedInt(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfEncryptedInt(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfEncryptedInt = function(nums) {
    
};
```

### TypeScript

```typescript
function sumOfEncryptedInt(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfEncryptedInt($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfEncryptedInt(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfEncryptedInt(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfEncryptedInt(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumOfEncryptedInt(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_of_encrypted_int(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumOfEncryptedInt(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_encrypted_int(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-encrypted-int nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_encrypted_int(Nums :: [integer()]) -> integer().
sum_of_encrypted_int(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_encrypted_int(nums :: [integer]) :: integer
  def sum_of_encrypted_int(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfEncryptedInt(nums: Array<Int64>): Int64 {

    }
}
```

