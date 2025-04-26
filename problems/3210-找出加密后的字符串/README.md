# 3210. 找出加密后的字符串

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code>。请你使用以下算法加密字符串：</p>

<ul>
	<li>对于字符串 <code>s</code> 中的每个字符 <code>c</code>，用字符串中 <code>c</code> 后面的第 <code>k</code> 个字符替换 <code>c</code>（以循环方式）。</li>
</ul>

<p>返回加密后的字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "dart", k = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">"tdar"</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>i = 0</code>，<code>'d'</code> 后面的第 3 个字符是 <code>'t'</code>。</li>
	<li>对于 <code>i = 1</code>，<code>'a'</code> 后面的第 3 个字符是 <code>'d'</code>。</li>
	<li>对于 <code>i = 2</code>，<code>'r'</code> 后面的第 3 个字符是 <code>'a'</code>。</li>
	<li>对于 <code>i = 3</code>，<code>'t'</code> 后面的第 3 个字符是 <code>'r'</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aaa", k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">"aaa"</span></p>

<p><strong>解释：</strong></p>

<p>由于所有字符都相同，加密后的字符串也将相同。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Make a new string such that for each character in <code>s</code>, character <code>i</code> will correspond to <code>(i + k) % s.length</code> character in the original string.

## 示例

```
"dart"
3
"aaa"
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string getEncryptedString(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String getEncryptedString(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        
```

### C

```c
char* getEncryptedString(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string GetEncryptedString(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var getEncryptedString = function(s, k) {
    
};
```

### TypeScript

```typescript
function getEncryptedString(s: string, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return String
     */
    function getEncryptedString($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getEncryptedString(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getEncryptedString(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String getEncryptedString(String s, int k) {
    
  }
}
```

### Go

```golang
func getEncryptedString(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def get_encrypted_string(s, k)
    
end
```

### Scala

```scala
object Solution {
    def getEncryptedString(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_encrypted_string(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (get-encrypted-string s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec get_encrypted_string(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
get_encrypted_string(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_encrypted_string(s :: String.t, k :: integer) :: String.t
  def get_encrypted_string(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getEncryptedString(s: String, k: Int64): String {

    }
}
```

