# 面试题 17.13. 恢复空格

## 题目描述

<p>哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子<code>&quot;I reset the computer. It still didn&rsquo;t boot!&quot;</code>已经变成了<code>&quot;iresetthecomputeritstilldidntboot&quot;</code>。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典<code>dictionary</code>，不过，有些词没在词典里。假设文章用<code>sentence</code>表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。</p>

<p><strong>注意：</strong>本题相对原题稍作改动，只需返回未识别的字符数</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>
dictionary = [&quot;looked&quot;,&quot;just&quot;,&quot;like&quot;,&quot;her&quot;,&quot;brother&quot;]
sentence = &quot;jesslookedjustliketimherbrother&quot;
<strong>输出：</strong> 7
<strong>解释：</strong> 断句后为&quot;<strong>jess</strong> looked just like <strong>tim</strong> her brother&quot;，共7个未识别字符。
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= len(sentence) &lt;= 1000</code></li>
	<li><code>dictionary</code>中总字符数不超过 150000。</li>
	<li>你可以认为<code>dictionary</code>和<code>sentence</code>中只包含小写字母。</li>
</ul>


## 难度

Medium

## 标签

- 字典树
- 数组
- 哈希表
- 字符串
- 动态规划
- 哈希函数
- 滚动哈希

## 提示

1. 试试递归方法。
2. 你能把所有的可能性都试一试吗？那会是什么样子？
3. 你可以用两种方法中的一种来考虑递归算法：(1)对于每个字符，我应该在这里放一个空格吗？(2)下一个空格应该放在哪里？两种方案都可以递归地解决。
4. 递归算法是否会反复遇到相同的子问题？你能用一个散列表进行优化吗？
5. 在现实生活中，我们知道有些路径不会构成一个词。例如，没有以hellothisism开头的单词。能在明知行不通的情况下提前终止吗？
6. 如果想提前终止，可以试一试trie。

## 示例

```
["looked","just","like","her","brother"]
"jesslookedjustliketimherbrother"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int respace(vector<string>& dictionary, string sentence) {
        
    }
};
```

### Java

```java
class Solution {
    public int respace(String[] dictionary, String sentence) {
        
    }
}
```

### Python

```python
class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        
```

### C

```c
int respace(char** dictionary, int dictionarySize, char* sentence) {
    
}
```

### C#

```csharp
public class Solution {
    public int Respace(string[] dictionary, string sentence) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} dictionary
 * @param {string} sentence
 * @return {number}
 */
var respace = function(dictionary, sentence) {
    
};
```

### TypeScript

```typescript
function respace(dictionary: string[], sentence: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $dictionary
     * @param String $sentence
     * @return Integer
     */
    function respace($dictionary, $sentence) {
        
    }
}
```

### Swift

```swift
class Solution {
    func respace(_ dictionary: [String], _ sentence: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun respace(dictionary: Array<String>, sentence: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int respace(List<String> dictionary, String sentence) {
    
  }
}
```

### Go

```golang
func respace(dictionary []string, sentence string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} dictionary
# @param {String} sentence
# @return {Integer}
def respace(dictionary, sentence)
    
end
```

### Scala

```scala
object Solution {
    def respace(dictionary: Array[String], sentence: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn respace(dictionary: Vec<String>, sentence: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (respace dictionary sentence)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec respace(Dictionary :: [unicode:unicode_binary()], Sentence :: unicode:unicode_binary()) -> integer().
respace(Dictionary, Sentence) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec respace(dictionary :: [String.t], sentence :: String.t) :: integer
  def respace(dictionary, sentence) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func respace(dictionary: Array<String>, sentence: String): Int64 {

    }
}
```

