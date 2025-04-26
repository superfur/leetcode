# 862. 和至少为 K 的最短子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，找出 <code>nums</code> 中和至少为 <code>k</code> 的 <strong>最短非空子数组</strong> ，并返回该子数组的长度。如果不存在这样的 <strong>子数组</strong> ，返回 <code>-1</code> 。</p>

<p><strong>子数组</strong> 是数组中 <strong>连续</strong> 的一部分。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], k = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2], k = 4
<strong>输出：</strong>-1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,-1,2], k = 3
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 队列
- 数组
- 二分查找
- 前缀和
- 滑动窗口
- 单调队列
- 堆（优先队列）

## 示例

```
[1]
1
[1,2]
4
[2,-1,2]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shortestSubarray(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int shortestSubarray(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int shortestSubarray(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShortestSubarray(int[] nums, int k) {
        
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
var shortestSubarray = function(nums, k) {
    
};
```

### TypeScript

```typescript
function shortestSubarray(nums: number[], k: number): number {
    
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
    function shortestSubarray($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shortestSubarray(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shortestSubarray(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shortestSubarray(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func shortestSubarray(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def shortest_subarray(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def shortestSubarray(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shortest_subarray(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shortest-subarray nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec shortest_subarray(Nums :: [integer()], K :: integer()) -> integer().
shortest_subarray(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shortest_subarray(nums :: [integer], k :: integer) :: integer
  def shortest_subarray(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shortestSubarray(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

