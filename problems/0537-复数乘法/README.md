# 537. 复数乘法

## 题目描述

<p><a href="https://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365?fr=aladdin" target="_blank">复数</a> 可以用字符串表示，遵循 <code>"<strong>实部</strong>+<strong>虚部</strong>i"</code> 的形式，并满足下述条件：</p>

<ul>
	<li><code>实部</code> 是一个整数，取值范围是 <code>[-100, 100]</code></li>
	<li><code>虚部</code> 也是一个整数，取值范围是 <code>[-100, 100]</code></li>
	<li><code>i<sup>2</sup> == -1</code></li>
</ul>

<p>给你两个字符串表示的复数 <code>num1</code> 和 <code>num2</code> ，请你遵循复数表示形式，返回表示它们乘积的字符串。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num1 = "1+1i", num2 = "1+1i"
<strong>输出：</strong>"0+2i"
<strong>解释：</strong>(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num1 = "1+-1i", num2 = "1+-1i"
<strong>输出：</strong>"0+-2i"
<strong>解释：</strong>(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>num1</code> 和 <code>num2</code> 都是有效的复数表示。</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串
- 模拟

## 示例

```
"1+1i"
"1+1i"
"1+-1i"
"1+-1i"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        
    }
};
```

### Java

```java
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
```

### C

```c
char* complexNumberMultiply(char* num1, char* num2) {
    
}
```

### C#

```csharp
public class Solution {
    public string ComplexNumberMultiply(string num1, string num2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var complexNumberMultiply = function(num1, num2) {
    
};
```

### TypeScript

```typescript
function complexNumberMultiply(num1: string, num2: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num1
     * @param String $num2
     * @return String
     */
    function complexNumberMultiply($num1, $num2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func complexNumberMultiply(_ num1: String, _ num2: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun complexNumberMultiply(num1: String, num2: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String complexNumberMultiply(String num1, String num2) {
    
  }
}
```

### Go

```golang
func complexNumberMultiply(num1 string, num2 string) string {
    
}
```

### Ruby

```ruby
# @param {String} num1
# @param {String} num2
# @return {String}
def complex_number_multiply(num1, num2)
    
end
```

### Scala

```scala
object Solution {
    def complexNumberMultiply(num1: String, num2: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn complex_number_multiply(num1: String, num2: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (complex-number-multiply num1 num2)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec complex_number_multiply(Num1 :: unicode:unicode_binary(), Num2 :: unicode:unicode_binary()) -> unicode:unicode_binary().
complex_number_multiply(Num1, Num2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec complex_number_multiply(num1 :: String.t, num2 :: String.t) :: String.t
  def complex_number_multiply(num1, num2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func complexNumberMultiply(num1: String, num2: String): String {

    }
}
```

