# 93. 复原 IP 地址

## 题目描述

<p><strong>有效 IP 地址</strong> 正好由四个整数（每个整数位于 <code>0</code> 到 <code>255</code> 之间组成，且不能含有前导 <code>0</code>），整数之间用 <code>'.'</code> 分隔。</p>

<ul>
	<li>例如：<code>"0.1.2.201"</code> 和<code> "192.168.1.1"</code> 是 <strong>有效</strong> IP 地址，但是 <code>"0.011.255.245"</code>、<code>"192.168.1.312"</code> 和 <code>"192.168@1.1"</code> 是 <strong>无效</strong> IP 地址。</li>
</ul>

<p>给定一个只包含数字的字符串 <code>s</code> ，用以表示一个 IP 地址，返回所有可能的<strong>有效 IP 地址</strong>，这些地址可以通过在 <code>s</code> 中插入&nbsp;<code>'.'</code> 来形成。你 <strong>不能</strong>&nbsp;重新排序或删除 <code>s</code> 中的任何数字。你可以按 <strong>任何</strong> 顺序返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "25525511135"
<strong>输出：</strong>["255.255.11.135","255.255.111.35"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "0000"
<strong>输出：</strong>["0.0.0.0"]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "101023"
<strong>输出：</strong>["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 20</code></li>
	<li><code>s</code> 仅由数字组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 回溯

## 示例

```
"25525511135"
"0000"
"101023"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> restoreIpAddresses(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** restoreIpAddresses(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> RestoreIpAddresses(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    
};
```

### TypeScript

```typescript
function restoreIpAddresses(s: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function restoreIpAddresses($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func restoreIpAddresses(_ s: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun restoreIpAddresses(s: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> restoreIpAddresses(String s) {
    
  }
}
```

### Go

```golang
func restoreIpAddresses(s string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def restore_ip_addresses(s)
    
end
```

### Scala

```scala
object Solution {
    def restoreIpAddresses(s: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn restore_ip_addresses(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (restore-ip-addresses s)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec restore_ip_addresses(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
restore_ip_addresses(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec restore_ip_addresses(s :: String.t) :: [String.t]
  def restore_ip_addresses(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func restoreIpAddresses(s: String): ArrayList<String> {

    }
}
```

