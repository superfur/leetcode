# 1512. 好数对的数目

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。</p>

<p>如果一组数字 <code>(i,j)</code> 满足 <code>nums[i]</code> == <code>nums[j]</code> 且 <code>i</code> &lt; <code>j</code> ，就可以认为这是一组 <strong>好数对</strong> 。</p>

<p>返回好数对的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,1,1,3]
<strong>输出：</strong>4
<strong>解释：</strong>有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,1,1]
<strong>输出：</strong>6
<strong>解释：</strong>数组中的每组数字都是好数对</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 数学
- 计数

## 提示

1. Count how many times each number appears. If a number appears n times, then n * (n – 1) // 2 good pairs can be made with this number.

## 示例

```
[1,2,3,1,1,3]
[1,1,1,1]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int numIdenticalPairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
```

### C

```c
int numIdenticalPairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    
};
```

### TypeScript

```typescript
function numIdenticalPairs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function numIdenticalPairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numIdenticalPairs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numIdenticalPairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func numIdenticalPairs(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def num_identical_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def numIdenticalPairs(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_identical_pairs(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-identical-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_identical_pairs(Nums :: [integer()]) -> integer().
num_identical_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_identical_pairs(nums :: [integer]) :: integer
  def num_identical_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numIdenticalPairs(nums: Array<Int64>): Int64 {

    }
}
```

