# 2552. 统计上升四元组

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，它包含&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;的所有数字，请你返回上升四元组的数目。</p>

<p>如果一个四元组&nbsp;<code>(i, j, k, l)</code>&nbsp;满足以下条件，我们称它是上升的：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; k &lt; l &lt; n</code>&nbsp;且</li>
	<li><code>nums[i] &lt; nums[k] &lt; nums[j] &lt; nums[l]</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,3,2,4,5]
<b>输出：</b>2
<b>解释：</b>
- 当 i = 0 ，j = 1 ，k = 2 且 l = 3 时，有 nums[i] &lt; nums[k] &lt; nums[j] &lt; nums[l] 。
- 当 i = 0 ，j = 1 ，k = 2 且 l = 4 时，有 nums[i] &lt; nums[k] &lt; nums[j] &lt; nums[l] 。
没有其他的四元组，所以我们返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>0
<b>解释：</b>只存在一个四元组 i = 0 ，j = 1 ，k = 2 ，l = 3 ，但是 nums[j] &lt; nums[k] ，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 4000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li><code>nums</code>&nbsp;中所有数字 <strong>互不相同</strong>&nbsp;，<code>nums</code>&nbsp;是一个排列。</li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 数组
- 动态规划
- 枚举
- 前缀和

## 提示

1. Can you loop over all possible (j, k) and find the answer?
2. We can pre-compute all possible (i, j) and (k, l) and store them in 2 matrices.
3. The answer will the sum of prefix[j][k] * suffix[k][j].

## 示例

```
[1,3,2,4,5]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long countQuadruplets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
```

### C

```c
long long countQuadruplets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountQuadruplets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    
};
```

### TypeScript

```typescript
function countQuadruplets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countQuadruplets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countQuadruplets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countQuadruplets(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countQuadruplets(List<int> nums) {
    
  }
}
```

### Go

```golang
func countQuadruplets(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_quadruplets(nums)
    
end
```

### Scala

```scala
object Solution {
    def countQuadruplets(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-quadruplets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_quadruplets(Nums :: [integer()]) -> integer().
count_quadruplets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_quadruplets(nums :: [integer]) :: integer
  def count_quadruplets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countQuadruplets(nums: Array<Int64>): Int64 {

    }
}
```

