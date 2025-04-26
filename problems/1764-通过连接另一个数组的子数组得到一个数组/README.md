# 1764. 通过连接另一个数组的子数组得到一个数组

## 题目描述

<p>给你一个长度为 <code>n</code> 的二维整数数组 <code>groups</code> ，同时给你一个整数数组 <code>nums</code> 。</p>

<p>你是否可以从 <code>nums</code> 中选出 <code>n</code> 个 <strong>不相交</strong> 的子数组，使得第 <code>i</code> 个子数组与 <code>groups[i]</code> （下标从 <strong>0</strong> 开始）完全相同，且如果 <code>i > 0</code> ，那么第 <code>(i-1)</code> 个子数组在 <code>nums</code> 中出现的位置在第 <code>i</code> 个子数组前面。（也就是说，这些子数组在 <code>nums</code> 中出现的顺序需要与 <code>groups</code> 顺序相同）</p>

<p>如果你可以找出这样的 <code>n</code> 个子数组，请你返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>如果不存在下标为 <code>k</code> 的元素 <code>nums[k]</code> 属于不止一个子数组，就称这些子数组是 <strong>不相交</strong> 的。子数组指的是原数组中连续元素组成的一个序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
<b>输出：</b>true
<b>解释：</b>你可以分别在 nums 中选出第 0 个子数组 [1,-1,0,<strong>1,</strong><strong>-1,</strong><strong>-1</strong>,3,-2,0] 和第 1 个子数组 [1,-1,0,1,-1,-1,<strong>3,</strong><strong>-2,0</strong>] 。
这两个子数组是不相交的，因为它们没有任何共同的元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
<b>输出：</b>false
<strong>解释：</strong>选择子数组 [<strong>1,2,3,4</strong>,10,-2] 和 [1,2,3,4,<strong>10,-2</strong>] 是不正确的，因为它们出现的顺序与 groups 中顺序不同。
[10,-2] 必须出现在 [1,2,3,4] 之前。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
<b>输出：</b>false
<strong>解释：</strong>选择子数组 [7,7,<strong>1,2,3</strong>,4,7,7] 和 [7,7,1,2,<strong>3,4</strong>,7,7] 是不正确的，因为它们不是不相交子数组。
它们有一个共同的元素 nums[4] （下标从 0 开始）。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>groups.length == n</code></li>
	<li><code>1 <= n <= 10<sup>3</sup></code></li>
	<li><code>1 <= groups[i].length, sum(groups[i].length) <= 10<sup><span style="">3</span></sup></code></li>
	<li><code>1 <= nums.length <= 10<sup>3</sup></code></li>
	<li><code>-10<sup>7</sup> <= groups[i][j], nums[k] <= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 字符串匹配

## 提示

1. When we use a subarray, the room for the next subarrays will be the suffix after the used subarray.
2. If we can match a group with multiple subarrays, we should choose the first one, as this will just leave the largest room for the next subarrays.

## 示例

```
[[1,-1,-1],[3,-2,0]]
[1,-1,0,1,-1,-1,3,-2,0]
[[10,-2],[1,2,3,4]]
[1,2,3,4,10,-2]
[[1,2,3],[3,4]]
[7,7,1,2,3,4,7,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canChoose(vector<vector<int>>& groups, vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canChoose(int[][] groups, int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        
```

### C

```c
bool canChoose(int** groups, int groupsSize, int* groupsColSize, int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanChoose(int[][] groups, int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} groups
 * @param {number[]} nums
 * @return {boolean}
 */
var canChoose = function(groups, nums) {
    
};
```

### TypeScript

```typescript
function canChoose(groups: number[][], nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $groups
     * @param Integer[] $nums
     * @return Boolean
     */
    function canChoose($groups, $nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canChoose(_ groups: [[Int]], _ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canChoose(groups: Array<IntArray>, nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canChoose(List<List<int>> groups, List<int> nums) {
    
  }
}
```

### Go

```golang
func canChoose(groups [][]int, nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} groups
# @param {Integer[]} nums
# @return {Boolean}
def can_choose(groups, nums)
    
end
```

### Scala

```scala
object Solution {
    def canChoose(groups: Array[Array[Int]], nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_choose(groups: Vec<Vec<i32>>, nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-choose groups nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_choose(Groups :: [[integer()]], Nums :: [integer()]) -> boolean().
can_choose(Groups, Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_choose(groups :: [[integer]], nums :: [integer]) :: boolean
  def can_choose(groups, nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canChoose(groups: Array<Array<Int64>>, nums: Array<Int64>): Bool {

    }
}
```

