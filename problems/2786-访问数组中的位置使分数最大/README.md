# 2786. 访问数组中的位置使分数最大

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个正整数&nbsp;<code>x</code>&nbsp;。</p>

<p>你 <strong>一开始</strong>&nbsp;在数组的位置 <code>0</code>&nbsp;处，你可以按照下述规则访问数组中的其他位置：</p>

<ul>
	<li>如果你当前在位置&nbsp;<code>i</code>&nbsp;，那么你可以移动到满足&nbsp;<code>i &lt; j</code>&nbsp;的&nbsp;<strong>任意</strong>&nbsp;位置&nbsp;<code>j</code>&nbsp;。</li>
	<li>对于你访问的位置 <code>i</code>&nbsp;，你可以获得分数&nbsp;<code>nums[i]</code>&nbsp;。</li>
	<li>如果你从位置 <code>i</code>&nbsp;移动到位置 <code>j</code>&nbsp;且&nbsp;<code>nums[i]</code> 和&nbsp;<code>nums[j]</code>&nbsp;的 <strong>奇偶性</strong>&nbsp;不同，那么你将失去分数&nbsp;<code>x</code>&nbsp;。</li>
</ul>

<p>请你返回你能得到的 <strong>最大</strong>&nbsp;得分之和。</p>

<p><strong>注意</strong>&nbsp;，你一开始的分数为&nbsp;<code>nums[0]</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,3,6,1,9,2], x = 5
<b>输出：</b>13
<b>解释：</b>我们可以按顺序访问数组中的位置：0 -&gt; 2 -&gt; 3 -&gt; 4 。
对应位置的值为 2 ，6 ，1 和 9 。因为 6 和 1 的奇偶性不同，所以下标从 2 -&gt; 3 让你失去 x = 5 分。
总得分为：2 + 6 + 1 + 9 - 5 = 13 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,4,6,8], x = 3
<b>输出：</b>20
<b>解释：</b>数组中的所有元素奇偶性都一样，所以我们可以将每个元素都访问一次，而且不会失去任何分数。
总得分为：2 + 4 + 6 + 8 = 20 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], x &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. How can we use dynamic programming to solve the problem?
2. Let dp[i] be the answer to the subarray nums[0…i]. What are the transitions of this dp?

## 示例

```
[2,3,6,1,9,2]
5
[2,4,6,8]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxScore(vector<int>& nums, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxScore(int[] nums, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxScore(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        
```

### C

```c
long long maxScore(int* nums, int numsSize, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxScore(int[] nums, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var maxScore = function(nums, x) {
    
};
```

### TypeScript

```typescript
function maxScore(nums: number[], x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @return Integer
     */
    function maxScore($nums, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxScore(_ nums: [Int], _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxScore(nums: IntArray, x: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxScore(List<int> nums, int x) {
    
  }
}
```

### Go

```golang
func maxScore(nums []int, x int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def max_score(nums, x)
    
end
```

### Scala

```scala
object Solution {
    def maxScore(nums: Array[Int], x: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(nums: Vec<i32>, x: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-score nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_score(Nums :: [integer()], X :: integer()) -> integer().
max_score(Nums, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_score(nums :: [integer], x :: integer) :: integer
  def max_score(nums, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxScore(nums: Array<Int64>, x: Int64): Int64 {

    }
}
```

