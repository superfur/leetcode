# 3287. 求出数组中最大序列值

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。</p>

<p>定义长度为 <code>2 * x</code>&nbsp;的序列 <code>seq</code>&nbsp;的 <strong>值</strong>&nbsp;为：</p>

<ul>
	<li><code>(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1])</code>.</li>
</ul>

<p>请你求出 <code>nums</code>&nbsp;中所有长度为 <code>2 * k</code>&nbsp;的 <span data-keyword="subsequence-array">子序列</span> 的 <strong>最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,6,7], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><strong>解释：</strong></p>

<p>子序列&nbsp;<code>[2, 7]</code>&nbsp;的值最大，为&nbsp;<code>2 XOR 7 = 5</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [4,2,5,6,7], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>子序列&nbsp;<code>[4, 5, 6, 7]</code>&nbsp;的值最大，为&nbsp;<code>(4 OR 5) XOR (6 OR 7) = 2</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 400</code></li>
	<li><code>1 &lt;= nums[i] &lt; 2<sup>7</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length / 2</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划

## 提示

1. Find all the possible <code>OR</code> till each <code>i</code> with <code>k</code> elements backward and forward.

## 示例

```
[2,6,7]
1
[4,2,5,6,7]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxValue(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxValue(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maxValue(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxValue(int[] nums, int k) {
        
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
var maxValue = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxValue(nums: number[], k: number): number {
    
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
    function maxValue($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxValue(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxValue(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxValue(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxValue(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_value(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxValue(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_value(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-value nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_value(Nums :: [integer()], K :: integer()) -> integer().
max_value(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_value(nums :: [integer], k :: integer) :: integer
  def max_value(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxValue(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

