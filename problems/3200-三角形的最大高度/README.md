# 3200. 三角形的最大高度

## 题目描述

<p>给你两个整数 <code>red</code> 和 <code>blue</code>，分别表示红色球和蓝色球的数量。你需要使用这些球来组成一个三角形，满足第 1 行有 1 个球，第 2 行有 2 个球，第 3 行有 3 个球，依此类推。</p>

<p>每一行的球必须是 <strong>相同 </strong>颜色，且相邻行的颜色必须<strong> 不同</strong>。</p>

<p>返回可以实现的三角形的 <strong>最大 </strong>高度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">red = 2, blue = 4</span></p>

<p><strong>输出：</strong> 3</p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/16/brb.png" style="width: 300px; height: 240px; padding: 10px;" /></p>

<p>上图显示了唯一可能的排列方式。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">red = 2, blue = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/16/br.png" style="width: 150px; height: 135px; padding: 10px;" /><br />
上图显示了唯一可能的排列方式。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">red = 1, blue = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">red = 10, blue = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/16/br.png" style="width: 150px; height: 135px; padding: 10px;" /><br />
上图显示了唯一可能的排列方式。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= red, blue &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举

## 提示

1. Count the max height using both possibilities. That is, red ball as top and blue ball as top.
2. For counting the max height, use a simple for loop and remove the number of balls required at this level.

## 示例

```
2
4
2
1
1
1
10
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxHeightOfTriangle(int red, int blue) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
```

### C

```c
int maxHeightOfTriangle(int red, int blue) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxHeightOfTriangle(int red, int blue) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} red
 * @param {number} blue
 * @return {number}
 */
var maxHeightOfTriangle = function(red, blue) {
    
};
```

### TypeScript

```typescript
function maxHeightOfTriangle(red: number, blue: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $red
     * @param Integer $blue
     * @return Integer
     */
    function maxHeightOfTriangle($red, $blue) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxHeightOfTriangle(_ red: Int, _ blue: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxHeightOfTriangle(red: Int, blue: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxHeightOfTriangle(int red, int blue) {
    
  }
}
```

### Go

```golang
func maxHeightOfTriangle(red int, blue int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} red
# @param {Integer} blue
# @return {Integer}
def max_height_of_triangle(red, blue)
    
end
```

### Scala

```scala
object Solution {
    def maxHeightOfTriangle(red: Int, blue: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_height_of_triangle(red: i32, blue: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-height-of-triangle red blue)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_height_of_triangle(Red :: integer(), Blue :: integer()) -> integer().
max_height_of_triangle(Red, Blue) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_height_of_triangle(red :: integer, blue :: integer) :: integer
  def max_height_of_triangle(red, blue) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxHeightOfTriangle(red: Int64, blue: Int64): Int64 {

    }
}
```

