# 521. 最长特殊序列 Ⅰ

## 题目描述

<p>给你两个字符串&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>，请返回 <em>这两个字符串中 <strong>最长的特殊序列</strong>&nbsp;</em> 的长度。如果不存在，则返回 <code>-1</code>&nbsp;。</p>

<p><strong>「最长特殊序列」</strong>&nbsp;定义如下：该序列为&nbsp;<strong>某字符串独有的最长<span data-keyword="subsequence-array">子序列</span>（即不能是其他字符串的子序列）</strong>&nbsp;。</p>

<p>字符串&nbsp;<code>s</code>&nbsp;的子序列是在从&nbsp;<code>s</code>&nbsp;中删除任意数量的字符后可以获得的字符串。</p>

<ul>
	<li>例如，<code>"abc"</code> 是 <code>"aebdc"</code> 的子序列，因为删除 <code>"a<em><strong>e</strong></em>b<strong><em>d</em></strong>c"</code> 中斜体加粗的字符可以得到 <code>"abc"</code> 。 <code>"aebdc"</code> 的子序列还包括 <code>"aebdc"</code> 、 <code>"aeb"</code> 和 <code>""</code> (空字符串)。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> a = "aba", b = "cdc"
<strong>输出:</strong> 3
<strong>解释:</strong> 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>a = "aaa", b = "bbb"
<strong>输出：</strong>3
<strong>解释:</strong> 最长特殊序列是 "aaa" 和 "bbb" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>a = "aaa", b = "aaa"
<strong>输出：</strong>-1
<strong>解释:</strong> 字符串 a 的每个子序列也是字符串 b 的每个子序列。同样，字符串 b 的每个子序列也是字符串 a 的子序列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a.length, b.length &lt;= 100</code></li>
	<li><code>a</code>&nbsp;和&nbsp;<code>b</code>&nbsp;由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Think very simple.
2. If <code>a == b</code>, the answer is -1.
3. Otherwise, the answer is the string <code>a</code> or the string <code>b</code>.

## 示例

```
"aba"
"cdc"
"aaa"
"bbb"
"aaa"
"aaa"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLUSlength(string a, string b) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLUSlength(String a, String b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        
```

### C

```c
int findLUSlength(char* a, char* b) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLUSlength(string a, string b) {
        
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
var findLUSlength = function(a, b) {
    
};
```

### TypeScript

```typescript
function findLUSlength(a: string, b: string): number {
    
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
    function findLUSlength($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLUSlength(_ a: String, _ b: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLUSlength(a: String, b: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLUSlength(String a, String b) {
    
  }
}
```

### Go

```golang
func findLUSlength(a string, b string) int {
    
}
```

### Ruby

```ruby
# @param {String} a
# @param {String} b
# @return {Integer}
def find_lu_slength(a, b)
    
end
```

### Scala

```scala
object Solution {
    def findLUSlength(a: String, b: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_lu_slength(a: String, b: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-lu-slength a b)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_lu_slength(A :: unicode:unicode_binary(), B :: unicode:unicode_binary()) -> integer().
find_lu_slength(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_lu_slength(a :: String.t, b :: String.t) :: integer
  def find_lu_slength(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLUSlength(a: String, b: String): Int64 {

    }
}
```

