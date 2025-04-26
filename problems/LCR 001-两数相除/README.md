# LCR 001. 两数相除

## 题目描述

<p>给定两个整数 <code>a</code> 和 <code>b</code> ，求它们的除法的商 <code>a/b</code> ，要求不得使用乘号 <code>&#39;*&#39;</code>、除号 <code>&#39;/&#39;</code> 以及求余符号 <code>&#39;%&#39;</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>注意：</strong></p>

<ul>
	<li>整数除法的结果应当截去（<code>truncate</code>）其小数部分，例如：<code>truncate(8.345) = 8</code>&nbsp;以及&nbsp;<code>truncate(-2.7335) = -2</code></li>
	<li>假设我们的环境只能存储 32 位有符号整数，其数值范围是 <code>[&minus;2<sup>31</sup>,&nbsp;2<sup>31</sup>&minus;1]</code>。本题中，如果除法结果溢出，则返回 <code>2<sup>31&nbsp;</sup>&minus; 1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>a = 15, b = 2
<strong>输出：</strong>7
<strong><span style="white-space: pre-wrap;">解释：</span></strong>15/2 = truncate(7.5) = 7
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = 7, b = -3
<strong>输出：</strong><span style="white-space: pre-wrap;">-2</span>
<strong><span style="white-space: pre-wrap;">解释：</span></strong>7/-3 = truncate(-2.33333..) = -2</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>a = 0, b = 1
<strong>输出：</strong><span style="white-space: pre-wrap;">0</span></pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>a = 1, b = 1
<strong>输出：</strong><span style="white-space: pre-wrap;">1</span></pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= a, b &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
	<li><code>b != 0</code></li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 29&nbsp;题相同：<a href="https://leetcode-cn.com/problems/divide-two-integers/">https://leetcode-cn.com/problems/divide-two-integers/</a></p>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数学

## 示例

```
15
2
7
-3
-7
3
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int divide(int a, int b) {

    }
};
```

### Java

```java
class Solution {
    public int divide(int a, int b) {

    }
}
```

### Python

```python
class Solution(object):
    def divide(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def divide(self, a: int, b: int) -> int:
```

### C

```c


int divide(int a, int b){

}
```

### C#

```csharp
public class Solution {
    public int Divide(int a, int b) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var divide = function(a, b) {

};
```

### TypeScript

```typescript
function divide(a: number, b: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function divide($a, $b) {

    }
}
```

### Swift

```swift
class Solution {
    func divide(_ a: Int, _ b: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun divide(a: Int, b: Int): Int {

    }
}
```

### Go

```golang
func divide(a int, b int) int {

}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def divide(a, b)

end
```

### Scala

```scala
object Solution {
    def divide(a: Int, b: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn divide(a: i32, b: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (divide a b)
  (-> exact-integer? exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec divide(A :: integer(), B :: integer()) -> integer().
divide(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec divide(a :: integer, b :: integer) :: integer
  def divide(a, b) do

  end
end
```

