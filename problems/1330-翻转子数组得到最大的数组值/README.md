# 1330. 翻转子数组得到最大的数组值

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 。「数组值」定义为所有满足&nbsp;<code>0 &lt;= i &lt; nums.length-1</code>&nbsp;的&nbsp;<code>|nums[i]-nums[i+1]|</code>&nbsp;的和。</p>

<p>你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作&nbsp;<strong>一次</strong> 。</p>

<p>请你找到可行的最大 <strong>数组值&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,1,5,4]
<strong>输出：</strong>10
<strong>解释：</strong>通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,9,24,2,1,10]
<strong>输出：</strong>68
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 3*10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li>答案保证在 32 位整数范围内。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 数学

## 提示

1. What's the score after reversing a sub-array [L, R] ?
2. It's the score without reversing it + abs(a[R] - a[L-1]) + abs(a[L] - a[R+1]) - abs(a[L] - a[L-1]) - abs(a[R] - a[R+1])
3. How to maximize that formula given that abs(x - y) = max(x - y, y - x) ?
4. This can be written as max(max(a[R] - a[L - 1], a[L - 1] - a[R]) + max(a[R + 1] - a[L], a[L] - a[R + 1]) - value(L) - value(R + 1)) over all L < R where value(i) = abs(a[i] - a[i-1])
5. This can be divided into 4 cases.

## 示例

```
[2,3,1,5,4]
[2,4,9,24,2,1,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxValueAfterReverse(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxValueAfterReverse(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        
```

### C

```c
int maxValueAfterReverse(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxValueAfterReverse(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxValueAfterReverse = function(nums) {
    
};
```

### TypeScript

```typescript
function maxValueAfterReverse(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxValueAfterReverse($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxValueAfterReverse(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxValueAfterReverse(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxValueAfterReverse(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxValueAfterReverse(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_value_after_reverse(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxValueAfterReverse(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_value_after_reverse(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-value-after-reverse nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_value_after_reverse(Nums :: [integer()]) -> integer().
max_value_after_reverse(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_value_after_reverse(nums :: [integer]) :: integer
  def max_value_after_reverse(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxValueAfterReverse(nums: Array<Int64>): Int64 {

    }
}
```

