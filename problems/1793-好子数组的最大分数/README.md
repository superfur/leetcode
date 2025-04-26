# 1793. 好子数组的最大分数

## 题目描述

<p>给你一个整数数组 <code>nums</code> <strong>（下标从 0 开始）</strong>和一个整数 <code>k</code> 。</p>

<p>一个子数组 <code>(i, j)</code> 的 <strong>分数</strong> 定义为 <code>min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1)</code> 。一个 <strong>好</strong> 子数组的两个端点下标需要满足 <code>i &lt;= k &lt;= j</code> 。</p>

<p>请你返回 <strong>好</strong> 子数组的最大可能 <strong>分数</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,4,3,7,4,5], k = 3
<b>输出：</b>15
<b>解释：</b>最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [5,5,4,5,4,1,1,1], k = 0
<b>输出：</b>20
<b>解释：</b>最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt; nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 双指针
- 二分查找
- 单调栈

## 提示

1. Try thinking about the prefix before index k and the suffix after index k as two separate arrays.
2. Using two pointers or binary search, we can find the maximum prefix of each array where the numbers are less than or equal to a certain value

## 示例

```
[1,4,3,7,4,5]
3
[5,5,4,5,4,1,1,1]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumScore(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumScore(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumScore(int[] nums, int k) {
        
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
var maximumScore = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumScore(nums: number[], k: number): number {
    
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
    function maximumScore($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumScore(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumScore(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumScore(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-score nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_score(Nums :: [integer()], K :: integer()) -> integer().
maximum_score(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_score(nums :: [integer], k :: integer) :: integer
  def maximum_score(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumScore(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

