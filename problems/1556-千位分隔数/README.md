# 1556. 千位分隔数

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>，请你每隔三位添加点（即 &quot;.&quot; 符号）作为千位分隔符，并将结果以字符串格式返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 987
<strong>输出：</strong>&quot;987&quot;
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 1234
<strong>输出：</strong>&quot;1.234&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 123456789
<strong>输出：</strong>&quot;123.456.789&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 0
<strong>输出：</strong>&quot;0&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt; 2^31</code></li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Scan from the back of the integer and use dots to connect blocks with length 3 except the last block.

## 示例

```
987
1234
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string thousandSeparator(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public String thousandSeparator(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def thousandSeparator(self, n: int) -> str:
        
```

### C

```c
char* thousandSeparator(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public string ThousandSeparator(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string}
 */
var thousandSeparator = function(n) {
    
};
```

### TypeScript

```typescript
function thousandSeparator(n: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String
     */
    function thousandSeparator($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func thousandSeparator(_ n: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun thousandSeparator(n: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String thousandSeparator(int n) {
    
  }
}
```

### Go

```golang
func thousandSeparator(n int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String}
def thousand_separator(n)
    
end
```

### Scala

```scala
object Solution {
    def thousandSeparator(n: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn thousand_separator(n: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (thousand-separator n)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec thousand_separator(N :: integer()) -> unicode:unicode_binary().
thousand_separator(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec thousand_separator(n :: integer) :: String.t
  def thousand_separator(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func thousandSeparator(n: Int64): String {

    }
}
```

