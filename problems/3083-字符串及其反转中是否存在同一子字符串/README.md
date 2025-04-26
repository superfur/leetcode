# 3083. 字符串及其反转中是否存在同一子字符串

## 题目描述

<p>给你一个字符串 <code>s</code> ，请你判断字符串 <code>s</code> 是否存在一个长度为 <code>2</code> 的子字符串，在 <code>s</code> 反转后的字符串中也出现。</p>

<p>如果存在这样的子字符串，返回 <code>true</code>；如果不存在，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "leetcode"</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">true</span></p>

<p><strong>解释：</strong>子字符串 <code>"ee"</code> 的长度为 <code>2</code>，它也出现在 <code>reverse(s) == "edocteel"</code> 中。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "abcba"</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">true</span></p>

<p><strong>解释：</strong>所有长度为 <code>2</code> 的子字符串 <code>"ab"</code>、<code>"bc"</code>、<code>"cb"</code>、<code>"ba"</code> 也都出现在 <code>reverse(s) == "abcba"</code> 中。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "abcd"</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">false</span></p>

<p><strong>解释：</strong>字符串 <code>s</code> 中不存在满足「在其反转后的字符串中也出现」且长度为 <code>2</code> 的子字符串。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li>字符串 <code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Make a new string by reversing the string <code>s</code>.
2. For every substring of length <code>2</code> in <code>s</code>, check if there is a corresponding substring in the reverse of <code>s</code>.

## 示例

```
"leetcode"
"abcba"
"abcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isSubstringPresent(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isSubstringPresent(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        
```

### C

```c
bool isSubstringPresent(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsSubstringPresent(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {boolean}
 */
var isSubstringPresent = function(s) {
    
};
```

### TypeScript

```typescript
function isSubstringPresent(s: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Boolean
     */
    function isSubstringPresent($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isSubstringPresent(_ s: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isSubstringPresent(s: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isSubstringPresent(String s) {
    
  }
}
```

### Go

```golang
func isSubstringPresent(s string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Boolean}
def is_substring_present(s)
    
end
```

### Scala

```scala
object Solution {
    def isSubstringPresent(s: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_substring_present(s: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-substring-present s)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_substring_present(S :: unicode:unicode_binary()) -> boolean().
is_substring_present(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_substring_present(s :: String.t) :: boolean
  def is_substring_present(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isSubstringPresent(s: String): Bool {

    }
}
```

