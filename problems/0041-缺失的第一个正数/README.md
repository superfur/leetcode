# 41. 缺失的第一个正数

## 题目描述

<p>给你一个未排序的整数数组 <code>nums</code> ，请你找出其中没有出现的最小的正整数。</p>
请你实现时间复杂度为 <code>O(n)</code> 并且只使用常数级别额外空间的解决方案。

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,0]
<strong>输出：</strong>3
<strong>解释：</strong>范围 [1,2] 中的数字都在数组中。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,-1,1]
<strong>输出：</strong>2
<strong>解释：</strong>1 在数组中，但 2 没有。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,8,9,11,12]
<strong>输出：</strong>1
<strong>解释：</strong>最小的正数 1 没有出现。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表

## 提示

1. Think about how you would solve the problem in non-constant space.  Can you apply that logic to the existing space?
2. We don't care about duplicates or non-positive integers
3. Remember that O(2n) = O(n)

## 示例

```
[1,2,0]
[3,4,-1,1]
[7,8,9,11,12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int firstMissingPositive(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
```

### C

```c
int firstMissingPositive(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FirstMissingPositive(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
    
};
```

### TypeScript

```typescript
function firstMissingPositive(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function firstMissingPositive($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func firstMissingPositive(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun firstMissingPositive(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int firstMissingPositive(List<int> nums) {
    
  }
}
```

### Go

```golang
func firstMissingPositive(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
    
end
```

### Scala

```scala
object Solution {
    def firstMissingPositive(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (first-missing-positive nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec first_missing_positive(Nums :: [integer()]) -> integer().
first_missing_positive(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec first_missing_positive(nums :: [integer]) :: integer
  def first_missing_positive(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func firstMissingPositive(nums: Array<Int64>): Int64 {

    }
}
```

