# 9. 回文数

## 题目描述

<p>给你一个整数 <code>x</code> ，如果 <code>x</code> 是一个回文整数，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p><span data-keyword="palindrome-integer">回文数</span>是指正序（从左向右）和倒序（从右向左）读都是一样的整数。</p>

<ul>
	<li>例如，<code>121</code> 是回文，而 <code>123</code> 不是。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>x = 121
<strong>输出：</strong>true
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>x = -121
<strong>输出：</strong>false
<strong>解释：</strong>从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>x = 10
<strong>输出：</strong>false
<strong>解释：</strong>从右向左读, 为 01 。因此它不是一个回文数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能不将整数转为字符串来解决这个问题吗？</p>


## 难度

Easy

## 标签

- 数学

## 提示

1. Beware of overflow when you reverse the integer.

## 示例

```
121
-121
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPalindrome(int x) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPalindrome(int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
```

### C

```c
bool isPalindrome(int x) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPalindrome(int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
};
```

### TypeScript

```typescript
function isPalindrome(x: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPalindrome(x: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPalindrome(int x) {
    
  }
}
```

### Go

```golang
func isPalindrome(x int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    
end
```

### Scala

```scala
object Solution {
    def isPalindrome(x: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-palindrome x)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_palindrome(X :: integer()) -> boolean().
is_palindrome(X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_palindrome(x :: integer) :: boolean
  def is_palindrome(x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPalindrome(x: Int64): Bool {

    }
}
```

