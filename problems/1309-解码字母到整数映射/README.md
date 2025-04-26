# 1309. 解码字母到整数映射

## 题目描述

<p>给你一个字符串&nbsp;<code>s</code>，它由数字（<code>'0'</code> - <code>'9'</code>）和&nbsp;<code>'#'</code>&nbsp;组成。我们希望按下述规则将&nbsp;<code>s</code>&nbsp;映射为一些小写英文字符：</p>

<ul>
	<li>字符（<code>'a'</code> - <code>'i'</code>）分别用（<code>'1'</code> -&nbsp;<code>'9'</code>）表示。</li>
	<li>字符（<code>'j'</code> - <code>'z'</code>）分别用（<code>'10#'</code>&nbsp;-&nbsp;<code>'26#'</code>）表示。&nbsp;</li>
</ul>

<p>返回映射之后形成的新字符串。</p>

<p>题目数据保证映射始终唯一。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "10#11#12"
<strong>输出：</strong>"jkab"
<strong>解释：</strong>"j" -&gt; "10#" , "k" -&gt; "11#" , "a" -&gt; "1" , "b" -&gt; "2".
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "1326#"
<strong>输出：</strong>"acz"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s[i]</code> 只包含数字（<code>'0'</code>-<code>'9'</code>）和&nbsp;<code>'#'</code>&nbsp;字符。</li>
	<li><code>s</code>&nbsp;是映射始终存在的有效字符串。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Scan from right to left, in each step of the scanning check whether there is a trailing "#" 2 indexes away.

## 示例

```
"10#11#12"
"1326#"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string freqAlphabets(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String freqAlphabets(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def freqAlphabets(self, s: str) -> str:
        
```

### C

```c
char* freqAlphabets(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string FreqAlphabets(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function(s) {
    
};
```

### TypeScript

```typescript
function freqAlphabets(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function freqAlphabets($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func freqAlphabets(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun freqAlphabets(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String freqAlphabets(String s) {
    
  }
}
```

### Go

```golang
func freqAlphabets(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def freq_alphabets(s)
    
end
```

### Scala

```scala
object Solution {
    def freqAlphabets(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn freq_alphabets(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (freq-alphabets s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec freq_alphabets(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
freq_alphabets(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec freq_alphabets(s :: String.t) :: String.t
  def freq_alphabets(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func freqAlphabets(s: String): String {

    }
}
```

