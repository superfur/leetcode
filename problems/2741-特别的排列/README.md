# 2741. 特别的排列

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，它包含 <code>n</code>&nbsp;个 <strong>互不相同</strong>&nbsp;的正整数。如果&nbsp;<code>nums</code>&nbsp;的一个排列满足以下条件，我们称它是一个特别的排列：</p>

<ul>
	<li>对于&nbsp;<code>0 &lt;= i &lt; n - 1</code>&nbsp;的下标 <code>i</code>&nbsp;，要么&nbsp;<code>nums[i] % nums[i+1] == 0</code>&nbsp;，要么&nbsp;<code>nums[i+1] % nums[i] == 0</code>&nbsp;。</li>
</ul>

<p>请你返回特别排列的总数目，由于答案可能很大，请将它对<strong>&nbsp;</strong><code>10<sup>9&nbsp;</sup>+ 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,3,6]
<b>输出：</b>2
<b>解释：</b>[3,6,2] 和 [2,6,3] 是 nums 两个特别的排列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,4,3]
<b>输出：</b>2
<b>解释：</b>[3,1,4] 和 [4,1,3] 是 nums 两个特别的排列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 14</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 提示

1. Can we solve this problem using DP with bit masking?
2. You just need two states in DP which are last_ind in the permutation and the mask of numbers already used.

## 示例

```
[2,3,6]
[1,4,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int specialPerm(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int specialPerm(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
```

### C

```c
int specialPerm(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SpecialPerm(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var specialPerm = function(nums) {
    
};
```

### TypeScript

```typescript
function specialPerm(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function specialPerm($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func specialPerm(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun specialPerm(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int specialPerm(List<int> nums) {
    
  }
}
```

### Go

```golang
func specialPerm(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def special_perm(nums)
    
end
```

### Scala

```scala
object Solution {
    def specialPerm(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn special_perm(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (special-perm nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec special_perm(Nums :: [integer()]) -> integer().
special_perm(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec special_perm(nums :: [integer]) :: integer
  def special_perm(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func specialPerm(nums: Array<Int64>): Int64 {

    }
}
```

