# LCR 063. 单词替换

## 题目描述

<p>在英语中，有一个叫做&nbsp;<code>词根(root)</code> 的概念，它可以跟着其他一些词组成另一个较长的单词&mdash;&mdash;我们称这个词为&nbsp;<code>继承词(successor)</code>。例如，词根<code>an</code>，跟随着单词&nbsp;<code>other</code>(其他)，可以形成新的单词&nbsp;<code>another</code>(另一个)。</p>

<p>现在，给定一个由许多词根组成的词典和一个句子，需要将句子中的所有<code>继承词</code>用<code>词根</code>替换掉。如果<code>继承词</code>有许多可以形成它的<code>词根</code>，则用最短的词根替换它。</p>

<p>需要输出替换之后的句子。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;cat&quot;,&quot;bat&quot;,&quot;rat&quot;], sentence = &quot;the cattle was rattled by the battery&quot;
<strong>输出：</strong>&quot;the cat was rat by the bat&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;a&quot;,&quot;b&quot;,&quot;c&quot;], sentence = &quot;aadsfasf absbs bbab cadsfafs&quot;
<strong>输出：</strong>&quot;a a b c&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;a&quot;, &quot;aa&quot;, &quot;aaa&quot;, &quot;aaaa&quot;], sentence = &quot;a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa&quot;
<strong>输出：</strong>&quot;a a a a a a a a bbb baba a&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;catt&quot;,&quot;cat&quot;,&quot;bat&quot;,&quot;rat&quot;], sentence = &quot;the cattle was rattled by the battery&quot;
<strong>输出：</strong>&quot;the cat was rat by the bat&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>dictionary = [&quot;ac&quot;,&quot;ab&quot;], sentence = &quot;it is abnormal that this solution is accepted&quot;
<strong>输出：</strong>&quot;it is ab that this solution is ac&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= dictionary.length&nbsp;&lt;= 1000</code></li>
	<li><code>1 &lt;= dictionary[i].length &lt;= 100</code></li>
	<li><code>dictionary[i]</code>&nbsp;仅由小写字母组成。</li>
	<li><code>1 &lt;= sentence.length &lt;= 10^6</code></li>
	<li><code>sentence</code>&nbsp;仅由小写字母和空格组成。</li>
	<li><code>sentence</code> 中单词的总量在范围 <code>[1, 1000]</code> 内。</li>
	<li><code>sentence</code> 中每个单词的长度在范围 <code>[1, 1000]</code> 内。</li>
	<li><code>sentence</code> 中单词之间由一个空格隔开。</li>
	<li><code>sentence</code>&nbsp;没有前导或尾随空格。</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 648&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/replace-words/">https://leetcode-cn.com/problems/replace-words/</a></p>


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
["a", "aa", "aaa", "aaaa"]
"a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
["catt","cat","bat","rat"]
"the cattle was rattled by the battery"
["ac","ab"]
"it is abnormal that this solution is accepted"
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


char * replaceWords(char ** dictionary, int dictionarySize, char * sentence){

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

