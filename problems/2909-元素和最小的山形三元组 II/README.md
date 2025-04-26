# 2909. 元素和最小的山形三元组 II

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。</p>

<p>如果下标三元组 <code>(i, j, k)</code> 满足下述全部条件，则认为它是一个 <strong>山形三元组</strong> ：</p>

<ul>
	<li><code>i &lt; j &lt; k</code></li>
	<li><code>nums[i] &lt; nums[j]</code> 且 <code>nums[k] &lt; nums[j]</code></li>
</ul>

<p>请你找出 <code>nums</code> 中 <strong>元素和最小</strong> 的山形三元组，并返回其 <strong>元素和</strong> 。如果不存在满足条件的三元组，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [8,6,1,5,3]
<strong>输出：</strong>9
<strong>解释：</strong>三元组 (2, 3, 4) 是一个元素和等于 9 的山形三元组，因为： 
- 2 &lt; 3 &lt; 4
- nums[2] &lt; nums[3] 且 nums[4] &lt; nums[3]
这个三元组的元素和等于 nums[2] + nums[3] + nums[4] = 9 。可以证明不存在元素和小于 9 的山形三元组。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,4,8,7,10,2]
<strong>输出：</strong>13
<strong>解释：</strong>三元组 (1, 3, 5) 是一个元素和等于 13 的山形三元组，因为： 
- 1 &lt; 3 &lt; 5 
- nums[1] &lt; nums[3] 且 nums[5] &lt; nums[3]
这个三元组的元素和等于 nums[1] + nums[3] + nums[5] = 13 。可以证明不存在元素和小于 13 的山形三元组。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [6,5,4,3,4,5]
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明 nums 中不存在山形三元组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 提示

1. If you fix index <code>j</code>, <code>i</code> will be the smallest integer to the left of <code>j</code>, and <code>k</code> the largest integer to the right of <code>j</code>.
2. To find <code>i</code> and <code>k</code>, preprocess the prefix minimum array <code>prefix_min[i] = min(nums[0], nums[1], ..., nums[i])</code>, and the suffix minimum array <code>suffix_min[i] = min(nums[i], nums[i + 1], ..., nums[i - 1])</code>.

## 示例

```
[8,6,1,5,3]
[5,4,8,7,10,2]
[6,5,4,3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSum(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSum(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumSum(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSum(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumSum = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumSum(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSum(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSum(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSum(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumSum(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumSum(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_sum(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-sum nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_sum(Nums :: [integer()]) -> integer().
minimum_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(nums :: [integer]) :: integer
  def minimum_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSum(nums: Array<Int64>): Int64 {

    }
}
```

