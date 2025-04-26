# 1509. 三次操作后最大值与最小值的最小差

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>每次操作你可以选择&nbsp;<code>nums</code>&nbsp;中的任意一个元素并将它改成 <strong>任意值</strong> 。</p>

<p>在&nbsp;<strong>执行最多三次移动后&nbsp;</strong>，返回&nbsp;<code>nums</code>&nbsp;中最大值与最小值的最小差值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,3,2,4]
<strong>输出：</strong>0
<strong>解释：</strong>我们最多可以走 3 步。
第一步，将 2 变为 3 。 nums 变成 [5,3,3,4] 。
第二步，将 4 改为 3 。 nums 变成 [5,3,3,3] 。
第三步，将 5 改为 3 。 nums 变成 [3,3,3,3] 。
执行 3 次移动后，最小值和最大值之间的差值为 3 - 3 = 0 。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,0,10,14]
<strong>输出：</strong>1
<strong>解释：</strong>我们最多可以走 3 步。
第一步，将 5 改为 0 。 nums变成 [1,0,0,10,14] 。
第二步，将 10 改为 0 。 nums变成 [1,0,0,0,14] 。
第三步，将 14 改为 1 。 nums变成 [1,0,0,0,1] 。
执行 3 步后，最小值和最大值之间的差值为 1 - 0 = 1 。
可以看出，没有办法可以在 3 步内使差值变为0。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,100,20]
<strong>输出：</strong>0
<strong>解释：</strong>我们最多可以走 3 步。
第一步，将 100 改为 7 。 nums 变成 [3,7,20] 。
第二步，将 20 改为 7 。 nums 变成 [3,7,7] 。
第三步，将 3 改为 7 。 nums 变成 [7,7,7] 。
执行 3 步后，最小值和最大值之间的差值是 7 - 7 = 0。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. The minimum difference possible is obtained by removing three elements between the three smallest and three largest values in the array.

## 示例

```
[5,3,2,4]
[1,5,0,10,14]
[3,100,20]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDifference(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDifference(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
```

### C

```c
int minDifference(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDifference(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minDifference = function(nums) {
    
};
```

### TypeScript

```typescript
function minDifference(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minDifference($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDifference(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDifference(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDifference(List<int> nums) {
    
  }
}
```

### Go

```golang
func minDifference(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_difference(nums)
    
end
```

### Scala

```scala
object Solution {
    def minDifference(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_difference(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-difference nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_difference(Nums :: [integer()]) -> integer().
min_difference(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_difference(nums :: [integer]) :: integer
  def min_difference(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDifference(nums: Array<Int64>): Int64 {

    }
}
```

