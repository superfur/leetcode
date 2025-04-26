# 2284. 最多单词数的发件人

## 题目描述

<p>给你一个聊天记录，共包含 <code>n</code>&nbsp;条信息。给你两个字符串数组&nbsp;<code>messages</code> 和&nbsp;<code>senders</code>&nbsp;，其中&nbsp;<code>messages[i]</code>&nbsp;是&nbsp;<code>senders[i]</code>&nbsp;发出的一条&nbsp;<strong>信息</strong>&nbsp;。</p>

<p>一条 <strong>信息</strong>&nbsp;是若干用单个空格连接的 <strong>单词</strong>&nbsp;，信息开头和结尾不会有多余空格。发件人的 <strong>单词计数</strong>&nbsp;是这个发件人总共发出的 <strong>单词数</strong>&nbsp;。注意，一个发件人可能会发出多于一条信息。</p>

<p>请你返回发出单词数 <strong>最多</strong>&nbsp;的发件人名字。如果有多个发件人发出最多单词数，请你返回 <strong>字典序</strong>&nbsp;最大的名字。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>字典序里，大写字母小于小写字母。</li>
	<li><code>"Alice"</code> 和&nbsp;<code>"alice"</code>&nbsp;是不同的名字。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"], senders = ["Alice","userTwo","userThree","Alice"]
<b>输出：</b>"Alice"
<b>解释：</b>Alice 总共发出了 2 + 3 = 5 个单词。
userTwo 发出了 2 个单词。
userThree 发出了 3 个单词。
由于 Alice 发出单词数最多，所以我们返回 "Alice" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>messages = ["How is leetcode for everyone","Leetcode is useful for practice"], senders = ["Bob","Charlie"]
<b>输出：</b>"Charlie"
<b>解释：</b>Bob 总共发出了 5 个单词。
Charlie 总共发出了 5 个单词。
由于最多单词数打平，返回字典序最大的名字，也就是 Charlie 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == messages.length == senders.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= messages[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= senders[i].length &lt;= 10</code></li>
	<li><code>messages[i]</code>&nbsp;包含大写字母、小写字母和&nbsp;<code>' '</code>&nbsp;。</li>
	<li><code>messages[i]</code>&nbsp;中所有单词都由 <strong>单个空格</strong>&nbsp;隔开。</li>
	<li><code>messages[i]</code>&nbsp;不包含前导和后缀空格。</li>
	<li><code>senders[i]</code>&nbsp;只包含大写英文字母和小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 计数

## 提示

1. The number of words in a message is equal to the number of spaces + 1.
2. Use a hash map to count the total number of words from each sender.

## 示例

```
["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
["Alice","userTwo","userThree","Alice"]
["How is leetcode for everyone","Leetcode is useful for practice"]
["Bob","Charlie"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestWordCount(vector<string>& messages, vector<string>& senders) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestWordCount(String[] messages, String[] senders) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestWordCount(self, messages, senders):
        """
        :type messages: List[str]
        :type senders: List[str]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        
```

### C

```c
char* largestWordCount(char** messages, int messagesSize, char** senders, int sendersSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestWordCount(string[] messages, string[] senders) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} messages
 * @param {string[]} senders
 * @return {string}
 */
var largestWordCount = function(messages, senders) {
    
};
```

### TypeScript

```typescript
function largestWordCount(messages: string[], senders: string[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $messages
     * @param String[] $senders
     * @return String
     */
    function largestWordCount($messages, $senders) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestWordCount(_ messages: [String], _ senders: [String]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestWordCount(messages: Array<String>, senders: Array<String>): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestWordCount(List<String> messages, List<String> senders) {
    
  }
}
```

### Go

```golang
func largestWordCount(messages []string, senders []string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} messages
# @param {String[]} senders
# @return {String}
def largest_word_count(messages, senders)
    
end
```

### Scala

```scala
object Solution {
    def largestWordCount(messages: Array[String], senders: Array[String]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_word_count(messages: Vec<String>, senders: Vec<String>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-word-count messages senders)
  (-> (listof string?) (listof string?) string?)
  )
```

### Erlang

```erlang
-spec largest_word_count(Messages :: [unicode:unicode_binary()], Senders :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
largest_word_count(Messages, Senders) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_word_count(messages :: [String.t], senders :: [String.t]) :: String.t
  def largest_word_count(messages, senders) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestWordCount(messages: Array<String>, senders: Array<String>): String {

    }
}
```

