# 964. 表示数字的最少运算符

## 题目描述

<p>给定一个正整数 <code>x</code>，我们将会写出一个形如&nbsp;<code>x (op1) x (op2) x (op3) x ...</code>&nbsp;的表达式，其中每个运算符&nbsp;<code>op1</code>，<code>op2</code>，… 可以是加、减、乘、除（<code>+</code>，<code>-</code>，<code>*</code>，或是&nbsp;<code>/</code>）之一。例如，对于&nbsp;<code>x = 3</code>，我们可以写出表达式&nbsp;<code>3 * 3 / 3 + 3 - 3</code>，该式的值为 3 。</p>

<p>在写这样的表达式时，我们需要遵守下面的惯例：</p>

<ul>
	<li>除运算符（<code>/</code>）返回有理数。</li>
	<li>任何地方都没有括号。</li>
	<li>我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。</li>
	<li>不允许使用一元否定运算符（<code>-</code>）。例如，“<code>x - x</code>” 是一个有效的表达式，因为它只使用减法，但是 “<code>-x + x</code>” 不是，因为它使用了否定运算符。&nbsp;</li>
</ul>

<p>我们希望编写一个能使表达式等于给定的目标值 <code>target</code> 且运算符最少的表达式。返回所用运算符的最少数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 3, target = 19
<strong>输出：</strong>5
<strong>解释：</strong>3 * 3 + 3 * 3 + 3 / 3 。表达式包含 5 个运算符。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>x = 5, target = 501
<strong>输出：</strong>8
<strong>解释：</strong>5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5 。表达式包含 8 个运算符。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 100, target = 100000000
<strong>输出：</strong>3
<strong>解释：</strong>100 * 100 * 100 * 100 。表达式包含 3 个运算符。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= x &lt;= 100</code></li>
	<li><code>1 &lt;= target &lt;= 2 * 10<sup>8</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数学
- 动态规划

## 示例

```
3
19
5
501
100
100000000
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int leastOpsExpressTarget(int x, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int leastOpsExpressTarget(int x, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        """
        :type x: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        
```

### C

```c
int leastOpsExpressTarget(int x, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int LeastOpsExpressTarget(int x, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} target
 * @return {number}
 */
var leastOpsExpressTarget = function(x, target) {
    
};
```

### TypeScript

```typescript
function leastOpsExpressTarget(x: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $target
     * @return Integer
     */
    function leastOpsExpressTarget($x, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func leastOpsExpressTarget(_ x: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun leastOpsExpressTarget(x: Int, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int leastOpsExpressTarget(int x, int target) {
    
  }
}
```

### Go

```golang
func leastOpsExpressTarget(x int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} target
# @return {Integer}
def least_ops_express_target(x, target)
    
end
```

### Scala

```scala
object Solution {
    def leastOpsExpressTarget(x: Int, target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn least_ops_express_target(x: i32, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (least-ops-express-target x target)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec least_ops_express_target(X :: integer(), Target :: integer()) -> integer().
least_ops_express_target(X, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec least_ops_express_target(x :: integer, target :: integer) :: integer
  def least_ops_express_target(x, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func leastOpsExpressTarget(x: Int64, target: Int64): Int64 {

    }
}
```

