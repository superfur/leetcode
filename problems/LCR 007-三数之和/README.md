# LCR 007. 三数之和

## 题目描述

<p>给定一个包含 <code>n</code> 个整数的数组&nbsp;<code>nums</code>，判断&nbsp;<code>nums</code>&nbsp;中是否存在三个元素&nbsp;<code>a</code> ，<code>b</code> ，<code>c</code> <em>，</em>使得&nbsp;<code>a + b + c = 0</code> ？请找出所有和为 <code>0</code> 且&nbsp;<strong>不重复&nbsp;</strong>的三元组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,0,1,2,-1,-4]
<strong>输出：</strong>[[-1,-1,2],[-1,0,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 15&nbsp;题相同：<a href="https://leetcode-cn.com/problems/3sum/">https://leetcode-cn.com/problems/3sum/</a></p>


## 难度

Medium

## 标签

- 数组
- 双指针
- 排序

## 示例

```
[-1,0,1,2,-1,-4]
[]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {

};
```

### TypeScript

```typescript
function threeSum(nums: number[]): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function threeSum($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {

    }
}
```

### Go

```golang
func threeSum(nums []int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def three_sum(nums)

end
```

### Scala

```scala
object Solution {
    def threeSum(nums: Array[Int]): List[List[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (three-sum nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec three_sum(Nums :: [integer()]) -> [[integer()]].
three_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec three_sum(nums :: [integer]) :: [[integer]]
  def three_sum(nums) do

  end
end
```

