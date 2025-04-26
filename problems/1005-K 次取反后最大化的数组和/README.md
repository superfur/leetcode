# 1005. K 次取反后最大化的数组和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> ，按以下方法修改该数组：</p>

<ul>
	<li>选择某个下标 <code>i</code>&nbsp;并将 <code>nums[i]</code> 替换为 <code>-nums[i]</code> 。</li>
</ul>

<p>重复这个过程恰好 <code>k</code> 次。可以多次选择同一个下标 <code>i</code> 。</p>

<p>以这种方式修改数组后，返回数组 <strong>可能的最大和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,2,3], k = 1
<strong>输出：</strong>5
<strong>解释：</strong>选择下标 1 ，nums 变为 [4,-2,3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,-1,0,2], k = 3
<strong>输出：</strong>6
<strong>解释：</strong>选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,-3,-1,5,-4], k = 2
<strong>输出：</strong>13
<strong>解释：</strong>选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 排序

## 示例

```
[4,2,3]
1
[3,-1,0,2]
3
[2,-3,-1,5,-4]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestSumAfterKNegations(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int largestSumAfterKNegations(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestSumAfterKNegations(int[] nums, int k) {
        
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
var largestSumAfterKNegations = function(nums, k) {
    
};
```

### TypeScript

```typescript
function largestSumAfterKNegations(nums: number[], k: number): number {
    
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
    function largestSumAfterKNegations($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestSumAfterKNegations(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestSumAfterKNegations(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestSumAfterKNegations(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func largestSumAfterKNegations(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_sum_after_k_negations(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def largestSumAfterKNegations(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_sum_after_k_negations(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-sum-after-k-negations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_sum_after_k_negations(Nums :: [integer()], K :: integer()) -> integer().
largest_sum_after_k_negations(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_sum_after_k_negations(nums :: [integer], k :: integer) :: integer
  def largest_sum_after_k_negations(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestSumAfterKNegations(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

