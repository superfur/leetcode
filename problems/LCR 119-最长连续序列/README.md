# LCR 119. 最长连续序列

## 题目描述

<p>给定一个未排序的整数数组 <code>nums</code> ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [100,4,200,1,3,2]
<strong>输出：</strong>4
<strong>解释：</strong>最长数字连续序列是 <code>[1, 2, 3, 4]。它的长度为 4。</code></pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,3,7,2,5,8,4,6,0,1]
<strong>输出：</strong>9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>可以设计并实现时间复杂度为&nbsp;<code>O(n)</code><em> </em>的解决方案吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 128&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/longest-consecutive-sequence/">https://leetcode-cn.com/problems/longest-consecutive-sequence/</a></p>


## 难度

Medium

## 标签

- 并查集
- 数组
- 哈希表

## 示例

```
[100,4,200,1,3,2]
[0,3,7,2,5,8,4,6,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int longestConsecutive(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
```

### C

```c


int longestConsecutive(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int LongestConsecutive(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {

};
```

### TypeScript

```typescript
function longestConsecutive(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestConsecutive($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestConsecutive(nums: IntArray): Int {

    }
}
```

### Go

```golang
func longestConsecutive(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_consecutive(nums)

end
```

### Scala

```scala
object Solution {
    def longestConsecutive(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (longest-consecutive nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec longest_consecutive(Nums :: [integer()]) -> integer().
longest_consecutive(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_consecutive(nums :: [integer]) :: integer
  def longest_consecutive(nums) do

  end
end
```

