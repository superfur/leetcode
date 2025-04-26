# 1417. 重新格式化字符串

## 题目描述

<p>给你一个混合了数字和字母的字符串 <code>s</code>，其中的字母均为小写英文字母。</p>

<p>请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。</p>

<p>请你返回 <strong>重新格式化后</strong> 的字符串；如果无法按要求重新格式化，则返回一个 <strong>空字符串</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;a0b1c2&quot;
<strong>输出：</strong>&quot;0a1b2c&quot;
<strong>解释：</strong>&quot;0a1b2c&quot; 中任意两个相邻字符的类型都不同。 &quot;a0b1c2&quot;, &quot;0a1b2c&quot;, &quot;0c2a1b&quot; 也是满足题目要求的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;leetcode&quot;
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>&quot;leetcode&quot; 中只有字母，所以无法满足重新格式化的条件。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;1229857369&quot;
<strong>输出：</strong>&quot;&quot;
<strong>解释：</strong>&quot;1229857369&quot; 中只有数字，所以无法满足重新格式化的条件。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>s = &quot;covid2019&quot;
<strong>输出：</strong>&quot;c2o0v1i9d&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>s = &quot;ab123&quot;
<strong>输出：</strong>&quot;1a2b3&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> 仅由小写英文字母和/或数字组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Count the number of letters and digits in the string. if cntLetters - cntDigits has any of the values [-1, 0, 1] we have an answer, otherwise we don't have any answer.
2. Build the string anyway as you wish. Keep in mind that you need to start with the type that have more characters if cntLetters ≠ cntDigits.

## 示例

```
"a0b1c2"
"leetcode"
"1229857369"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string reformat(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String reformat(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def reformat(self, s: str) -> str:
        
```

### C

```c
char* reformat(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string Reformat(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var reformat = function(s) {
    
};
```

### TypeScript

```typescript
function reformat(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function reformat($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reformat(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reformat(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String reformat(String s) {
    
  }
}
```

### Go

```golang
func reformat(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def reformat(s)
    
end
```

### Scala

```scala
object Solution {
    def reformat(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reformat(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (reformat s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec reformat(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
reformat(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reformat(s :: String.t) :: String.t
  def reformat(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reformat(s: String): String {

    }
}
```

