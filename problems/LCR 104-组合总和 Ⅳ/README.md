# LCR 104. 组合总和 Ⅳ

## 题目描述

<p>给定一个由 <strong>不同</strong>&nbsp;正整数组成的数组 <code>nums</code> ，和一个目标整数 <code>target</code> 。请从 <code>nums</code> 中找出并返回总和为 <code>target</code> 的元素组合的个数。数组中的数字可以在一次排列中出现任意次，但是顺序不同的序列被视作不同的组合。</p>

<p>题目数据保证答案符合 32 位整数范围。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], target = 4
<strong>输出：</strong>7
<strong>解释：</strong>
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [9], target = 3
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
	<li><code>1 &lt;= target &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 377&nbsp;题相同：<a href="https://leetcode-cn.com/problems/combination-sum-iv/">https://leetcode-cn.com/problems/combination-sum-iv/</a></p>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[1,2,3]
4
[9]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {

    }
};
```

### Java

```java
class Solution {
    public int combinationSum4(int[] nums, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
```

### C

```c


int combinationSum4(int* nums, int numsSize, int target){

}
```

### C#

```csharp
public class Solution {
    public int CombinationSum4(int[] nums, int target) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {

};
```

### TypeScript

```typescript
function combinationSum4(nums: number[], target: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function combinationSum4($nums, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func combinationSum4(_ nums: [Int], _ target: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun combinationSum4(nums: IntArray, target: Int): Int {

    }
}
```

### Go

```golang
func combinationSum4(nums []int, target int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def combination_sum4(nums, target)

end
```

### Scala

```scala
object Solution {
    def combinationSum4(nums: Array[Int], target: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (combination-sum4 nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec combination_sum4(Nums :: [integer()], Target :: integer()) -> integer().
combination_sum4(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec combination_sum4(nums :: [integer], target :: integer) :: integer
  def combination_sum4(nums, target) do

  end
end
```

