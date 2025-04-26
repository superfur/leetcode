# 2420. 找到所有好下标

## 题目描述

<p>给你一个大小为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个正整数&nbsp;<code>k</code>&nbsp;。</p>

<p>对于&nbsp;<code>k &lt;= i &lt; n - k</code>&nbsp;之间的一个下标&nbsp;<code>i</code>&nbsp;，如果它满足以下条件，我们就称它为一个&nbsp;<strong>好</strong>&nbsp;下标：</p>

<ul>
	<li>下标 <code>i</code> <strong>之前</strong> 的 <code>k</code>&nbsp;个元素是 <strong>非递增的</strong>&nbsp;。</li>
	<li>下标 <code>i</code> <strong>之后</strong>&nbsp;的 <code>k</code>&nbsp;个元素是 <strong>非递减的</strong>&nbsp;。</li>
</ul>

<p>按 <strong>升序</strong>&nbsp;返回所有好下标。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,1,1,3,4,1], k = 2
<b>输出：</b>[2,3]
<b>解释：</b>数组中有两个好下标：
- 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
- 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,1,2], k = 2
<b>输出：</b>[]
<b>解释：</b>数组中没有好下标。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= n / 2</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 前缀和

## 提示

1. Iterate over all indices i. How do you quickly check the two conditions?
2. Precompute for each index whether the conditions are satisfied on the left and the right of the index. You can do that with two iterations, from left to right and right to left.

## 示例

```
[2,1,1,1,3,4,1]
2
[2,1,1,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> goodIndices(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* goodIndices(int* nums, int numsSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> GoodIndices(int[] nums, int k) {
        
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
var goodIndices = function(nums, k) {
    
};
```

### TypeScript

```typescript
function goodIndices(nums: number[], k: number): number[] {
    
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
    function goodIndices($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func goodIndices(_ nums: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun goodIndices(nums: IntArray, k: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> goodIndices(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func goodIndices(nums []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def good_indices(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def goodIndices(nums: Array[Int], k: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn good_indices(nums: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (good-indices nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec good_indices(Nums :: [integer()], K :: integer()) -> [integer()].
good_indices(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec good_indices(nums :: [integer], k :: integer) :: [integer]
  def good_indices(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func goodIndices(nums: Array<Int64>, k: Int64): ArrayList<Int64> {

    }
}
```

