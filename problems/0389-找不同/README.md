# 389. 找不同

## 题目描述

<p>给定两个字符串 <code>s</code> 和 <code>t</code>&nbsp;，它们只包含小写字母。</p>

<p>字符串 <code>t</code>&nbsp;由字符串 <code>s</code> 随机重排，然后在随机位置添加一个字母。</p>

<p>请找出在 <code>t</code>&nbsp;中被添加的字母。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abcd", t = "abcde"
<strong>输出：</strong>"e"
<strong>解释：</strong>'e' 是那个被添加的字母。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "", t = "y"
<strong>输出：</strong>"y"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 1000</code></li>
	<li><code>t.length == s.length + 1</code></li>
	<li><code>s</code> 和 <code>t</code> 只包含小写字母</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 哈希表
- 字符串
- 排序

## 示例

```
"abcd"
"abcde"
""
"y"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    char findTheDifference(string s, string t) {
        
    }
};
```

### Java

```java
class Solution {
    public char findTheDifference(String s, String t) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
```

### C

```c
char findTheDifference(char* s, char* t) {
    
}
```

### C#

```csharp
public class Solution {
    public char FindTheDifference(string s, string t) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    
};
```

### TypeScript

```typescript
function findTheDifference(s: string, t: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function findTheDifference($s, $t) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findTheDifference(_ s: String, _ t: String) -> Character {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTheDifference(s: String, t: String): Char {
        
    }
}
```

### Dart

```dart
class Solution {
  String findTheDifference(String s, String t) {
    
  }
}
```

### Go

```golang
func findTheDifference(s string, t string) byte {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {String} t
# @return {Character}
def find_the_difference(s, t)
    
end
```

### Scala

```scala
object Solution {
    def findTheDifference(s: String, t: String): Char = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_the_difference(s: String, t: String) -> char {
        
    }
}
```

### Racket

```racket
(define/contract (find-the-difference s t)
  (-> string? string? char?)
  )
```

### Erlang

```erlang
-spec find_the_difference(S :: unicode:unicode_binary(), T :: unicode:unicode_binary()) -> char().
find_the_difference(S, T) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_the_difference(s :: String.t, t :: String.t) :: char
  def find_the_difference(s, t) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findTheDifference(s: String, t: String): Rune {

    }
}
```

