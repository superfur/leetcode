# 1702. 修改后的最大二进制字符串

## 题目描述

<p>给你一个二进制字符串 <code>binary</code> ，它仅有 <code>0</code> 或者 <code>1</code> 组成。你可以使用下面的操作任意次对它进行修改：</p>

<ul>
	<li>操作 1 ：如果二进制串包含子字符串 <code>"00"</code> ，你可以用 <code>"10"</code> 将其替换。

	<ul>
		<li>比方说， <code>"<strong>00</strong>010" -> "<strong>10</strong>010"</code></li>
	</ul>
	</li>
	<li>操作 2 ：如果二进制串包含子字符串 <code>"10"</code> ，你可以用 <code>"01"</code> 将其替换。
	<ul>
		<li>比方说， <code>"000<strong>10</strong>" -> "000<strong>01</strong>"</code></li>
	</ul>
	</li>
</ul>

<p>请你返回执行上述操作任意次以后能得到的 <strong>最大二进制字符串</strong> 。如果二进制字符串 <code>x</code> 对应的十进制数字大于二进制字符串 <code>y</code> 对应的十进制数字，那么我们称二进制字符串<em> </em><code>x</code><em> </em>大于二进制字符串<em> </em><code>y</code><em> </em>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>binary = "000110"
<b>输出：</b>"111011"
<b>解释：</b>一个可行的转换为：
"0001<strong>10</strong>" -> "0001<strong>01</strong>" 
"<strong>00</strong>0101" -> "<strong>10</strong>0101" 
"1<strong>00</strong>101" -> "1<strong>10</strong>101" 
"110<strong>10</strong>1" -> "110<strong>01</strong>1" 
"11<strong>00</strong>11" -> "11<strong>10</strong>11"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>binary = "01"
<b>输出：</b>"01"
<b>解释：</b>"01" 没办法进行任何转换。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= binary.length <= 10<sup>5</sup></code></li>
	<li><code>binary</code> 仅包含 <code>'0'</code> 和 <code>'1'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串

## 提示

1. Note that with the operations, you can always make the string only contain at most 1 zero.

## 示例

```
"000110"
"01"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string maximumBinaryString(string binary) {
        
    }
};
```

### Java

```java
class Solution {
    public String maximumBinaryString(String binary) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        
```

### C

```c
char* maximumBinaryString(char* binary) {
    
}
```

### C#

```csharp
public class Solution {
    public string MaximumBinaryString(string binary) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} binary
 * @return {string}
 */
var maximumBinaryString = function(binary) {
    
};
```

### TypeScript

```typescript
function maximumBinaryString(binary: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $binary
     * @return String
     */
    function maximumBinaryString($binary) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumBinaryString(_ binary: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumBinaryString(binary: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String maximumBinaryString(String binary) {
    
  }
}
```

### Go

```golang
func maximumBinaryString(binary string) string {
    
}
```

### Ruby

```ruby
# @param {String} binary
# @return {String}
def maximum_binary_string(binary)
    
end
```

### Scala

```scala
object Solution {
    def maximumBinaryString(binary: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_binary_string(binary: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-binary-string binary)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec maximum_binary_string(Binary :: unicode:unicode_binary()) -> unicode:unicode_binary().
maximum_binary_string(Binary) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_binary_string(binary :: String.t) :: String.t
  def maximum_binary_string(binary) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumBinaryString(binary: String): String {

    }
}
```

