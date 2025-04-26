# 2309. 兼具大小写的最好英文字母

## 题目描述

<p>给你一个由英文字母组成的字符串 <code>s</code> ，请你找出并返回 <code>s</code> 中的 <strong>最好</strong> 英文字母。返回的字母必须为大写形式。如果不存在满足条件的字母，则返回一个空字符串。</p>

<p><strong>最好</strong> 英文字母的大写和小写形式必须 <strong>都</strong> 在 <code>s</code> 中出现。</p>

<p>英文字母 <code>b</code> 比另一个英文字母&nbsp;<code>a</code>&nbsp;<strong>更好</strong> 的前提是：英文字母表中，<code>b</code> 在 <code>a</code> 之 <strong>后</strong> 出现。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "l<em><strong>Ee</strong></em>TcOd<em><strong>E</strong></em>"
<strong>输出：</strong>"E"
<strong>解释：</strong>
字母 'E' 是唯一一个大写和小写形式都出现的字母。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a<em><strong>rR</strong></em>AzFif"
<strong>输出：</strong>"R"
<strong>解释：</strong>
字母 'R' 是大写和小写形式都出现的最好英文字母。
注意 'A' 和 'F' 的大写和小写形式也都出现了，但是 'R' 比 'F' 和 'A' 更好。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "AbCdEfGhIjK"
<strong>输出：</strong>""
<strong>解释：</strong>
不存在大写和小写形式都出现的字母。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> 由小写和大写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串
- 枚举

## 提示

1. Consider iterating through the string and storing each unique character that occurs in a set.
2. From Z to A, check whether both the uppercase and lowercase version occur in the set.

## 示例

```
"lEeTcOdE"
"arRAzFif"
"AbCdEfGhIjK"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string greatestLetter(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public String greatestLetter(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def greatestLetter(self, s: str) -> str:
        
```

### C

```c
char* greatestLetter(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public string GreatestLetter(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string}
 */
var greatestLetter = function(s) {
    
};
```

### TypeScript

```typescript
function greatestLetter(s: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String
     */
    function greatestLetter($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func greatestLetter(_ s: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun greatestLetter(s: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String greatestLetter(String s) {
    
  }
}
```

### Go

```golang
func greatestLetter(s string) string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String}
def greatest_letter(s)
    
end
```

### Scala

```scala
object Solution {
    def greatestLetter(s: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn greatest_letter(s: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (greatest-letter s)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec greatest_letter(S :: unicode:unicode_binary()) -> unicode:unicode_binary().
greatest_letter(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec greatest_letter(s :: String.t) :: String.t
  def greatest_letter(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func greatestLetter(s: String): String {

    }
}
```

