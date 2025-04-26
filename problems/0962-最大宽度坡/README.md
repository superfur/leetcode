# 962. 最大宽度坡

## 题目描述

<p>给定一个整数数组&nbsp;<code>A</code>，<em>坡</em>是元组&nbsp;<code>(i, j)</code>，其中&nbsp;&nbsp;<code>i &lt; j</code>&nbsp;且&nbsp;<code>A[i] &lt;= A[j]</code>。这样的坡的宽度为&nbsp;<code>j - i</code>。</p>

<p>找出&nbsp;<code>A</code>&nbsp;中的坡的最大宽度，如果不存在，返回 0 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[6,0,8,2,1,5]
<strong>输出：</strong>4
<strong>解释：</strong>
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[9,8,1,0,1,9,4,0,4,1]
<strong>输出：</strong>7
<strong>解释：</strong>
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 50000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 50000</code></li>
</ol>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 栈
- 数组
- 双指针
- 单调栈

## 示例

```
[6,0,8,2,1,5]
[9,8,1,0,1,9,4,0,4,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxWidthRamp(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxWidthRamp(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
```

### C

```c
int maxWidthRamp(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxWidthRamp(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxWidthRamp = function(nums) {
    
};
```

### TypeScript

```typescript
function maxWidthRamp(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxWidthRamp($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxWidthRamp(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxWidthRamp(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxWidthRamp(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxWidthRamp(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_width_ramp(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxWidthRamp(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_width_ramp(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-width-ramp nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_width_ramp(Nums :: [integer()]) -> integer().
max_width_ramp(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_width_ramp(nums :: [integer]) :: integer
  def max_width_ramp(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxWidthRamp(nums: Array<Int64>): Int64 {

    }
}
```

