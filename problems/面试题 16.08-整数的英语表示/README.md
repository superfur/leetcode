# 面试题 16.08. 整数的英语表示

## 题目描述

<p>给定一个整数，打印该整数的英文描述。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>123
<strong>输出：</strong>"One Hundred Twenty Three"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>12345
<strong>输出：</strong>"Twelve Thousand Three Hundred Forty Five"</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>1234567
<strong>输出：</strong>"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>1234567891
<strong>输出：</strong>"One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"</pre>

<p>注意：本题与&nbsp;273 题相同：<a href="https://leetcode-cn.com/problems/integer-to-english-words/">https://leetcode-cn.com/problems/integer-to-english-words/</a></p>


## 难度

Hard

## 标签

- 递归
- 数学
- 字符串

## 提示

1. 试着从三位作为一段的角度思考。
2. 你考虑过负数吗？你的解决方案是否适用于100 030 000这样的值？
3. 考虑把一个数字分成由3位数组成的序列。

## 示例

```
123
12345
1234567
1234567891
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string numberToWords(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public String numberToWords(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def numberToWords(self, num: int) -> str:
        
```

### C

```c
char* numberToWords(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public string NumberToWords(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var numberToWords = function(num) {
    
};
```

### TypeScript

```typescript
function numberToWords(num: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return String
     */
    function numberToWords($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberToWords(_ num: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberToWords(num: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String numberToWords(int num) {
    
  }
}
```

### Go

```golang
func numberToWords(num int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {String}
def number_to_words(num)
    
end
```

### Scala

```scala
object Solution {
    def numberToWords(num: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_to_words(num: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (number-to-words num)
  (-> exact-integer? string?)
  )
```

### Erlang

```erlang
-spec number_to_words(Num :: integer()) -> unicode:unicode_binary().
number_to_words(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_to_words(num :: integer) :: String.t
  def number_to_words(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberToWords(num: Int64): String {

    }
}
```

