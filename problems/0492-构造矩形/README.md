# 492. 构造矩形

## 题目描述

<p>作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：</p>

<ol>
	<li>你设计的矩形页面必须等于给定的目标面积。</li>
	<li>宽度 <code>W</code>&nbsp;不应大于长度 <code>L</code> ，换言之，要求 <code>L &gt;= W </code>。</li>
	<li>长度 <code>L</code> 和宽度 <code>W</code>&nbsp;之间的差距应当尽可能小。</li>
</ol>

<p>返回一个&nbsp;<em>数组</em>&nbsp;<code>[L, W]</code>，其中 <em><code>L</code> 和 <code>W</code> 是你按照顺序设计的网页的长度和宽度</em>。<br />
&nbsp;</p>

<p><strong>示例1：</strong></p>

<pre>
<strong>输入:</strong> 4
<strong>输出:</strong> [2, 2]
<strong>解释:</strong> 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> area = 37
<strong>输出:</strong> [37,1]
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> area = 122122
<strong>输出:</strong> [427,286]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= area &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. The W is always less than or equal to the square root of the area, so we start searching at sqrt(area) till we find the result.

## 示例

```
4
37
122122
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> constructRectangle(int area) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] constructRectangle(int area) {
        
    }
}
```

### Python

```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructRectangle(int area, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ConstructRectangle(int area) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
    
};
```

### TypeScript

```typescript
function constructRectangle(area: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $area
     * @return Integer[]
     */
    function constructRectangle($area) {
        
    }
}
```

### Swift

```swift
class Solution {
    func constructRectangle(_ area: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun constructRectangle(area: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> constructRectangle(int area) {
    
  }
}
```

### Go

```golang
func constructRectangle(area int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} area
# @return {Integer[]}
def construct_rectangle(area)
    
end
```

### Scala

```scala
object Solution {
    def constructRectangle(area: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn construct_rectangle(area: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (construct-rectangle area)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec construct_rectangle(Area :: integer()) -> [integer()].
construct_rectangle(Area) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec construct_rectangle(area :: integer) :: [integer]
  def construct_rectangle(area) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func constructRectangle(area: Int64): Array<Int64> {

    }
}
```

