# 2527. 查询数组异或美丽值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>三个下标&nbsp;<code>i</code>&nbsp;，<code>j</code>&nbsp;和&nbsp;<code>k</code>&nbsp;的 <strong>有效值</strong>&nbsp;定义为&nbsp;<code>((nums[i] | nums[j]) &amp; nums[k])</code>&nbsp;。</p>

<p>一个数组的 <strong>异或美丽值</strong>&nbsp;是数组中所有满足&nbsp;<code>0 &lt;= i, j, k &lt; n</code>&nbsp;&nbsp;<strong>的三元组</strong>&nbsp;<code>(i, j, k)</code>&nbsp;的 <strong>有效值</strong>&nbsp;的异或结果。</p>

<p>请你返回&nbsp;<code>nums</code>&nbsp;的异或美丽值。</p>

<p><b>注意：</b></p>

<ul>
	<li><code>val1 | val2</code>&nbsp;是&nbsp;<code>val1</code> 和&nbsp;<code>val2</code>&nbsp;的按位或。</li>
	<li><code>val1 &amp; val2</code>&nbsp;是&nbsp;<code>val1</code> 和&nbsp;<code>val2</code>&nbsp;的按位与。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,4]
<b>输出：</b>5
<b>解释：</b>
三元组和它们对应的有效值如下：
- (0,0,0) 有效值为 ((1 | 1) &amp; 1) = 1
- (0,0,1) 有效值为 ((1 | 1) &amp; 4) = 0
- (0,1,0) 有效值为 ((1 | 4) &amp; 1) = 1
- (0,1,1) 有效值为 ((1 | 4) &amp; 4) = 4
- (1,0,0) 有效值为 ((4 | 1) &amp; 1) = 1
- (1,0,1) 有效值为 ((4 | 1) &amp; 4) = 4
- (1,1,0) 有效值为 ((4 | 4) &amp; 1) = 0
- (1,1,1) 有效值为 ((4 | 4) &amp; 4) = 4 
数组的异或美丽值为所有有效值的按位异或 1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [15,45,20,2,34,35,5,44,32,30]
<b>输出：</b>34
<code><span style=""><b>解释：</b>数组的异或美丽值为</span> 34 。</code>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 数学

## 提示

1. Try to simplify the given expression.
2. Try constructing the answer bit by bit.

## 示例

```
[1,4]
[15,45,20,2,34,35,5,44,32,30]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int xorBeauty(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int xorBeauty(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def xorBeauty(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        
```

### C

```c
int xorBeauty(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int XorBeauty(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var xorBeauty = function(nums) {
    
};
```

### TypeScript

```typescript
function xorBeauty(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function xorBeauty($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func xorBeauty(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun xorBeauty(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int xorBeauty(List<int> nums) {
    
  }
}
```

### Go

```golang
func xorBeauty(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def xor_beauty(nums)
    
end
```

### Scala

```scala
object Solution {
    def xorBeauty(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn xor_beauty(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (xor-beauty nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec xor_beauty(Nums :: [integer()]) -> integer().
xor_beauty(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec xor_beauty(nums :: [integer]) :: integer
  def xor_beauty(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func xorBeauty(nums: Array<Int64>): Int64 {

    }
}
```

