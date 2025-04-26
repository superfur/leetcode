# 1911. 最大交替子序列和

## 题目描述

<p>一个下标从 <strong>0</strong> 开始的数组的 <strong>交替和</strong> 定义为 <strong>偶数</strong> 下标处元素之 <strong>和</strong> 减去 <strong>奇数</strong> 下标处元素之 <strong>和</strong> 。</p>

<ul>
	<li>比方说，数组 <code>[4,2,5,3]</code> 的交替和为 <code>(4 + 5) - (2 + 3) = 4</code> 。</li>
</ul>

<p>给你一个数组 <code>nums</code> ，请你返回 <code>nums</code> 中任意子序列的 <strong>最大交替和</strong> （子序列的下标 <strong>重新</strong> 从 0 开始编号）。</p>

<ul>
</ul>

<p>一个数组的 <strong>子序列</strong> 是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说，<code>[2,7,4]</code> 是 <code>[4,<strong>2</strong>,3,<strong>7</strong>,2,1,<strong>4</strong>]</code> 的一个子序列（加粗元素），但是 <code>[2,4,2]</code> 不是。</p>

<p> </p>

<p><b>示例 1：</b></p>

<pre><b>输入：</b>nums = [<strong>4</strong>,<strong>2</strong>,<strong>5</strong>,3]
<b>输出：</b>7
<b>解释：</b>最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [5,6,7,<strong>8</strong>]
<b>输出：</b>8
<b>解释：</b>最优子序列为 [8] ，交替和为 8 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [<strong>6</strong>,2,<strong>1</strong>,2,4,<strong>5</strong>]
<b>输出：</b>10
<b>解释：</b>最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Is only tracking a single sum enough to solve the problem?
2. How does tracking an odd sum and an even sum reduce the number of states?

## 示例

```
[4,2,5,3]
[5,6,7,8]
[6,2,1,2,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxAlternatingSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
```

### C

```c
long long maxAlternatingSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxAlternatingSum = function(nums) {
    
};
```

### TypeScript

```typescript
function maxAlternatingSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxAlternatingSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAlternatingSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAlternatingSum(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxAlternatingSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxAlternatingSum(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_alternating_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxAlternatingSum(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_alternating_sum(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-alternating-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_alternating_sum(Nums :: [integer()]) -> integer().
max_alternating_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_alternating_sum(nums :: [integer]) :: integer
  def max_alternating_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAlternatingSum(nums: Array<Int64>): Int64 {

    }
}
```

