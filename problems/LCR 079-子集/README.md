# LCR 079. 子集

## 题目描述

<p>给定一个整数数组&nbsp;<code>nums</code> ，数组中的元素 <strong>互不相同</strong> 。返回该数组所有可能的子集（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。你可以按 <strong>任意顺序</strong> 返回解集。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[[],[0]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 78&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/subsets/">https://leetcode-cn.com/problems/subsets/</a></p>


## 难度

Medium

## 标签

- 位运算
- 数组
- 回溯

## 示例

```
[1,2,3]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> subsets(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** subsets(int* nums, int numsSize, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {

};
```

### TypeScript

```typescript
function subsets(nums: number[]): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsets($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {

    }
}
```

### Go

```golang
func subsets(nums []int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def subsets(nums)

end
```

### Scala

```scala
object Solution {
    def subsets(nums: Array[Int]): List[List[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (subsets nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec subsets(Nums :: [integer()]) -> [[integer()]].
subsets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subsets(nums :: [integer]) :: [[integer]]
  def subsets(nums) do

  end
end
```

