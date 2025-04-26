# 2598. 执行操作后的最大 MEX

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 和一个整数 <code>value</code> 。</p>

<p>在一步操作中，你可以对 <code>nums</code> 中的任一元素加上或减去 <code>value</code> 。</p>

<ul>
	<li>例如，如果 <code>nums = [1,2,3]</code> 且 <code>value = 2</code> ，你可以选择 <code>nums[0]</code> 减去 <code>value</code> ，得到 <code>nums = [-1,2,3]</code> 。</li>
</ul>

<p>数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。</p>

<ul>
	<li>例如，<code>[-1,2,3]</code> 的 MEX 是 <code>0</code> ，而 <code>[1,0,3]</code> 的 MEX 是 <code>2</code> 。</li>
</ul>

<p>返回在执行上述操作 <strong>任意次</strong> 后，<code>nums</code><em> </em>的最大 MEX <em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,-10,7,13,6,8], value = 5
<strong>输出：</strong>4
<strong>解释：</strong>执行下述操作可以得到这一结果：
- nums[1] 加上 value 两次，nums = [1,<em><strong>0</strong></em>,7,13,6,8]
- nums[2] 减去 value 一次，nums = [1,0,<em><strong>2</strong></em>,13,6,8]
- nums[3] 减去 value 两次，nums = [1,0,2,<em><strong>3</strong></em>,6,8]
nums 的 MEX 是 4 。可以证明 4 是可以取到的最大 MEX 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,-10,7,13,6,8], value = 7
<strong>输出：</strong>2
<strong>解释：</strong>执行下述操作可以得到这一结果：
- nums[2] 减去 value 一次，nums = [1,-10,<em><strong>0</strong></em>,13,6,8]
nums 的 MEX 是 2 。可以证明 2 是可以取到的最大 MEX 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, value &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 数学

## 提示

1. Think about using modular arithmetic.
2. if x = nums[i] (mod value), then we can make nums[i] equal to x  after some number of operations
3. How does finding the frequency of (nums[i] mod value) help?

## 示例

```
[1,-10,7,13,6,8]
5
[1,-10,7,13,6,8]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findSmallestInteger(vector<int>& nums, int value) {
        
    }
};
```

### Java

```java
class Solution {
    public int findSmallestInteger(int[] nums, int value) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
```

### C

```c
int findSmallestInteger(int* nums, int numsSize, int value) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindSmallestInteger(int[] nums, int value) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} value
 * @return {number}
 */
var findSmallestInteger = function(nums, value) {
    
};
```

### TypeScript

```typescript
function findSmallestInteger(nums: number[], value: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $value
     * @return Integer
     */
    function findSmallestInteger($nums, $value) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSmallestInteger(_ nums: [Int], _ value: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSmallestInteger(nums: IntArray, value: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findSmallestInteger(List<int> nums, int value) {
    
  }
}
```

### Go

```golang
func findSmallestInteger(nums []int, value int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} value
# @return {Integer}
def find_smallest_integer(nums, value)
    
end
```

### Scala

```scala
object Solution {
    def findSmallestInteger(nums: Array[Int], value: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_smallest_integer(nums: Vec<i32>, value: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-smallest-integer nums value)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_smallest_integer(Nums :: [integer()], Value :: integer()) -> integer().
find_smallest_integer(Nums, Value) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_smallest_integer(nums :: [integer], value :: integer) :: integer
  def find_smallest_integer(nums, value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSmallestInteger(nums: Array<Int64>, value: Int64): Int64 {

    }
}
```

