# LCR 004. 只出现一次的数字 II

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> ，除某个元素仅出现 <strong>一次</strong> 外，其余每个元素都恰出现 <strong>三次 。</strong>请你找出并返回那个只出现了一次的元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,3,2]
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,0,1,0,1,100]
<strong>输出：</strong>100
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>nums</code> 中，除某个元素仅出现 <strong>一次</strong> 外，其余每个元素都恰出现 <strong>三次</strong></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 137&nbsp;题相同：<a href="https://leetcode-cn.com/problems/single-number-ii/">https://leetcode-cn.com/problems/single-number-ii/</a></p>


## 难度

Medium

## 标签

- 位运算
- 数组

## 示例

```
[2,2,3,2]
[0,1,0,1,0,1,99]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int singleNumber(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
```

### C

```c


int singleNumber(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int SingleNumber(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {

};
```

### TypeScript

```typescript
function singleNumber(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNumber($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun singleNumber(nums: IntArray): Int {

    }
}
```

### Go

```golang
func singleNumber(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def single_number(nums)

end
```

### Scala

```scala
object Solution {
    def singleNumber(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (single-number nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec single_number(Nums :: [integer()]) -> integer().
single_number(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec single_number(nums :: [integer]) :: integer
  def single_number(nums) do

  end
end
```

