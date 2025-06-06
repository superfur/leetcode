# 1569. 将子数组重新排序得到同一个二叉搜索树的方案数

## 题目描述

<p>给你一个数组 <code>nums</code>&nbsp;表示 <code>1</code>&nbsp;到 <code>n</code>&nbsp;的一个排列。我们按照元素在 <code>nums</code>&nbsp;中的顺序依次插入一个初始为空的二叉搜索树（BST）。请你统计将 <code>nums</code>&nbsp;重新排序后，统计满足如下条件的方案数：重排后得到的二叉搜索树与 <code>nums</code>&nbsp;原本数字顺序得到的二叉搜索树相同。</p>

<p>比方说，给你&nbsp;<code>nums = [2,1,3]</code>，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组&nbsp;<code>[2,3,1]</code>&nbsp;也能得到相同的 BST，但&nbsp;<code>[3,2,1]</code>&nbsp;会得到一棵不同的&nbsp;BST 。</p>

<p>请你返回重排 <code>nums</code>&nbsp;后，与原数组 <code>nums</code> 得到相同二叉搜索树的方案数。</p>

<p>由于答案可能会很大，请将结果对<strong>&nbsp;</strong><code>10^9 + 7</code>&nbsp;取余数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/bb.png" style="height: 101px; width: 121px;" /></p>

<pre>
<strong>输入：</strong>nums = [2,1,3]
<strong>输出：</strong>1
<strong>解释：</strong>我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/ex1.png" style="height: 161px; width: 241px;" /></strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,5,1,2]
<strong>输出：</strong>5
<strong>解释：</strong>下面 5 个数组会得到相同的 BST：
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/ex4.png" style="height: 161px; width: 121px;" /></strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>0
<strong>解释：</strong>没有别的排列顺序能得到相同的 BST 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li><code>nums</code>&nbsp;中所有数 <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 树
- 并查集
- 二叉搜索树
- 记忆化搜索
- 数组
- 数学
- 分治
- 动态规划
- 二叉树
- 组合数学

## 提示

1. Use a divide and conquer strategy.
2. The first number will always be the root. Consider the numbers smaller and larger than the root separately. When merging the results together, how many ways can you order x elements in x+y positions?

## 示例

```
[2,1,3]
[3,4,5,1,2]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfWays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfWays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        
```

### C

```c
int numOfWays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfWays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numOfWays = function(nums) {
    
};
```

### TypeScript

```typescript
function numOfWays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numOfWays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfWays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfWays(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfWays(List<int> nums) {
    
  }
}
```

### Go

```golang
func numOfWays(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def num_of_ways(nums)
    
end
```

### Scala

```scala
object Solution {
    def numOfWays(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_ways(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-ways nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_ways(Nums :: [integer()]) -> integer().
num_of_ways(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_ways(nums :: [integer]) :: integer
  def num_of_ways(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfWays(nums: Array<Int64>): Int64 {

    }
}
```

