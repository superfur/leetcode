# 44. 通配符匹配

## 题目描述

<div class="title__3Vvk">给你一个输入字符串 (<code>s</code>) 和一个字符模式 (<code>p</code>) ，请你实现一个支持 <code>'?'</code> 和 <code>'*'</code> 匹配规则的通配符匹配：</div>

<ul>
	<li class="title__3Vvk"><code>'?'</code> 可以匹配任何单个字符。</li>
	<li class="title__3Vvk"><code>'*'</code> 可以匹配任意字符序列（包括空字符序列）。</li>
</ul>

<div class="original__bRMd">
<div>
<p>判定匹配成功的充要条件是：字符模式必须能够 <strong>完全匹配</strong> 输入字符串（而不是部分匹配）。</p>
</div>
</div>
&nbsp;

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "aa", p = "a"
<strong>输出：</strong>false
<strong>解释：</strong>"a" 无法匹配 "aa" 整个字符串。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "aa", p = "*"
<strong>输出：</strong>true
<strong>解释：</strong>'*' 可以匹配任意字符串。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "cb", p = "?a"
<strong>输出：</strong>false
<strong>解释：</strong>'?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length, p.length &lt;= 2000</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
	<li><code>p</code> 仅由小写英文字母、<code>'?'</code> 或 <code>'*'</code> 组成</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 递归
- 字符串
- 动态规划

## 示例

```
"aa"
"a"
"aa"
"*"
"cb"
"?a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isMatch(String s, String p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
```

### C

```c
bool isMatch(char* s, char* p) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsMatch(string s, string p) {
        
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
var isMatch = function(s, p) {
    
};
```

### TypeScript

```typescript
function isMatch(s: string, p: string): boolean {
    
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
    function isMatch($s, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isMatch(s: String, p: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isMatch(String s, String p) {
    
  }
}
```

### Go

```golang
func isMatch(s string, p string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} p
# @return {Boolean}
def is_match(s, p)
    
end
```

### Scala

```scala
object Solution {
    def isMatch(s: String, p: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-match s p)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_match(S :: unicode:unicode_binary(), P :: unicode:unicode_binary()) -> boolean().
is_match(S, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_match(s :: String.t, p :: String.t) :: boolean
  def is_match(s, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isMatch(s: String, p: String): Bool {

    }
}
```

