# 697. 数组的度

## 题目描述

<p>给定一个非空且只包含非负数的整数数组&nbsp;<code>nums</code>，数组的 <strong>度</strong> 的定义是指数组里任一元素出现频数的最大值。</p>

<p>你的任务是在 <code>nums</code> 中找到与&nbsp;<code>nums</code>&nbsp;拥有相同大小的度的最短连续子数组，返回其长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,3,1]
<strong>输出：</strong>2
<strong>解释：</strong>
输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
连续子数组里面拥有相同度的有如下所示：
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,3,1,4,2]
<strong>输出：</strong>6
<strong>解释：</strong>
数组的度是 3 ，因为元素 2 重复出现 3 次。
所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length</code>&nbsp;在 <code>1</code> 到 <code>50,000</code> 范围内。</li>
	<li><code>nums[i]</code>&nbsp;是一个在 <code>0</code> 到 <code>49,999</code> 范围内的整数。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Say 5 is the only element that occurs the most number of times - for example, nums = [1, 5, 2, 3, 5, 4, 5, 6].  What is the answer?

## 示例

```
[1,2,2,3,1]
[1,2,2,3,1,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findShortestSubArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
```

### C

```c
int findShortestSubArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindShortestSubArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findShortestSubArray = function(nums) {
    
};
```

### TypeScript

```typescript
function findShortestSubArray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findShortestSubArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findShortestSubArray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findShortestSubArray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findShortestSubArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func findShortestSubArray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_shortest_sub_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def findShortestSubArray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_shortest_sub_array(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-shortest-sub-array nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_shortest_sub_array(Nums :: [integer()]) -> integer().
find_shortest_sub_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_shortest_sub_array(nums :: [integer]) :: integer
  def find_shortest_sub_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findShortestSubArray(nums: Array<Int64>): Int64 {

    }
}
```

