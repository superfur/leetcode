# 面试题 16.18. 模式匹配

## 题目描述

<p>你有两个字符串，即<code>pattern</code>和<code>value</code>。 <code>pattern</code>字符串由字母<code>&quot;a&quot;</code>和<code>&quot;b&quot;</code>组成，用于描述字符串中的模式。例如，字符串<code>&quot;catcatgocatgo&quot;</code>匹配模式<code>&quot;aabab&quot;</code>（其中<code>&quot;cat&quot;</code>是<code>&quot;a&quot;</code>，<code>&quot;go&quot;</code>是<code>&quot;b&quot;</code>），该字符串也匹配像<code>&quot;a&quot;</code>、<code>&quot;ab&quot;</code>和<code>&quot;b&quot;</code>这样的模式。但需注意<code>&quot;a&quot;</code>和<code>&quot;b&quot;</code>不能同时表示相同的字符串。编写一个方法判断<code>value</code>字符串是否匹配<code>pattern</code>字符串。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> pattern = &quot;abba&quot;, value = &quot;dogcatcatdog&quot;
<strong>输出：</strong> true
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> pattern = &quot;abba&quot;, value = &quot;dogcatcatfish&quot;
<strong>输出：</strong> false
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong> pattern = &quot;aaaa&quot;, value = &quot;dogcatcatdog&quot;
<strong>输出：</strong> false
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong> pattern = &quot;abba&quot;, value = &quot;dogdogdogdog&quot;
<strong>输出：</strong> true
<strong>解释：</strong> &quot;a&quot;=&quot;dogdog&quot;,b=&quot;&quot;，反之也符合规则
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= len(pattern) &lt;= 1000</code></li>
	<li><code>0 &lt;= len(value) &lt;= 1000</code></li>
	<li>你可以假设<code>pattern</code>只包含字母<code>&quot;a&quot;</code>和<code>&quot;b&quot;</code>，<code>value</code>仅包含小写字母。</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串
- 回溯
- 枚举

## 提示

1. 从蛮力解法开始。你能试一下a和b的所有可能性吗?
2. 观察其中一个子字符串，a或b都可以，必须从字符串的开头开始。这减少了可能性的种类。
3. 不要忘记处理pattern中的第一个字符是b的可能性。
4. 谨慎地选择分析时间复杂度的方式。如果遍历O(n2)个子字符串，每个子字符串都进行O(n)次的字符串比较，那么总体运行时间为O(n3)。
5. 假设你确定了一个模式中“a”部分的值。b有多少种可能性?
6. 由于a的值决定b的值（反之亦然），并且a或b必须出现于值的起始处，所以你应该只有O(n)种可能来分解模式串。
7. 你应该能够有一个O(n2)的算法。

## 示例

```
"abba"
"dogcatcatdog"
"abba"
"dogcatcatfish"
"aaaa"
"dogcatcatdog"
"abba"
"dogdogdogdog"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool patternMatching(string pattern, string value) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean patternMatching(String pattern, String value) {
        
    }
}
```

### Python

```python
class Solution(object):
    def patternMatching(self, pattern, value):
        """
        :type pattern: str
        :type value: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        
```

### C

```c
bool patternMatching(char* pattern, char* value) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PatternMatching(string pattern, string value) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} pattern
 * @param {string} value
 * @return {boolean}
 */
var patternMatching = function(pattern, value) {
    
};
```

### TypeScript

```typescript
function patternMatching(pattern: string, value: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $pattern
     * @param String $value
     * @return Boolean
     */
    function patternMatching($pattern, $value) {
        
    }
}
```

### Swift

```swift
class Solution {
    func patternMatching(_ pattern: String, _ value: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun patternMatching(pattern: String, value: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool patternMatching(String pattern, String value) {
    
  }
}
```

### Go

```golang
func patternMatching(pattern string, value string) bool {
    
}
```

### Ruby

```ruby
# @param {String} pattern
# @param {String} value
# @return {Boolean}
def pattern_matching(pattern, value)
    
end
```

### Scala

```scala
object Solution {
    def patternMatching(pattern: String, value: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pattern_matching(pattern: String, value: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (pattern-matching pattern value)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec pattern_matching(Pattern :: unicode:unicode_binary(), Value :: unicode:unicode_binary()) -> boolean().
pattern_matching(Pattern, Value) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pattern_matching(pattern :: String.t, value :: String.t) :: boolean
  def pattern_matching(pattern, value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func patternMatching(pattern: String, value: String): Bool {

    }
}
```

