# 2099. 找到和最大的长度为 K 的子序列

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你需要找到&nbsp;<code>nums</code>&nbsp;中长度为 <code>k</code>&nbsp;的 <strong>子序列</strong>&nbsp;，且这个子序列的&nbsp;<strong>和最大&nbsp;</strong>。</p>

<p>请你返回 <strong>任意</strong> 一个长度为&nbsp;<code>k</code>&nbsp;的整数子序列。</p>

<p><strong>子序列</strong>&nbsp;定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,1,3,3], k = 2
<b>输出：</b>[3,3]
<strong>解释：</strong>
子序列有最大和：3 + 3 = 6 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [-1,-2,3,4], k = 3
<b>输出：</b>[-1,3,4]
<b>解释：</b>
子序列有最大和：-1 + 3 + 4 = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [3,4,3,3], k = 2
<b>输出：</b>[3,4]
<strong>解释：</strong>
子序列有最大和：3 + 4 = 7 。
另一个可行的子序列为 [4, 3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序
- 堆（优先队列）

## 提示

1. From a greedy perspective, what k elements should you pick?
2. Could you sort the array while maintaining the index?

## 示例

```
[2,1,3,3]
2
[-1,-2,3,4]
3
[3,4,3,3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxSubsequence(int* nums, int numsSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaxSubsequence(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSubsequence = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxSubsequence(nums: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function maxSubsequence($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSubsequence(_ nums: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSubsequence(nums: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maxSubsequence(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxSubsequence(nums []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_subsequence(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxSubsequence(nums: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_subsequence(nums: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (max-subsequence nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec max_subsequence(Nums :: [integer()], K :: integer()) -> [integer()].
max_subsequence(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_subsequence(nums :: [integer], k :: integer) :: [integer]
  def max_subsequence(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSubsequence(nums: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

