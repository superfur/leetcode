# LCR 137. 模糊搜索验证

## 题目描述

<p>请设计一个程序来支持用户在文本编辑器中的模糊搜索功能。用户输入内容中可能使用到如下两种通配符：</p>

<ul>
	<li><code>'.'</code> 匹配任意单个字符。</li>
	<li><code>'*'</code> 匹配零个或多个前面的那一个元素。</li>
</ul>

<p>&nbsp;</p>

<p>请返回用户输入内容 <code>input</code> 所有字符是否可以匹配原文字符串 <code>article</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>article = "aa", input = "a"
<strong>输出：</strong>false
<strong>解释：</strong>"a" 无法匹配 "aa" 整个字符串。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>article = "aa", input = "a*"
<strong>输出：</strong>true
<strong>解释：</strong>因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
</pre>

<p><strong>示例&nbsp;3：</strong></p>

<pre>
<strong>输入：</strong>article = "ab", input = ".*"
<strong>输出：</strong>true
<strong>解释：</strong>".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= article.length &lt;= 20</code></li>
	<li><code>1 &lt;= input.length &lt;= 20</code></li>
	<li><code>article</code> 只包含从 <code>a-z</code> 的小写字母。</li>
	<li><code>input</code> 只包含从 <code>a-z</code> 的小写字母，以及字符 <code>.</code> 和 <code>*</code> 。</li>
	<li>保证每次出现字符 <code>*</code> 时，前面都匹配到有效的字符</li>
</ul>

<p>&nbsp;</p>

<p>注意：本题与主站 10&nbsp;题相同：<a href="https://leetcode-cn.com/problems/regular-expression-matching/">https://leetcode-cn.com/problems/regular-expression-matching/</a></p>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 递归
- 字符串
- 动态规划

## 示例

```
"aa"
"a"
"aa"
"a*"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool articleMatch(string s, string p) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean articleMatch(String s, String p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def articleMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def articleMatch(self, s: str, p: str) -> bool:
        
```

### C

```c
bool articleMatch(char* s, char* p) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ArticleMatch(string s, string p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var articleMatch = function(s, p) {
    
};
```

### TypeScript

```typescript
function articleMatch(s: string, p: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $p
     * @return Boolean
     */
    function articleMatch($s, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func articleMatch(_ s: String, _ p: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun articleMatch(s: String, p: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool articleMatch(String s, String p) {
    
  }
}
```

### Go

```golang
func articleMatch(s string, p string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} p
# @return {Boolean}
def article_match(s, p)
    
end
```

### Scala

```scala
object Solution {
    def articleMatch(s: String, p: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn article_match(s: String, p: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (article-match s p)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec article_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
article_match(S, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec article_match(s :: String.t, p :: String.t) :: boolean
  def article_match(s, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func articleMatch(s: String, p: String): Bool {

    }
}
```

