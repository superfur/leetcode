# 1027. 最长等差数列

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，返回 <code>nums</code>&nbsp;中最长等差子序列的<strong>长度</strong>。</p>

<p>回想一下，<code>nums</code> 的子序列是一个列表&nbsp;<code>nums[i<sub>1</sub>], nums[i<sub>2</sub>], ..., nums[i<sub>k</sub>]</code> ，且&nbsp;<code>0 &lt;= i<sub>1</sub> &lt; i<sub>2</sub> &lt; ... &lt; i<sub>k</sub> &lt;= nums.length - 1</code>。并且如果&nbsp;<code>seq[i+1] - seq[i]</code>(&nbsp;<code>0 &lt;= i &lt; seq.length - 1</code>) 的值都相同，那么序列&nbsp;<code>seq</code>&nbsp;是等差的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,6,9,12]
<strong>输出：</strong>4
<strong>解释： </strong>
整个数组是公差为 3 的等差数列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [9,4,7,2,10]
<strong>输出：</strong>3
<strong>解释：</strong>
最长的等差子序列是 [4,7,10]。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [20,1,15,3,10,5,8]
<strong>输出：</strong>4
<strong>解释：</strong>
最长的等差子序列是 [20,15,10,5]。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 500</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 二分查找
- 动态规划

## 示例

```
[3,6,9,12]
[9,4,7,2,10]
[20,1,15,3,10,5,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestArithSeqLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestArithSeqLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
```

### C

```c
int longestArithSeqLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestArithSeqLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestArithSeqLength = function(nums) {
    
};
```

### TypeScript

```typescript
function longestArithSeqLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestArithSeqLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestArithSeqLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestArithSeqLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestArithSeqLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func longestArithSeqLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_arith_seq_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def longestArithSeqLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-arith-seq-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_arith_seq_length(Nums :: [integer()]) -> integer().
longest_arith_seq_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_arith_seq_length(nums :: [integer]) :: integer
  def longest_arith_seq_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestArithSeqLength(nums: Array<Int64>): Int64 {

    }
}
```

