# 686. 重复叠加字符串匹配

## 题目描述

<p>给定两个字符串&nbsp;<code>a</code> 和 <code>b</code>，寻找重复叠加字符串 <code>a</code> 的最小次数，使得字符串 <code>b</code> 成为叠加后的字符串 <code>a</code> 的子串，如果不存在则返回 <code>-1</code>。</p>

<p><strong>注意：</strong>字符串 <code>&quot;abc&quot;</code>&nbsp;重复叠加 0 次是 <code>&quot;&quot;</code>，重复叠加 1 次是&nbsp;<code>&quot;abc&quot;</code>，重复叠加 2 次是&nbsp;<code>&quot;abcabc&quot;</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>a = &quot;abcd&quot;, b = &quot;cdabcdab&quot;
<strong>输出：</strong>3
<strong>解释：</strong>a 重复叠加三遍后为 &quot;ab<strong>cdabcdab</strong>cd&quot;, 此时 b 是其子串。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>a = &quot;a&quot;, b = &quot;aa&quot;
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>a = &quot;a&quot;, b = &quot;a&quot;
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>a = &quot;abc&quot;, b = &quot;wxyz&quot;
<strong>输出：</strong>-1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= b.length &lt;= 10<sup>4</sup></code></li>
	<li><code>a</code> 和 <code>b</code> 由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 字符串匹配

## 示例

```
"abcd"
"cdabcdab"
"a"
"aa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int repeatedStringMatch(string a, string b) {
        
    }
};
```

### Java

```java
class Solution {
    public int repeatedStringMatch(String a, String b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
```

### C

```c
int repeatedStringMatch(char* a, char* b) {
    
}
```

### C#

```csharp
public class Solution {
    public int RepeatedStringMatch(string a, string b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var repeatedStringMatch = function(a, b) {
    
};
```

### TypeScript

```typescript
function repeatedStringMatch(a: string, b: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $a
     * @param String $b
     * @return Integer
     */
    function repeatedStringMatch($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func repeatedStringMatch(_ a: String, _ b: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun repeatedStringMatch(a: String, b: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int repeatedStringMatch(String a, String b) {
    
  }
}
```

### Go

```golang
func repeatedStringMatch(a string, b string) int {
    
}
```

### Ruby

```ruby
# @param {String} a
# @param {String} b
# @return {Integer}
def repeated_string_match(a, b)
    
end
```

### Scala

```scala
object Solution {
    def repeatedStringMatch(a: String, b: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn repeated_string_match(a: String, b: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (repeated-string-match a b)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec repeated_string_match(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> integer().
repeated_string_match(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec repeated_string_match(a :: String.t, b :: String.t) :: integer
  def repeated_string_match(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func repeatedStringMatch(a: String, b: String): Int64 {

    }
}
```

