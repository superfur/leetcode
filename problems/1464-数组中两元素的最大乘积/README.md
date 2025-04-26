# 1464. 数组中两元素的最大乘积

## 题目描述

<p>给你一个整数数组 <code>nums</code>，请你选择数组的两个不同下标 <code>i</code> 和 <code>j</code><em>，</em>使 <code>(nums[i]-1)*(nums[j]-1)</code> 取得最大值。</p>

<p>请你计算并返回该式的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,4,5,2]
<strong>输出：</strong>12 
<strong>解释：</strong>如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,5,4,5]
<strong>输出：</strong>16
<strong>解释：</strong>选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,7]
<strong>输出：</strong>12
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^3</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序
- 堆（优先队列）

## 提示

1. Use brute force: two loops to select i and j, then select the maximum value of (nums[i]-1)*(nums[j]-1).

## 示例

```
[3,4,5,2]
[1,5,4,5]
[3,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxProduct(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
```

### C

```c
int maxProduct(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxProduct(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    
};
```

### TypeScript

```typescript
function maxProduct(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxProduct($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxProduct(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxProduct(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxProduct(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_product(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxProduct(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_product(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-product nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_product(Nums :: [integer()]) -> integer().
max_product(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_product(nums :: [integer]) :: integer
  def max_product(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxProduct(nums: Array<Int64>): Int64 {

    }
}
```

