# 719. 找出第 K 小的数对距离

## 题目描述

<p>数对 <code>(a,b)</code> 由整数 <code>a</code> 和 <code>b</code> 组成，其数对距离定义为 <code>a</code> 和 <code>b</code> 的绝对差值。</p>

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，数对由 <code>nums[i]</code> 和 <code>nums[j]</code> 组成且满足 <code>0 &lt;= i &lt; j &lt; nums.length</code> 。返回 <strong>所有数对距离中</strong> 第 <code>k</code> 小的数对距离。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,1], k = 1
<strong>输出：</strong>0
<strong>解释：</strong>数对和对应的距离如下：
(1,3) -&gt; 2
(1,1) -&gt; 0
(3,1) -&gt; 2
距离第 1 小的数对是 (1,1) ，距离为 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1], k = 2
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,6,1], k = 3
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= n * (n - 1) / 2</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 双指针
- 二分查找
- 排序

## 提示

1. Binary search for the answer.  How can you check how many pairs have distance <= X?

## 示例

```
[1,3,1]
1
[1,1,1]
2
[1,6,1]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestDistancePair(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int smallestDistancePair(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestDistancePair(int[] nums, int k) {
        
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
var smallestDistancePair = function(nums, k) {
    
};
```

### TypeScript

```typescript
function smallestDistancePair(nums: number[], k: number): number {
    
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
    function smallestDistancePair($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestDistancePair(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestDistancePair(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestDistancePair(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func smallestDistancePair(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def smallest_distance_pair(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def smallestDistancePair(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_distance_pair(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-distance-pair nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_distance_pair(Nums :: [integer()], K :: integer()) -> integer().
smallest_distance_pair(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_distance_pair(nums :: [integer], k :: integer) :: integer
  def smallest_distance_pair(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestDistancePair(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

