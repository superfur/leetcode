# 2680. 最大或值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code> 。每一次操作中，你可以选择一个数并将它乘&nbsp;<code>2</code>&nbsp;。</p>

<p>你最多可以进行 <code>k</code>&nbsp;次操作，请你返回<em>&nbsp;</em><code>nums[0] | nums[1] | ... | nums[n - 1]</code>&nbsp;的最大值。</p>

<p><code>a | b</code>&nbsp;表示两个整数 <code>a</code>&nbsp;和 <code>b</code>&nbsp;的 <strong>按位或</strong>&nbsp;运算。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [12,9], k = 1
<b>输出：</b>30
<b>解释：</b>如果我们对下标为 1 的元素进行操作，新的数组为 [12,18] 。此时得到最优答案为 12 和 18 的按位或运算的结果，也就是 30 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [8,1,2], k = 2
<b>输出：</b>35
<b>解释：</b>如果我们对下标 0 处的元素进行操作，得到新数组 [32,1,2] 。此时得到最优答案为 32|1|2 = 35 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 15</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 数组
- 前缀和

## 提示

1. The optimal solution should apply all the k operations on a single number.
2. Calculate the prefix or and the suffix or and perform k operations over each element, and maximize the answer.

## 示例

```
[12,9]
1
[8,1,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumOr(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumOr(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        
```

### C

```c
long long maximumOr(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumOr(int[] nums, int k) {
        
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
var maximumOr = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumOr(nums: number[], k: number): number {
    
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
    function maximumOr($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumOr(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumOr(nums: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumOr(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumOr(nums []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_or(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumOr(nums: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_or(nums: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-or nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_or(Nums :: [integer()], K :: integer()) -> integer().
maximum_or(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_or(nums :: [integer], k :: integer) :: integer
  def maximum_or(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumOr(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

