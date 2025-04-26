# 2016. 增量元素之间的最大差值

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，该数组的大小为 <code>n</code> ，请你计算 <code>nums[j] - nums[i]</code> 能求得的 <strong>最大差值 </strong>，其中 <code>0 &lt;= i &lt; j &lt; n</code> 且 <code>nums[i] &lt; nums[j]</code> 。</p>

<p>返回 <strong>最大差值</strong> 。如果不存在满足要求的 <code>i</code> 和 <code>j</code> ，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [7,<em><strong>1</strong></em>,<em><strong>5</strong></em>,4]
<strong>输出：</strong>4
<strong>解释：</strong>
最大差值出现在 i = 1 且 j = 2 时，nums[j] - nums[i] = 5 - 1 = 4 。
注意，尽管 i = 1 且 j = 0 时 ，nums[j] - nums[i] = 7 - 1 = 6 &gt; 4 ，但 i &gt; j 不满足题面要求，所以 6 不是有效的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [9,4,3,2]
<strong>输出：</strong>-1
<strong>解释：</strong>
不存在同时满足 i &lt; j 和 nums[i] &lt; nums[j] 这两个条件的 i, j 组合。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [<em><strong>1</strong></em>,5,2,<em><strong>10</strong></em>]
<strong>输出：</strong>9
<strong>解释：</strong>
最大差值出现在 i = 0 且 j = 3 时，nums[j] - nums[i] = 10 - 1 = 9 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Could you keep track of the minimum element visited while traversing?
2. We have a potential candidate for the answer if the prefix min is lesser than nums[i].

## 示例

```
[7,1,5,4]
[9,4,3,2]
[1,5,2,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumDifference(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumDifference(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumDifference(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumDifference(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumDifference($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumDifference(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumDifference(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumDifference(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumDifference(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_difference(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumDifference(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_difference(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_difference(Nums :: [integer()]) -> integer().
maximum_difference(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_difference(nums :: [integer]) :: integer
  def maximum_difference(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumDifference(nums: Array<Int64>): Int64 {

    }
}
```

