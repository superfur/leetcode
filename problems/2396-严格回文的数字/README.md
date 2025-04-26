# 2396. 严格回文的数字

## 题目描述

<p>如果一个整数 <code>n</code>&nbsp;在 <code>b</code>&nbsp;进制下（<code>b</code>&nbsp;为 <code>2</code>&nbsp;到 <code>n - 2</code>&nbsp;之间的所有整数）对应的字符串&nbsp;<strong>全部</strong>&nbsp;都是 <strong>回文的</strong>&nbsp;，那么我们称这个数&nbsp;<code>n</code>&nbsp;是 <strong>严格回文</strong>&nbsp;的。</p>

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，如果 <code>n</code>&nbsp;是 <strong>严格回文</strong>&nbsp;的，请返回&nbsp;<code>true</code> ，否则返回<em>&nbsp;</em><code>false</code>&nbsp;。</p>

<p>如果一个字符串从前往后读和从后往前读完全相同，那么这个字符串是 <strong>回文的</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 9
<b>输出：</b>false
<b>解释：</b>在 2 进制下：9 = 1001 ，是回文的。
在 3 进制下：9 = 100 ，不是回文的。
所以，9 不是严格回文数字，我们返回 false 。
注意在 4, 5, 6 和 7 进制下，n = 9 都不是回文的。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 4
<b>输出：</b>false
<b>解释：</b>我们只考虑 2 进制：4 = 100 ，不是回文的。
所以我们返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>4 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 脑筋急转弯
- 数学
- 双指针

## 提示

1. Consider the representation of the given number in the base n - 2.
2. The number n in base (n - 2) is always 12, which is not palindromic.

## 示例

```
9
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isStrictlyPalindromic(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isStrictlyPalindromic(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
```

### C

```c
bool isStrictlyPalindromic(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsStrictlyPalindromic(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {boolean}
 */
var isStrictlyPalindromic = function(n) {
    
};
```

### TypeScript

```typescript
function isStrictlyPalindromic(n: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Boolean
     */
    function isStrictlyPalindromic($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isStrictlyPalindromic(_ n: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isStrictlyPalindromic(n: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isStrictlyPalindromic(int n) {
    
  }
}
```

### Go

```golang
func isStrictlyPalindromic(n int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Boolean}
def is_strictly_palindromic(n)
    
end
```

### Scala

```scala
object Solution {
    def isStrictlyPalindromic(n: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_strictly_palindromic(n: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-strictly-palindromic n)
  (-> exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_strictly_palindromic(N :: integer()) -> boolean().
is_strictly_palindromic(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_strictly_palindromic(n :: integer) :: boolean
  def is_strictly_palindromic(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isStrictlyPalindromic(n: Int64): Bool {

    }
}
```

