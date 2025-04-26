# 1033. 移动石子直到连续

## 题目描述

<p>三枚石子放置在数轴上，位置分别为 <code>a</code>，<code>b</code>，<code>c</code>。</p>

<p>每一回合，你可以从两端之一拿起一枚石子（位置最大或最小），并将其放入两端之间的任一空闲位置。形式上，假设这三枚石子当前分别位于位置 <code>x, y, z</code> 且 <code>x < y < z</code>。那么就可以从位置 <code>x</code> 或者是位置 <code>z</code> 拿起一枚石子，并将该石子移动到某一整数位置 <code>k</code> 处，其中 <code>x < k < z</code> 且 <code>k != y</code>。</p>

<p>当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。</p>

<p>要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案：<code>answer = [minimum_moves, maximum_moves]</code></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>a = 1, b = 2, c = 5
<strong>输出：</strong>[1, 2]
<strong>解释：</strong>将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = 4, b = 3, c = 2
<strong>输出：</strong>[0, 0]
<strong>解释：</strong>我们无法进行任何移动。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 <= a <= 100</code></li>
	<li><code>1 <= b <= 100</code></li>
	<li><code>1 <= c <= 100</code></li>
	<li><code>a != b, b != c, c != a</code></li>
</ol>


## 难度

Medium

## 标签

- 脑筋急转弯
- 数学

## 提示

1. For the minimum:  We can always do it in at most 2 moves, by moving one stone next to another, then the third stone next to the other two.  When can we do it in 1 move?  0 moves?

For the maximum:  Every move, the maximum position minus the minimum position must decrease by at least 1.

## 示例

```
1
2
5
4
3
2
3
5
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numMovesStones(int a, int b, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numMovesStones(int a, int b, int c, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] NumMovesStones(int a, int b, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number[]}
 */
var numMovesStones = function(a, b, c) {
    
};
```

### TypeScript

```typescript
function numMovesStones(a: number, b: number, c: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer[]
     */
    function numMovesStones($a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numMovesStones(_ a: Int, _ b: Int, _ c: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numMovesStones(a: Int, b: Int, c: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numMovesStones(int a, int b, int c) {
    
  }
}
```

### Go

```golang
func numMovesStones(a int, b int, c int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer[]}
def num_moves_stones(a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def numMovesStones(a: Int, b: Int, c: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_moves_stones(a: i32, b: i32, c: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (num-moves-stones a b c)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec num_moves_stones(A :: integer(), B :: integer(), C :: integer()) -> [integer()].
num_moves_stones(A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_moves_stones(a :: integer, b :: integer, c :: integer) :: [integer]
  def num_moves_stones(a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numMovesStones(a: Int64, b: Int64, c: Int64): Array<Int64> {

    }
}
```

