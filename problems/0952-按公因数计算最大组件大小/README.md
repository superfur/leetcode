# 952. 按公因数计算最大组件大小

## 题目描述

<p>给定一个由不同正整数的组成的非空数组&nbsp;<code>nums</code> ，考虑下面的图：</p>

<ul>
	<li>有&nbsp;<code>nums.length</code>&nbsp;个节点，按从&nbsp;<code>nums[0]</code>&nbsp;到&nbsp;<code>nums[nums.length - 1]</code>&nbsp;标记；</li>
	<li>只有当&nbsp;<code>nums[i]</code>&nbsp;和&nbsp;<code>nums[j]</code>&nbsp;共用一个大于 1 的公因数时，<code>nums[i]</code>&nbsp;和&nbsp;<code>nums[j]</code>之间才有一条边。</li>
</ul>

<p>返回 <em>图中最大连通组件的大小</em> 。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/12/01/ex1.png" style="height: 97px; width: 500px;" /></p>

<pre>
<strong>输入：</strong>nums = [4,6,15,35]
<strong>输出：</strong>4
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/12/01/ex2.png" style="height: 85px; width: 500px;" /></p>

<pre>
<strong>输入：</strong>nums = [20,50,9,63]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2018/12/01/ex3.png" style="height: 260px; width: 500px;" /></p>

<pre>
<strong>输入：</strong>nums = [2,3,6,7,4,12,21,39]
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums</code>&nbsp;中所有值都 <strong>不同</strong></li>
</ul>


## 难度

Hard

## 标签

- 并查集
- 数组
- 哈希表
- 数学
- 数论

## 示例

```
[4,6,15,35]
[20,50,9,63]
[2,3,6,7,4,12,21,39]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestComponentSize(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestComponentSize(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
```

### C

```c
int largestComponentSize(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestComponentSize(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var largestComponentSize = function(nums) {
    
};
```

### TypeScript

```typescript
function largestComponentSize(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function largestComponentSize($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestComponentSize(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestComponentSize(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestComponentSize(List<int> nums) {
    
  }
}
```

### Go

```golang
func largestComponentSize(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def largest_component_size(nums)
    
end
```

### Scala

```scala
object Solution {
    def largestComponentSize(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_component_size(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-component-size nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_component_size(Nums :: [integer()]) -> integer().
largest_component_size(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_component_size(nums :: [integer]) :: integer
  def largest_component_size(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestComponentSize(nums: Array<Int64>): Int64 {

    }
}
```

