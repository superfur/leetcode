# LCR 130. 衣橱整理

## 题目描述

<p>家居整理师将待整理衣橱划分为 <code>m x n</code> 的二维矩阵 <code>grid</code>，其中 <code>grid[i][j]</code> 代表一个需要整理的格子。整理师自 <code>grid[0][0]</code> 开始 <strong>逐行逐列</strong> 地整理每个格子。</p>

<p>整理规则为：在整理过程中，可以选择&nbsp;<strong>向右移动一格&nbsp;</strong>或&nbsp;<strong>向下移动一格</strong>，但不能移动到衣柜之外。同时，不需要整理 <code>digit(i)&nbsp;+ digit(j)&nbsp;&gt; cnt</code> 的格子，其中 <code>digit(x)</code>&nbsp;表示数字&nbsp;<code>x</code> 的各数位之和。</p>

<p>请返回整理师&nbsp;<strong>总共需要整理多少个格子</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>m = 4, n = 7, cnt = 5
<strong>输出：</strong>18
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 100</code></li>
	<li><code>0 &lt;= cnt &lt;= 20</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 动态规划

## 示例

```
4
7
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int wardrobeFinishing(int m, int n, int cnt) {
        
    }
};
```

### Java

```java
class Solution {
    public int wardrobeFinishing(int m, int n, int cnt) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wardrobeFinishing(self, m, n, cnt):
        """
        :type m: int
        :type n: int
        :type cnt: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        
```

### C

```c
int wardrobeFinishing(int m, int n, int cnt) {
    
}
```

### C#

```csharp
public class Solution {
    public int WardrobeFinishing(int m, int n, int cnt) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} m
 * @param {number} n
 * @param {number} cnt
 * @return {number}
 */
var wardrobeFinishing = function(m, n, cnt) {
    
};
```

### TypeScript

```typescript
function wardrobeFinishing(m: number, n: number, cnt: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $m
     * @param Integer $n
     * @param Integer $cnt
     * @return Integer
     */
    function wardrobeFinishing($m, $n, $cnt) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wardrobeFinishing(_ m: Int, _ n: Int, _ cnt: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wardrobeFinishing(m: Int, n: Int, cnt: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int wardrobeFinishing(int m, int n, int cnt) {
    
  }
}
```

### Go

```golang
func wardrobeFinishing(m int, n int, cnt int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} m
# @param {Integer} n
# @param {Integer} cnt
# @return {Integer}
def wardrobe_finishing(m, n, cnt)
    
end
```

### Scala

```scala
object Solution {
    def wardrobeFinishing(m: Int, n: Int, cnt: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn wardrobe_finishing(m: i32, n: i32, cnt: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (wardrobe-finishing m n cnt)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec wardrobe_finishing(M :: integer(), N :: integer(), Cnt :: integer()) -> integer().
wardrobe_finishing(M, N, Cnt) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec wardrobe_finishing(m :: integer, n :: integer, cnt :: integer) :: integer
  def wardrobe_finishing(m, n, cnt) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wardrobeFinishing(m: Int64, n: Int64, cnt: Int64): Int64 {

    }
}
```

