# 3365. 重排子字符串以形成目标字符串

## 题目描述

<p>给你两个字符串 <code>s</code> 和 <code>t</code>（它们互为字母异位词），以及一个整数 <code>k</code>。</p>

<p>你的任务是判断是否可以将字符串 <code>s</code> 分割成 <code>k</code> 个等长的子字符串，然后重新排列这些子字符串，并以任意顺序连接它们，使得最终得到的新字符串与给定的字符串 <code>t</code> 相匹配。</p>

<p>如果可以做到，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p><strong>字母异位词&nbsp;</strong>是指由另一个单词或短语的所有字母重新排列形成的单词或短语，使用所有原始字母恰好一次。</p>

<p><strong>子字符串&nbsp;</strong>是字符串中的一个连续&nbsp;<b>非空&nbsp;</b>字符序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abcd", t = "cdab", k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将 <code>s</code> 分割成 2 个长度为 2 的子字符串：<code>["ab", "cd"]</code>。</li>
	<li>重新排列这些子字符串为 <code>["cd", "ab"]</code>，然后连接它们得到 <code>"cdab"</code>，与 <code>t</code> 相匹配。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aabbcc", t = "bbaacc", k = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将 <code>s</code> 分割成 3 个长度为 2 的子字符串：<code>["aa", "bb", "cc"]</code>。</li>
	<li>重新排列这些子字符串为 <code>["bb", "aa", "cc"]</code>，然后连接它们得到 <code>"bbaacc"</code>，与 <code>t</code> 相匹配。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aabbcc", t = "bbaacc", k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将 <code>s</code> 分割成 2 个长度为 3 的子字符串：<code>["aab", "bcc"]</code>。</li>
	<li>这些子字符串无法重新排列形成 <code>t = "bbaacc"</code>，所以输出 <code>false</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length == t.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
	<li><code>s.length</code> 能被 <code>k</code> 整除。</li>
	<li><code>s</code> 和 <code>t</code> 仅由小写英文字母组成。</li>
	<li>输入保证 <code>s</code> 和 <code>t</code> 互为字母异位词。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 排序

## 提示

1. Split <code>s</code> into <code>k</code> equal-sized substrings, use a map to track frequencies, and check if rearranging them can form <code>t</code>.

## 示例

```
"abcd"
"cdab"
2
"aabbcc"
"bbaacc"
3
"aabbcc"
"bbaacc"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPossibleToRearrange(string s, string t, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPossibleToRearrange(String s, String t, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPossibleToRearrange(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        
```

### C

```c
bool isPossibleToRearrange(char* s, char* t, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPossibleToRearrange(string s, string t, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @param {number} k
 * @return {boolean}
 */
var isPossibleToRearrange = function(s, t, k) {
    
};
```

### TypeScript

```typescript
function isPossibleToRearrange(s: string, t: string, k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @param Integer $k
     * @return Boolean
     */
    function isPossibleToRearrange($s, $t, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPossibleToRearrange(_ s: String, _ t: String, _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPossibleToRearrange(s: String, t: String, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPossibleToRearrange(String s, String t, int k) {
    
  }
}
```

### Go

```golang
func isPossibleToRearrange(s string, t string, k int) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @param {Integer} k
# @return {Boolean}
def is_possible_to_rearrange(s, t, k)
    
end
```

### Scala

```scala
object Solution {
    def isPossibleToRearrange(s: String, t: String, k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_possible_to_rearrange(s: String, t: String, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-possible-to-rearrange s t k)
  (-> string? string? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_possible_to_rearrange(S :: unicode:unicode_binary(), T :: unicode:unicode_binary(), K :: integer()) -> boolean().
is_possible_to_rearrange(S, T, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_possible_to_rearrange(s :: String.t, t :: String.t, k :: integer) :: boolean
  def is_possible_to_rearrange(s, t, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPossibleToRearrange(s: String, t: String, k: Int64): Bool {

    }
}
```

