# LCR 067. 数组中两个数的最大异或值

## 题目描述

<p>给定一个整数数组 <code>nums</code> ，返回<em> </em><code>nums[i] XOR nums[j]</code> 的最大运算结果，其中 <code>0 &le; i &le; j &lt; n</code> 。</p>

<p>&nbsp;</p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,10,5,25,2,8]
<strong>输出：</strong>28
<strong>解释：</strong>最大运算结果是 5 XOR 25 = 28.</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4]
<strong>输出：</strong>6
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [8,10,2]
<strong>输出：</strong>10
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>nums = [14,70,53,83,49,91,36,80,92,51,66,70]
<strong>输出：</strong>127
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>
</div>
</div>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以在 <code>O(n)</code> 的时间解决这个问题吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 421&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/">https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/</a></p>


## 难度

Medium

## 标签

- 位运算
- 字典树
- 数组
- 哈希表

## 示例

```
[3,10,5,25,2,8]
[0]
[2,4]
[8,10,2]
[14,70,53,83,49,91,36,80,92,51,66,70]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int findMaximumXOR(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
```

### C

```c


int findMaximumXOR(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int FindMaximumXOR(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaximumXOR = function(nums) {

};
```

### TypeScript

```typescript
function findMaximumXOR(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaximumXOR($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func findMaximumXOR(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaximumXOR(nums: IntArray): Int {

    }
}
```

### Go

```golang
func findMaximumXOR(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_maximum_xor(nums)

end
```

### Scala

```scala
object Solution {
    def findMaximumXOR(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_maximum_xor(nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (find-maximum-xor nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec find_maximum_xor(Nums :: [integer()]) -> integer().
find_maximum_xor(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_maximum_xor(nums :: [integer]) :: integer
  def find_maximum_xor(nums) do

  end
end
```

