# 1403. 非递增顺序的最小子序列

## 题目描述

<p>给你一个数组 <code>nums</code>，请你从中抽取一个子序列，满足该子序列的元素之和 <strong>严格</strong> 大于未包含在该子序列中的各元素之和。</p>

<p>如果存在多个解决方案，只需返回 <strong>长度最小</strong> 的子序列。如果仍然有多个解决方案，则返回 <strong>元素之和最大</strong> 的子序列。</p>

<p>与子数组不同的地方在于，「数组的子序列」不强调元素在原数组中的连续性，也就是说，它可以通过从数组中分离一些（也可能不分离）元素得到。</p>

<p><strong>注意</strong>，题目数据保证满足所有约束条件的解决方案是 <strong>唯一</strong> 的。同时，返回的答案应当按 <strong>非递增顺序</strong> 排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,3,10,9,8]
<strong>输出：</strong>[10,9] 
<strong>解释：</strong>子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。&nbsp;
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,4,7,6,7]
<strong>输出：</strong>[7,7,6] 
<strong>解释：</strong>子序列 [7,7] 的和为 14 ，不严格大于剩下的其他元素之和（14 = 4 + 4 + 6）。因此，[7,6,7] 是满足题意的最小子序列。注意，元素按非递增顺序返回。  
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort elements and take each element from the largest until accomplish the conditions.

## 示例

```
[4,3,10,9,8]
[4,4,7,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minSubsequence(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minSubsequence(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> MinSubsequence(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var minSubsequence = function(nums) {
    
};
```

### TypeScript

```typescript
function minSubsequence(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function minSubsequence($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSubsequence(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSubsequence(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minSubsequence(List<int> nums) {
    
  }
}
```

### Go

```golang
func minSubsequence(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def min_subsequence(nums)
    
end
```

### Scala

```scala
object Solution {
    def minSubsequence(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_subsequence(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (min-subsequence nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_subsequence(Nums :: [integer()]) -> [integer()].
min_subsequence(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_subsequence(nums :: [integer]) :: [integer]
  def min_subsequence(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSubsequence(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

