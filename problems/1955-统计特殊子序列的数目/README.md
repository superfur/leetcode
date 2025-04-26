# 1955. 统计特殊子序列的数目

## 题目描述

<p><strong>特殊序列</strong> 是由&nbsp;<strong>正整数</strong>&nbsp;个 <code>0</code>&nbsp;，紧接着&nbsp;<strong>正整数</strong>&nbsp;个 <code>1</code>&nbsp;，最后 <strong>正整数</strong>&nbsp;个 <code>2</code>&nbsp;组成的序列。</p>

<ul>
	<li>比方说，<code>[0,1,2]</code> 和&nbsp;<code>[0,0,1,1,1,2]</code>&nbsp;是特殊序列。</li>
	<li>相反，<code>[2,1,0]</code>&nbsp;，<code>[1]</code>&nbsp;和&nbsp;<code>[0,1,2,0]</code>&nbsp;就不是特殊序列。</li>
</ul>

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;（<strong>仅</strong>&nbsp;包含整数&nbsp;<code>0</code>，<code>1</code>&nbsp;和&nbsp;<code>2</code>），请你返回 <b>不同特殊子序列的数目</b>&nbsp;。由于答案可能很大，请你将它对&nbsp;<code>10<sup>9</sup> + 7</code> <strong>取余</strong> 后返回。</p>

<p>一个数组的 <strong>子序列</strong>&nbsp;是从原数组中删除零个或者若干个元素后，剩下元素不改变顺序得到的序列。如果两个子序列的 <strong>下标集合</strong>&nbsp;不同，那么这两个子序列是 <strong>不同的</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [0,1,2,2]
<b>输出：</b>3
<b>解释：</b>特殊子序列为 [<strong>0</strong>,<strong>1</strong>,<strong>2</strong>,2]，[<strong>0</strong>,<strong>1</strong>,2,<strong>2</strong>] 和 [<strong>0</strong>,<strong>1</strong>,<strong>2</strong>,<strong>2</strong>] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,2,0,0]
<b>输出：</b>0
<b>解释：</b>数组 [2,2,0,0] 中没有特殊子序列。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [0,1,2,0,1,2]
<b>输出：</b>7
<b>解释：</b>特殊子序列包括：
- [<strong>0</strong>,<strong>1</strong>,<strong>2</strong>,0,1,2]
- [<strong>0</strong>,<strong>1</strong>,2,0,1,<strong>2</strong>]
- [<strong>0</strong>,<strong>1</strong>,<strong>2</strong>,0,1,<strong>2</strong>]
- [<strong>0</strong>,<strong>1</strong>,2,0,<strong>1</strong>,<strong>2</strong>]
- [<strong>0</strong>,1,2,<strong>0</strong>,<strong>1</strong>,<strong>2</strong>]
- [<strong>0</strong>,1,2,0,<strong>1</strong>,<strong>2</strong>]
- [0,1,2,<strong>0</strong>,<strong>1</strong>,<strong>2</strong>]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. Can we first solve a simpler problem? Counting the number of subsequences with 1s followed by 0s.
2. How can we keep track of the partially matched subsequences to help us find the answer?

## 示例

```
[0,1,2,2]
[2,2,0,0]
[0,1,2,0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSpecialSubsequences(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSpecialSubsequences(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSpecialSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        
```

### C

```c
int countSpecialSubsequences(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSpecialSubsequences(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countSpecialSubsequences = function(nums) {
    
};
```

### TypeScript

```typescript
function countSpecialSubsequences(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countSpecialSubsequences($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSpecialSubsequences(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSpecialSubsequences(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSpecialSubsequences(List<int> nums) {
    
  }
}
```

### Go

```golang
func countSpecialSubsequences(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_special_subsequences(nums)
    
end
```

### Scala

```scala
object Solution {
    def countSpecialSubsequences(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_special_subsequences(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-special-subsequences nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_special_subsequences(Nums :: [integer()]) -> integer().
count_special_subsequences(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_special_subsequences(nums :: [integer]) :: integer
  def count_special_subsequences(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSpecialSubsequences(nums: Array<Int64>): Int64 {

    }
}
```

