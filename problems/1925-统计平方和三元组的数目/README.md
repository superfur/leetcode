# 1925. 统计平方和三元组的数目

## 题目描述

<p>一个 <strong>平方和三元组</strong> <code>(a,b,c)</code> 指的是满足 <code>a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup></code> 的 <strong>整数 </strong>三元组 <code>a</code>，<code>b</code> 和 <code>c</code> 。</p>

<p>给你一个整数 <code>n</code> ，请你返回满足<em> </em><code>1 &lt;= a, b, c &lt;= n</code> 的 <strong>平方和三元组</strong> 的数目。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 5
<b>输出：</b>2
<b>解释：</b>平方和三元组为 (3,4,5) 和 (4,3,5) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 10
<b>输出：</b>4
<b>解释：</b>平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 250</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 枚举

## 提示

1. Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n
2. You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt

## 示例

```
5
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countTriples(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countTriples(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countTriples(self, n: int) -> int:
        
```

### C

```c
int countTriples(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountTriples(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countTriples = function(n) {
    
};
```

### TypeScript

```typescript
function countTriples(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countTriples($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countTriples(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countTriples(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countTriples(int n) {
    
  }
}
```

### Go

```golang
func countTriples(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_triples(n)
    
end
```

### Scala

```scala
object Solution {
    def countTriples(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_triples(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-triples n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_triples(N :: integer()) -> integer().
count_triples(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_triples(n :: integer) :: integer
  def count_triples(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countTriples(n: Int64): Int64 {

    }
}
```

