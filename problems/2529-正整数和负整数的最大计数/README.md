# 2529. 正整数和负整数的最大计数

## 题目描述

<p>给你一个按 <strong>非递减顺序</strong> 排列的数组 <code>nums</code> ，返回正整数数目和负整数数目中的最大值。</p>

<ul>
	<li>换句话讲，如果 <code>nums</code> 中正整数的数目是 <code>pos</code> ，而负整数的数目是 <code>neg</code> ，返回 <code>pos</code> 和 <code>neg</code>二者中的最大值。</li>
</ul>

<p><strong>注意：</strong><code>0</code> 既不是正整数也不是负整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-2,-1,-1,1,2,3]
<strong>输出：</strong>3
<strong>解释：</strong>共有 3 个正整数和 3 个负整数。计数得到的最大值是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-3,-2,-1,0,0,1,2]
<strong>输出：</strong>3
<strong>解释：</strong>共有 2 个正整数和 3 个负整数。计数得到的最大值是 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,20,66,1314]
<strong>输出：</strong>4
<strong>解释：</strong>共有 4 个正整数和 0 个负整数。计数得到的最大值是 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>-2000 &lt;= nums[i] &lt;= 2000</code></li>
	<li><code>nums</code> 按 <strong>非递减顺序</strong> 排列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以设计并实现时间复杂度为 <code>O(log(n))</code> 的算法解决此问题吗？</p>


## 难度

Easy

## 标签

- 数组
- 二分查找
- 计数

## 提示

1. Count how many positive integers and negative integers are in the array.
2. Since the array is sorted, can we use the binary search?

## 示例

```
[-2,-1,-1,1,2,3]
[-3,-2,-1,0,0,1,2]
[5,20,66,1314]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumCount(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumCount(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumCount(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumCount(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumCount = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumCount(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumCount($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumCount(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumCount(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumCount(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumCount(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_count(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumCount(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_count(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-count nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_count(Nums :: [integer()]) -> integer().
maximum_count(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_count(nums :: [integer]) :: integer
  def maximum_count(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumCount(nums: Array<Int64>): Int64 {

    }
}
```

