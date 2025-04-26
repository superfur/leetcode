# 984. 不含 AAA 或 BBB 的字符串

## 题目描述

<p>给定两个整数 <code>a</code>&nbsp;和 <code>b</code>&nbsp;，返回&nbsp;<strong>任意</strong>&nbsp;字符串 <code>s</code>&nbsp;，要求满足：</p>

<ul>
	<li><code>s</code>&nbsp;的长度为 <code>a + b</code>，且正好包含&nbsp;<code>a</code>&nbsp;个 <code>'a'</code>&nbsp;字母与&nbsp;<code>b</code> 个 <code>'b'</code>&nbsp;字母；</li>
	<li>子串&nbsp;<code>'aaa'</code>&nbsp;没有出现在 <code>s</code>&nbsp;中；</li>
	<li>子串&nbsp;<code>'bbb'</code> 没有出现在 <code>s</code>&nbsp;中。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>a = 1, b = 2
<strong>输出：</strong>"abb"
<strong>解释：</strong>"abb", "bab" 和 "bba" 都是正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = 4, b = 1
<strong>输出：</strong>"aabaa"</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= a, b&nbsp;&lt;= 100</code></li>
	<li>对于给定的 <code>a</code> 和 <code>b</code>，保证存在满足要求的 <code>s</code>&nbsp;</li>
</ul>
<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​</span></span></span>

## 难度

Medium

## 标签

- 贪心
- 字符串

## 示例

```
1
2
4
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string strWithout3a3b(int a, int b) {
        
    }
};
```

### Java

```java
class Solution {
    public String strWithout3a3b(int a, int b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def strWithout3a3b(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        
```

### C

```c
char* strWithout3a3b(int a, int b) {
    
}
```

### C#

```csharp
public class Solution {
    public string StrWithout3a3b(int a, int b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
var strWithout3a3b = function(a, b) {
    
};
```

### TypeScript

```typescript
function strWithout3a3b(a: number, b: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @return String
     */
    function strWithout3a3b($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func strWithout3a3b(_ a: Int, _ b: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun strWithout3a3b(a: Int, b: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String strWithout3a3b(int a, int b) {
    
  }
}
```

### Go

```golang
func strWithout3a3b(a int, b int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @return {String}
def str_without3a3b(a, b)
    
end
```

### Scala

```scala
object Solution {
    def strWithout3a3b(a: Int, b: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn str_without3a3b(a: i32, b: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (str-without3a3b a b)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec str_without3a3b(A :: integer(), B :: integer()) -> unicode:unicode_binary().
str_without3a3b(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec str_without3a3b(a :: integer, b :: integer) :: String.t
  def str_without3a3b(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func strWithout3a3b(a: Int64, b: Int64): String {

    }
}
```

