# 2654. 使数组所有元素变成 1 的最少操作次数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的 <strong>正</strong>&nbsp;整数数组&nbsp;<code>nums</code>&nbsp;。你可以对数组执行以下操作 <strong>任意</strong>&nbsp;次：</p>

<ul>
	<li>选择一个满足&nbsp;<code>0 &lt;= i &lt; n - 1</code>&nbsp;的下标 <code>i</code>&nbsp;，将&nbsp;<code>nums[i]</code> 或者&nbsp;<code>nums[i+1]</code>&nbsp;两者之一替换成它们的最大公约数。</li>
</ul>

<p>请你返回使数组 <code>nums</code>&nbsp;中所有元素都等于 <code>1</code>&nbsp;的 <strong>最少</strong>&nbsp;操作次数。如果无法让数组全部变成 <code>1</code>&nbsp;，请你返回 <code>-1</code>&nbsp;。</p>

<p>两个正整数的最大公约数指的是能整除这两个数的最大正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,6,3,4]
<b>输出：</b>4
<b>解释：</b>我们可以执行以下操作：
- 选择下标 i = 2 ，将 nums[2] 替换为 gcd(3,4) = 1 ，得到 nums = [2,6,1,4] 。
- 选择下标 i = 1 ，将 nums[1] 替换为 gcd(6,1) = 1 ，得到 nums = [2,1,1,4] 。
- 选择下标 i = 0 ，将 nums[0] 替换为 gcd(2,1) = 1 ，得到 nums = [1,1,1,4] 。
- 选择下标 i = 2 ，将 nums[3] 替换为 gcd(1,4) = 1 ，得到 nums = [1,1,1,1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,10,6,14]
<b>输出：</b>-1
<b>解释：</b>无法将所有元素都变成 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 数论

## 提示

1. Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.
2. Try finding the shortest subarray with a gcd equal to 1.

## 示例

```
[2,6,3,4]
[2,10,6,14]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
```

### C

```c
int minOperations(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: Array<Int64>): Int64 {

    }
}
```

