# 392. 判断子序列

## 题目描述

<p>给定字符串 <strong>s</strong> 和 <strong>t</strong> ，判断 <strong>s</strong> 是否为 <strong>t</strong> 的子序列。</p>

<p>字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，<code>"ace"</code>是<code>"abcde"</code>的一个子序列，而<code>"aec"</code>不是）。</p>

<p><strong>进阶：</strong></p>

<p>如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？</p>

<p><strong>致谢：</strong></p>

<p>特别感谢<strong> </strong><a href="https://leetcode.com/pbrother/">@pbrother </a>添加此问题并且创建所有测试用例。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abc", t = "ahbgdc"
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "axc", t = "ahbgdc"
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 <= s.length <= 100</code></li>
	<li><code>0 <= t.length <= 10^4</code></li>
	<li>两个字符串都只由小写字符组成。</li>
</ul>


## 难度

Easy

## 标签

- 双指针
- 字符串
- 动态规划

## 示例

```
"abc"
"ahbgdc"
"axc"
"ahbgdc"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isSubsequence(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
```

### C

```c
bool isSubsequence(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsSubsequence(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    
};
```

### TypeScript

```typescript
function isSubsequence(s: string, t: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isSubsequence($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isSubsequence(_ s: String, _ t: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isSubsequence(s: String, t: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isSubsequence(String s, String t) {
    
  }
}
```

### Go

```golang
func isSubsequence(s string, t string) bool {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Boolean}
def is_subsequence(s, t)
    
end
```

### Scala

```scala
object Solution {
    def isSubsequence(s: String, t: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_subsequence(s: String, t: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-subsequence s t)
  (-> string? string? boolean?)
  )
```

### Erlang

```erlang
-spec is_subsequence(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> boolean().
is_subsequence(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_subsequence(s :: String.t, t :: String.t) :: boolean
  def is_subsequence(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isSubsequence(s: String, t: String): Bool {

    }
}
```

