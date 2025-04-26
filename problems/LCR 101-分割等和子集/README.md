# LCR 101. 分割等和子集

## 题目描述

<p>给定一个非空的正整数数组 <code>nums</code> ，请判断能否将这些数字分成元素和相等的两部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,11,5]
<strong>输出：</strong>true
<strong>解释：</strong>nums<strong> </strong>可以分割成 [1, 5, 5] 和 [11] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,5]
<strong>输出：</strong>false
<strong>解释：</strong>nums<strong> </strong>不可以分为和相等的两部分
</pre>

<p>&nbsp;</p>

<p><meta charset="UTF-8" /></p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 416&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/partition-equal-subset-sum/">https://leetcode-cn.com/problems/partition-equal-subset-sum/</a></p>


## 难度

Easy

## 标签

- 数学
- 字符串
- 模拟

## 示例

```
[1,5,11,5]
[1,2,3,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public boolean canPartition(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
```

### Python3

```python3
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
```

### C

```c


bool canPartition(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public bool CanPartition(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canPartition = function(nums) {

};
```

### TypeScript

```typescript
function canPartition(nums: number[]): boolean {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canPartition($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func canPartition(_ nums: [Int]) -> Bool {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canPartition(nums: IntArray): Boolean {

    }
}
```

### Go

```golang
func canPartition(nums []int) bool {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def can_partition(nums)

end
```

### Scala

```scala
object Solution {
    def canPartition(nums: Array[Int]): Boolean = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_partition(nums: Vec<i32>) -> bool {

    }
}
```

### Racket

```racket
(define/contract (can-partition nums)
  (-> (listof exact-integer?) boolean?)

  )
```

### Erlang

```erlang
-spec can_partition(Nums :: [integer()]) -> boolean().
can_partition(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_partition(nums :: [integer]) :: boolean
  def can_partition(nums) do

  end
end
```

