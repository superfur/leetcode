# LCR 008. 长度最小的子数组

## 题目描述

<p>给定一个含有&nbsp;<code>n</code><strong>&nbsp;</strong>个正整数的数组和一个正整数 <code>target</code><strong> 。</strong></p>

<p>找出该数组中满足其和<strong> </strong><code>&ge; target</code><strong> </strong>的长度最小的 <strong>连续子数组</strong>&nbsp;<code>[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]</code> ，并返回其长度<strong>。</strong>如果不存在符合条件的子数组，返回 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = 7, nums = [2,3,1,2,4,3]
<strong>输出：</strong>2
<strong>解释：</strong>子数组&nbsp;<code>[4,3]</code>&nbsp;是该条件下的长度最小的子数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = 4, nums = [1,4,4]
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>target = 11, nums = [1,1,1,1,1,1,1,1]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p>提示：</p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p>进阶：</p>

<ul>
	<li>如果你已经实现<em> </em><code>O(n)</code> 时间复杂度的解法, 请尝试设计一个 <code>O(n log(n))</code> 时间复杂度的解法。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 209&nbsp;题相同：<a href="https://leetcode-cn.com/problems/minimum-size-subarray-sum/">https://leetcode-cn.com/problems/minimum-size-subarray-sum/</a></p>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 前缀和
- 滑动窗口

## 示例

```
7
[2,3,1,2,4,3]
4
[1,4,4]
11
[1,1,1,1,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int minSubArrayLen(int target, int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
```

### C

```c


int minSubArrayLen(int target, int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {

};
```

### TypeScript

```typescript
function minSubArrayLen(target: number, nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @param Integer[] $nums
     * @return Integer
     */
    function minSubArrayLen($target, $nums) {

    }
}
```

### Swift

```swift
class Solution {
    func minSubArrayLen(_ target: Int, _ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSubArrayLen(target: Int, nums: IntArray): Int {

    }
}
```

### Go

```golang
func minSubArrayLen(target int, nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer} target
# @param {Integer[]} nums
# @return {Integer}
def min_sub_array_len(target, nums)

end
```

### Scala

```scala
object Solution {
    def minSubArrayLen(target: Int, nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (min-sub-array-len target nums)
  (-> exact-integer? (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec min_sub_array_len(Target :: integer(), Nums :: [integer()]) -> integer().
min_sub_array_len(Target, Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_sub_array_len(target :: integer, nums :: [integer]) :: integer
  def min_sub_array_len(target, nums) do

  end
end
```

