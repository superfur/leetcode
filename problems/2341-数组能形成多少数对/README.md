# 2341. 数组能形成多少数对

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。在一步操作中，你可以执行以下步骤：</p>

<ul>
	<li>从 <code>nums</code> 选出 <strong>两个</strong> <strong>相等的</strong> 整数</li>
	<li>从 <code>nums</code> 中移除这两个整数，形成一个 <strong>数对</strong></li>
</ul>

<p>请你在 <code>nums</code> 上多次执行此操作直到无法继续执行。</p>

<p>返回一个下标从 <strong>0</strong> 开始、长度为 <code>2</code> 的整数数组 <code>answer</code> 作为答案，其中<em> </em><code>answer[0]</code><em> </em>是形成的数对数目，<code>answer[1]</code> 是对 <code>nums</code> 尽可能执行上述操作后剩下的整数数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,2,1,3,2,2]
<strong>输出：</strong>[3,1]
<strong>解释：</strong>
nums[0] 和 nums[3] 形成一个数对，并从 nums 中移除，nums = [3,2,3,2,2] 。
nums[0] 和 nums[2] 形成一个数对，并从 nums 中移除，nums = [2,2,2] 。
nums[0] 和 nums[1] 形成一个数对，并从 nums 中移除，nums = [2] 。
无法形成更多数对。总共形成 3 个数对，nums 中剩下 1 个数字。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1]
<strong>输出：</strong>[1,0]
<strong>解释：</strong>nums[0] 和 nums[1] 形成一个数对，并从 nums 中移除，nums = [] 。
无法形成更多数对。总共形成 1 个数对，nums 中剩下 0 个数字。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [0]
<strong>输出：</strong>[0,1]
<strong>解释：</strong>无法形成数对，nums 中剩下 1 个数字。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. What do we need to know to find how many pairs we can make? We need to know the frequency of each integer.
2. When will there be a leftover number? When the frequency of an integer is an odd number.

## 示例

```
[1,3,2,1,3,2,2]
[1,1]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] numberOfPairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfPairs(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] NumberOfPairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var numberOfPairs = function(nums) {
    
};
```

### TypeScript

```typescript
function numberOfPairs(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function numberOfPairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfPairs(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfPairs(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numberOfPairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func numberOfPairs(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def number_of_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def numberOfPairs(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_pairs(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-pairs nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec number_of_pairs(Nums :: [integer()]) -> [integer()].
number_of_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_pairs(nums :: [integer]) :: [integer]
  def number_of_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfPairs(nums: Array<Int64>): Array<Int64> {

    }
}
```

