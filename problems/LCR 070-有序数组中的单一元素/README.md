# LCR 070. 有序数组中的单一元素

## 题目描述

<p>给定一个只包含整数的有序数组 <code>nums</code>&nbsp;，每个元素都会出现两次，唯有一个数只会出现一次，请找出这个唯一的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> nums = [1,1,2,3,3,4,4,8,8]
<strong>输出:</strong> 2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> nums =  [3,3,7,7,10,11,11]
<strong>输出:</strong> 10
</pre>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" /></p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i]&nbsp;&lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>采用的方案可以在 <code>O(log n)</code> 时间复杂度和 <code>O(1)</code> 空间复杂度中运行吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 540&nbsp;题相同：<a href="https://leetcode-cn.com/problems/single-element-in-a-sorted-array/">https://leetcode-cn.com/problems/single-element-in-a-sorted-array/</a></p>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 示例

```
[1,1,2,3,3,4,4,8,8]
[3,3,7,7,10,11,11]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int singleNonDuplicate(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
```

### C

```c


int singleNonDuplicate(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int SingleNonDuplicate(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {

};
```

### TypeScript

```typescript
function singleNonDuplicate(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function singleNonDuplicate($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func singleNonDuplicate(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun singleNonDuplicate(nums: IntArray): Int {

    }
}
```

### Go

```golang
func singleNonDuplicate(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def single_non_duplicate(nums)

end
```

### Scala

```scala
object Solution {
    def singleNonDuplicate(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn single_non_duplicate(nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (single-non-duplicate nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec single_non_duplicate(Nums :: [integer()]) -> integer().
single_non_duplicate(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec single_non_duplicate(nums :: [integer]) :: integer
  def single_non_duplicate(nums) do

  end
end
```

