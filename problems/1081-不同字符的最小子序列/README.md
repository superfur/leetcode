# 1081. 不同字符的最小子序列

## 题目描述

<p>返回 <code>s</code> 字典序最小的<span data-keyword="subsequence-array">子序列</span>，该子序列包含 <code>s</code> 的所有不同字符，且只包含一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong><code>s = "bcabc"</code>
<strong>输出<code>：</code></strong><code>"abc"</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong><code>s = "cbacdcbc"</code>
<strong>输出：</strong><code>"acdb"</code></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>该题与 316 <a href="https://leetcode.cn/problems/remove-duplicate-letters/">https://leetcode.cn/problems/remove-duplicate-letters/</a> 相同</p>


## 难度

Medium

## 标签

- 栈
- 贪心
- 字符串
- 单调栈

## 提示

1. Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.

## 示例

```
"bcabc"
"cbacdcbc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string smallestSubsequence(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String smallestSubsequence(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
```

### C

```c
char* smallestSubsequence(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string SmallestSubsequence(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var smallestSubsequence = function(s) {
    
};
```

### TypeScript

```typescript
function smallestSubsequence(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function smallestSubsequence($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestSubsequence(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestSubsequence(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String smallestSubsequence(String s) {
    
  }
}
```

### Go

```golang
func smallestSubsequence(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def smallest_subsequence(s)
    
end
```

### Scala

```scala
object Solution {
    def smallestSubsequence(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_subsequence(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-subsequence s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec smallest_subsequence(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
smallest_subsequence(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_subsequence(s :: String.t) :: String.t
  def smallest_subsequence(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestSubsequence(s: String): String {

    }
}
```

