# 162. 寻找峰值

## 题目描述

<p>峰值元素是指其值严格大于左右相邻值的元素。</p>

<p>给你一个整数数组&nbsp;<code>nums</code>，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 <strong>任何一个峰值</strong> 所在位置即可。</p>

<p>你可以假设&nbsp;<code>nums[-1] = nums[n] = -∞</code> 。</p>

<p>你必须实现时间复杂度为 <code>O(log n)</code><em> </em>的算法来解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[1,2,3,1]</code>
<strong>输出：</strong>2
<strong>解释：</strong>3 是峰值元素，你的函数应该返回其索引 2。</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = <code>[</code>1,2,1,3,5,6,4]
<strong>输出：</strong>1 或 5 
<strong>解释：</strong>你的函数可以返回索引 1，其峰值元素为 2；
&nbsp;    或者返回索引 5， 其峰值元素为 6。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>对于所有有效的 <code>i</code> 都有 <code>nums[i] != nums[i + 1]</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 示例

```
[1,2,3,1]
[1,2,1,3,5,6,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findPeakElement(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
```

### C

```c
int findPeakElement(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindPeakElement(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findPeakElement = function(nums) {
    
};
```

### TypeScript

```typescript
function findPeakElement(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findPeakElement($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPeakElement(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findPeakElement(List<int> nums) {
    
  }
}
```

### Go

```golang
func findPeakElement(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_peak_element(nums)
    
end
```

### Scala

```scala
object Solution {
    def findPeakElement(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_peak_element(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-peak-element nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_peak_element(Nums :: [integer()]) -> integer().
find_peak_element(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_peak_element(nums :: [integer]) :: integer
  def find_peak_element(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPeakElement(nums: Array<Int64>): Int64 {

    }
}
```

