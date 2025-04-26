# 805. 数组的均值分割

## 题目描述

<p>给定你一个整数数组<meta charset="UTF-8" />&nbsp;<code>nums</code></p>

<p>我们要将<meta charset="UTF-8" />&nbsp;<code>nums</code>&nbsp;数组中的每个元素移动到&nbsp;<code>A</code>&nbsp;数组 或者&nbsp;<code>B</code>&nbsp;数组中，使得&nbsp;<code>A</code>&nbsp;数组和<meta charset="UTF-8" />&nbsp;<code>B</code>&nbsp;数组不为空，并且<meta charset="UTF-8" />&nbsp;<code>average(A) == average(B)</code>&nbsp;。</p>

<p>如果可以完成则返回<code>true</code>&nbsp;， 否则返回 <code>false</code>&nbsp;&nbsp;。</p>

<p><strong>注意：</strong>对于数组<meta charset="UTF-8" />&nbsp;<code>arr</code>&nbsp;, <meta charset="UTF-8" />&nbsp;<code>average(arr)</code>&nbsp;是<meta charset="UTF-8" />&nbsp;<code>arr</code>&nbsp;的所有元素的和除以<meta charset="UTF-8" />&nbsp;<code>arr</code>&nbsp;长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [1,2,3,4,5,6,7,8]
<strong>输出:</strong> true
<strong>解释: </strong>我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [3,1]
<strong>输出:</strong> false
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 30</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 数学
- 动态规划
- 状态压缩

## 示例

```
[1,2,3,4,5,6,7,8]
[3,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool splitArraySameAverage(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean splitArraySameAverage(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        
```

### C

```c
bool splitArraySameAverage(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool SplitArraySameAverage(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var splitArraySameAverage = function(nums) {
    
};
```

### TypeScript

```typescript
function splitArraySameAverage(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function splitArraySameAverage($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func splitArraySameAverage(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitArraySameAverage(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool splitArraySameAverage(List<int> nums) {
    
  }
}
```

### Go

```golang
func splitArraySameAverage(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def split_array_same_average(nums)
    
end
```

### Scala

```scala
object Solution {
    def splitArraySameAverage(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_array_same_average(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (split-array-same-average nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec split_array_same_average(Nums :: [integer()]) -> boolean().
split_array_same_average(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec split_array_same_average(nums :: [integer]) :: boolean
  def split_array_same_average(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func splitArraySameAverage(nums: Array<Int64>): Bool {

    }
}
```

