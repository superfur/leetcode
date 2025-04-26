# 2810. 故障键盘

## 题目描述

<p>你的笔记本键盘存在故障，每当你在上面输入字符 <code>'i'</code> 时，它会反转你所写的字符串。而输入其他字符则可以正常工作。</p>

<p>给你一个下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，请你用故障键盘依次输入每个字符。</p>

<p>返回最终笔记本屏幕上输出的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "string"
<strong>输出：</strong>"rtsng"
<strong>解释：</strong>
输入第 1 个字符后，屏幕上的文本是："s" 。
输入第 2 个字符后，屏幕上的文本是："st" 。
输入第 3 个字符后，屏幕上的文本是："str" 。
因为第 4 个字符是 'i' ，屏幕上的文本被反转，变成 "rts" 。
输入第 5 个字符后，屏幕上的文本是："rtsn" 。
输入第 6 个字符后，屏幕上的文本是： "rtsng" 。
因此，返回 "rtsng" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "poiinter"
<strong>输出：</strong>"ponter"
<strong>解释：</strong>
输入第 1 个字符后，屏幕上的文本是："p" 。
输入第 2 个字符后，屏幕上的文本是："po" 。
因为第 3 个字符是 'i' ，屏幕上的文本被反转，变成 "op" 。
因为第 4 个字符是 'i' ，屏幕上的文本被反转，变成 "po" 。
输入第 5 个字符后，屏幕上的文本是："pon" 。
输入第 6 个字符后，屏幕上的文本是："pont" 。
输入第 7 个字符后，屏幕上的文本是："ponte" 。
输入第 8 个字符后，屏幕上的文本是："ponter" 。
因此，返回 "ponter" 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>s[0] != 'i'</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 提示

1. Try to build a new string by traversing the given string and reversing whenever you get the character ‘i’.

## 示例

```
"string"
"poiinter"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string finalString(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String finalString(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def finalString(self, s: str) -> str:
        
```

### C

```c
char* finalString(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string FinalString(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var finalString = function(s) {
    
};
```

### TypeScript

```typescript
function finalString(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function finalString($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func finalString(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun finalString(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String finalString(String s) {
    
  }
}
```

### Go

```golang
func finalString(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def final_string(s)
    
end
```

### Scala

```scala
object Solution {
    def finalString(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn final_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (final-string s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec final_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
final_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec final_string(s :: String.t) :: String.t
  def final_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func finalString(s: String): String {

    }
}
```

