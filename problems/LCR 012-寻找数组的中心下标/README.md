# LCR 012. 寻找数组的中心下标

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> ，请计算数组的 <strong>中心下标 </strong>。</p>

<p>数组<strong> 中心下标</strong><strong> </strong>是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。</p>

<p>如果中心下标位于数组最左端，那么左侧数之和视为 <code>0</code> ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。</p>

<p>如果数组有多个中心下标，应该返回 <strong>最靠近左边</strong> 的那一个。如果数组不存在中心下标，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,7,3,6,5,6]
<strong>输出：</strong>3
<strong>解释：</strong>
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1, 2, 3]
<strong>输出：</strong>-1
<strong>解释：</strong>
数组中不存在满足此条件的中心下标。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2, 1, -1]
<strong>输出：</strong>0
<strong>解释：</strong>
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 724&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/find-pivot-index/">https://leetcode-cn.com/problems/find-pivot-index/</a></p>


## 难度

Easy

## 标签

- 数组
- 前缀和

## 示例

```
[1,7,3,6,5,6]
[1,2,3]
[2,1,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int pivotIndex(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
```

### C

```c
int pivotIndex(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int PivotIndex(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    
};
```

### TypeScript

```typescript
function pivotIndex(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function pivotIndex($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pivotIndex(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pivotIndex(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int pivotIndex(List<int> nums) {
    
  }
}
```

### Go

```golang
func pivotIndex(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def pivot_index(nums)
    
end
```

### Scala

```scala
object Solution {
    def pivotIndex(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (pivot-index nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec pivot_index(Nums :: [integer()]) -> integer().
pivot_index(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pivot_index(nums :: [integer]) :: integer
  def pivot_index(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pivotIndex(nums: Array<Int64>): Int64 {

    }
}
```

