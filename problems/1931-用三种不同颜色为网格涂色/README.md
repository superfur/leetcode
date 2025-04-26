# 1931. 用三种不同颜色为网格涂色

## 题目描述

<p>给你两个整数 <code>m</code> 和 <code>n</code> 。构造一个 <code>m x n</code> 的网格，其中每个单元格最开始是白色。请你用 <strong>红、绿、蓝</strong> 三种颜色为每个单元格涂色。所有单元格都需要被涂色。</p>

<p>涂色方案需要满足：<strong>不存在相邻两个单元格颜色相同的情况</strong> 。返回网格涂色的方法数。因为答案可能非常大， 返回 <strong>对 </strong><code>10<sup>9</sup> + 7</code><strong> 取余</strong> 的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/colorthegrid.png" style="width: 200px; height: 50px;" />
<pre>
<strong>输入：</strong>m = 1, n = 1
<strong>输出：</strong>3
<strong>解释：</strong>如上图所示，存在三种可能的涂色方案。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/copy-of-colorthegrid.png" style="width: 321px; height: 121px;" />
<pre>
<strong>输入：</strong>m = 1, n = 2
<strong>输出：</strong>6
<strong>解释：</strong>如上图所示，存在六种可能的涂色方案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>m = 5, n = 5
<strong>输出：</strong>580986
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= m <= 5</code></li>
	<li><code>1 <= n <= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 提示

1. Represent each colored column by a bitmask based on each cell color.
2. Use bitmasks DP with state (currentCell, prevColumn).

## 示例

```
1
1
1
2
5
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int colorTheGrid(int m, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int colorTheGrid(int m, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
```

### C

```c
int colorTheGrid(int m, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int ColorTheGrid(int m, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var colorTheGrid = function(m, n) {
    
};
```

### TypeScript

```typescript
function colorTheGrid(m: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @return Integer
     */
    function colorTheGrid($m, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func colorTheGrid(_ m: Int, _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun colorTheGrid(m: Int, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int colorTheGrid(int m, int n) {
    
  }
}
```

### Go

```golang
func colorTheGrid(m int, n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @return {Integer}
def color_the_grid(m, n)
    
end
```

### Scala

```scala
object Solution {
    def colorTheGrid(m: Int, n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn color_the_grid(m: i32, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (color-the-grid m n)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec color_the_grid(M :: integer(), N :: integer()) -> integer().
color_the_grid(M, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec color_the_grid(m :: integer, n :: integer) :: integer
  def color_the_grid(m, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func colorTheGrid(m: Int64, n: Int64): Int64 {

    }
}
```

