# 299. 猜数字游戏

## 题目描述

<p>你在和朋友一起玩 <a href="https://baike.baidu.com/item/%E7%8C%9C%E6%95%B0%E5%AD%97/83200?fromtitle=Bulls+and+Cows&amp;fromid=12003488&amp;fr=aladdin" target="_blank">猜数字（Bulls and Cows）</a>游戏，该游戏规则如下：</p>

<p>写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：</p>

<ul>
	<li>猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛），</li>
	<li>有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。</li>
</ul>

<p>给你一个秘密数字&nbsp;<code>secret</code> 和朋友猜测的数字&nbsp;<code>guess</code> ，请你返回对朋友这次猜测的提示。</p>

<p>提示的格式为 <code>"xAyB"</code> ，<code>x</code> 是公牛个数， <code>y</code> 是奶牛个数，<code>A</code> 表示公牛，<code>B</code>&nbsp;表示奶牛。</p>

<p>请注意秘密数字和朋友猜测的数字都可能含有重复数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>secret = "1807", guess = "7810"
<strong>输出：</strong>"1A3B"
<strong>解释：</strong>数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1807"
  |
"<em><strong>7</strong></em>8<em><strong>10</strong></em>"</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>secret = "1123", guess = "0111"
<strong>输出：</strong>"1A1B"
<strong>解释：</strong>数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1123"        "1123"
  |      or     |
"01<em><strong>1</strong></em>1"        "011<em><strong>1</strong></em>"
注意，两个不匹配的 1 中，只有一个会算作奶牛（数字猜对位置不对）。通过重新排列非公牛数字，其中仅有一个 1 可以成为公牛数字。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= secret.length, guess.length &lt;= 1000</code></li>
	<li><code>secret.length == guess.length</code></li>
	<li><code>secret</code> 和 <code>guess</code> 仅由数字组成</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 示例

```
"1807"
"7810"
"1123"
"0111"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getHint(string secret, string guess) {
        
    }
};
```

### Java

```java
class Solution {
    public String getHint(String secret, String guess) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
```

### C

```c
char* getHint(char* secret, char* guess) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetHint(string secret, string guess) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    
};
```

### TypeScript

```typescript
function getHint(secret: string, guess: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $secret
     * @param String $guess
     * @return String
     */
    function getHint($secret, $guess) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getHint(_ secret: String, _ guess: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getHint(secret: String, guess: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getHint(String secret, String guess) {
    
  }
}
```

### Go

```golang
func getHint(secret string, guess string) string {
    
}
```

### Ruby

```ruby
# @param {String} secret
# @param {String} guess
# @return {String}
def get_hint(secret, guess)
    
end
```

### Scala

```scala
object Solution {
    def getHint(secret: String, guess: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_hint(secret: String, guess: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-hint secret guess)
  (-> string? string? string?)
  )
```

### Erlang

```erlang
-spec get_hint(Secret :: unicode:unicode_binary(), Guess :: unicode:unicode_binary()) -> unicode:unicode_binary().
get_hint(Secret, Guess) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_hint(secret :: String.t, guess :: String.t) :: String.t
  def get_hint(secret, guess) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getHint(secret: String, guess: String): String {

    }
}
```

