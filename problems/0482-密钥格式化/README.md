# 482. 密钥格式化

## 题目描述

<p>给定一个许可密钥字符串 <code>s</code>，仅由字母、数字字符和破折号组成。字符串由 <code>n</code> 个破折号分成 <code>n + 1</code> 组。你也会得到一个整数 <code>k</code> 。</p>

<p>我们想要重新格式化字符串&nbsp;<code>s</code>，使每一组包含 <code>k</code> 个字符，除了第一组，它可以比 <code>k</code> 短，但仍然必须包含至少一个字符。此外，两组之间必须插入破折号，并且应该将所有小写字母转换为大写字母。</p>

<p>返回 <em>重新格式化的许可密钥</em> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>S = "5F3Z-2e-9-w", k = 4
<strong>输出：</strong>"5F3Z-2E9W"
<strong>解释：</strong>字符串 S 被分成了两个部分，每部分 4 个字符；
&nbsp;    注意，两个额外的破折号需要删掉。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>S = "2-5g-3-J", k = 2
<strong>输出：</strong>"2-5G-3J"
<strong>解释：</strong>字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含字母、数字和破折号&nbsp;<code>'-'</code>.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 示例

```
"5F3Z-2e-9-w"
4
"2-5g-3-J"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string licenseKeyFormatting(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String licenseKeyFormatting(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
```

### C

```c
char* licenseKeyFormatting(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string LicenseKeyFormatting(string s, int k) {
        
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
var licenseKeyFormatting = function(s, k) {
    
};
```

### TypeScript

```typescript
function licenseKeyFormatting(s: string, k: number): string {
    
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
    function licenseKeyFormatting($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func licenseKeyFormatting(_ s: String, _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun licenseKeyFormatting(s: String, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String licenseKeyFormatting(String s, int k) {
    
  }
}
```

### Go

```golang
func licenseKeyFormatting(s string, k int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {String}
def license_key_formatting(s, k)
    
end
```

### Scala

```scala
object Solution {
    def licenseKeyFormatting(s: String, k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn license_key_formatting(s: String, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (license-key-formatting s k)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec license_key_formatting(S :: unicode:unicode_binary(), K :: integer()) -> unicode:unicode_binary().
license_key_formatting(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec license_key_formatting(s :: String.t, k :: integer) :: String.t
  def license_key_formatting(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func licenseKeyFormatting(s: String, k: Int64): String {

    }
}
```

