# 396. 旋转函数

## 题目描述

<p>给定一个长度为 <code>n</code> 的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>假设&nbsp;<code>arr<sub>k</sub></code>&nbsp;是数组&nbsp;<code>nums</code>&nbsp;顺时针旋转 <code>k</code> 个位置后的数组，我们定义&nbsp;<code>nums</code>&nbsp;的 <strong>旋转函数</strong>&nbsp;&nbsp;<code>F</code>&nbsp;为：</p>

<ul>
	<li><code>F(k) = 0 * arr<sub>k</sub>[0] + 1 * arr<sub>k</sub>[1] + ... + (n - 1) * arr<sub>k</sub>[n - 1]</code></li>
</ul>

<p>返回&nbsp;<em><code>F(0), F(1), ..., F(n-1)</code>中的最大值&nbsp;</em>。</p>

<p>生成的测试用例让答案符合&nbsp;<strong>32 位</strong> 整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [4,3,2,6]
<strong>输出:</strong> 26
<strong>解释:</strong>
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [100]
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划

## 示例

```
[4,3,2,6]
[100]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxRotateFunction(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        
```

### C

```c
int maxRotateFunction(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxRotateFunction(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxRotateFunction = function(nums) {
    
};
```

### TypeScript

```typescript
function maxRotateFunction(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxRotateFunction($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxRotateFunction(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxRotateFunction(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxRotateFunction(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxRotateFunction(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_rotate_function(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxRotateFunction(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_rotate_function(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-rotate-function nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_rotate_function(Nums :: [integer()]) -> integer().
max_rotate_function(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_rotate_function(nums :: [integer]) :: integer
  def max_rotate_function(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxRotateFunction(nums: Array<Int64>): Int64 {

    }
}
```

