# LCR 181. 字符串中的单词反转

## 题目描述

<p>你在与一位习惯从右往左阅读的朋友发消息，他发出的文字顺序都与正常相反但单词内容正确，为了和他顺利交流你决定写一个转换程序，把他所发的消息 <code>message</code> 转换为正常语序。</p>

<p>注意：输入字符串 <code>message</code> 中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> message = "<code>the sky is blue</code>"
<strong>输出:&nbsp;</strong>"<code>blue is sky the</code>"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入:</strong> message = " &nbsp;hello world! &nbsp;"
<strong>输出:&nbsp;</strong>"world! hello"
<strong>解释: </strong>输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入:</strong> message = "a good &nbsp; example"
<strong>输出:&nbsp;</strong>"example good a"
<strong>解释: </strong>如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= message.length &lt;= 10<sup>4</sup></code></li>
	<li><code>message</code> 中包含英文大小写字母、空格和数字</li>
</ul>

<p><strong>注意：</strong></p>

<ul>
	<li>本题与主站 151 题相同：<a href="https://leetcode-cn.com/problems/reverse-words-in-a-string/">https://leetcode-cn.com/problems/reverse-words-in-a-string/</a></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 示例

```
"the sky is blue"
"  hello world!  "
"a good   example"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reverseMessage(string message) {
        
    }
};
```

### Java

```java
class Solution {
    public String reverseMessage(String message) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseMessage(self, message):
        """
        :type message: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reverseMessage(self, message: str) -> str:
        
```

### C

```c
char* reverseMessage(char* message) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReverseMessage(string message) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} message
 * @return {string}
 */
var reverseMessage = function(message) {
    
};
```

### TypeScript

```typescript
function reverseMessage(message: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $message
     * @return String
     */
    function reverseMessage($message) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseMessage(_ message: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseMessage(message: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reverseMessage(String message) {
    
  }
}
```

### Go

```golang
func reverseMessage(message string) string {
    
}
```

### Ruby

```ruby
# @param {String} message
# @return {String}
def reverse_message(message)
    
end
```

### Scala

```scala
object Solution {
    def reverseMessage(message: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_message(message: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-message message)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reverse_message(Message :: unicode:unicode_binary()) -> unicode:unicode_binary().
reverse_message(Message) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_message(message :: String.t) :: String.t
  def reverse_message(message) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseMessage(message: String): String {

    }
}
```

