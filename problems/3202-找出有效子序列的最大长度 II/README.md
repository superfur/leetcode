# 3202. 找出有效子序列的最大长度 II

## 题目描述

给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个 <strong>正</strong>&nbsp;整数&nbsp;<code>k</code>&nbsp;。
<p><code>nums</code>&nbsp;的一个&nbsp;<span data-keyword="subsequence-array">子序列</span> <code>sub</code>&nbsp;的长度为 <code>x</code>&nbsp;，如果其满足以下条件，则称其为 <strong>有效子序列</strong>&nbsp;：</p>

<ul>
	<li><code>(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k</code></li>
</ul>
返回 <code>nums</code>&nbsp;的 <strong>最长</strong><strong>有效子序列</strong>&nbsp;的长度。

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4,5], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><b>解释：</b></p>

<p>最长有效子序列是&nbsp;<code>[1, 2, 3, 4, 5]</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,4,2,3,1,4], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>最长有效子序列是&nbsp;<code>[1, 4, 1, 4]</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>3</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>3</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Fix the value of <code>(subs[0] + subs[1]) % k</code> from the <code>k</code> possible values. Let it be <code>val</code>.
2. Let <code>dp[i]</code> store the maximum length of a subsequence with its last element <code>x</code> such that <code>x % k == i</code>.
3. Answer for a subsequence ending at index <code>y</code> is <code>dp[(k + val - (y % k)) % k] + 1</code>.

## 示例

```
[1,2,3,4,5]
2
[1,4,2,3,1,4]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumLength(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumLength(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumLength(int[] nums, int k) {
        
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
var maximumLength = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumLength(nums: number[], k: number): number {
    
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
    function maximumLength($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumLength(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumLength(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_length(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-length nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_length(Nums :: [integer()], K :: integer()) -> integer().
maximum_length(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer], k :: integer) :: integer
  def maximum_length(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumLength(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

