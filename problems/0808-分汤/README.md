# 808. 分汤

## 题目描述

<p>有&nbsp;<strong>A&nbsp;和&nbsp;B 两种类型&nbsp;</strong>的汤。一开始每种类型的汤有&nbsp;<code>n</code>&nbsp;毫升。有四种分配操作：</p>

<ol>
	<li>提供 <code>100ml</code> 的 <strong>汤A</strong> 和 <code>0ml</code> 的 <strong>汤B</strong> 。</li>
	<li>提供 <code>75ml</code> 的 <strong>汤A</strong> 和 <code>25ml</code> 的 <strong>汤B</strong> 。</li>
	<li>提供 <code>50ml</code> 的 <strong>汤A</strong> 和 <code>50ml</code> 的 <strong>汤B</strong> 。</li>
	<li>提供 <code>25ml</code> 的 <strong>汤A</strong> 和 <code>75ml</code> 的 <strong>汤B</strong> 。</li>
</ol>

<p>当我们把汤分配给某人之后，汤就没有了。每个回合，我们将从四种概率同为 <code>0.25</code> 的操作中进行分配选择。如果汤的剩余量不足以完成某次操作，我们将尽可能分配。当两种类型的汤都分配完时，停止操作。</p>

<p><strong>注意&nbsp;</strong>不存在先分配 <code>100</code> ml <strong>汤B</strong> 的操作。</p>

<p>需要返回的值：&nbsp;<strong>汤A&nbsp;</strong>先分配完的概率 +&nbsp;&nbsp;<strong>汤A和汤B&nbsp;</strong>同时分配完的概率 / 2。返回值在正确答案&nbsp;<code>10<sup>-5</sup></code>&nbsp;的范围内将被认为是正确的。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> n = 50
<strong>输出:</strong> 0.62500
<strong>解释:</strong>如果我们选择前两个操作<strong>，</strong>A 首先将变为空。
对于第三个操作，A 和 B 会同时变为空。
对于第四个操作，B 首先将变为空。<strong>
</strong>所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> n = 100
<strong>输出:</strong> 0.71875
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code>​​​​​​​</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 概率与统计

## 示例

```
50
100
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double soupServings(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public double soupServings(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def soupServings(self, n):
        """
        :type n: int
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def soupServings(self, n: int) -> float:
        
```

### C

```c
double soupServings(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public double SoupServings(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var soupServings = function(n) {
    
};
```

### TypeScript

```typescript
function soupServings(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Float
     */
    function soupServings($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func soupServings(_ n: Int) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun soupServings(n: Int): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double soupServings(int n) {
    
  }
}
```

### Go

```golang
func soupServings(n int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Float}
def soup_servings(n)
    
end
```

### Scala

```scala
object Solution {
    def soupServings(n: Int): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn soup_servings(n: i32) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (soup-servings n)
  (-> exact-integer? flonum?)
  )
```

### Erlang

```erlang
-spec soup_servings(N :: integer()) -> float().
soup_servings(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec soup_servings(n :: integer) :: float
  def soup_servings(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func soupServings(n: Int64): Float64 {

    }
}
```

