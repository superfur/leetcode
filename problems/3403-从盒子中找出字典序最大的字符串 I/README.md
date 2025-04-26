# 3403. 从盒子中找出字典序最大的字符串 I

## 题目描述

<p>给你一个字符串 <code>word</code> 和一个整数 <code>numFriends</code>。</p>

<p>Alice 正在为她的 <code>numFriends</code> 位朋友组织一个游戏。游戏分为多个回合，在每一回合中：</p>

<ul>
	<li><code>word</code> 被分割成 <code>numFriends</code> 个&nbsp;<strong>非空&nbsp;</strong>字符串，且该分割方式与之前的任意回合所采用的都 <strong>不完全相同&nbsp;</strong>。</li>
	<li>所有分割出的字符串都会被放入一个盒子中。</li>
</ul>

<p>在所有回合结束后，找出盒子中&nbsp;<span data-keyword="lexicographically-smaller-string">字典序最大的&nbsp;</span>字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">word = "dbca", numFriends = 2</span></p>

<p><strong>输出:</strong> <span class="example-io">"dbc"</span></p>

<p><strong>解释:</strong>&nbsp;</p>

<p>所有可能的分割方式为：</p>

<ul>
	<li><code>"d"</code> 和 <code>"bca"</code>。</li>
	<li><code>"db"</code> 和 <code>"ca"</code>。</li>
	<li><code>"dbc"</code> 和 <code>"a"</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">word = "gggg", numFriends = 4</span></p>

<p><strong>输出:</strong> <span class="example-io">"g"</span></p>

<p><strong>解释:</strong>&nbsp;</p>

<p>唯一可能的分割方式为：<code>"g"</code>, <code>"g"</code>, <code>"g"</code>, 和 <code>"g"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= word.length &lt;= 5&nbsp;* 10<sup>3</sup></code></li>
	<li><code>word</code> 仅由小写英文字母组成。</li>
	<li><code>1 &lt;= numFriends &lt;= word.length</code></li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串
- 枚举

## 提示

1. Find lexicographically largest substring of size <code>n - numFriends + 1</code> or less starting at every index.

## 示例

```
"dbca"
2
"gggg"
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string answerString(string word, int numFriends) {
        
    }
};
```

### Java

```java
class Solution {
    public String answerString(String word, int numFriends) {
        
    }
}
```

### Python

```python
class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
```

### C

```c
char* answerString(char* word, int numFriends) {
    
}
```

### C#

```csharp
public class Solution {
    public string AnswerString(string word, int numFriends) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @param {number} numFriends
 * @return {string}
 */
var answerString = function(word, numFriends) {
    
};
```

### TypeScript

```typescript
function answerString(word: string, numFriends: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @param Integer $numFriends
     * @return String
     */
    function answerString($word, $numFriends) {
        
    }
}
```

### Swift

```swift
class Solution {
    func answerString(_ word: String, _ numFriends: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun answerString(word: String, numFriends: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String answerString(String word, int numFriends) {
    
  }
}
```

### Go

```golang
func answerString(word string, numFriends int) string {
    
}
```

### Ruby

```ruby
# @param {String} word
# @param {Integer} num_friends
# @return {String}
def answer_string(word, num_friends)
    
end
```

### Scala

```scala
object Solution {
    def answerString(word: String, numFriends: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn answer_string(word: String, num_friends: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (answer-string word numFriends)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec answer_string(Word :: unicode:unicode_binary(), NumFriends :: integer()) -> unicode:unicode_binary().
answer_string(Word, NumFriends) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec answer_string(word :: String.t, num_friends :: integer) :: String.t
  def answer_string(word, num_friends) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func answerString(word: String, numFriends: Int64): String {

    }
}
```

