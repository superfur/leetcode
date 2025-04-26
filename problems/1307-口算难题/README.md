# 1307. 口算难题

## 题目描述

<p>给你一个方程，左边用&nbsp;<code>words</code>&nbsp;表示，右边用&nbsp;<code>result</code> 表示。</p>

<p>你需要根据以下规则检查方程是否可解：</p>

<ul>
	<li>每个字符都会被解码成一位数字（0 - 9）。</li>
	<li>每对不同的字符必须映射到不同的数字。</li>
	<li>每个 <code>words[i]</code> 和 <code>result</code>&nbsp;都会被解码成一个没有前导零的数字。</li>
	<li>左侧数字之和（<code>words</code>）等于右侧数字（<code>result</code>）。&nbsp;</li>
</ul>

<p>如果方程可解，返回&nbsp;<code>True</code>，否则返回&nbsp;<code>False</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = [&quot;SEND&quot;,&quot;MORE&quot;], result = &quot;MONEY&quot;
<strong>输出：</strong>true
<strong>解释：</strong>映射 &#39;S&#39;-&gt; 9, &#39;E&#39;-&gt;5, &#39;N&#39;-&gt;6, &#39;D&#39;-&gt;7, &#39;M&#39;-&gt;1, &#39;O&#39;-&gt;0, &#39;R&#39;-&gt;8, &#39;Y&#39;-&gt;&#39;2&#39;
所以 &quot;SEND&quot; + &quot;MORE&quot; = &quot;MONEY&quot; ,  9567 + 1085 = 10652</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = [&quot;SIX&quot;,&quot;SEVEN&quot;,&quot;SEVEN&quot;], result = &quot;TWENTY&quot;
<strong>输出：</strong>true
<strong>解释：</strong>映射 &#39;S&#39;-&gt; 6, &#39;I&#39;-&gt;5, &#39;X&#39;-&gt;0, &#39;E&#39;-&gt;8, &#39;V&#39;-&gt;7, &#39;N&#39;-&gt;2, &#39;T&#39;-&gt;1, &#39;W&#39;-&gt;&#39;3&#39;, &#39;Y&#39;-&gt;4
所以 &quot;SIX&quot; + &quot;SEVEN&quot; + &quot;SEVEN&quot; = &quot;TWENTY&quot; ,  650 + 68782 + 68782 = 138214</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>words = [&quot;THIS&quot;,&quot;IS&quot;,&quot;TOO&quot;], result = &quot;FUNNY&quot;
<strong>输出：</strong>true
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>words = [&quot;LEET&quot;,&quot;CODE&quot;], result = &quot;POINT&quot;
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= words.length &lt;= 5</code></li>
	<li><code>1 &lt;= words[i].length,&nbsp;results.length&nbsp;&lt;= 7</code></li>
	<li><code>words[i], result</code>&nbsp;只含有大写英文字母</li>
	<li>表达式中使用的不同字符数最大为&nbsp;10</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 字符串
- 回溯

## 提示

1. Use Backtracking and pruning to solve this problem.
2. If you set the values of some digits (from right to left), the other digits will be constrained.

## 示例

```
["SEND","MORE"]
"MONEY"
["SIX","SEVEN","SEVEN"]
"TWENTY"
["LEET","CODE"]
"POINT"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isSolvable(vector<string>& words, string result) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isSolvable(String[] words, String result) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isSolvable(self, words, result):
        """
        :type words: List[str]
        :type result: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        
```

### C

```c
bool isSolvable(char** words, int wordsSize, char* result) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsSolvable(string[] words, string result) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} result
 * @return {boolean}
 */
var isSolvable = function(words, result) {
    
};
```

### TypeScript

```typescript
function isSolvable(words: string[], result: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $result
     * @return Boolean
     */
    function isSolvable($words, $result) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isSolvable(_ words: [String], _ result: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isSolvable(words: Array<String>, result: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isSolvable(List<String> words, String result) {
    
  }
}
```

### Go

```golang
func isSolvable(words []string, result string) bool {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} result
# @return {Boolean}
def is_solvable(words, result)
    
end
```

### Scala

```scala
object Solution {
    def isSolvable(words: Array[String], result: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_solvable(words: Vec<String>, result: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-solvable words result)
  (-> (listof string?) string? boolean?)
  )
```

### Erlang

```erlang
-spec is_solvable(Words :: [unicode:unicode_binary()], Result :: unicode:unicode_binary()) -> boolean().
is_solvable(Words, Result) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_solvable(words :: [String.t], result :: String.t) :: boolean
  def is_solvable(words, result) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isSolvable(words: Array<String>, result: String): Bool {

    }
}
```

