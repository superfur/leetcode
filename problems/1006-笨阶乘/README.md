# 1006. 笨阶乘

## 题目描述

<p>通常，正整数 <code>n</code> 的阶乘是所有小于或等于 <code>n</code> 的正整数的乘积。例如，<code>factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1</code>。</p>

<p>相反，我们设计了一个笨阶乘 <code>clumsy</code>：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。</p>

<p>例如，<code>clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1</code>。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。</p>

<p>另外，我们使用的除法是地板除法（<em>floor division</em>），所以&nbsp;<code>10 * 9 / 8</code>&nbsp;等于&nbsp;<code>11</code>。这保证结果是一个整数。</p>

<p>实现上面定义的笨函数：给定一个整数 <code>N</code>，它返回 <code>N</code> 的笨阶乘。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>4
<strong>输出：</strong>7
<strong>解释：</strong>7 = 4 * 3 / 2 + 1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>10
<strong>输出：</strong>12
<strong>解释：</strong>12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 10000</code></li>
	<li><code>-2^31 &lt;= answer &lt;= 2^31 - 1</code>&nbsp; （答案保证符合 32 位整数。）</li>
</ol>


## 难度

Medium

## 标签

- 栈
- 数学
- 模拟

## 示例

```
4
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int clumsy(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int clumsy(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def clumsy(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def clumsy(self, n: int) -> int:
        
```

### C

```c
int clumsy(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int Clumsy(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var clumsy = function(n) {
    
};
```

### TypeScript

```typescript
function clumsy(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function clumsy($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func clumsy(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun clumsy(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int clumsy(int n) {
    
  }
}
```

### Go

```golang
func clumsy(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def clumsy(n)
    
end
```

### Scala

```scala
object Solution {
    def clumsy(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn clumsy(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (clumsy n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec clumsy(N :: integer()) -> integer().
clumsy(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec clumsy(n :: integer) :: integer
  def clumsy(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func clumsy(n: Int64): Int64 {

    }
}
```

