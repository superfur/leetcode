# 1770. 执行乘法运算的最大分数

## 题目描述

<p>给你两个长度分别 <code>n</code> 和 <code>m</code> 的整数数组 <code>nums</code> 和 <code>multipliers</code><strong> </strong>，其中 <code>n &gt;= m</code> ，数组下标 <strong>从 1 开始</strong> 计数。</p>

<p>初始时，你的分数为 <code>0</code> 。你需要执行恰好 <code>m</code> 步操作。在第 <code>i</code> 步操作（<strong>从 1 开始</strong> 计数）中，需要：</p>

<ul>
	<li>选择数组 <code>nums</code> <strong>开头处或者末尾处</strong> 的整数 <code>x</code> 。</li>
	<li>你获得 <code>multipliers[i] * x</code> 分，并累加到你的分数中。</li>
	<li>将 <code>x</code> 从数组 <code>nums</code> 中移除。</li>
</ul>

<p>在执行<em> </em><code>m</code> 步操作后，返回 <strong>最大</strong> 分数<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3], multipliers = [3,2,1]
<strong>输出：</strong>14
<strong>解释：</strong>一种最优解决方案如下：
- 选择末尾处的整数 3 ，[1,2,<strong>3</strong>] ，得 3 * 3 = 9 分，累加到分数中。
- 选择末尾处的整数 2 ，[1,<strong>2</strong>] ，得 2 * 2 = 4 分，累加到分数中。
- 选择末尾处的整数 1 ，[<strong>1</strong>] ，得 1 * 1 = 1 分，累加到分数中。
总分数为 9 + 4 + 1 = 14 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
<strong>输出：</strong>102
<strong>解释：</strong>一种最优解决方案如下：
- 选择开头处的整数 -5 ，[<strong>-5</strong>,-3,-3,-2,7,1] ，得 -5 * -10 = 50 分，累加到分数中。
- 选择开头处的整数 -3 ，[<strong>-3</strong>,-3,-2,7,1] ，得 -3 * -5 = 15 分，累加到分数中。
- 选择开头处的整数 -3 ，[<strong>-3</strong>,-2,7,1] ，得 -3 * 3 = -9 分，累加到分数中。
- 选择末尾处的整数 1 ，[-2,7,<strong>1</strong>] ，得 1 * 4 = 4 分，累加到分数中。
- 选择末尾处的整数 7 ，[-2,<strong>7</strong>] ，得 7 * 6 = 42 分，累加到分数中。
总分数为 50 + 15 - 9 + 4 + 42 = 102 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == multipliers.length</code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>3</sup></code></li>
	<li><code>m &lt;= n &lt;= 10<sup>5</sup></code><code> </code></li>
	<li><code>-1000 &lt;= nums[i], multipliers[i] &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划

## 提示

1. At first glance, the solution seems to be greedy, but if you try to greedily take the largest value from the beginning or the end, this will not be optimal.
2. You should try all scenarios but this will be costly.
3. Memoizing the pre-visited states while trying all the possible scenarios will reduce the complexity, and hence dp is a perfect choice here.

## 示例

```
[1,2,3]
[3,2,1]
[-5,-3,-3,-2,7,1]
[-10,-5,3,4,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumScore(int[] nums, int[] multipliers) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumScore(self, nums, multipliers):
        """
        :type nums: List[int]
        :type multipliers: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
```

### C

```c
int maximumScore(int* nums, int numsSize, int* multipliers, int multipliersSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumScore(int[] nums, int[] multipliers) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} multipliers
 * @return {number}
 */
var maximumScore = function(nums, multipliers) {
    
};
```

### TypeScript

```typescript
function maximumScore(nums: number[], multipliers: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $multipliers
     * @return Integer
     */
    function maximumScore($nums, $multipliers) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumScore(_ nums: [Int], _ multipliers: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumScore(nums: IntArray, multipliers: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumScore(List<int> nums, List<int> multipliers) {
    
  }
}
```

### Go

```golang
func maximumScore(nums []int, multipliers []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} multipliers
# @return {Integer}
def maximum_score(nums, multipliers)
    
end
```

### Scala

```scala
object Solution {
    def maximumScore(nums: Array[Int], multipliers: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_score(nums: Vec<i32>, multipliers: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-score nums multipliers)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_score(Nums :: [integer()], Multipliers :: [integer()]) -> integer().
maximum_score(Nums, Multipliers) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_score(nums :: [integer], multipliers :: [integer]) :: integer
  def maximum_score(nums, multipliers) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumScore(nums: Array<Int64>, multipliers: Array<Int64>): Int64 {

    }
}
```

