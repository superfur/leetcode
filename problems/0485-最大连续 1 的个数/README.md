# 485. 最大连续 1 的个数

## 题目描述

<p>给定一个二进制数组 <code>nums</code> ， 计算其中最大连续 <code>1</code> 的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,0,1,1,1]
<strong>输出：</strong>3
<strong>解释：</strong>开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>nums = [1,0,1,1,0,1]
<b>输出：</b>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code>&nbsp;不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code>.</li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. You need to think about two things as far as any window is concerned. One is the starting point for the window. How do you detect that a new window of 1s has started? The next part is detecting the ending point for this window.

How do you detect the ending point for an existing window? If you figure these two things out, you will be able to detect the windows of consecutive ones. All that remains afterward is to find the longest such window and return the size.

## 示例

```
[1,1,0,1,1,1]
[1,0,1,1,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
```

### C

```c
int findMaxConsecutiveOnes(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    
};
```

### TypeScript

```typescript
function findMaxConsecutiveOnes(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMaxConsecutiveOnes($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMaxConsecutiveOnes(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMaxConsecutiveOnes(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMaxConsecutiveOnes(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMaxConsecutiveOnes(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_max_consecutive_ones(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMaxConsecutiveOnes(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-max-consecutive-ones nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_max_consecutive_ones(Nums :: [integer()]) -> integer().
find_max_consecutive_ones(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_max_consecutive_ones(nums :: [integer]) :: integer
  def find_max_consecutive_ones(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMaxConsecutiveOnes(nums: Array<Int64>): Int64 {

    }
}
```

