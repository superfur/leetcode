# 1799. N 次操作后的最大分数和

## 题目描述

<p>给你 <code>nums</code> ，它是一个大小为 <code>2 * n</code> 的正整数数组。你必须对这个数组执行 <code>n</code> 次操作。</p>

<p>在第 <code>i</code> 次操作时（操作编号从 <strong>1</strong> 开始），你需要：</p>

<ul>
	<li>选择两个元素 <code>x</code> 和 <code>y</code> 。</li>
	<li>获得分数 <code>i * gcd(x, y)</code> 。</li>
	<li>将 <code>x</code> 和 <code>y</code> 从 <code>nums</code> 中删除。</li>
</ul>

<p>请你返回 <code>n</code> 次操作后你能获得的分数和最大为多少。</p>

<p>函数 <code>gcd(x, y)</code> 是 <code>x</code> 和 <code>y</code> 的最大公约数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,2]
<b>输出：</b>1
<b>解释：</b>最优操作是：
(1 * gcd(1, 2)) = 1
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [3,4,6,8]
<b>输出：</b>11
<b>解释：</b>最优操作是：
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,4,5,6]
<b>输出：</b>14
<b>解释：</b>最优操作是：
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 7</code></li>
	<li><code>nums.length == 2 * n</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 数学
- 动态规划
- 回溯
- 状态压缩
- 数论

## 提示

1. Find every way to split the array until n groups of 2. Brute force recursion is acceptable.
2. Calculate the gcd of every pair and greedily multiply the largest gcds.

## 示例

```
[1,2]
[3,4,6,8]
[1,2,3,4,5,6]
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

