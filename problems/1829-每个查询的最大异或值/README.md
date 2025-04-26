# 1829. 每个查询的最大异或值

## 题目描述

<p>给你一个 <strong>有序</strong> 数组 <code>nums</code> ，它由 <code>n</code> 个非负整数组成，同时给你一个整数 <code>maximumBit</code> 。你需要执行以下查询 <code>n</code> 次：</p>

<ol>
	<li>找到一个非负整数 <code>k < 2<sup>maximumBit</sup></code> ，使得 <code>nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k</code> 的结果 <strong>最大化</strong> 。<code>k</code> 是第 <code>i</code> 个查询的答案。</li>
	<li>从当前数组 <code>nums</code> 删除 <strong>最后</strong> 一个元素。</li>
</ol>

<p>请你返回一个数组 <code>answer</code> ，其中<em> </em><code>answer[i]</code>是第 <code>i</code> 个查询的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [0,1,1,3], maximumBit = 2
<b>输出：</b>[0,3,2,3]
<b>解释：</b>查询的答案如下：
第一个查询：nums = [0,1,1,3]，k = 0，因为 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3 。
第二个查询：nums = [0,1,1]，k = 3，因为 0 XOR 1 XOR 1 XOR 3 = 3 。
第三个查询：nums = [0,1]，k = 2，因为 0 XOR 1 XOR 2 = 3 。
第四个查询：nums = [0]，k = 3，因为 0 XOR 3 = 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,4,7], maximumBit = 3
<b>输出：</b>[5,2,6,5]
<b>解释：</b>查询的答案如下：
第一个查询：nums = [2,3,4,7]，k = 5，因为 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7。
第二个查询：nums = [2,3,4]，k = 2，因为 2 XOR 3 XOR 4 XOR 2 = 7 。
第三个查询：nums = [2,3]，k = 6，因为 2 XOR 3 XOR 6 = 7 。
第四个查询：nums = [2]，k = 5，因为 2 XOR 5 = 7 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [0,1,2,2,5,7], maximumBit = 3
<b>输出：</b>[4,3,6,4,6,7]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length == n</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= maximumBit <= 20</code></li>
	<li><code>0 <= nums[i] < 2<sup>maximumBit</sup></code></li>
	<li><code>nums</code>​​​ 中的数字已经按 <strong>升序</strong> 排好序。</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 前缀和

## 提示

1. Note that the maximum possible XOR result is always 2^(maximumBit) - 1
2. So the answer for a prefix is the XOR of that prefix XORed with 2^(maximumBit)-1

## 示例

```
[0,1,1,3]
2
[2,3,4,7]
3
[0,1,2,2,5,7]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getMaximumXor(int* nums, int numsSize, int maximumBit, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetMaximumXor(int[] nums, int maximumBit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} maximumBit
 * @return {number[]}
 */
var getMaximumXor = function(nums, maximumBit) {
    
};
```

### TypeScript

```typescript
function getMaximumXor(nums: number[], maximumBit: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $maximumBit
     * @return Integer[]
     */
    function getMaximumXor($nums, $maximumBit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaximumXor(_ nums: [Int], _ maximumBit: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaximumXor(nums: IntArray, maximumBit: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getMaximumXor(List<int> nums, int maximumBit) {
    
  }
}
```

### Go

```golang
func getMaximumXor(nums []int, maximumBit int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} maximum_bit
# @return {Integer[]}
def get_maximum_xor(nums, maximum_bit)
    
end
```

### Scala

```scala
object Solution {
    def getMaximumXor(nums: Array[Int], maximumBit: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_maximum_xor(nums: Vec<i32>, maximum_bit: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-maximum-xor nums maximumBit)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_maximum_xor(Nums :: [integer()], MaximumBit :: integer()) -> [integer()].
get_maximum_xor(Nums, MaximumBit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_maximum_xor(nums :: [integer], maximum_bit :: integer) :: [integer]
  def get_maximum_xor(nums, maximum_bit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaximumXor(nums: Array<Int64>, maximumBit: Int64): Array<Int64> {

    }
}
```

