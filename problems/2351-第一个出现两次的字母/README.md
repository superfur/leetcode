# 2351. 第一个出现两次的字母

## 题目描述

<p>给你一个由小写英文字母组成的字符串 <code>s</code> ，请你找出并返回第一个出现 <strong>两次</strong> 的字母。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>如果 <code>a</code> 的 <strong>第二次</strong> 出现比 <code>b</code> 的 <strong>第二次</strong> 出现在字符串中的位置更靠前，则认为字母 <code>a</code> 在字母 <code>b</code> 之前出现两次。</li>
	<li><code>s</code> 包含至少一个出现两次的字母。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>s = "abccbaacz"
<strong>输出：</strong>"c"
<strong>解释：</strong>
字母 'a' 在下标 0 、5 和 6 处出现。
字母 'b' 在下标 1 和 4 处出现。
字母 'c' 在下标 2 、3 和 7 处出现。
字母 'z' 在下标 8 处出现。
字母 'c' 是第一个出现两次的字母，因为在所有字母中，'c' 第二次出现的下标是最小的。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>s = "abcdd"
<strong>输出：</strong>"d"
<strong>解释：</strong>
只有字母 'd' 出现两次，所以返回 'd' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>s</code> 包含至少一个重复字母</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 哈希表
- 字符串
- 计数

## 提示

1. Iterate through the string from left to right. Keep track of the elements you have already seen in a set.
2. If the current element is already in the set, return that element.

## 示例

```
"abccbaacz"
"abcdd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    char repeatedCharacter(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public char repeatedCharacter(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
```

### C

```c
char repeatedCharacter(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public char RepeatedCharacter(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {character}
 */
var repeatedCharacter = function(s) {
    
};
```

### TypeScript

```typescript
function repeatedCharacter(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function repeatedCharacter($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func repeatedCharacter(_ s: String) -> Character {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun repeatedCharacter(s: String): Char {
        
    }
}
```

### Dart

```dart
class Solution {
  String repeatedCharacter(String s) {
    
  }
}
```

### Go

```golang
func repeatedCharacter(s string) byte {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Character}
def repeated_character(s)
    
end
```

### Scala

```scala
object Solution {
    def repeatedCharacter(s: String): Char = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn repeated_character(s: String) -> char {
        
    }
}
```

### Racket

```racket
(define/contract (repeated-character s)
  (-> string? char?)
  )
```

### Erlang

```erlang
-spec repeated_character(S :: unicode:unicode_binary()) -> char().
repeated_character(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec repeated_character(s :: String.t) :: char
  def repeated_character(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func repeatedCharacter(s: String): Rune {

    }
}
```

