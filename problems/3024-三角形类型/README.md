# 3024. 三角形类型

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>3</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;，需要用它们来构造三角形。</p>

<ul>
	<li>如果一个三角形的所有边长度相等，那么这个三角形称为&nbsp;<strong>equilateral</strong>&nbsp;。</li>
	<li>如果一个三角形恰好有两条边长度相等，那么这个三角形称为&nbsp;<strong>isosceles</strong>&nbsp;。</li>
	<li>如果一个三角形三条边的长度互不相同，那么这个三角形称为&nbsp;<strong>scalene</strong>&nbsp;。</li>
</ul>

<p>如果这个数组无法构成一个三角形，请你返回字符串&nbsp;<code>"none"</code>&nbsp;，否则返回一个字符串表示这个三角形的类型。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,3,3]
<b>输出：</b>"equilateral"
<b>解释：</b>由于三条边长度相等，所以可以构成一个等边三角形，返回 "equilateral" 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [3,4,5]
<b>输出：</b>"scalene"
<b>解释：</b>
nums[0] + nums[1] = 3 + 4 = 7 ，大于 nums[2] = 5 <span style="text-wrap: wrap;">。</span>
nums[0] + nums[2] = 3 + 5 = 8 ，大于 nums[1] = 4 。
nums[1] + nums[2] = 4 + 5 = 9 ，大于 nums[0] = 3 。
由于任意两边之和都大于第三边，所以可以构成一个三角形，因为三条边的长度互不相等，所以返回 "scalene"。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length == 3</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 排序

## 提示

1. The condition for a valid triangle is that for any two sides, the sum of their lengths must be greater than the third side.
2. Simply count the number of unique edge lengths after checking it’s a valid triangle.

## 示例

```
[3,3,3]
[3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string triangleType(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public String triangleType(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
```

### C

```c
char* triangleType(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string TriangleType(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {string}
 */
var triangleType = function(nums) {
    
};
```

### TypeScript

```typescript
function triangleType(nums: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return String
     */
    function triangleType($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func triangleType(_ nums: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun triangleType(nums: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String triangleType(List<int> nums) {
    
  }
}
```

### Go

```golang
func triangleType(nums []int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {String}
def triangle_type(nums)
    
end
```

### Scala

```scala
object Solution {
    def triangleType(nums: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn triangle_type(nums: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (triangle-type nums)
  (-> (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec triangle_type(Nums :: [integer()]) -> unicode:unicode_binary().
triangle_type(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec triangle_type(nums :: [integer]) :: String.t
  def triangle_type(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func triangleType(nums: Array<Int64>): String {

    }
}
```

