# 2855. 使数组成为递增数组的最少右移次数

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>nums</code>&nbsp;，数组中的元素为&nbsp;<strong>互不相同</strong>&nbsp;的正整数。请你返回让 <code>nums</code>&nbsp;成为递增数组的 <strong>最少右移</strong>&nbsp;次数，如果无法得到递增数组，返回 <code>-1</code>&nbsp;。</p>

<p>一次 <strong>右移</strong>&nbsp;指的是同时对所有下标进行操作，将下标为 <code>i</code>&nbsp;的元素移动到下标&nbsp;<code>(i + 1) % n</code>&nbsp;处。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,4,5,1,2]
<b>输出：</b>2
<b>解释：</b>
第一次右移后，nums = [2,3,4,5,1] 。
第二次右移后，nums = [1,2,3,4,5] 。
现在 nums 是递增数组了，所以答案为 2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,5]
<b>输出：</b>0
<b>解释：</b>nums 已经是递增数组了，所以答案为 0 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,4]
<b>输出：</b>-1
<b>解释：</b>无法将数组变为递增数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code>&nbsp;中的整数互不相同。</li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Find the pivot point around which the array is rotated.
2. Will the answer exist if there is more than one point where <code>nums[i] < nums[i-1]</code>?

## 示例

```
[3,4,5,1,2]
[1,3,5]
[2,1,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumRightShifts(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumRightShifts(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumRightShifts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumRightShifts(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumRightShifts(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumRightShifts = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumRightShifts(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumRightShifts($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumRightShifts(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumRightShifts(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumRightShifts(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumRightShifts(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_right_shifts(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumRightShifts(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_right_shifts(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-right-shifts nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_right_shifts(Nums :: [integer()]) -> integer().
minimum_right_shifts(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_right_shifts(nums :: [integer]) :: integer
  def minimum_right_shifts(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumRightShifts(nums: ArrayList<Int64>): Int64 {

    }
}
```

