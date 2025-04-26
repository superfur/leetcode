# 2808. 使循环数组所有元素相等的最少秒数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>每一秒，你可以对数组执行以下操作：</p>

<ul>
	<li>对于范围在&nbsp;<code>[0, n - 1]</code>&nbsp;内的每一个下标&nbsp;<code>i</code>&nbsp;，将&nbsp;<code>nums[i]</code> 替换成&nbsp;<code>nums[i]</code>&nbsp;，<code>nums[(i - 1 + n) % n]</code>&nbsp;或者&nbsp;<code>nums[(i + 1) % n]</code>&nbsp;三者之一。</li>
</ul>

<p><strong>注意</strong>，所有元素会被同时替换。</p>

<p>请你返回将数组 <code>nums</code>&nbsp;中所有元素变成相等元素所需要的 <strong>最少</strong>&nbsp;秒数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,2,1,2]
<b>输出：</b>1
<b>解释：</b>我们可以在 1 秒内将数组变成相等元素：
- 第 1 秒，将每个位置的元素分别变为 [nums[3],nums[1],nums[3],nums[3]] 。变化后，nums = [2,2,2,2] 。
1 秒是将数组变成相等元素所需要的最少秒数。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,1,3,3,2]
<b>输出：</b>2
<b>解释：</b>我们可以在 2 秒内将数组变成相等元素：
- 第 1 秒，将每个位置的元素分别变为 [nums[0],nums[2],nums[2],nums[2],nums[3]] 。变化后，nums = [2,3,3,3,3] 。
- 第 2 秒，将每个位置的元素分别变为 [nums[1],nums[1],nums[2],nums[3],nums[4]] 。变化后，nums = [3,3,3,3,3] 。
2 秒是将数组变成相等元素所需要的最少秒数。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [5,5,5,5]
<b>输出：</b>0
<b>解释：</b>不需要执行任何操作，因为一开始数组中的元素已经全部相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 提示

1. For every possible x - the final value of the array, calculate the number of seconds needed to make all elements equal to x.
2. Notice that if you take two consecutive occurrences (i, j) of x, then the number of operations to make segment [i + 1, j - 1] equal to x is floor((j - i) / 2)

## 示例

```
[1,2,1,2]
[2,1,3,3,2]
[5,5,5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSeconds(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSeconds(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumSeconds(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSeconds(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSeconds = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumSeconds(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumSeconds($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSeconds(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSeconds(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSeconds(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumSeconds(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_seconds(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumSeconds(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_seconds(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-seconds nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_seconds(Nums :: [integer()]) -> integer().
minimum_seconds(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_seconds(nums :: [integer]) :: integer
  def minimum_seconds(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSeconds(nums: ArrayList<Int64>): Int64 {

    }
}
```

