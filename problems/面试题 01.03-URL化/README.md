# 面试题 01.03. URL化

## 题目描述

<p>URL化。编写一种方法，将字符串中的空格全部替换为<code>%20</code>。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用<code>Java</code>实现的话，请使用字符数组实现，以便直接在数组上操作。）</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>："Mr John Smith    ", 13
<strong>输出</strong>："Mr%20John%20Smith"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入</strong>："               ", 5
<strong>输出</strong>："%20%20%20%20%20"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>字符串长度在 [0, 500000] 范围内。</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. 从尾到头开始修改字符串通常最容易。
2. 你可能需要知道空格的数量。你能数一下吗？

## 示例

```
"Mr John Smith    "
13
"               "
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string replaceSpaces(string S, int length) {
        
    }
};
```

### Java

```java
class Solution {
    public String replaceSpaces(String S, int length) {
        
    }
}
```

### Python

```python
class Solution(object):
    def replaceSpaces(self, S, length):
        """
        :type S: str
        :type length: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        
```

### C

```c
char* replaceSpaces(char* S, int length) {
    
}
```

### C#

```csharp
public class Solution {
    public string ReplaceSpaces(string S, int length) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} S
 * @param {number} length
 * @return {string}
 */
var replaceSpaces = function(S, length) {
    
};
```

### TypeScript

```typescript
function replaceSpaces(S: string, length: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $S
     * @param Integer $length
     * @return String
     */
    function replaceSpaces($S, $length) {
        
    }
}
```

### Swift

```swift
class Solution {
    func replaceSpaces(_ S: String, _ length: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun replaceSpaces(S: String, length: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String replaceSpaces(String S, int length) {
    
  }
}
```

### Go

```golang
func replaceSpaces(S string, length int) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} length
# @return {String}
def replace_spaces(s, length)
    
end
```

### Scala

```scala
object Solution {
    def replaceSpaces(S: String, length: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn replace_spaces(s: String, length: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (replace-spaces S length)
  (-> string? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec replace_spaces(S :: unicode:unicode_binary(), Length :: integer()) -> unicode:unicode_binary().
replace_spaces(S, Length) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec replace_spaces(s :: String.t, length :: integer) :: String.t
  def replace_spaces(s, length) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func replaceSpaces(S: String, length: Int64): String {

    }
}
```

