# LCR 089. 打家劫舍

## 题目描述

<p>一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响小偷偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，<strong>如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警</strong>。</p>

<p>给定一个代表每个房屋存放金额的非负整数数组 <code>nums</code>&nbsp;，请计算<strong>&nbsp;不触动警报装置的情况下 </strong>，一夜之内能够偷窃到的最高金额。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums =<strong> </strong>[1,2,3,1]
<strong>输出：</strong>4
<strong>解释：</strong>偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
&nbsp;    偷窃到的最高金额 = 1 + 3 = 4 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums =<strong> </strong>[2,7,9,3,1]
<strong>输出：</strong>12
<strong>解释：</strong>偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
&nbsp;    偷窃到的最高金额 = 2 + 9 + 1 = 12 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 400</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 198&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/house-robber/">https://leetcode-cn.com/problems/house-robber/</a></p>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[1,2,3,1]
[2,7,9,3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {

    }
};
```

### Java

```java
class Solution {
    public int rob(int[] nums) {

    }
}
```

### Python

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def rob(self, nums: List[int]) -> int:
```

### C

```c


int rob(int* nums, int numsSize){

}
```

### C#

```csharp
public class Solution {
    public int Rob(int[] nums) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {

};
```

### TypeScript

```typescript
function rob(nums: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function rob($nums) {

    }
}
```

### Swift

```swift
class Solution {
    func rob(_ nums: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rob(nums: IntArray): Int {

    }
}
```

### Go

```golang
func rob(nums []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def rob(nums)

end
```

### Scala

```scala
object Solution {
    def rob(nums: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (rob nums)
  (-> (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec rob(Nums :: [integer()]) -> integer().
rob(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rob(nums :: [integer]) :: integer
  def rob(nums) do

  end
end
```

