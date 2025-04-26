# 2579. 统计染色格子数

## 题目描述

<p>有一个无穷大的二维网格图，一开始所有格子都未染色。给你一个正整数&nbsp;<code>n</code>&nbsp;，表示你需要执行以下步骤&nbsp;<code>n</code>&nbsp;分钟：</p>

<ul>
	<li>第一分钟，将 <strong>任一</strong> 格子染成蓝色。</li>
	<li>之后的每一分钟，将与蓝色格子相邻的 <strong>所有</strong> 未染色格子染成蓝色。</li>
</ul>

<p>下图分别是 1、2、3 分钟后的网格图。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png" style="width: 500px; height: 279px;">
<p>请你返回 <code>n</code>&nbsp;分钟之后 <strong>被染色的格子&nbsp;</strong>数目。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre><b>输入：</b>n = 1
<b>输出：</b>1
<b>解释：</b>1 分钟后，只有 1 个蓝色的格子，所以返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 2
<b>输出：</b>5
<b>解释：</b>2 分钟后，有 4 个在边缘的蓝色格子和 1 个在中间的蓝色格子，所以返回 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Derive a mathematical relation between total number of colored cells and the time elapsed in minutes.

## 示例

```
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long coloredCells(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public long coloredCells(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def coloredCells(self, n: int) -> int:
        
```

### C

```c
long long coloredCells(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public long ColoredCells(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var coloredCells = function(n) {
    
};
```

### TypeScript

```typescript
function coloredCells(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function coloredCells($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func coloredCells(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun coloredCells(n: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int coloredCells(int n) {
    
  }
}
```

### Go

```golang
func coloredCells(n int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def colored_cells(n)
    
end
```

### Scala

```scala
object Solution {
    def coloredCells(n: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn colored_cells(n: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (colored-cells n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec colored_cells(N :: integer()) -> integer().
colored_cells(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec colored_cells(n :: integer) :: integer
  def colored_cells(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func coloredCells(n: Int64): Int64 {

    }
}
```

