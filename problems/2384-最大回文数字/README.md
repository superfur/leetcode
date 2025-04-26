# 2384. 最大回文数字

## 题目描述

<p>给你一个仅由数字（<code>0 - 9</code>）组成的字符串 <code>num</code> 。</p>

<p>请你找出能够使用 <code>num</code> 中数字形成的 <strong>最大回文</strong> 整数，并以字符串形式返回。该整数不含 <strong>前导零</strong> 。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>你 <strong>无需</strong> 使用 <code>num</code> 中的所有数字，但你必须使用 <strong>至少</strong> 一个数字。</li>
	<li>数字可以重新排序。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "444947137"
<strong>输出：</strong>"7449447"
<strong>解释：</strong>
从 "<em><strong>44494</strong></em><em><strong>7</strong></em>13<em><strong>7</strong></em>" 中选用数字 "4449477"，可以形成回文整数 "7449447" 。
可以证明 "7449447" 是能够形成的最大回文整数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = "00009"
<strong>输出：</strong>"9"
<strong>解释：</strong>
可以证明 "9" 能够形成的最大回文整数。
注意返回的整数不应含前导零。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> 由数字（<code>0 - 9</code>）组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 字符串
- 计数

## 提示

1. In order to form a valid palindrome, other than the middle digit in an odd-length palindrome, every digit needs to exist on both sides.
2. A longer palindrome implies a larger valued palindrome. For palindromes of the same length, the larger digits should occur first.
3. We can count the occurrences of each digit and build the palindrome starting from the ends. Starting from the larger digits, if there are still at least 2 occurrences of a digit, we can place these digits on each side.
4. Make sure to consider the special case for the center digit (if any) and zeroes. There should not be leading zeroes.

## 示例

```
"444947137"
"00009"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestPalindromic(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestPalindromic(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestPalindromic(self, num):
        """
        :type num: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestPalindromic(self, num: str) -> str:
        
```

### C

```c
char* largestPalindromic(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestPalindromic(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var largestPalindromic = function(num) {
    
};
```

### TypeScript

```typescript
function largestPalindromic(num: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestPalindromic($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestPalindromic(_ num: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestPalindromic(num: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestPalindromic(String num) {
    
  }
}
```

### Go

```golang
func largestPalindromic(num string) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {String}
def largest_palindromic(num)
    
end
```

### Scala

```scala
object Solution {
    def largestPalindromic(num: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_palindromic(num: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-palindromic num)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec largest_palindromic(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_palindromic(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_palindromic(num :: String.t) :: String.t
  def largest_palindromic(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestPalindromic(num: String): String {

    }
}
```

