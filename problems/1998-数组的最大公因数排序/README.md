# 1998. 数组的最大公因数排序

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，你可以在 <code>nums</code> 上执行下述操作 <strong>任意次</strong> ：</p>

<ul>
	<li>如果 <code>gcd(nums[i], nums[j]) &gt; 1</code> ，交换 <code>nums[i]</code> 和 <code>nums[j]</code> 的位置。其中 <code>gcd(nums[i], nums[j])</code> 是&nbsp;<code>nums[i]</code> 和 <code>nums[j]</code> 的最大公因数。</li>
</ul>

<p>如果能使用上述交换方式将 <code>nums</code> 按 <strong>非递减顺序</strong> 排列，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,21,3]
<strong>输出：</strong>true
<strong>解释：</strong>可以执行下述操作完成对 [7,21,3] 的排序：
- 交换 7 和 21 因为 gcd(7,21) = 7 。nums = [<u><strong>21</strong></u>,<u><strong>7</strong></u>,3]
- 交换 21 和 3 因为 gcd(21,3) = 3 。nums = [<u><strong>3</strong></u>,7,<u><strong>21</strong></u>]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,2,6,2]
<strong>输出：</strong>false
<strong>解释：</strong>无法完成排序，因为 5 不能与其他元素交换。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,5,9,3,15]
<strong>输出：</strong>true
<strong>解释：</strong>
可以执行下述操作完成对 [10,5,9,3,15] 的排序：
- 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [<u><strong>15</strong></u>,5,9,3,<u><strong>10</strong></u>]
- 交换 15 和 3 因为 gcd(15,3) = 3 。nums = [<u><strong>3</strong></u>,5,9,<u><strong>15</strong></u>,10]
- 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [3,5,9,<u><strong>10</strong></u>,<u><strong>15</strong></u>]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 并查集
- 数组
- 数学
- 数论
- 排序

## 提示

1. Can we build a graph with all the prime numbers and the original array?
2. We can use union-find to determine which indices are connected (i.e., which indices can be swapped).

## 示例

```
[7,21,3]
[5,2,6,2]
[10,5,9,3,15]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool gcdSort(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean gcdSort(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def gcdSort(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        
```

### C

```c
bool gcdSort(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool GcdSort(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var gcdSort = function(nums) {
    
};
```

### TypeScript

```typescript
function gcdSort(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function gcdSort($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func gcdSort(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun gcdSort(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool gcdSort(List<int> nums) {
    
  }
}
```

### Go

```golang
func gcdSort(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def gcd_sort(nums)
    
end
```

### Scala

```scala
object Solution {
    def gcdSort(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn gcd_sort(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (gcd-sort nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec gcd_sort(Nums :: [integer()]) -> boolean().
gcd_sort(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec gcd_sort(nums :: [integer]) :: boolean
  def gcd_sort(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func gcdSort(nums: Array<Int64>): Bool {

    }
}
```

