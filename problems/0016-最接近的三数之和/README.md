# 16. 最接近的三数之和

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组&nbsp;<code>nums</code><em>&nbsp;</em>和 一个目标值&nbsp;<code>target</code>。请你从 <code>nums</code><em> </em>中选出三个整数，使它们的和与&nbsp;<code>target</code>&nbsp;最接近。</p>

<p>返回这三个数的和。</p>

<p>假定每组输入只存在恰好一个解。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,2,1,-4], target = 1
<strong>输出：</strong>2
<strong>解释：</strong>与 target 最接近的和是 2 (-1 + 2 + 1 = 2)。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,0,0], target = 1
<strong>输出：</strong>0
<strong>解释：</strong>与 target 最接近的和是 0（0 + 0 + 0 = 0）。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 排序

## 示例

```
[-1,2,1,-4]
1
[0,0,0]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int threeSumClosest(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int ThreeSumClosest(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
    
};
```

### TypeScript

```typescript
function threeSumClosest(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function threeSumClosest($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun threeSumClosest(nums: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int threeSumClosest(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func threeSumClosest(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def three_sum_closest(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def threeSumClosest(nums: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn three_sum_closest(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (three-sum-closest nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec three_sum_closest(Nums :: [integer()], Target :: integer()) -> integer().
three_sum_closest(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec three_sum_closest(nums :: [integer], target :: integer) :: integer
  def three_sum_closest(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func threeSumClosest(nums: Array<Int64>, target: Int64): Int64 {

    }
}
```

