# 2342. 数位和相等数对的最大和

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>nums</code> ，数组中的元素都是 <strong>正</strong> 整数。请你选出两个下标 <code>i</code> 和 <code>j</code>（<code>i != j</code>），且 <code>nums[i]</code> 的数位和 与&nbsp; <code>nums[j]</code> 的数位和相等。</p>

<p>请你找出所有满足条件的下标 <code>i</code> 和 <code>j</code> ，找出并返回<em> </em><code>nums[i] + nums[j]</code><em> </em>可以得到的 <strong>最大值</strong><em>。</em>如果不存在这样的下标对，返回 -1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [18,43,36,13,7]
<strong>输出：</strong>54
<strong>解释：</strong>满足条件的数对 (i, j) 为：
- (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
- (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
所以可以获得的最大和是 54 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,12,19,14]
<strong>输出：</strong>-1
<strong>解释：</strong>不存在满足条件的数对，返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序
- 堆（优先队列）

## 提示

1. What is the largest possible sum of digits a number can have?
2. Group the array elements by the sum of their digits, and find the largest two elements of each group.

## 示例

```
[18,43,36,13,7]
[10,12,19,14]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_sum(Nums :: [integer()]) -> integer().
maximum_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_sum(nums :: [integer]) :: integer
  def maximum_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumSum(nums: Array<Int64>): Int64 {

    }
}
```

