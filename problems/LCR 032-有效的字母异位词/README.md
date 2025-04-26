# LCR 032. 有效的字母异位词

## 题目描述

<p>给定两个字符串 <code>s</code> 和 <code>t</code> ，编写一个函数来判断它们是不是一组变位词（字母异位词）。</p>

<p><strong>注意：</strong>若&nbsp;<code><em>s</em></code> 和 <code><em>t</em></code><em>&nbsp;</em>中每个字符出现的次数都相同且<strong>字符顺序不完全相同</strong>，则称&nbsp;<code><em>s</em></code> 和 <code><em>t</em></code><em>&nbsp;</em>互为变位词（字母异位词）。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "anagram", t = "nagaram"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "rat", t = "car"
<strong>输出：</strong>false</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "a", t = "a"
<strong>输出：</strong>false</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code>&nbsp;和&nbsp;<code>t</code>&nbsp;仅包含小写字母</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶:&nbsp;</strong>如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？</p>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 242&nbsp;题相似（字母异位词定义不同）：<a href="https://leetcode-cn.com/problems/valid-anagram/">https://leetcode-cn.com/problems/valid-anagram/</a></p>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 排序

## 示例

```
"anagram"
"nagaram"
"rat"
"car"
"a"
"a"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {

    }
};
```

### Java

```java
class Solution {
    public boolean isAnagram(String s, String t) {

    }
}
```

### Python

```python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
```

### Python3

```python3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
```

### C

```c


bool isAnagram(char * s, char * t){

}
```

### C#

```csharp
public class Solution {
    public bool IsAnagram(string s, string t) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {

};
```

### TypeScript

```typescript
function isAnagram(s: string, t: string): boolean {

};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isAnagram($s, $t) {

    }
}
```

### Swift

```swift
class Solution {
    func isAnagram(_ s: String, _ t: String) -> Bool {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isAnagram(s: String, t: String): Boolean {

    }
}
```

### Go

```golang
func isAnagram(s string, t string) bool {

}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_anagram(s, t)

end
```

### Scala

```scala
object Solution {
    def isAnagram(s: String, t: String): Boolean = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

    }
}
```

### Racket

```racket
(define/contract (is-anagram s t)
  (-> string? string? boolean?)

  )
```

### Erlang

```erlang
-spec is_anagram(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_anagram(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
  def is_anagram(s, t) do

  end
end
```

