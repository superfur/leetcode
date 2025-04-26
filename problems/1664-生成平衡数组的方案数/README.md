# 1664. 生成平衡数组的方案数

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。你需要选择 <strong>恰好</strong> 一个下标（下标从 <strong>0</strong> 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。</p>

<p>比方说，如果 <code>nums = [6,1,7,4,1]</code> ，那么：</p>

<ul>
	<li>选择删除下标 <code>1</code> ，剩下的数组为 <code>nums = [6,7,4,1]</code> 。</li>
	<li>选择删除下标 <code>2</code> ，剩下的数组为 <code>nums = [6,1,4,1]</code> 。</li>
	<li>选择删除下标 <code>4</code> ，剩下的数组为 <code>nums = [6,1,7,4]</code> 。</li>
</ul>

<p>如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 <strong>平衡数组</strong> 。</p>

<p>请你返回删除操作后，剩下的数组<em> </em><code>nums</code><em> </em>是 <strong>平衡数组</strong> 的 <strong>方案数</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,6,4]
<b>输出：</b>1
<strong>解释：</strong>
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,1,1]
<b>输出：</b>3
<b>解释：</b>你可以删除任意元素，剩余数组都是平衡数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3]
<b>输出：</b>0
<b>解释：</b>不管删除哪个元素，剩下数组都不是平衡数组。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. The parity of the indices after the removed element changes.
2. Calculate prefix sums for even and odd indices separately to calculate for each index in O(1).

## 示例

```
[2,1,6,4]
[1,1,1]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToMakeFair(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToMakeFair(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        
```

### C

```c
int waysToMakeFair(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToMakeFair(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var waysToMakeFair = function(nums) {
    
};
```

### TypeScript

```typescript
function waysToMakeFair(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function waysToMakeFair($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToMakeFair(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToMakeFair(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToMakeFair(List<int> nums) {
    
  }
}
```

### Go

```golang
func waysToMakeFair(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def ways_to_make_fair(nums)
    
end
```

### Scala

```scala
object Solution {
    def waysToMakeFair(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_make_fair(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-make-fair nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_make_fair(Nums :: [integer()]) -> integer().
ways_to_make_fair(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_make_fair(nums :: [integer]) :: integer
  def ways_to_make_fair(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToMakeFair(nums: Array<Int64>): Int64 {

    }
}
```

