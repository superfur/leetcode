# LCR 017. 最小覆盖子串

## 题目描述

<p>给定两个字符串 <code>s</code> 和&nbsp;<code>t</code> 。返回 <code>s</code> 中包含&nbsp;<code>t</code>&nbsp;的所有字符的最短子字符串。如果 <code>s</code> 中不存在符合条件的子字符串，则返回空字符串 <code>&quot;&quot;</code> 。</p>

<p>如果 <code>s</code> 中存在多个符合条件的子字符串，返回任意一个。</p>

<p>&nbsp;</p>

<p><strong>注意： </strong>对于 <code>t</code> 中重复字符，我们寻找的子字符串中该字符数量必须不少于 <code>t</code> 中该字符数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;ADOBECODEBANC&quot;, t = &quot;ABC&quot;
<strong>输出：</strong>&quot;BANC&quot; 
<strong>解释：</strong>最短子字符串 &quot;BANC&quot; 包含了字符串 t 的所有字符 &#39;A&#39;、&#39;B&#39;、&#39;C&#39;</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;a&quot;, t = &quot;a&quot;
<strong>输出：</strong>&quot;a&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = &quot;a&quot;, t = &quot;aa&quot;
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>t 中两个字符 &#39;a&#39; 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能设计一个在 <code>o(n)</code> 时间内解决此问题的算法吗？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 76&nbsp;题相似（本题答案不唯一）：<a href="https://leetcode-cn.com/problems/minimum-window-substring/">https://leetcode-cn.com/problems/minimum-window-substring/</a></p>


## 难度

Hard

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 示例

```
"ADOBECODEBANC"
"ABC"
"a"
"a"
"a"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string minWindow(string s, string t) {

    }
};
```

### Java

```java
class Solution {
    public String minWindow(String s, String t) {

    }
}
```

### Python

```python
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
```

### Python3

```python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
```

### C

```c


char * minWindow(char * s, char * t){

}
```

### C#

```csharp
public class Solution {
    public string MinWindow(string s, string t) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
var minWindow = function(s, t) {

};
```

### TypeScript

```typescript
function minWindow(s: string, t: string): string {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function minWindow($s, $t) {

    }
}
```

### Swift

```swift
class Solution {
    func minWindow(_ s: String, _ t: String) -> String {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minWindow(s: String, t: String): String {

    }
}
```

### Go

```golang
func minWindow(s string, t string) string {

}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {String}
def min_window(s, t)

end
```

### Scala

```scala
object Solution {
    def minWindow(s: String, t: String): String = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_window(s: String, t: String) -> String {

    }
}
```

### Racket

```racket
(define/contract (min-window s t)
  (-> string? string? string?)

  )
```

### Erlang

```erlang
-spec min_window(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> unicode:unicode_binary().
min_window(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_window(s :: String.t, t :: String.t) :: String.t
  def min_window(s, t) do

  end
end
```

