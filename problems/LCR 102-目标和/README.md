# LCR 102. 目标和

## 题目描述

<p>给定一个正整数数组 <code>nums</code> 和一个整数 <code>target</code> 。</p>

<p>向数组中的每个整数前添加&nbsp;<code>&#39;+&#39;</code> 或 <code>&#39;-&#39;</code> ，然后串联起所有整数，可以构造一个 <strong>表达式</strong> ：</p>

<ul>
	<li>例如，<code>nums = [2, 1]</code> ，可以在 <code>2</code> 之前添加 <code>&#39;+&#39;</code> ，在 <code>1</code> 之前添加 <code>&#39;-&#39;</code> ，然后串联起来得到表达式 <code>&quot;+2-1&quot;</code> 。</li>
</ul>

<p>返回可以通过上述方法构造的、运算结果等于 <code>target</code> 的不同 <strong>表达式</strong> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1,1], target = 3
<strong>输出：</strong>5
<strong>解释：</strong>一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], target = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 20</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 1000</code></li>
	<li><code>-1000 &lt;= target &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 494&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/target-sum/">https://leetcode-cn.com/problems/target-sum/</a></p>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 回溯

## 示例

```
[1,1,1,1,1]
3
[1]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {

    }
};
```

### Java

```java
class Solution {
    public int findTargetSumWays(int[] nums, int target) {

    }
}
```

### Python

```python
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
```

### C

```c


int findTargetSumWays(int* nums, int numsSize, int target){

}
```

### C#

```csharp
public class Solution {
    public int FindTargetSumWays(int[] nums, int target) {

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
var findTargetSumWays = function(nums, target) {

};
```

### TypeScript

```typescript
function findTargetSumWays(nums: number[], target: number): number {

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
    function findTargetSumWays($nums, $target) {

    }
}
```

### Swift

```swift
class Solution {
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTargetSumWays(nums: IntArray, target: Int): Int {

    }
}
```

### Go

```golang
func findTargetSumWays(nums []int, target int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def find_target_sum_ways(nums, target)

end
```

### Scala

```scala
object Solution {
    def findTargetSumWays(nums: Array[Int], target: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_target_sum_ways(nums: Vec<i32>, target: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (find-target-sum-ways nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec find_target_sum_ways(Nums :: [integer()], Target :: integer()) -> integer().
find_target_sum_ways(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_target_sum_ways(nums :: [integer], target :: integer) :: integer
  def find_target_sum_ways(nums, target) do

  end
end
```

