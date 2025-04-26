# 908. 最小差值 I

## 题目描述

<p>给你一个整数数组 <code>nums</code>，和一个整数 <code>k</code> 。</p>

<p>在一个操作中，您可以选择 <code>0 &lt;= i &lt; nums.length</code> 的任何索引 <code>i</code> 。将 <code>nums[i]</code> 改为 <code>nums[i] + x</code> ，其中 <code>x</code> 是一个范围为 <code>[-k, k]</code> 的任意整数。对于每个索引 <code>i</code> ，最多 <strong>只能 </strong>应用 <strong>一次</strong> 此操作。</p>

<p><code>nums</code>&nbsp;的&nbsp;<strong>分数&nbsp;</strong>是&nbsp;<code>nums</code>&nbsp;中最大和最小元素的差值。&nbsp;</p>

<p><em>在对&nbsp; <code>nums</code> 中的每个索引最多应用一次上述操作后，返回&nbsp;<code>nums</code> 的最低 <strong>分数</strong></em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], k = 0
<strong>输出：</strong>0
<strong>解释：</strong>分数是 max(nums) - min(nums) = 1 - 1 = 0。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,10], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>将 nums 改为 [2,8]。分数是 max(nums) - min(nums) = 8 - 2 = 6。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,6], k = 3
<strong>输出：</strong>0
<strong>解释：</strong>将 nums 改为 [4,4,4]。分数是 max(nums) - min(nums) = 4 - 4 = 0。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 示例

```
[1]
0
[0,10]
2
[1,3,6]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestRangeI(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestRangeI(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int smallestRangeI(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestRangeI(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var smallestRangeI = function(nums, k) {
    
};
```

### TypeScript

```typescript
function smallestRangeI(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function smallestRangeI($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestRangeI(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestRangeI(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestRangeI(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func smallestRangeI(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_range_i(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def smallestRangeI(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_range_i(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-range-i nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_range_i(Nums :: [integer()], K :: integer()) -> integer().
smallest_range_i(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_range_i(nums :: [integer], k :: integer) :: integer
  def smallest_range_i(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestRangeI(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

