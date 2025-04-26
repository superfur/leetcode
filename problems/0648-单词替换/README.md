# 648. 单词替换

## 题目描述

<p>在英语中，我们有一个叫做&nbsp;<strong>词根</strong>(root) 的概念，可以词根&nbsp;<strong>后面&nbsp;</strong>添加其他一些词组成另一个较长的单词——我们称这个词为 <strong>衍生词</strong>&nbsp;(<strong>derivative</strong>)。例如，词根&nbsp;<code>help</code>，跟随着 <strong>继承</strong>词&nbsp;<code>"ful"</code>，可以形成新的单词&nbsp;<code>"helpful"</code>。</p>

<p>现在，给定一个由许多&nbsp;<strong>词根&nbsp;</strong>组成的词典 <code>dictionary</code> 和一个用空格分隔单词形成的句子 <code>sentence</code>。你需要将句子中的所有&nbsp;<strong>衍生词&nbsp;</strong>用&nbsp;<strong>词根&nbsp;</strong>替换掉。如果&nbsp;<strong>衍生词&nbsp;</strong>有许多可以形成它的&nbsp;<strong>词根</strong>，则用&nbsp;<strong>最短&nbsp;</strong>的 <strong>词根</strong> 替换它。</p>

<p>你需要输出替换之后的句子。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
<strong>输出：</strong>"the cat was rat by the bat"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
<strong>输出：</strong>"a a b c"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= dictionary.length&nbsp;&lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code>&nbsp;仅由小写字母组成。</li>
	<li><code>1 &lt;= sentence.length &lt;= 10<sup>6</sup></code></li>
	<li><code>sentence</code>&nbsp;仅由小写字母和空格组成。</li>
	<li><code>sentence</code> 中单词的总量在范围 <code>[1, 1000]</code> 内。</li>
	<li><code>sentence</code> 中每个单词的长度在范围 <code>[1, 1000]</code> 内。</li>
	<li><code>sentence</code> 中单词之间由一个空格隔开。</li>
	<li><code>sentence</code>&nbsp;没有前导或尾随空格。</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串

## 示例

```
["cat","bat","rat"]
"the cattle was rattled by the battery"
["a","b","c"]
"aadsfasf absbs bbab cadsfafs"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string replaceWords(vector<string>& dictionary, string sentence) {
        
    }
};
```

### Java

```java
class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        
    }
}
```

### Python

```python
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
```

### C

```c
char* replaceWords(char** dictionary, int dictionarySize, char* sentence) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReplaceWords(IList<string> dictionary, string sentence) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {string}
 */
var replaceWords = function(dictionary, sentence) {
    
};
```

### TypeScript

```typescript
function replaceWords(dictionary: string[], sentence: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $dictionary
     * @param String $sentence
     * @return String
     */
    function replaceWords($dictionary, $sentence) {
        
    }
}
```

### Swift

```swift
class Solution {
    func replaceWords(_ dictionary: [String], _ sentence: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun replaceWords(dictionary: List<String>, sentence: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String replaceWords(List<String> dictionary, String sentence) {
    
  }
}
```

### Go

```golang
func replaceWords(dictionary []string, sentence string) string {
    
}
```

### Ruby

```ruby
# @param {String[]} dictionary
# @param {String} sentence
# @return {String}
def replace_words(dictionary, sentence)
    
end
```

### Scala

```scala
object Solution {
    def replaceWords(dictionary: List[String], sentence: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (replace-words dictionary sentence)
  (-> (listof string?) string? string?)
  )
```

### Erlang

```erlang
-spec replace_words(Dictionary :: [unicode:unicode_binary()], Sentence :: unicode:unicode_binary()) -> unicode:unicode_binary().
replace_words(Dictionary, Sentence) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec replace_words(dictionary :: [String.t], sentence :: String.t) :: String.t
  def replace_words(dictionary, sentence) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func replaceWords(dictionary: ArrayList<String>, sentence: String): String {

    }
}
```

