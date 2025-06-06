# 565. 数组嵌套

## 题目描述

<p>索引从<code>0</code>开始长度为<code>N</code>的数组<code>A</code>，包含<code>0</code>到<code>N - 1</code>的所有整数。找到最大的集合<code>S</code>并返回其大小，其中 <code>S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }</code>且遵守以下的规则。</p>

<p>假设选择索引为<code>i</code>的元素<code>A[i]</code>为<code>S</code>的第一个元素，<code>S</code>的下一个元素应该是<code>A[A[i]]</code>，之后是<code>A[A[A[i]]]...</code> 以此类推，不断添加直到<code>S</code>出现重复的元素。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> A = [5,4,0,3,1,6,2]
<strong>输出:</strong> 4
<strong>解释:</strong> 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt; nums.length</code></li>
	<li><code>A</code>中不含有重复的元素。</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 数组

## 示例

```
[5,4,0,3,1,6,2]
[0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int arrayNesting(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
```

### C

```c
int arrayNesting(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ArrayNesting(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var arrayNesting = function(nums) {
    
};
```

### TypeScript

```typescript
function arrayNesting(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function arrayNesting($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arrayNesting(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arrayNesting(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int arrayNesting(List<int> nums) {
    
  }
}
```

### Go

```golang
func arrayNesting(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def array_nesting(nums)
    
end
```

### Scala

```scala
object Solution {
    def arrayNesting(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn array_nesting(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (array-nesting nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec array_nesting(Nums :: [integer()]) -> integer().
array_nesting(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec array_nesting(nums :: [integer]) :: integer
  def array_nesting(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arrayNesting(nums: Array<Int64>): Int64 {

    }
}
```

