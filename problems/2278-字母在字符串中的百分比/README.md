# 2278. 字母在字符串中的百分比

## 题目描述

<p>给你一个字符串 <code>s</code> 和一个字符 <code>letter</code> ，返回在 <code>s</code> 中等于&nbsp;<code>letter</code>&nbsp;字符所占的 <strong>百分比</strong> ，向下取整到最接近的百分比。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "foobar", letter = "o"
<strong>输出：</strong>33
<strong>解释：</strong>
等于字母 'o' 的字符在 s 中占到的百分比是 2 / 6 * 100% = 33% ，向下取整，所以返回 33 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "jjjj", letter = "k"
<strong>输出：</strong>0
<strong>解释：</strong>
等于字母 'k' 的字符在 s 中占到的百分比是 0% ，所以返回 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
	<li><code>letter</code> 是一个小写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 提示

1. Can we count the number of occurrences of letter in s?
2. Recall that the percentage is calculated as (occurrences / total) * 100.

## 示例

```
"foobar"
"o"
"jjjj"
"k"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int percentageLetter(string s, char letter) {
        
    }
};
```

### Java

```java
class Solution {
    public int percentageLetter(String s, char letter) {
        
    }
}
```

### Python

```python
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
```

### C

```c
int percentageLetter(char* s, char letter) {
    
}
```

### C#

```csharp
public class Solution {
    public int PercentageLetter(string s, char letter) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {character} letter
 * @return {number}
 */
var percentageLetter = function(s, letter) {
    
};
```

### TypeScript

```typescript
function percentageLetter(s: string, letter: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param String $letter
     * @return Integer
     */
    function percentageLetter($s, $letter) {
        
    }
}
```

### Swift

```swift
class Solution {
    func percentageLetter(_ s: String, _ letter: Character) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun percentageLetter(s: String, letter: Char): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int percentageLetter(String s, String letter) {
    
  }
}
```

### Go

```golang
func percentageLetter(s string, letter byte) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Character} letter
# @return {Integer}
def percentage_letter(s, letter)
    
end
```

### Scala

```scala
object Solution {
    def percentageLetter(s: String, letter: Char): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (percentage-letter s letter)
  (-> string? char? exact-integer?)
  )
```

### Erlang

```erlang
-spec percentage_letter(S :: unicode:unicode_binary(), Letter :: char()) -> integer().
percentage_letter(S, Letter) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec percentage_letter(s :: String.t, letter :: char) :: integer
  def percentage_letter(s, letter) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func percentageLetter(s: String, letter: Rune): Int64 {

    }
}
```

