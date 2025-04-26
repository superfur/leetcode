# 3334. 数组的最大因子得分

## 题目描述

<p>给你一个整数数组 <code>nums</code>。</p>

<p><strong>因子得分 </strong>定义为数组所有元素的最小公倍数（LCM）与最大公约数（GCD）的<strong> 乘积</strong>。</p>

<p>在 <strong>最多</strong> 移除一个元素的情况下，返回 <code>nums</code> 的<strong> 最大因子得分</strong>。</p>

<p><strong>注意</strong>，单个数字的 <span data-keyword="lcm-function">LCM</span> 和 <span data-keyword="gcd-function">GCD</span> 都是其本身，而<strong> </strong><strong>空数组</strong> 的因子得分为 0。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,4,8,16]</span></p>

<p><strong>输出：</strong> <span class="example-io">64</span></p>

<p><strong>解释：</strong></p>

<p>移除数字 2 后，剩余元素的 GCD 为 4，LCM 为 16，因此最大因子得分为 <code>4 * 16 = 64</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">60</span></p>

<p><strong>解释：</strong></p>

<p>无需移除任何元素即可获得最大因子得分 60。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3]</span></p>

<p><strong>输出：</strong> 9</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 30</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 数论

## 提示

1. Use brute force approach with two loops.
2. Optimize using prefix and suffix arrays.

## 示例

```
[2,4,8,16]
[1,2,3,4,5]
[3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxScore(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxScore(int[] nums) {
        
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
long long maxScore(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxScore(int[] nums) {
        
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
    fun maxScore(nums: IntArray): Long {
        
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
func maxScore(nums []int) int64 {
    
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
    def maxScore(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_score(nums: Vec<i32>) -> i64 {
        
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

