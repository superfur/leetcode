# 面试题 01.06. 字符串压缩

## 题目描述

<p>字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。比如，字符串<code>aabcccccaaa</code>会变为<code>a2b1c5a3</code>。若“压缩”后的字符串没有变短，则返回原先的字符串。你可以假设字符串中只包含大小写英文字母（a至z）。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>："aabcccccaaa"
<strong>输出</strong>："a2b1c5a3"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入</strong>："abbccd"
<strong>输出</strong>："abbccd"
<strong>解释</strong>："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>字符串长度在 <code>[0, 50000]</code> 范围内。</li>
</ol>


## 难度

Easy

## 标签

- 双指针
- 字符串

## 提示

1. 先做容易的事。压缩字符串，然后再比较长度。
2. 注意不要把字符串重复连接在一起。这会非常低效。

## 示例

```
"aabcccccaa"
"abbccd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string compressString(string S) {
        
    }
};
```

### Java

```java
class Solution {
    public String compressString(String S) {
        
    }
}
```

### Python

```python
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def compressString(self, S: str) -> str:
        
```

### C

```c
char* compressString(char* S) {
    
}
```

### C#

```csharp
public class Solution {
    public string CompressString(string S) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} S
 * @return {string}
 */
var compressString = function(S) {
    
};
```

### TypeScript

```typescript
function compressString(S: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $S
     * @return String
     */
    function compressString($S) {
        
    }
}
```

### Swift

```swift
class Solution {
    func compressString(_ S: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun compressString(S: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String compressString(String S) {
    
  }
}
```

### Go

```golang
func compressString(S string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def compress_string(s)
    
end
```

### Scala

```scala
object Solution {
    def compressString(S: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn compress_string(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (compress-string S)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec compress_string(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
compress_string(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec compress_string(s :: String.t) :: String.t
  def compress_string(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func compressString(S: String): String {

    }
}
```

