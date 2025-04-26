# 1144. 递减元素使数组呈锯齿状

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，每次 <strong>操作</strong>&nbsp;会从中选择一个元素并 <strong>将该元素的值减少&nbsp;1</strong>。</p>

<p>如果符合下列情况之一，则数组&nbsp;<code>A</code>&nbsp;就是 <strong>锯齿数组</strong>：</p>

<ul>
	<li>每个偶数索引对应的元素都大于相邻的元素，即&nbsp;<code>A[0] &gt; A[1] &lt; A[2] &gt; A[3] &lt; A[4] &gt; ...</code></li>
	<li>或者，每个奇数索引对应的元素都大于相邻的元素，即&nbsp;<code>A[0] &lt; A[1] &gt; A[2] &lt; A[3] &gt; A[4] &lt; ...</code></li>
</ul>

<p>返回将数组&nbsp;<code>nums</code>&nbsp;转换为锯齿数组所需的最小操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>2
<strong>解释：</strong>我们可以把 2 递减到 0，或把 3 递减到 1。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [9,6,1,6,2]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Do each case (even indexed is greater, odd indexed is greater) separately. In say the even case, you should decrease each even-indexed element until it is lower than its immediate neighbors.

## 示例

```
[1,2,3]
[9,6,1,6,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int movesToMakeZigzag(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
```

### C

```c
int movesToMakeZigzag(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MovesToMakeZigzag(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var movesToMakeZigzag = function(nums) {
    
};
```

### TypeScript

```typescript
function movesToMakeZigzag(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function movesToMakeZigzag($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func movesToMakeZigzag(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun movesToMakeZigzag(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int movesToMakeZigzag(List<int> nums) {
    
  }
}
```

### Go

```golang
func movesToMakeZigzag(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def moves_to_make_zigzag(nums)
    
end
```

### Scala

```scala
object Solution {
    def movesToMakeZigzag(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn moves_to_make_zigzag(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (moves-to-make-zigzag nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec moves_to_make_zigzag(Nums :: [integer()]) -> integer().
moves_to_make_zigzag(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec moves_to_make_zigzag(nums :: [integer]) :: integer
  def moves_to_make_zigzag(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func movesToMakeZigzag(nums: Array<Int64>): Int64 {

    }
}
```

