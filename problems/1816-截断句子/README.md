# 1816. 截断句子

## 题目描述

<p><strong>句子</strong> 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。</p>

<ul>
	<li>例如，<code>"Hello World"</code>、<code>"HELLO"</code> 和 <code>"hello world hello world"</code> 都是句子。</li>
</ul>

<p>给你一个句子 <code>s</code>​​​​​​ 和一个整数 <code>k</code>​​​​​​ ，请你将 <code>s</code>​​ <strong>截断</strong> ​，​​​使截断后的句子仅含 <strong>前</strong> <code>k</code>​​​​​​ 个单词。返回 <strong>截断</strong> <code>s</code>​​​​<em>​​ </em>后得到的句子<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "Hello how are you Contestant", k = 4
<strong>输出：</strong>"Hello how are you"
<strong>解释：</strong>
s 中的单词为 ["Hello", "how" "are", "you", "Contestant"]
前 4 个单词为 ["Hello", "how", "are", "you"]
因此，应当返回 "Hello how are you"
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "What is the solution to this problem", k = 4
<strong>输出：</strong>"What is the solution"
<strong>解释：</strong>
s 中的单词为 ["What", "is" "the", "solution", "to", "this", "problem"]
前 4 个单词为 ["What", "is", "the", "solution"]
因此，应当返回 "What is the solution"</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = "chopper is not a tanuki", k = 5
<strong>输出：</strong>"chopper is not a tanuki"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>k</code> 的取值范围是 <code>[1,  s 中单词的数目]</code></li>
	<li><code>s</code> 仅由大小写英文字母和空格组成</li>
	<li><code>s</code> 中的单词之间由单个空格隔开</li>
	<li>不存在前导或尾随空格</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. It's easier to solve this problem on an array of strings so parse the string to an array of words
2. After return the first k words as a sentence

## 示例

```
"Hello how are you Contestant"
4
"What is the solution to this problem"
4
"chopper is not a tanuki"
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string truncateSentence(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String truncateSentence(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
```

### C

```c
char* truncateSentence(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string TruncateSentence(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var truncateSentence = function(s, k) {
    
};
```

### TypeScript

```typescript
function truncateSentence(s: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function truncateSentence($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func truncateSentence(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun truncateSentence(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String truncateSentence(String s, int k) {
    
  }
}
```

### Go

```golang
func truncateSentence(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def truncate_sentence(s, k)
    
end
```

### Scala

```scala
object Solution {
    def truncateSentence(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (truncate-sentence s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec truncate_sentence(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
truncate_sentence(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec truncate_sentence(s :: String.t, k :: integer) :: String.t
  def truncate_sentence(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func truncateSentence(s: String, k: Int64): String {

    }
}
```

