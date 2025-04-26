# 1358. 包含所有三种字符的子字符串数目

## 题目描述

<p>给你一个字符串 <code>s</code>&nbsp;，它只包含三种字符 a, b 和 c 。</p>

<p>请你返回 a，b 和 c 都&nbsp;<strong>至少&nbsp;</strong>出现过一次的子字符串数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = &quot;abcabc&quot;
<strong>输出：</strong>10
<strong>解释：</strong>包含 a，b 和 c 各至少一次的子字符串为<em> &quot;</em>abc<em>&quot;, &quot;</em>abca<em>&quot;, &quot;</em>abcab<em>&quot;, &quot;</em>abcabc<em>&quot;, &quot;</em>bca<em>&quot;, &quot;</em>bcab<em>&quot;, &quot;</em>bcabc<em>&quot;, &quot;</em>cab<em>&quot;, &quot;</em>cabc<em>&quot; </em>和<em> &quot;</em>abc<em>&quot; </em>(<strong>相同</strong><strong>字符串算多次</strong>)<em>。</em>
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = &quot;aaacb&quot;
<strong>输出：</strong>3
<strong>解释：</strong>包含 a，b 和 c 各至少一次的子字符串为<em> &quot;</em>aaacb<em>&quot;, &quot;</em>aacb<em>&quot; </em>和<em> &quot;</em>acb<em>&quot; 。</em>
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>s = &quot;abc&quot;
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 5 x 10^4</code></li>
	<li><code>s</code>&nbsp;只包含字符 a，b 和 c 。</li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 字符串
- 滑动窗口

## 提示

1. For each position we simply need to find the first occurrence of a/b/c on or after this position.
2. So we can pre-compute three link-list of indices of each a, b, and c.

## 示例

```
"abcabc"
"aaacb"
"abc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
```

### C

```c
int numberOfSubstrings(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function numberOfSubstrings(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function numberOfSubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSubstrings(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSubstrings(String s) {
    
  }
}
```

### Go

```golang
func numberOfSubstrings(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def number_of_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSubstrings(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-substrings s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_substrings(S :: unicode:unicode_binary()) -> integer().
number_of_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_substrings(s :: String.t) :: integer
  def number_of_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSubstrings(s: String): Int64 {

    }
}
```

