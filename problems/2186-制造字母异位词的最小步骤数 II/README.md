# 2186. 制造字母异位词的最小步骤数 II

## 题目描述

<p>给你两个字符串 <code>s</code> 和 <code>t</code> 。在一步操作中，你可以给 <code>s</code> 或者 <code>t</code> 追加 <strong>任一字符</strong> 。</p>

<p>返回使 <code>s</code> 和 <code>t</code> 互为 <strong>字母异位词</strong> 所需的最少步骤数<em>。</em></p>

<p><strong>字母异位词 </strong>指字母相同但是顺序不同（或者相同）的字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "<em><strong>lee</strong>t</em>co<em><strong>de</strong></em>", t = "co<em><strong>a</strong></em>t<em><strong>s</strong></em>"
<strong>输出：</strong>7
<strong>解释：</strong>
- 执行 2 步操作，将 "as" 追加到 s = "leetcode" 中，得到 s = "leetcode<em><strong>as</strong></em>" 。
- 执行 5 步操作，将 "leede" 追加到 t = "coats" 中，得到 t = "coats<em><strong>leede</strong></em>" 。
"leetcodeas" 和 "coatsleede" 互为字母异位词。
总共用去 2 + 5 = 7 步。
可以证明，无法用少于 7 步操作使这两个字符串互为字母异位词。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "night", t = "thing"
<strong>输出：</strong>0
<strong>解释：</strong>给出的字符串已经互为字母异位词。因此，不需要任何进一步操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 由小写英文字符组成</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 计数

## 提示

1. Notice that for anagrams, the order of the letters is irrelevant.
2. For each letter, we can count its frequency in s and t.
3. For each letter, its contribution to the answer is the absolute difference between its frequency in s and t.

## 示例

```
"leetcode"
"coats"
"night"
"thing"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSteps(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSteps(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
```

### C

```c
int minSteps(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSteps(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {number}
 */
var minSteps = function(s, t) {
    
};
```

### TypeScript

```typescript
function minSteps(s: string, t: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Integer
     */
    function minSteps($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSteps(_ s: String, _ t: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSteps(s: String, t: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSteps(String s, String t) {
    
  }
}
```

### Go

```golang
func minSteps(s string, t string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Integer}
def min_steps(s, t)
    
end
```

### Scala

```scala
object Solution {
    def minSteps(s: String, t: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_steps(s: String, t: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-steps s t)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_steps(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> integer().
min_steps(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_steps(s :: String.t, t :: String.t) :: integer
  def min_steps(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSteps(s: String, t: String): Int64 {

    }
}
```

