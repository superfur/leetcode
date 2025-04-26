# 3392. 统计符合条件长度为 3 的子数组数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，请你返回长度为 3 的 <span data-keyword="subarray-nonempty">子数组</span>，满足第一个数和第三个数的和恰好为第二个数的一半。</p>

<p><strong>子数组</strong>&nbsp;指的是一个数组中连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,1,4,1]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<p>只有子数组&nbsp;<code>[1,4,1]</code>&nbsp;包含 3 个元素且第一个和第三个数字之和是中间数字的一半。number.</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p><code>[1,1,1]</code>&nbsp;是唯一长度为 3 的子数组，但第一个数和第三个数的和不是第二个数的一半。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 100</code></li>
	<li><code><font face="monospace">-100 &lt;= nums[i] &lt;= 100</font></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. The constraints are small. Consider checking every subarray.

## 示例

```
[1,2,1,4,1]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSubarrays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
```

### C

```c
int countSubarrays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSubarrays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function countSubarrays(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubarrays(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubarrays(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubarrays(List<int> nums) {
    
  }
}
```

### Go

```golang
func countSubarrays(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def countSubarrays(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-subarrays nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_subarrays(Nums :: [integer()]) -> integer().
count_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_subarrays(nums :: [integer]) :: integer
  def count_subarrays(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubarrays(nums: Array<Int64>): Int64 {

    }
}
```

