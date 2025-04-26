# 3084. 统计以给定字符开头和结尾的子字符串总数

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符 <code>c </code>。返回在字符串 <code>s</code> 中并且以 <code>c</code> 字符开头和结尾的<span data-keyword="substring-nonempty">非空子字符串</span>的总数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "abada", c = "a"</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">6</span></p>

<p><strong>解释：</strong>以 <code>"a"</code> 开头和结尾的子字符串有： <code>"<strong><u>a</u></strong>bada"</code>、<code>"<u><strong>aba</strong></u>da"</code>、<code>"<u><strong>abada</strong></u>"</code>、<code>"ab<u><strong>a</strong></u>da"</code>、<code>"ab<u><strong>ada</strong></u>"</code>、<code>"abad<u><strong>a</strong></u>"</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">s = "zzz", c = "z"</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">6</span></p>

<p><strong>解释：</strong>字符串 <code>s</code> 中总共有 <code>6</code> 个子字符串，并且它们都以 <code>"z"</code> 开头和结尾。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>c</code> 均由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串
- 计数

## 提示

1. Count the number of characters <code>'c'</code> in string <code>s</code>, let’s call it <code>m</code>.
2. We can select <code>2</code> numbers <code>i</code> and <code>j</code> such that <code>i <= j</code> are the start and end indices of substring. Note that <code>i</code> and <code>j</code> can be the same.
3. The answer is <code>m * (m + 1) / 2</code>.

## 示例

```
"abada"
"a"
"zzz"
"z"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countSubstrings(string s, char c) {
        
    }
};
```

### Java

```java
class Solution {
    public long countSubstrings(String s, char c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        
```

### C

```c
long long countSubstrings(char* s, char c) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountSubstrings(string s, char c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {character} c
 * @return {number}
 */
var countSubstrings = function(s, c) {
    
};
```

### TypeScript

```typescript
function countSubstrings(s: string, c: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $c
     * @return Integer
     */
    function countSubstrings($s, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubstrings(_ s: String, _ c: Character) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubstrings(s: String, c: Char): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubstrings(String s, String c) {
    
  }
}
```

### Go

```golang
func countSubstrings(s string, c byte) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Character} c
# @return {Integer}
def count_substrings(s, c)
    
end
```

### Scala

```scala
object Solution {
    def countSubstrings(s: String, c: Char): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_substrings(s: String, c: char) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-substrings s c)
  (-> string? char? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_substrings(S :: unicode:unicode_binary(), C :: char()) -> integer().
count_substrings(S, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_substrings(s :: String.t, c :: char) :: integer
  def count_substrings(s, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubstrings(s: String, c: Rune): Int64 {

    }
}
```

