# 2587. 重排数组以得到最大前缀分数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。你可以将 <code>nums</code> 中的元素按 <strong>任意顺序</strong> 重排（包括给定顺序）。</p>

<p>令 <code>prefix</code> 为一个数组，它包含了 <code>nums</code> 重新排列后的前缀和。换句话说，<code>prefix[i]</code> 是 <code>nums</code> 重新排列后下标从 <code>0</code> 到 <code>i</code> 的元素之和。<code>nums</code> 的 <strong>分数</strong> 是 <code>prefix</code> 数组中正整数的个数。</p>

<p>返回可以得到的最大分数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,-1,0,1,-3,3,-3]
<strong>输出：</strong>6
<strong>解释：</strong>数组重排为 nums = [2,3,1,-1,-3,0,-3] 。
prefix = [2,5,6,5,2,2,-1] ，分数为 6 。
可以证明 6 是能够得到的最大分数。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [-2,-3,0]
<strong>输出：</strong>0
<strong>解释：</strong>不管怎么重排数组得到的分数都是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 前缀和
- 排序

## 提示

1. The best order of the array is in decreasing order.
2. Sort the array in decreasing order and count the number of positive values in the prefix sum array.

## 示例

```
[2,-1,0,1,-3,3,-3]
[-2,-3,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxScore(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxScore(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
```

### C

```c
int maxScore(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxScore(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxScore = function(nums) {
    
};
```

### TypeScript

```typescript
function maxScore(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxScore($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxScore(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_score(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(Nums :: [integer()]) -> integer().
max_score(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(nums :: [integer]) :: integer
  def max_score(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(nums: Array<Int64>): Int64 {

    }
}
```

