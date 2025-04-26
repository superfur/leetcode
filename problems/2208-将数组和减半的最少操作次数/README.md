# 2208. 将数组和减半的最少操作次数

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>&nbsp;。每一次操作中，你可以从&nbsp;<code>nums</code>&nbsp;中选择 <strong>任意</strong>&nbsp;一个数并将它减小到 <strong>恰好</strong>&nbsp;一半。（注意，在后续操作中你可以对减半过的数继续执行操作）</p>

<p>请你返回将 <code>nums</code>&nbsp;数组和 <strong>至少</strong>&nbsp;减少一半的 <strong>最少</strong>&nbsp;操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [5,19,8,1]
<b>输出：</b>3
<b>解释：</b>初始 nums 的和为 5 + 19 + 8 + 1 = 33 。
以下是将数组和减少至少一半的一种方法：
选择数字 19 并减小为 9.5 。
选择数字 9.5 并减小为 4.75 。
选择数字 8 并减小为 4 。
最终数组为 [5, 4.75, 4, 1] ，和为 5 + 4.75 + 4 + 1 = 14.75 。
nums 的和减小了 33 - 14.75 = 18.25 ，减小的部分超过了初始数组和的一半，18.25 &gt;= 33/2 = 16.5 。
我们需要 3 个操作实现题目要求，所以返回 3 。
可以证明，无法通过少于 3 个操作使数组和减少至少一半。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [3,8,20]
<b>输出：</b>3
<strong>解释：</strong>初始 nums 的和为 3 + 8 + 20 = 31 。
以下是将数组和减少至少一半的一种方法：
选择数字 20 并减小为 10 。
选择数字 10 并减小为 5 。
选择数字 3 并减小为 1.5 。
最终数组为 [1.5, 8, 5] ，和为 1.5 + 8 + 5 = 14.5 。
nums 的和减小了 31 - 14.5 = 16.5 ，减小的部分超过了初始数组和的一半， 16.5 &gt;= 31/2 = 15.5 。
我们需要 3 个操作实现题目要求，所以返回 3 。
可以证明，无法通过少于 3 个操作使数组和减少至少一半。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. It is always optimal to halve the largest element.
2. What data structure allows for an efficient query of the maximum element?
3. Use a heap or priority queue to maintain the current elements.

## 示例

```
[5,19,8,1]
[3,8,20]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int halveArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int halveArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def halveArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
```

### C

```c
int halveArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int HalveArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var halveArray = function(nums) {
    
};
```

### TypeScript

```typescript
function halveArray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function halveArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func halveArray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun halveArray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int halveArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func halveArray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def halve_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def halveArray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn halve_array(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (halve-array nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec halve_array(Nums :: [integer()]) -> integer().
halve_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec halve_array(nums :: [integer]) :: integer
  def halve_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func halveArray(nums: Array<Int64>): Int64 {

    }
}
```

