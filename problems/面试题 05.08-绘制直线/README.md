# 面试题 05.08. 绘制直线

## 题目描述

<p>已知一个由像素点组成的单色屏幕，每行均有 <code>w</code> 个像素点，所有像素点初始为 <code>0</code>，左上角位置为 <code>(0,0)</code>。</p>

<p>现将每行的像素点按照「每 <code>32</code> 个像素点」为一组存放在一个 <code>int</code> 中，再依次存入长度为 <code>length</code> 的一维数组中。</p>

<p>我们将在屏幕上绘制一条从点 <code>(x1,y)</code> 到点 <code>(x2,y)</code> 的直线（即像素点修改为 <code>1</code>），请返回绘制过后的数组。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li>用例保证屏幕宽度 <code>w</code> 可被 32 整除（即一个 <code>int</code> 不会分布在两行上）</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：length = 1, w = 32, x1 = 30, x2 = 31, y = 0
<strong> 输出</strong>：[3]
<strong> 解释</strong>：在第 0 行的第 30 位到第 31 位画一条直线，屏幕二进制形式表示为 [00000000000000000000000000000011]，因此返回 [3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：length = 3, w = 96, x1 = 0, x2 = 95, y = 0
<strong> 输出</strong>：[-1, -1, -1]
<strong> 解释</strong>：由于二进制 <strong>11111111111111111111111111111111</strong> 的 int 类型代表 -1，因此返回 [-1,-1,-1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= length &lt;= 10^5</code></li>
	<li><code>1 &lt;= w &lt;= 3 * 10^5</code></li>
	<li><code>0 &lt;= x1 &lt;= x2 &lt; w</code></li>
	<li><code>0 &lt;= y &lt;= 10</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 数学

## 提示

1. 先试试简单解法。你能设置一个特定的“像素”吗？
2. 当你画一条长线时，你会得到即将变成1的序列的全部字节。你可以一次性设置它吗？
3. 那这条线的起点和终点呢？你需要单独设置这些像素，还是可以同时设置所有像素？
4. 当x1和x2在同一个字节中时，你的代码能否处理这种情况。

## 示例

```
1
32
30
31
0
3
96
0
95
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> drawLine(int length, int w, int x1, int x2, int y) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] drawLine(int length, int w, int x1, int x2, int y) {
        
    }
}
```

### Python

```python
class Solution(object):
    def drawLine(self, length, w, x1, x2, y):
        """
        :type length: int
        :type w: int
        :type x1: int
        :type x2: int
        :type y: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* drawLine(int length, int w, int x1, int x2, int y, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] DrawLine(int length, int w, int x1, int x2, int y) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} length
 * @param {number} w
 * @param {number} x1
 * @param {number} x2
 * @param {number} y
 * @return {number[]}
 */
var drawLine = function(length, w, x1, x2, y) {
    
};
```

### TypeScript

```typescript
function drawLine(length: number, w: number, x1: number, x2: number, y: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $length
     * @param Integer $w
     * @param Integer $x1
     * @param Integer $x2
     * @param Integer $y
     * @return Integer[]
     */
    function drawLine($length, $w, $x1, $x2, $y) {
        
    }
}
```

### Swift

```swift
class Solution {
    func drawLine(_ length: Int, _ w: Int, _ x1: Int, _ x2: Int, _ y: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun drawLine(length: Int, w: Int, x1: Int, x2: Int, y: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> drawLine(int length, int w, int x1, int x2, int y) {
    
  }
}
```

### Go

```golang
func drawLine(length int, w int, x1 int, x2 int, y int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} length
# @param {Integer} w
# @param {Integer} x1
# @param {Integer} x2
# @param {Integer} y
# @return {Integer[]}
def draw_line(length, w, x1, x2, y)
    
end
```

### Scala

```scala
object Solution {
    def drawLine(length: Int, w: Int, x1: Int, x2: Int, y: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn draw_line(length: i32, w: i32, x1: i32, x2: i32, y: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (draw-line length w x1 x2 y)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec draw_line(Length :: integer(), W :: integer(), X1 :: integer(), X2 :: integer(), Y :: integer()) -> [integer()].
draw_line(Length, W, X1, X2, Y) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec draw_line(length :: integer, w :: integer, x1 :: integer, x2 :: integer, y :: integer) :: [integer]
  def draw_line(length, w, x1, x2, y) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func drawLine(length: Int64, w: Int64, x1: Int64, x2: Int64, y: Int64): Array<Int64> {

    }
}
```

