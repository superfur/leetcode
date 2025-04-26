# 1657. 确定两个字符串是否接近

## 题目描述

<p>如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 <strong>接近</strong> ：</p>

<ul>
	<li>操作 1：交换任意两个 <strong>现有</strong> 字符。

	<ul>
		<li>例如，<code>a<u>b</u>cd<u>e</u> -&gt; a<u>e</u>cd<u>b</u></code></li>
	</ul>
	</li>
	<li>操作 2：将一个 <strong>现有</strong> 字符的每次出现转换为另一个 <strong>现有</strong> 字符，并对另一个字符执行相同的操作。
	<ul>
		<li>例如，<code><u>aa</u>c<u>abb</u> -&gt; <u>bb</u>c<u>baa</u></code>（所有 <code>a</code> 转化为 <code>b</code> ，而所有的 <code>b</code> 转换为 <code>a</code> ）</li>
	</ul>
	</li>
</ul>

<p>你可以根据需要对任意一个字符串多次使用这两种操作。</p>

<p>给你两个字符串，<code>word1</code> 和 <code>word2</code> 。如果<em> </em><code>word1</code><em> </em>和<em> </em><code>word2</code><em> </em><strong>接近 </strong>，就返回 <code>true</code> ；否则，返回<em> </em><code>false</code><em> </em>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word1 = "abc", word2 = "bca"
<strong>输出：</strong>true
<strong>解释：</strong>2 次操作从 word1 获得 word2 。
执行操作 1："a<u>bc</u>" -&gt; "a<u>cb</u>"
执行操作 1："<u>a</u>c<u>b</u>" -&gt; "<u>b</u>c<u>a</u>"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word1 = "a", word2 = "aa"
<strong>输出：</strong>false
<strong>解释：</strong>不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>word1 = "cabbba", word2 = "abbccc"
<strong>输出：</strong>true
<strong>解释：</strong>3 次操作从 word1 获得 word2 。
执行操作 1："ca<u>b</u>bb<u>a</u>" -&gt; "ca<u>a</u>bb<u>b</u>"
执行操作 2：<code>"</code><u>c</u>aa<u>bbb</u>" -&gt; "<u>b</u>aa<u>ccc</u>"
执行操作 2："<u>baa</u>ccc" -&gt; "<u>abb</u>ccc"
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= word1.length, word2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>word1</code> 和 <code>word2</code> 仅包含小写英文字母</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数
- 排序

## 提示

1. Operation 1 allows you to freely reorder the string.
2. Operation 2 allows you to freely reassign the letters' frequencies.

## 示例

```
"abc"
"bca"
"a"
"aa"
"cabbba"
"abbccc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool closeStrings(string word1, string word2) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean closeStrings(String word1, String word2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
```

### C

```c
bool closeStrings(char* word1, char* word2) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CloseStrings(string word1, string word2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word1
 * @param {string} word2
 * @return {boolean}
 */
var closeStrings = function(word1, word2) {
    
};
```

### TypeScript

```typescript
function closeStrings(word1: string, word2: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    function closeStrings($word1, $word2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closeStrings(_ word1: String, _ word2: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closeStrings(word1: String, word2: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool closeStrings(String word1, String word2) {
    
  }
}
```

### Go

```golang
func closeStrings(word1 string, word2 string) bool {
    
}
```

### Ruby

```ruby
# @param {String} word1
# @param {String} word2
# @return {Boolean}
def close_strings(word1, word2)
    
end
```

### Scala

```scala
object Solution {
    def closeStrings(word1: String, word2: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn close_strings(word1: String, word2: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (close-strings word1 word2)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec close_strings(Word1 :: unicode:unicode_binary(), Word2 :: unicode:unicode_binary()) -> boolean().
close_strings(Word1, Word2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec close_strings(word1 :: String.t, word2 :: String.t) :: boolean
  def close_strings(word1, word2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closeStrings(word1: String, word2: String): Bool {

    }
}
```

