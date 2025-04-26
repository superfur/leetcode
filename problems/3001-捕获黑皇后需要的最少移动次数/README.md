# 3001. 捕获黑皇后需要的最少移动次数

## 题目描述

<p>现有一个下标从 <strong>1</strong> 开始的 <code>8 x 8</code> 棋盘，上面有 <code>3</code> 枚棋子。</p>

<p>给你 <code>6</code> 个整数 <code>a</code> 、<code>b</code> 、<code>c</code> 、<code>d</code> 、<code>e</code> 和 <code>f</code> ，其中：</p>

<ul>
	<li><code>(a, b)</code> 表示白色车的位置。</li>
	<li><code>(c, d)</code> 表示白色象的位置。</li>
	<li><code>(e, f)</code> 表示黑皇后的位置。</li>
</ul>

<p>假定你只能移动白色棋子，返回捕获黑皇后所需的<strong>最少</strong>移动次数。</p>

<p><strong>请注意</strong>：</p>

<ul>
	<li>车可以向垂直或水平方向移动任意数量的格子，但不能跳过其他棋子。</li>
	<li>象可以沿对角线方向移动任意数量的格子，但不能跳过其他棋子。</li>
	<li>如果车或象能移向皇后所在的格子，则认为它们可以捕获皇后。</li>
	<li>皇后不能移动。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/21/ex1.png" style="width: 600px; height: 600px; padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>a = 1, b = 1, c = 8, d = 8, e = 2, f = 3
<strong>输出：</strong>2
<strong>解释：</strong>将白色车先移动到 (1, 3) ，然后移动到 (2, 3) 来捕获黑皇后，共需移动 2 次。
由于起始时没有任何棋子正在攻击黑皇后，要想捕获黑皇后，移动次数不可能少于 2 次。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/12/21/ex2.png" style="width: 600px; height: 600px;padding: 10px; background: #fff; border-radius: .5rem;" />
<pre>
<strong>输入：</strong>a = 5, b = 3, c = 3, d = 4, e = 5, f = 2
<strong>输出：</strong>1
<strong>解释：</strong>可以通过以下任一方式移动 1 次捕获黑皇后：
- 将白色车移动到 (5, 2) 。
- 将白色象移动到 (5, 2) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a, b, c, d, e, f &lt;= 8</code></li>
	<li>两枚棋子不会同时出现在同一个格子上。</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 枚举

## 提示

1. The minimum number of moves can be either <code>1</code> or <code>2</code>.
2. The answer will be <code>1</code> if the queen is on the path of the rook or bishop and none of them is in between.

## 示例

```
1
1
8
8
2
3
5
3
3
4
5
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        """
        :type a: int
        :type b: int
        :type c: int
        :type d: int
        :type e: int
        :type f: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        
```

### C

```c
int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @param {number} d
 * @param {number} e
 * @param {number} f
 * @return {number}
 */
var minMovesToCaptureTheQueen = function(a, b, c, d, e, f) {
    
};
```

### TypeScript

```typescript
function minMovesToCaptureTheQueen(a: number, b: number, c: number, d: number, e: number, f: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @param Integer $d
     * @param Integer $e
     * @param Integer $f
     * @return Integer
     */
    function minMovesToCaptureTheQueen($a, $b, $c, $d, $e, $f) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMovesToCaptureTheQueen(_ a: Int, _ b: Int, _ c: Int, _ d: Int, _ e: Int, _ f: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMovesToCaptureTheQueen(a: Int, b: Int, c: Int, d: Int, e: Int, f: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMovesToCaptureTheQueen(int a, int b, int c, int d, int e, int f) {
    
  }
}
```

### Go

```golang
func minMovesToCaptureTheQueen(a int, b int, c int, d int, e int, f int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @param {Integer} d
# @param {Integer} e
# @param {Integer} f
# @return {Integer}
def min_moves_to_capture_the_queen(a, b, c, d, e, f)
    
end
```

### Scala

```scala
object Solution {
    def minMovesToCaptureTheQueen(a: Int, b: Int, c: Int, d: Int, e: Int, f: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_moves_to_capture_the_queen(a: i32, b: i32, c: i32, d: i32, e: i32, f: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-moves-to-capture-the-queen a b c d e f)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_moves_to_capture_the_queen(A :: integer(), B :: integer(), C :: integer(), D :: integer(), E :: integer(), F :: integer()) -> integer().
min_moves_to_capture_the_queen(A, B, C, D, E, F) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_moves_to_capture_the_queen(a :: integer, b :: integer, c :: integer, d :: integer, e :: integer, f :: integer) :: integer
  def min_moves_to_capture_the_queen(a, b, c, d, e, f) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMovesToCaptureTheQueen(a: Int64, b: Int64, c: Int64, d: Int64, e: Int64, f: Int64): Int64 {

    }
}
```

