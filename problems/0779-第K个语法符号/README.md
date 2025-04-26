# 779. 第K个语法符号

## 题目描述

<p>我们构建了一个包含 <code>n</code> 行(&nbsp;<strong>索引从 1&nbsp; 开始&nbsp;</strong>)的表。首先在第一行我们写上一个 <code>0</code>。接下来的每一行，将前一行中的<code>0</code>替换为<code>01</code>，<code>1</code>替换为<code>10</code>。</p>

<ul>
	<li>例如，对于 <code>n = 3</code> ，第 <code>1</code> 行是 <code>0</code> ，第 <code>2</code> 行是 <code>01</code> ，第3行是 <code>0110</code> 。</li>
</ul>

<p>给定行数&nbsp;<code>n</code>&nbsp;和序数 <code>k</code>，返回第 <code>n</code> 行中第 <code>k</code>&nbsp;个字符。（&nbsp;<code>k</code>&nbsp;<strong>从索引 1 开始</strong>）</p>

<p><br />
<strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 1, k = 1
<strong>输出:</strong> 0
<strong>解释: </strong>第一行：<u>0</u>
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 2, k = 1
<strong>输出:</strong> 0
<strong>解释:</strong> 
第一行: 0 
第二行: <u>0</u>1
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> n = 2, k = 2
<strong>输出:</strong> 1
<strong>解释:</strong>
第一行: 0
第二行: 0<u>1</u>
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 30</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>n - 1</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 递归
- 数学

## 提示

1. Try to represent the current (N, K) in terms of some (N-1, prevK).  What is prevK ?

## 示例

```
1
1
2
1
2
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kthGrammar(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kthGrammar(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
```

### C

```c
int kthGrammar(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KthGrammar(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthGrammar = function(n, k) {
    
};
```

### TypeScript

```typescript
function kthGrammar(n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function kthGrammar($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthGrammar(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthGrammar(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kthGrammar(int n, int k) {
    
  }
}
```

### Go

```golang
func kthGrammar(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_grammar(n, k)
    
end
```

### Scala

```scala
object Solution {
    def kthGrammar(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_grammar(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (kth-grammar n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec kth_grammar(N :: integer(), K :: integer()) -> integer().
kth_grammar(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_grammar(n :: integer, k :: integer) :: integer
  def kth_grammar(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthGrammar(n: Int64, k: Int64): Int64 {

    }
}
```

