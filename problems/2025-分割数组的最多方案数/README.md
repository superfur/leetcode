# 2025. 分割数组的最多方案数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始且长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。<strong>分割</strong>&nbsp;数组 <code>nums</code>&nbsp;的方案数定义为符合以下两个条件的 <code>pivot</code>&nbsp;数目：</p>

<ul>
	<li><code>1 &lt;= pivot &lt; n</code></li>
	<li><code>nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]</code></li>
</ul>

<p>同时给你一个整数&nbsp;<code>k</code>&nbsp;。你可以将&nbsp;<code>nums</code>&nbsp;中&nbsp;<strong>一个</strong>&nbsp;元素变为&nbsp;<code>k</code>&nbsp;或&nbsp;<strong>不改变</strong>&nbsp;数组。</p>

<p>请你返回在 <strong>至多</strong>&nbsp;改变一个元素的前提下，<strong>最多</strong>&nbsp;有多少种方法 <strong>分割</strong>&nbsp;<code>nums</code>&nbsp;使得上述两个条件都满足。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,-1,2], k = 3
<b>输出：</b>1
<b>解释：</b>一个最优的方案是将 nums[0] 改为 k&nbsp;。数组变为 [<em><strong>3</strong></em>,-1,2] 。
有一种方法分割数组：
- pivot = 2 ，我们有分割 [3,-1 | 2]：3 + -1 == 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [0,0,0], k = 1
<b>输出：</b>2
<b>解释：</b>一个最优的方案是不改动数组。
有两种方法分割数组：
- pivot = 1 ，我们有分割 [0 | 0,0]：0 == 0 + 0 。
- pivot = 2 ，我们有分割 [0,0 | 0]: 0 + 0 == 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
<b>输出：</b>4
<b>解释：</b>一个最优的方案是将 nums[2] 改为 k 。数组变为 [22,4,<em><strong>-33</strong></em>,-20,-15,15,-16,7,19,-10,0,-13,-14] 。
有四种方法分割数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= k, nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 计数
- 枚举
- 前缀和

## 提示

1. A pivot point splits the array into equal prefix and suffix. If no change is made to the array, the goal is to find the number of pivot p such that prefix[p-1] == suffix[p].
2. Consider how prefix and suffix will change when we change a number nums[i] to k.
3. When sweeping through each element, can you find the total number of pivots where the difference of prefix and suffix happens to equal to the changes of k-nums[i].

## 示例

```
[2,-1,2]
3
[0,0,0]
1
[22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14]
-33
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToPartition(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToPartition(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToPartition(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int waysToPartition(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToPartition(int[] nums, int k) {
        
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
var waysToPartition = function(nums, k) {
    
};
```

### TypeScript

```typescript
function waysToPartition(nums: number[], k: number): number {
    
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
    function waysToPartition($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToPartition(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToPartition(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToPartition(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func waysToPartition(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def ways_to_partition(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def waysToPartition(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_partition(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-partition nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_partition(Nums :: [integer()], K :: integer()) -> integer().
ways_to_partition(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_partition(nums :: [integer], k :: integer) :: integer
  def ways_to_partition(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToPartition(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

