# 3254. 长度为 K 的子数组的能量值 I

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个正整数&nbsp;<code>k</code>&nbsp;。</p>

<p>一个数组的 <strong>能量值</strong> 定义为：</p>

<ul>
	<li>如果 <strong>所有</strong>&nbsp;元素都是依次&nbsp;<strong>连续</strong> 且 <strong>上升</strong> 的，那么能量值为 <strong>最大</strong>&nbsp;的元素。</li>
	<li>否则为 -1 。</li>
</ul>

<p>你需要求出 <code>nums</code>&nbsp;中所有长度为 <code>k</code>&nbsp;的&nbsp;<span data-keyword="subarray-nonempty">子数组</span>&nbsp;的能量值。</p>

<p>请你返回一个长度为 <code>n - k + 1</code>&nbsp;的整数数组&nbsp;<code>results</code>&nbsp;，其中&nbsp;<code>results[i]</code>&nbsp;是子数组&nbsp;<code>nums[i..(i + k - 1)]</code>&nbsp;的能量值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4,3,2,5], k = 3</span></p>

<p><b>输出：</b>[3,4,-1,-1,-1]</p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;中总共有 5 个长度为 3 的子数组：</p>

<ul>
	<li><code>[1, 2, 3]</code>&nbsp;中最大元素为 3 。</li>
	<li><code>[2, 3, 4]</code>&nbsp;中最大元素为 4 。</li>
	<li><code>[3, 4, 3]</code>&nbsp;中元素 <strong>不是</strong>&nbsp;连续的。</li>
	<li><code>[4, 3, 2]</code>&nbsp;中元素 <b>不是</b>&nbsp;上升的。</li>
	<li><code>[3, 2, 5]</code>&nbsp;中元素 <strong>不是</strong>&nbsp;连续的。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,2,2,2,2], k = 4</span></p>

<p><span class="example-io"><b>输出：</b>[-1,-1]</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,2,3,2,3,2], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>[-1,3,-1,3,-1]</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 提示

1. Can we use a brute force solution with nested loops and HashSet?

## 示例

```
[1,2,3,4,3,2,5]
3
[2,2,2,2,2]
4
[3,2,3,2,3,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> resultsArray(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] resultsArray(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ResultsArray(int[] nums, int k) {
        
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
var resultsArray = function(nums, k) {
    
};
```

### TypeScript

```typescript
function resultsArray(nums: number[], k: number): number[] {
    
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
    function resultsArray($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func resultsArray(_ nums: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun resultsArray(nums: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> resultsArray(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func resultsArray(nums []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def results_array(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def resultsArray(nums: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn results_array(nums: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (results-array nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec results_array(Nums :: [integer()], K :: integer()) -> [integer()].
results_array(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec results_array(nums :: [integer], k :: integer) :: [integer]
  def results_array(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func resultsArray(nums: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

