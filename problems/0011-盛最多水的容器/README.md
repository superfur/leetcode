# 11. 盛最多水的容器

## 题目描述

<p>给定一个长度为 <code>n</code> 的整数数组&nbsp;<code>height</code>&nbsp;。有&nbsp;<code>n</code>&nbsp;条垂线，第 <code>i</code> 条线的两个端点是&nbsp;<code>(i, 0)</code>&nbsp;和&nbsp;<code>(i, height[i])</code>&nbsp;。</p>

<p>找出其中的两条线，使得它们与&nbsp;<code>x</code>&nbsp;轴共同构成的容器可以容纳最多的水。</p>

<p>返回容器可以储存的最大水量。</p>

<p><strong>说明：</strong>你不能倾斜容器。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" /></p>

<pre>
<strong>输入：</strong>[1,8,6,2,5,4,8,3,7]
<strong>输出：</strong>49 
<strong>解释：</strong>图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为&nbsp;49。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>height = [1,1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针

## 提示

1. If you simulate the problem, it will be O(n^2) which is not efficient.
2. Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.
3. How can you calculate the amount of water at each step?

## 示例

```
[1,8,6,2,5,4,8,3,7]
[1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxArea(int[] height) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
```

### C

```c
int maxArea(int* height, int heightSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxArea(int[] height) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
};
```

### TypeScript

```typescript
function maxArea(height: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $height
     * @return Integer
     */
    function maxArea($height) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxArea(_ height: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxArea(height: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxArea(List<int> height) {
    
  }
}
```

### Go

```golang
func maxArea(height []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} height
# @return {Integer}
def max_area(height)
    
end
```

### Scala

```scala
object Solution {
    def maxArea(height: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-area height)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_area(Height :: [integer()]) -> integer().
max_area(Height) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_area(height :: [integer]) :: integer
  def max_area(height) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxArea(height: Array<Int64>): Int64 {

    }
}
```

