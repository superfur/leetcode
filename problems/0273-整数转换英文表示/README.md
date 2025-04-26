# 273. 整数转换英文表示

## 题目描述

<p>将非负整数 <code>num</code> 转换为其对应的英文表示。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = 123
<strong>输出：</strong>"One Hundred Twenty Three"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = 12345
<strong>输出：</strong>"Twelve Thousand Three Hundred Forty Five"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = 1234567
<strong>输出：</strong>"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Hard

## 标签

- 递归
- 数学
- 字符串

## 提示

1. Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
2. Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
3. There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

## 示例

```
123
12345
1234567
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

