# 910. 最小差值 II

## 题目描述

<p>给你一个整数数组 <code>nums</code>，和一个整数&nbsp;<code>k</code> 。</p>

<p>对于每个下标 <code>i</code>（<code>0 &lt;= i &lt; nums.length</code>），将 <code>nums[i]</code> 变成<strong> </strong> <code>nums[i] + k</code> 或 <code>nums[i] - k</code> 。</p>

<p><code>nums</code> 的 <strong>分数</strong> 是 <code>nums</code> 中最大元素和最小元素的差值。</p>

<p>在更改每个下标对应的值之后，返回 <code>nums</code> 的最小 <strong>分数</strong> 。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], k = 0
<strong>输出：</strong>0
<strong>解释：</strong>分数 = max(nums) - min(nums) = 1 - 1 = 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,10], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,6], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 排序

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
    int smallestRangeII(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestRangeII(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int smallestRangeII(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestRangeII(int[] nums, int k) {
        
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
var smallestRangeII = function(nums, k) {
    
};
```

### TypeScript

```typescript
function smallestRangeII(nums: number[], k: number): number {
    
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
    function smallestRangeII($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestRangeII(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestRangeII(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestRangeII(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func smallestRangeII(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_range_ii(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def smallestRangeII(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_range_ii(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-range-ii nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_range_ii(Nums :: [integer()], K :: integer()) -> integer().
smallest_range_ii(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_range_ii(nums :: [integer], k :: integer) :: integer
  def smallest_range_ii(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestRangeII(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

