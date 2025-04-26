# 674. 最长连续递增序列

## 题目描述

<p>给定一个未经排序的整数数组，找到最长且<strong> 连续递增的子序列</strong>，并返回该序列的长度。</p>

<p><strong>连续递增的子序列</strong> 可以由两个下标 <code>l</code> 和 <code>r</code>（<code>l < r</code>）确定，如果对于每个 <code>l <= i < r</code>，都有 <code>nums[i] < nums[i + 1]</code> ，那么子序列 <code>[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]</code> 就是连续递增子序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,5,4,7]
<strong>输出：</strong>3
<strong>解释：</strong>最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,2,2]
<strong>输出：</strong>1
<strong>解释：</strong>最长连续递增序列是 [2], 长度为1。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 示例

```
[1,3,5,4,7]
[2,2,2,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
```

### C

```c
int findLengthOfLCIS(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLengthOfLCIS(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findLengthOfLCIS = function(nums) {
    
};
```

### TypeScript

```typescript
function findLengthOfLCIS(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findLengthOfLCIS($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLengthOfLCIS(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLengthOfLCIS(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLengthOfLCIS(List<int> nums) {
    
  }
}
```

### Go

```golang
func findLengthOfLCIS(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    
end
```

### Scala

```scala
object Solution {
    def findLengthOfLCIS(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_length_of_lcis(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-length-of-lcis nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_length_of_lcis(Nums :: [integer()]) -> integer().
find_length_of_lcis(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_length_of_lcis(nums :: [integer]) :: integer
  def find_length_of_lcis(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLengthOfLCIS(nums: Array<Int64>): Int64 {

    }
}
```

