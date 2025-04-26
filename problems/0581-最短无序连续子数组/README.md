# 581. 最短无序连续子数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，你需要找出一个 <strong>连续子数组</strong> ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。</p>

<p>请你找出符合题意的 <strong>最短</strong> 子数组，并输出它的长度。</p>

<p> </p>

<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,6,4,8,10,9,15]
<strong>输出：</strong>5
<strong>解释：</strong>你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>5</sup> <= nums[i] <= 10<sup>5</sup></code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你可以设计一个时间复杂度为 <code>O(n)</code> 的解决方案吗？</p>
</div>
</div>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 双指针
- 排序
- 单调栈

## 示例

```
[2,6,4,8,10,9,15]
[1,2,3,4]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
```

### C

```c
int findUnsortedSubarray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindUnsortedSubarray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findUnsortedSubarray = function(nums) {
    
};
```

### TypeScript

```typescript
function findUnsortedSubarray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findUnsortedSubarray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findUnsortedSubarray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findUnsortedSubarray(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findUnsortedSubarray(List<int> nums) {
    
  }
}
```

### Go

```golang
func findUnsortedSubarray(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_unsorted_subarray(nums)
    
end
```

### Scala

```scala
object Solution {
    def findUnsortedSubarray(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_unsorted_subarray(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-unsorted-subarray nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_unsorted_subarray(Nums :: [integer()]) -> integer().
find_unsorted_subarray(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_unsorted_subarray(nums :: [integer]) :: integer
  def find_unsorted_subarray(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findUnsortedSubarray(nums: Array<Int64>): Int64 {

    }
}
```

