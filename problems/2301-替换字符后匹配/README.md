# 2301. 替换字符后匹配

## 题目描述

<p>给你两个字符串&nbsp;<code>s</code> 和&nbsp;<code>sub</code>&nbsp;。同时给你一个二维字符数组&nbsp;<code>mappings</code> ，其中&nbsp;<code>mappings[i] = [old<sub>i</sub>, new<sub>i</sub>]</code>&nbsp;表示你可以将&nbsp;<code>sub</code>&nbsp;中任意数目的&nbsp;<code>old<sub>i</sub></code>&nbsp;字符替换为&nbsp;<code>new<sub>i</sub></code>&nbsp;。<code>sub</code>&nbsp;中每个字符 <b>不能</b>&nbsp;被替换超过一次。</p>

<p>如果使用 <code>mappings</code>&nbsp;替换 0 个或者若干个字符，可以将 <code>sub</code>&nbsp;变成 <code>s</code>&nbsp;的一个子字符串，请你返回&nbsp;<code>true</code>，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>一个 <strong>子字符串</strong>&nbsp;是字符串中连续非空的字符序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
<b>输出：</b>true
<b>解释：</b>将 sub 中第一个 'e' 用 '3' 替换，将 't' 用 '7' 替换。
现在 sub = "l3e7" ，它是 s 的子字符串，所以我们返回 true 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>s = "fooleetbar", sub = "f00l", mappings = [["o","0"]]
<b>输出：</b>false
<b>解释：</b>字符串 "f00l" 不是 s 的子串且没有可以进行的修改。
注意我们不能用 'o' 替换 '0' 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>s = "Fool33tbaR", sub = "leetd", mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
<b>输出：</b>true
<b>解释：</b>将 sub 里第一个和第二个 'e' 用 '3' 替换，用 'b' 替换 sub 里的 'd' 。
得到 sub = "l33tb" ，它是 s 的子字符串，所以我们返回 true 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= sub.length &lt;= s.length &lt;= 5000</code></li>
	<li><code>0 &lt;= mappings.length &lt;= 1000</code></li>
	<li><code>mappings[i].length == 2</code></li>
	<li><code>old<sub>i</sub> != new<sub>i</sub></code></li>
	<li><code>s</code> 和&nbsp;<code>sub</code>&nbsp;只包含大写和小写英文字母和数字。</li>
	<li><code>old<sub>i</sub></code> 和&nbsp;<code>new<sub>i</sub></code>&nbsp;是大写、小写字母或者是个数字。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 字符串
- 字符串匹配

## 提示

1. Enumerate all substrings of s with the same length as sub, and compare each substring to sub for equality.
2. How can you quickly tell if a character of s can result from replacing the corresponding character in sub?

## 示例

```
"fool3e7bar"
"leet"
[["e","3"],["t","7"],["t","8"]]
"fooleetbar"
"f00l"
[["o","0"]]
"Fool33tbaR"
"leetd"
[["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool matchReplacement(string s, string sub, vector<vector<char>>& mappings) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean matchReplacement(String s, String sub, char[][] mappings) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matchReplacement(self, s, sub, mappings):
        """
        :type s: str
        :type sub: str
        :type mappings: List[List[str]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        
```

### C

```c
bool matchReplacement(char* s, char* sub, char** mappings, int mappingsSize, int* mappingsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool MatchReplacement(string s, string sub, char[][] mappings) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} sub
 * @param {character[][]} mappings
 * @return {boolean}
 */
var matchReplacement = function(s, sub, mappings) {
    
};
```

### TypeScript

```typescript
function matchReplacement(s: string, sub: string, mappings: string[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $sub
     * @param String[][] $mappings
     * @return Boolean
     */
    function matchReplacement($s, $sub, $mappings) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matchReplacement(_ s: String, _ sub: String, _ mappings: [[Character]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matchReplacement(s: String, sub: String, mappings: Array<CharArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool matchReplacement(String s, String sub, List<List<String>> mappings) {
    
  }
}
```

### Go

```golang
func matchReplacement(s string, sub string, mappings [][]byte) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} sub
# @param {Character[][]} mappings
# @return {Boolean}
def match_replacement(s, sub, mappings)
    
end
```

### Scala

```scala
object Solution {
    def matchReplacement(s: String, sub: String, mappings: Array[Array[Char]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn match_replacement(s: String, sub: String, mappings: Vec<Vec<char>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (match-replacement s sub mappings)
  (-> string? string? (listof (listof char?)) boolean?)
  )
```

### Erlang

```erlang
-spec match_replacement(S :: unicode:unicode_binary(), Sub :: unicode:unicode_binary(), Mappings :: [[char()]]) -> boolean().
match_replacement(S, Sub, Mappings) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec match_replacement(s :: String.t, sub :: String.t, mappings :: [[char]]) :: boolean
  def match_replacement(s, sub, mappings) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matchReplacement(s: String, sub: String, mappings: Array<Array<Rune>>): Bool {

    }
}
```

