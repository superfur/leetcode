# 2317. 操作后的最大异或和

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。一次操作中，选择 <strong>任意</strong>&nbsp;非负整数&nbsp;<code>x</code>&nbsp;和一个下标&nbsp;<code>i</code>&nbsp;，<strong>更新</strong>&nbsp;<code>nums[i]</code>&nbsp;为&nbsp;<code>nums[i] AND (nums[i] XOR x)</code>&nbsp;。</p>

<p>注意，<code>AND</code>&nbsp;是逐位与运算，<code>XOR</code>&nbsp;是逐位异或运算。</p>

<p>请你执行 <strong>任意次</strong>&nbsp;更新操作，并返回&nbsp;<code>nums</code>&nbsp;中所有元素&nbsp;<strong>最大</strong>&nbsp;逐位异或和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,2,4,6]
<b>输出：</b>7
<b>解释：</b>选择 x = 4 和 i = 3 进行操作，num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2 。
现在，nums = [3, 2, 4, 2] 且所有元素逐位异或得到 3 XOR 2 XOR 4 XOR 2 = 7 。
可知 7 是能得到的最大逐位异或和。
注意，其他操作可能也能得到逐位异或和 7 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,9,2]
<b>输出：</b>11
<b>解释：</b>执行 0 次操作。
所有元素的逐位异或和为 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11 。
可知 11 是能得到的最大逐位异或和。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 数学

## 提示

1. Consider what it means to be able to choose any x for the operation and which integers could be obtained from a given nums[i].
2. The given operation can unset any bit in nums[i].
3. The nth bit of the XOR of all the elements is 1 if the nth bit is 1 for an odd number of elements. When can we ensure it is odd?
4. Try to set every bit of the result to 1 if possible.

## 示例

```
[3,2,4,6]
[1,2,3,9,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumXOR(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumXOR(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumXOR(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumXOR(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumXOR = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumXOR(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumXOR($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumXOR(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumXOR(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumXOR(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumXOR(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_xor(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumXOR(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_xor(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-xor nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_xor(Nums :: [integer()]) -> integer().
maximum_xor(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_xor(nums :: [integer]) :: integer
  def maximum_xor(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumXOR(nums: Array<Int64>): Int64 {

    }
}
```

