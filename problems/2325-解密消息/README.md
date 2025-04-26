# 2325. 解密消息

## 题目描述

<p>给你字符串 <code>key</code> 和 <code>message</code> ，分别表示一个加密密钥和一段加密消息。解密 <code>message</code> 的步骤如下：</p>

<ol>
	<li>使用 <code>key</code> 中 26 个英文小写字母第一次出现的顺序作为替换表中的字母 <strong>顺序</strong> 。</li>
	<li>将替换表与普通英文字母表对齐，形成对照表。</li>
	<li>按照对照表 <strong>替换</strong> <code>message</code> 中的每个字母。</li>
	<li>空格 <code>' '</code> 保持不变。</li>
</ol>

<ul>
	<li>例如，<code>key = "<em><strong>hap</strong></em>p<em><strong>y</strong></em> <em><strong>bo</strong></em>y"</code>（实际的加密密钥会包含字母表中每个字母 <strong>至少一次</strong>），据此，可以得到部分对照表（<code>'h' -&gt; 'a'</code>、<code>'a' -&gt; 'b'</code>、<code>'p' -&gt; 'c'</code>、<code>'y' -&gt; 'd'</code>、<code>'b' -&gt; 'e'</code>、<code>'o' -&gt; 'f'</code>）。</li>
</ul>

<p>返回解密后的消息。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/08/ex1new4.jpg" style="width: 752px; height: 150px;" /></p>

<pre>
<strong>输入：</strong>key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
<strong>输出：</strong>"this is a secret"
<strong>解释：</strong>对照表如上图所示。
提取 "<em><strong>the</strong></em> <em><strong>quick</strong></em> <em><strong>brown</strong></em> <em><strong>f</strong></em>o<em><strong>x</strong></em> <em><strong>j</strong></em>u<em><strong>mps</strong></em> o<em><strong>v</strong></em>er the <em><strong>lazy</strong></em> <em><strong>d</strong></em>o<em><strong>g</strong></em>" 中每个字母的首次出现可以得到替换表。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/05/08/ex2new.jpg" style="width: 754px; height: 150px;" /></p>

<pre>
<strong>输入：</strong>key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
<strong>输出：</strong>"the five boxing wizards jump quickly"
<strong>解释：</strong>对照表如上图所示。
提取 "<em><strong>eljuxhpwnyrdgtqkviszcfmabo</strong></em>" 中每个字母的首次出现可以得到替换表。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>26 &lt;= key.length &lt;= 2000</code></li>
	<li><code>key</code> 由小写英文字母及 <code>' '</code> 组成</li>
	<li><code>key</code> 包含英文字母表中每个字符（<code>'a'</code> 到 <code>'z'</code>）<strong>至少一次</strong></li>
	<li><code>1 &lt;= message.length &lt;= 2000</code></li>
	<li><code>message</code> 由小写英文字母和 <code>' '</code> 组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Iterate through the characters in the key to construct a mapping to the English alphabet.
2. Make sure to check that the current character is not already in the mapping (only the first appearance is considered).
3. Map the characters in the message according to the constructed mapping.

## 示例

```
"the quick brown fox jumps over the lazy dog"
"vkbs bs t suepuv"
"eljuxhpwnyrdgtqkviszcfmabo"
"zwx hnfx lqantp mnoeius ycgk vcnjrdb"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string decodeMessage(string key, string message) {
        
    }
};
```

### Java

```java
class Solution {
    public String decodeMessage(String key, String message) {
        
    }
}
```

### Python

```python
class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
```

### C

```c
char* decodeMessage(char* key, char* message) {
    
}
```

### C#

```csharp
public class Solution {
    public string DecodeMessage(string key, string message) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} key
 * @param {string} message
 * @return {string}
 */
var decodeMessage = function(key, message) {
    
};
```

### TypeScript

```typescript
function decodeMessage(key: string, message: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $key
     * @param String $message
     * @return String
     */
    function decodeMessage($key, $message) {
        
    }
}
```

### Swift

```swift
class Solution {
    func decodeMessage(_ key: String, _ message: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun decodeMessage(key: String, message: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String decodeMessage(String key, String message) {
    
  }
}
```

### Go

```golang
func decodeMessage(key string, message string) string {
    
}
```

### Ruby

```ruby
# @param {String} key
# @param {String} message
# @return {String}
def decode_message(key, message)
    
end
```

### Scala

```scala
object Solution {
    def decodeMessage(key: String, message: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn decode_message(key: String, message: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (decode-message key message)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec decode_message(Key :: unicode:unicode_binary(), Message :: unicode:unicode_binary()) -> unicode:unicode_binary().
decode_message(Key, Message) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec decode_message(key :: String.t, message :: String.t) :: String.t
  def decode_message(key, message) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func decodeMessage(key: String, message: String): String {

    }
}
```

