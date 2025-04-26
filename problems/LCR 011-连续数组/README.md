# LCR 011. 连续数组

## 题目描述

<p>给定一个二进制数组 <code>nums</code> , 找到含有相同数量的 <code>0</code> 和 <code>1</code> 的最长连续子数组，并返回该子数组的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> nums = [0,1]
<strong>输出:</strong> 2
<strong>解释:</strong> [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> nums = [0,1,0]
<strong>输出:</strong> 2
<strong>解释:</strong> [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 不是 <code>0</code> 就是 <code>1</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 525&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/contiguous-array/">https://leetcode-cn.com/problems/contiguous-array/</a></p>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 示例

```
[0,1]
[0,1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaxLength(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int findMaxLength(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
```

### C

```c


int findMaxLength(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int FindMaxLength(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxLength = function(nums) {

};
```

### TypeScript

```typescript
function findMaxLength(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxLength($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func findMaxLength(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxLength(nums: IntArray): Int {

    }
}
```

### Go

```golang
func findMaxLength(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_max_length(nums)

end
```

### Scala

```scala
object Solution {
    def findMaxLength(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (find-max-length nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec find_max_length(Nums :: [integer()]) -> integer().
find_max_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_length(nums :: [integer]) :: integer
  def find_max_length(nums) do

  end
end
```

