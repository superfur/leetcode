# 2597. 美丽子集的数目

## 题目描述

<p>给你一个由正整数组成的数组 <code>nums</code> 和一个 <strong>正</strong> 整数 <code>k</code> 。</p>

<p>如果 <code>nums</code> 的子集中，任意两个整数的绝对差均不等于 <code>k</code> ，则认为该子数组是一个 <strong>美丽</strong> 子集。</p>

<p>返回数组 <code>nums</code> 中 <strong>非空</strong> 且 <strong>美丽</strong> 的子集数目。</p>

<p><code>nums</code> 的子集定义为：可以经由 <code>nums</code> 删除某些元素（也可能不删除）得到的一个数组。只有在删除元素时选择的索引不同的情况下，两个子集才会被视作是不同的子集。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,6], k = 2
<strong>输出：</strong>4
<strong>解释：</strong>数组 nums 中的美丽子集有：[2], [4], [6], [2, 6] 。
可以证明数组 [2,4,6] 中只存在 4 个美丽子集。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], k = 1
<strong>输出：</strong>1
<strong>解释：</strong>数组 nums 中的美丽数组有：[1] 。
可以证明数组 [1] 中只存在 1 个美丽子集。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 18</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 动态规划
- 回溯
- 组合数学
- 排序

## 提示

1. Sort the array nums and create another array cnt of size nums[i].
2. Use backtracking to generate all the beautiful subsets. If cnt[nums[i] - k] is positive, then it is impossible to add nums[i] in the subset, and we just move to the next index. Otherwise, it is also possible to add nums[i] in the subset, in this case, increase cnt[nums[i]], and move to the next index.
3. Bonus: Can you solve the problem in O(n log n)?

## 示例

```
[2,4,6]
2
[1]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int beautifulSubsets(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int beautifulSubsets(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int beautifulSubsets(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int BeautifulSubsets(int[] nums, int k) {
        
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
var beautifulSubsets = function(nums, k) {
    
};
```

### TypeScript

```typescript
function beautifulSubsets(nums: number[], k: number): number {
    
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
    function beautifulSubsets($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautifulSubsets(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulSubsets(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int beautifulSubsets(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func beautifulSubsets(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def beautiful_subsets(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def beautifulSubsets(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_subsets(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (beautiful-subsets nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec beautiful_subsets(Nums :: [integer()], K :: integer()) -> integer().
beautiful_subsets(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_subsets(nums :: [integer], k :: integer) :: integer
  def beautiful_subsets(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautifulSubsets(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

