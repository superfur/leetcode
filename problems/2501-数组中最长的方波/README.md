# 2501. 数组中最长的方波

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。如果 <code>nums</code> 的子序列满足下述条件，则认为该子序列是一个 <strong>方波</strong> ：</p>

<ul>
	<li>子序列的长度至少为 <code>2</code> ，并且</li>
	<li>将子序列从小到大排序 <strong>之后</strong> ，除第一个元素外，每个元素都是前一个元素的 <strong>平方</strong> 。</li>
</ul>

<p>返回<em> </em><code>nums</code><em> </em>中 <strong>最长方波</strong> 的长度，如果不存在 <strong>方波</strong><em> </em>则返回<em> </em><code>-1</code> 。</p>

<p><strong>子序列</strong> 也是一个数组，可以由另一个数组删除一些或不删除元素且不改变剩余元素的顺序得到。</p>

<p>&nbsp;</p>

<p><strong>示例 1 ：</strong></p>

<pre><strong>输入：</strong>nums = [4,3,6,16,8,2]
<strong>输出：</strong>3
<strong>解释：</strong>选出子序列 [4,16,2] 。排序后，得到 [2,4,16] 。
- 4 = 2 * 2.
- 16 = 4 * 4.
因此，[4,16,2] 是一个方波.
可以证明长度为 4 的子序列都不是方波。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre><strong>输入：</strong>nums = [2,3,5,6,7]
<strong>输出：</strong>-1
<strong>解释：</strong>nums 不存在方波，所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 二分查找
- 动态规划
- 排序

## 提示

1. With the constraints, the length of the longest square streak possible is 5.
2. Store the elements of nums in a set to quickly check if it exists.

## 示例

```
[4,3,6,16,8,2]
[2,3,5,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSquareStreak(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
```

### C

```c
int longestSquareStreak(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSquareStreak(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSquareStreak = function(nums) {
    
};
```

### TypeScript

```typescript
function longestSquareStreak(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSquareStreak($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSquareStreak(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSquareStreak(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSquareStreak(List<int> nums) {
    
  }
}
```

### Go

```golang
func longestSquareStreak(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def longest_square_streak(nums)
    
end
```

### Scala

```scala
object Solution {
    def longestSquareStreak(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_square_streak(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-square-streak nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_square_streak(Nums :: [integer()]) -> integer().
longest_square_streak(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_square_streak(nums :: [integer]) :: integer
  def longest_square_streak(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSquareStreak(nums: Array<Int64>): Int64 {

    }
}
```

