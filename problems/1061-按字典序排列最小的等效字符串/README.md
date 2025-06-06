# 1061. 按字典序排列最小的等效字符串

## 题目描述

<p>给出长度相同的两个字符串<code>s1</code> 和&nbsp;<code>s2</code>&nbsp;，还有一个字符串&nbsp;<code>baseStr</code>&nbsp;。</p>

<p>其中 &nbsp;<code>s1[i]</code>&nbsp;和&nbsp;<code>s2[i]</code>&nbsp; 是一组等价字符。</p>

<ul>
	<li>举个例子，如果&nbsp;<code>s1 = "abc"</code> 且&nbsp;<code>s2 = "cde"</code>，那么就有&nbsp;<code>'a' == 'c', 'b' == 'd', 'c' == 'e'</code>。</li>
</ul>

<p>等价字符遵循任何等价关系的一般规则：</p>

<ul>
	<li><strong>&nbsp;自反性&nbsp;</strong>：<code>'a' == 'a'</code></li>
	<li>&nbsp;<strong>对称性&nbsp;</strong>：<code>'a' == 'b'</code> 则必定有 <code>'b' == 'a'</code></li>
	<li>&nbsp;<strong>传递性</strong> ：<code>'a' == 'b'</code> 且 <code>'b' == 'c'</code> 就表明 <code>'a' == 'c'</code></li>
</ul>

<p>例如，&nbsp;<code>s1 = "abc"</code>&nbsp;和&nbsp;<code>s2 = "cde"</code>&nbsp;的等价信息和之前的例子一样，那么&nbsp;<code>baseStr = "eed"</code>&nbsp;, <code>"acd"</code>&nbsp;或&nbsp;<code>"aab"</code>，这三个字符串都是等价的，而&nbsp;<code>"aab"</code>&nbsp;是&nbsp;<code>baseStr</code>&nbsp;的按字典序最小的等价字符串</p>

<p>利用<em>&nbsp;</em><code>s1</code>&nbsp;和&nbsp;<code>s2</code>&nbsp;的等价信息，找出并返回<em>&nbsp;</em><code>baseStr</code><em>&nbsp;</em>的按字典序排列最小的等价字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s1 = "parker", s2 = "morris", baseStr = "parser"
<strong>输出：</strong>"makkek"
<strong>解释：</strong>根据 <code>A</code> 和 <code>B 中的等价信息，</code>我们可以将这些字符分为 <code>[m,p]</code>, <code>[a,o]</code>, <code>[k,r,s]</code>, <code>[e,i] 共 4 组</code>。每组中的字符都是等价的，并按字典序排列。所以答案是 <code>"makkek"</code>。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s1 = "hello", s2 = "world", baseStr = "hold"
<strong>输出：</strong>"hdld"
<strong>解释：</strong>根据 <code>A</code> 和 <code>B 中的等价信息，</code>我们可以将这些字符分为 <code>[h,w]</code>, <code>[d,e,o]</code>, <code>[l,r] 共 3 组</code>。所以只有 S 中的第二个字符 <code>'o'</code> 变成 <code>'d'，最后答案为 </code><code>"hdld"</code>。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
<strong>输出：</strong>"aauaaaaada"
<strong>解释：</strong>我们可以把 A 和 B 中的等价字符分为 <code>[a,o,e,r,s,c]</code>, <code>[l,p]</code>, <code>[g,t]</code> 和 <code>[d,m] 共 4 组</code>，因此 <code>S</code> 中除了 <code>'u'</code> 和 <code>'d'</code> 之外的所有字母都转化成了 <code>'a'</code>，最后答案为 <code>"aauaaaaada"</code>。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s1.length, s2.length, baseStr &lt;= 1000</code></li>
	<li><code>s1.length == s2.length</code></li>
	<li>字符串<code>s1</code>,&nbsp;<code>s2</code>, and&nbsp;<code>baseStr</code>&nbsp;仅由从&nbsp;<code>'a'</code> 到&nbsp;<code>'z'</code>&nbsp;的小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 并查集
- 字符串

## 提示

1. Model these equalities as edges of a graph.
2. Group each connected component of the graph and assign each node of this component to the node with the lowest lexicographically character.
3. Finally convert the string with the precalculated information.

## 示例

```
"parker"
"morris"
"parser"
"hello"
"world"
"hold"
"leetcode"
"programs"
"sourcecode"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
```

### C

```c
char* smallestEquivalentString(char* s1, char* s2, char* baseStr) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestEquivalentString(string s1, string s2, string baseStr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s1
 * @param {string} s2
 * @param {string} baseStr
 * @return {string}
 */
var smallestEquivalentString = function(s1, s2, baseStr) {
    
};
```

### TypeScript

```typescript
function smallestEquivalentString(s1: string, s2: string, baseStr: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s1
     * @param String $s2
     * @param String $baseStr
     * @return String
     */
    function smallestEquivalentString($s1, $s2, $baseStr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestEquivalentString(_ s1: String, _ s2: String, _ baseStr: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestEquivalentString(s1: String, s2: String, baseStr: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestEquivalentString(String s1, String s2, String baseStr) {
    
  }
}
```

### Go

```golang
func smallestEquivalentString(s1 string, s2 string, baseStr string) string {
    
}
```

### Ruby

```ruby
# @param {String} s1
# @param {String} s2
# @param {String} base_str
# @return {String}
def smallest_equivalent_string(s1, s2, base_str)
    
end
```

### Scala

```scala
object Solution {
    def smallestEquivalentString(s1: String, s2: String, baseStr: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-equivalent-string s1 s2 baseStr)
  (-> string? string? string? string?)
  )
```

### Erlang

```erlang
-spec smallest_equivalent_string(S1 :: unicode:unicode_binary(), S2 :: unicode:unicode_binary(), BaseStr :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_equivalent_string(S1, S2, BaseStr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_equivalent_string(s1 :: String.t, s2 :: String.t, base_str :: String.t) :: String.t
  def smallest_equivalent_string(s1, s2, base_str) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestEquivalentString(s1: String, s2: String, baseStr: String): String {

    }
}
```

