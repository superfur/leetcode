# 2259. 移除指定数字得到的最大结果

## 题目描述

<p>给你一个表示某个正整数的字符串 <code>number</code> 和一个字符 <code>digit</code> 。</p>

<p>从 <code>number</code> 中 <strong>恰好</strong> 移除 <strong>一个</strong> 等于&nbsp;<code>digit</code> 的字符后，找出并返回按 <strong>十进制</strong> 表示 <strong>最大</strong> 的结果字符串。生成的测试用例满足 <code>digit</code> 在 <code>number</code> 中出现至少一次。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>number = "123", digit = "3"
<strong>输出：</strong>"12"
<strong>解释：</strong>"123" 中只有一个 '3' ，在移除 '3' 之后，结果为 "12" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>number = "1231", digit = "1"
<strong>输出：</strong>"231"
<strong>解释：</strong>可以移除第一个 '1' 得到 "231" 或者移除第二个 '1' 得到 "123" 。
由于 231 &gt; 123 ，返回 "231" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>number = "551", digit = "5"
<strong>输出：</strong>"51"
<strong>解释：</strong>可以从 "551" 中移除第一个或者第二个 '5' 。
两种方案的结果都是 "51" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= number.length &lt;= 100</code></li>
	<li><code>number</code> 由数字 <code>'1'</code> 到 <code>'9'</code> 组成</li>
	<li><code>digit</code> 是 <code>'1'</code> 到 <code>'9'</code> 中的一个数字</li>
	<li><code>digit</code> 在 <code>number</code> 中出现至少一次</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 字符串
- 枚举

## 提示

1. The maximum length of number is really small.
2. Iterate through the digits of number and every time we see digit, try removing it.
3. To remove a character at index i, concatenate the substring from index 0 to i - 1 and the substring from index i + 1 to number.length - 1.

## 示例

```
"123"
"3"
"1231"
"1"
"551"
"5"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string removeDigit(string number, char digit) {
        
    }
};
```

### Java

```java
class Solution {
    public String removeDigit(String number, char digit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
```

### C

```c
char* removeDigit(char* number, char digit) {
    
}
```

### C#

```csharp
public class Solution {
    public string RemoveDigit(string number, char digit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} number
 * @param {character} digit
 * @return {string}
 */
var removeDigit = function(number, digit) {
    
};
```

### TypeScript

```typescript
function removeDigit(number: string, digit: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $number
     * @param String $digit
     * @return String
     */
    function removeDigit($number, $digit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func removeDigit(_ number: String, _ digit: Character) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun removeDigit(number: String, digit: Char): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String removeDigit(String number, String digit) {
    
  }
}
```

### Go

```golang
func removeDigit(number string, digit byte) string {
    
}
```

### Ruby

```ruby
# @param {String} number
# @param {Character} digit
# @return {String}
def remove_digit(number, digit)
    
end
```

### Scala

```scala
object Solution {
    def removeDigit(number: String, digit: Char): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn remove_digit(number: String, digit: char) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (remove-digit number digit)
  (-> string? char? string?)
  )
```

### Erlang

```erlang
-spec remove_digit(Number :: unicode:unicode_binary(), Digit :: char()) -> unicode:unicode_binary().
remove_digit(Number, Digit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec remove_digit(number :: String.t, digit :: char) :: String.t
  def remove_digit(number, digit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func removeDigit(number: String, digit: Rune): String {

    }
}
```

