# 3158. 求出出现两次数字的 XOR 值

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;，数组中的数字 <strong>要么</strong> 出现一次，<strong>要么</strong>&nbsp;出现两次。</p>

<p>请你返回数组中所有出现两次数字的按位<em>&nbsp;</em><code>XOR</code>&nbsp;值，如果没有数字出现过两次，返回 0 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,1,3]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;中唯一出现过两次的数字是 1 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;中没有数字出现两次。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,2,1]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>数字 1 和&nbsp;2 出现过两次。<code>1 XOR 2 == 3</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
	<li><code>nums</code>&nbsp;中每个数字要么出现过一次，要么出现过两次。</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表

## 提示

1. The constraints are small. Brute force checking each value in the array.

## 示例

```
[1,2,1,3]
[1,2,3]
[1,2,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int duplicateNumbersXOR(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int duplicateNumbersXOR(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        
```

### C

```c
int duplicateNumbersXOR(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DuplicateNumbersXOR(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var duplicateNumbersXOR = function(nums) {
    
};
```

### TypeScript

```typescript
function duplicateNumbersXOR(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function duplicateNumbersXOR($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func duplicateNumbersXOR(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun duplicateNumbersXOR(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int duplicateNumbersXOR(List<int> nums) {
    
  }
}
```

### Go

```golang
func duplicateNumbersXOR(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def duplicate_numbers_xor(nums)
    
end
```

### Scala

```scala
object Solution {
    def duplicateNumbersXOR(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn duplicate_numbers_xor(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (duplicate-numbers-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec duplicate_numbers_xor(Nums :: [integer()]) -> integer().
duplicate_numbers_xor(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec duplicate_numbers_xor(nums :: [integer]) :: integer
  def duplicate_numbers_xor(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func duplicateNumbersXOR(nums: Array<Int64>): Int64 {

    }
}
```

