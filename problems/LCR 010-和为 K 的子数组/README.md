# LCR 010. 和为 K 的子数组

## 题目描述

<p>给定一个整数数组和一个整数&nbsp;<code>k</code><strong> ，</strong>请找到该数组中和为&nbsp;<code>k</code><strong>&nbsp;</strong>的连续子数组的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong>nums = [1,1,1], k = 2
<strong>输出:</strong> 2
<strong>解释:</strong> 此题 [1,1] 与 [1,1] 为两种不同的情况
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong>nums = [1,2,3], k = 3
<strong>输出:</strong> 2
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li>
	<p><code>-10<sup>7</sup>&nbsp;&lt;= k &lt;= 10<sup>7</sup></code></p>
	</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 560&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/subarray-sum-equals-k/">https://leetcode-cn.com/problems/subarray-sum-equals-k/</a></p>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 示例

```
[1,1,1]
2
[1,2,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {

    }
};
```

### Java

```java
class Solution {
    public int subarraySum(int[] nums, int k) {

    }
}
```

### Python

```python
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
```

### C

```c


int subarraySum(int* nums, int numsSize, int k){

}
```

### C#

```csharp
public class Solution {
    public int SubarraySum(int[] nums, int k) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {

};
```

### TypeScript

```typescript
function subarraySum(nums: number[], k: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function subarraySum($nums, $k) {

    }
}
```

### Swift

```swift
class Solution {
    func subarraySum(_ nums: [Int], _ k: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {

    }
}
```

### Go

```golang
func subarraySum(nums []int, k int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)

end
```

### Scala

```scala
object Solution {
    def subarraySum(nums: Array[Int], k: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec subarray_sum(Nums :: [integer()], K :: integer()) -> integer().
subarray_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarray_sum(nums :: [integer], k :: integer) :: integer
  def subarray_sum(nums, k) do

  end
end
```

