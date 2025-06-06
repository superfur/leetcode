# 2696. 删除子串后的字符串最小长度

## 题目描述

<p>给你一个仅由 <strong>大写</strong> 英文字符组成的字符串 <code>s</code> 。</p>

<p>你可以对此字符串执行一些操作，在每一步操作中，你可以从 <code>s</code> 中删除 <strong>任一个</strong> <code>"AB"</code> 或 <code>"CD"</code> 子字符串。</p>

<p>通过执行操作，删除所有&nbsp;<code>"AB"</code> 和 <code>"CD"</code> 子串，返回可获得的最终字符串的 <strong>最小</strong> 可能长度。</p>

<p><strong>注意</strong>，删除子串后，重新连接出的字符串可能会产生新的&nbsp;<code>"AB"</code> 或 <code>"CD"</code> 子串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ABFCACDB"
<strong>输出：</strong>2
<strong>解释：</strong>你可以执行下述操作：
- 从 "<em><strong>AB</strong></em>FCACDB" 中删除子串 "AB"，得到 s = "FCACDB" 。
- 从 "FCA<em><strong>CD</strong></em>B" 中删除子串 "CD"，得到 s = "FCAB" 。
- 从 "FC<strong><em>AB</em></strong>" 中删除子串 "AB"，得到 s = "FC" 。
最终字符串的长度为 2 。
可以证明 2 是可获得的最小长度。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "ACBBD"
<strong>输出：</strong>5
<strong>解释：</strong>无法执行操作，字符串长度不变。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由大写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 字符串
- 模拟

## 提示

1. Can we use brute force to solve the problem?
2. Repeatedly traverse the string to find and remove the substrings “AB” and “CD” until no more occurrences exist.
3. Can the solution be optimized using a stack?

## 示例

```
"ABFCACDB"
"ACBBD"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minLength(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minLength(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minLength(self, s: str) -> int:
        
```

### C

```c
int minLength(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinLength(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minLength = function(s) {
    
};
```

### TypeScript

```typescript
function minLength(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minLength($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minLength(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minLength(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minLength(String s) {
    
  }
}
```

### Go

```golang
func minLength(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def min_length(s)
    
end
```

### Scala

```scala
object Solution {
    def minLength(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_length(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-length s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_length(S :: unicode:unicode_binary()) -> integer().
min_length(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_length(s :: String.t) :: integer
  def min_length(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minLength(s: String): Int64 {

    }
}
```

