# 1108. IP 地址无效化

## 题目描述

<p>给你一个有效的 <a href="https://baike.baidu.com/item/IPv4" target="_blank">IPv4</a> 地址&nbsp;<code>address</code>，返回这个 IP 地址的无效化版本。</p>

<p>所谓无效化&nbsp;IP 地址，其实就是用&nbsp;<code>&quot;[.]&quot;</code>&nbsp;代替了每个 <code>&quot;.&quot;</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>address = &quot;1.1.1.1&quot;
<strong>输出：</strong>&quot;1[.]1[.]1[.]1&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>address = &quot;255.100.50.0&quot;
<strong>输出：</strong>&quot;255[.]100[.]50[.]0&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>给出的&nbsp;<code>address</code>&nbsp;是一个有效的 IPv4 地址</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 示例

```
"1.1.1.1"
"255.100.50.0"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string defangIPaddr(string address) {
        
    }
};
```

### Java

```java
class Solution {
    public String defangIPaddr(String address) {
        
    }
}
```

### Python

```python
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def defangIPaddr(self, address: str) -> str:
        
```

### C

```c
char* defangIPaddr(char* address) {
    
}
```

### C#

```csharp
public class Solution {
    public string DefangIPaddr(string address) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} address
 * @return {string}
 */
var defangIPaddr = function(address) {
    
};
```

### TypeScript

```typescript
function defangIPaddr(address: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $address
     * @return String
     */
    function defangIPaddr($address) {
        
    }
}
```

### Swift

```swift
class Solution {
    func defangIPaddr(_ address: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun defangIPaddr(address: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String defangIPaddr(String address) {
    
  }
}
```

### Go

```golang
func defangIPaddr(address string) string {
    
}
```

### Ruby

```ruby
# @param {String} address
# @return {String}
def defang_i_paddr(address)
    
end
```

### Scala

```scala
object Solution {
    def defangIPaddr(address: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn defang_i_paddr(address: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (defang-i-paddr address)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec defang_i_paddr(Address :: unicode:unicode_binary()) -> unicode:unicode_binary().
defang_i_paddr(Address) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec defang_i_paddr(address :: String.t) :: String.t
  def defang_i_paddr(address) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func defangIPaddr(address: String): String {

    }
}
```

