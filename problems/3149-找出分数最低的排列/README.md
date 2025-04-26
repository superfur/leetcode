# 3149. 找出分数最低的排列

## 题目描述

<p>给你一个数组 <code>nums</code> ，它是 <code>[0, 1, 2, ..., n - 1]</code> 的一个<span data-keyword="permutation">排列</span> 。对于任意一个 <code>[0, 1, 2, ..., n - 1]</code> 的排列 <code>perm</code> ，其 <strong>分数 </strong>定义为：</p>

<p><code>score(perm) = |perm[0] - nums[perm[1]]| + |perm[1] - nums[perm[2]]| + ... + |perm[n - 1] - nums[perm[0]]|</code></p>

<p>返回具有<strong> 最低</strong> 分数的排列 <code>perm</code> 。如果存在多个满足题意且分数相等的排列，则返回其中<span data-keyword="lexicographically-smaller-array">字典序最小</span>的一个。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,0,2]</span></p>

<p><strong>输出：</strong><span class="example-io">[0,1,2]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/04/example0gif.gif" style="width: 235px; height: 235px;" /></strong></p>

<p>字典序最小且分数最低的排列是 <code>[0,1,2]</code>。这个排列的分数是 <code>|0 - 0| + |1 - 2| + |2 - 1| = 2</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [0,2,1]</span></p>

<p><strong>输出：</strong><span class="example-io">[0,2,1]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/04/example1gif.gif" style="width: 235px; height: 235px;" /></strong></p>

<p>字典序最小且分数最低的排列是 <code>[0,2,1]</code>。这个排列的分数是 <code>|0 - 1| + |2 - 2| + |1 - 0| = 2</code> 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 14</code></li>
	<li><code>nums</code> 是 <code>[0, 1, 2, ..., n - 1]</code> 的一个排列。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 提示

1. The score function is cyclic, so we can always set <code>perm[0] = 0</code> for the smallest lexical order.
2. It’s similar to the Traveling Salesman Problem. Use Dynamic Programming.
3. Use a bitmask to track which elements have been assigned to <code>perm</code>.

## 示例

```
[1,0,2]
[0,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findPermutation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findPermutation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPermutation(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindPermutation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findPermutation = function(nums) {
    
};
```

### TypeScript

```typescript
function findPermutation(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function findPermutation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPermutation(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPermutation(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findPermutation(List<int> nums) {
    
  }
}
```

### Go

```golang
func findPermutation(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def find_permutation(nums)
    
end
```

### Scala

```scala
object Solution {
    def findPermutation(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_permutation(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-permutation nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_permutation(Nums :: [integer()]) -> [integer()].
find_permutation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_permutation(nums :: [integer]) :: [integer]
  def find_permutation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPermutation(nums: Array<Int64>): Array<Int64> {

    }
}
```

