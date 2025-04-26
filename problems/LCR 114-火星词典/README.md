# LCR 114. 火星词典

## 题目描述

<p>现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。</p>

<p>给定一个字符串列表 <code>words</code> ，作为这门语言的词典，<code>words</code> 中的字符串已经 <strong>按这门新语言的字母顺序进行了排序</strong> 。</p>

<p>请你根据该词典还原出此语言中已知的字母顺序，并 <strong>按字母递增顺序</strong> 排列。若不存在合法字母顺序，返回 <code>&quot;&quot;</code> 。若存在多种可能的合法字母顺序，返回其中 <strong>任意一种</strong> 顺序即可。</p>

<p>字符串 <code>s</code> <strong>字典顺序小于</strong> 字符串 <code>t</code> 有两种情况：</p>

<ul>
	<li>在第一个不同字母处，如果 <code>s</code> 中的字母在这门外星语言的字母顺序中位于 <code>t</code> 中字母之前，那么&nbsp;<code>s</code> 的字典顺序小于 <code>t</code> 。</li>
	<li>如果前面 <code>min(s.length, t.length)</code> 字母都相同，那么 <code>s.length &lt; t.length</code> 时，<code>s</code> 的字典顺序也小于 <code>t</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;wrt&quot;,&quot;wrf&quot;,&quot;er&quot;,&quot;ett&quot;,&quot;rftt&quot;]
<strong>输出：</strong>&quot;wertf&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;z&quot;,&quot;x&quot;]
<strong>输出：</strong>&quot;zx&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>words = [&quot;z&quot;,&quot;x&quot;,&quot;z&quot;]
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>不存在合法字母顺序，因此返回 &quot;&quot;。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 269&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/alien-dictionary/">https://leetcode-cn.com/problems/alien-dictionary/</a></p>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序
- 数组
- 字符串

## 示例

```
["wrt","wrf","er","ett","rftt"]
["z","x"]
["z","x","z"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {

    }
};
```

### Java

```java
class Solution {
    public String alienOrder(String[] words) {

    }
}
```

### Python

```python
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
```

### Python3

```python3
class Solution:
    def alienOrder(self, words: List[str]) -> str:
```

### C

```c


char * alienOrder(char ** words, int wordsSize){

}
```

### C#

```csharp
public class Solution {
    public string AlienOrder(string[] words) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @return {string}
 */
var alienOrder = function(words) {

};
```

### TypeScript

```typescript
function alienOrder(words: string[]): string {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @return String
     */
    function alienOrder($words) {

    }
}
```

### Swift

```swift
class Solution {
    func alienOrder(_ words: [String]) -> String {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun alienOrder(words: Array<String>): String {

    }
}
```

### Go

```golang
func alienOrder(words []string) string {

}
```

### Ruby

```ruby
# @param {String[]} words
# @return {String}
def alien_order(words)

end
```

### Scala

```scala
object Solution {
    def alienOrder(words: Array[String]): String = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn alien_order(words: Vec<String>) -> String {

    }
}
```

### Racket

```racket
(define/contract (alien-order words)
  (-> (listof string?) string?)

  )
```

### Erlang

```erlang
-spec alien_order(Words :: [unicode:unicode_binary()]) -> unicode:unicode_binary().
alien_order(Words) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec alien_order(words :: [String.t]) :: String.t
  def alien_order(words) do

  end
end
```

