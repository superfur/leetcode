# 468. 验证IP地址

## 题目描述

<p>给定一个字符串&nbsp;<code>queryIP</code>。如果是有效的 IPv4 地址，返回 <code>"IPv4"</code> ；如果是有效的 IPv6 地址，返回 <code>"IPv6"</code> ；如果不是上述类型的 IP 地址，返回 <code>"Neither"</code> 。</p>

<p><strong>有效的IPv4地址</strong> 是 <code>“x1.x2.x3.x4”</code> 形式的IP地址。 其中&nbsp;<code>0 &lt;= x<sub>i</sub>&nbsp;&lt;= 255</code>&nbsp;且&nbsp;<code>x<sub>i</sub></code>&nbsp;<strong>不能包含</strong> 前导零。例如:&nbsp;<code>“192.168.1.1”</code>&nbsp;、 <code>“192.168.1.0”</code> 为有效IPv4地址， <code>“192.168.01.1”</code> 为无效IPv4地址; <code>“192.168.1.00”</code> 、 <code>“192.168@1.1”</code> 为无效IPv4地址。</p>

<p><strong>一个有效的IPv6地址&nbsp;</strong>是一个格式为<code>“x1:x2:x3:x4:x5:x6:x7:x8”</code> 的IP地址，其中:</p>

<ul>
	<li><code>1 &lt;= x<sub>i</sub>.length &lt;= 4</code></li>
	<li><code>x<sub>i</sub></code>&nbsp;是一个 <strong>十六进制字符串</strong> ，可以包含数字、小写英文字母( <code>'a'</code> 到 <code>'f'</code> )和大写英文字母( <code>'A'</code> 到 <code>'F'</code> )。</li>
	<li>在&nbsp;<code>x<sub>i</sub></code>&nbsp;中允许前导零。</li>
</ul>

<p>例如 <code>"2001:0db8:85a3:0000:0000:8a2e:0370:7334"</code> 和 <code>"2001:db8:85a3:0:0:8A2E:0370:7334"</code> 是有效的 IPv6 地址，而 <code>"2001:0db8:85a3::8A2E:037j:7334"</code> 和 <code>"02001:0db8:85a3:0000:0000:8a2e:0370:7334"</code> 是无效的 IPv6 地址。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>queryIP = "172.16.254.1"
<strong>输出：</strong>"IPv4"
<strong>解释：</strong>有效的 IPv4 地址，返回 "IPv4"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
<strong>输出：</strong>"IPv6"
<strong>解释：</strong>有效的 IPv6 地址，返回 "IPv6"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>queryIP = "256.256.256.256"
<strong>输出：</strong>"Neither"
<strong>解释：</strong>既不是 IPv4 地址，又不是 IPv6 地址
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>queryIP</code> 仅由英文字母，数字，字符 <code>'.'</code> 和 <code>':'</code> 组成。</li>
</ul>


## 难度

Medium

## 标签

- 字符串

## 示例

```
"172.16.254.1"
"2001:0db8:85a3:0:0:8A2E:0370:7334"
"256.256.256.256"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string validIPAddress(string queryIP) {
        
    }
};
```

### Java

```java
class Solution {
    public String validIPAddress(String queryIP) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
```

### C

```c
char* validIPAddress(char* queryIP) {
    
}
```

### C#

```csharp
public class Solution {
    public string ValidIPAddress(string queryIP) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} queryIP
 * @return {string}
 */
var validIPAddress = function(queryIP) {
    
};
```

### TypeScript

```typescript
function validIPAddress(queryIP: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $queryIP
     * @return String
     */
    function validIPAddress($queryIP) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validIPAddress(_ queryIP: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validIPAddress(queryIP: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String validIPAddress(String queryIP) {
    
  }
}
```

### Go

```golang
func validIPAddress(queryIP string) string {
    
}
```

### Ruby

```ruby
# @param {String} query_ip
# @return {String}
def valid_ip_address(query_ip)
    
end
```

### Scala

```scala
object Solution {
    def validIPAddress(queryIP: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_ip_address(query_ip: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (valid-ip-address queryIP)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec valid_ip_address(QueryIP :: unicode:unicode_binary()) -> unicode:unicode_binary().
valid_ip_address(QueryIP) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_ip_address(query_ip :: String.t) :: String.t
  def valid_ip_address(query_ip) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validIPAddress(queryIP: String): String {

    }
}
```

