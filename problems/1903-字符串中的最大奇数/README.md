# 1903. 字符串中的最大奇数

## 题目描述

<p>给你一个字符串 <code>num</code> ，表示一个大整数。请你在字符串 <code>num</code> 的所有 <strong>非空子字符串</strong> 中找出 <strong>值最大的奇数</strong> ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串<em> </em><code>""</code><em> </em>。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续的字符序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "52"
<strong>输出：</strong>"5"
<strong>解释：</strong>非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num = "4206"
<strong>输出：</strong>""
<strong>解释：</strong>在 "4206" 中不存在奇数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>num = "35427"
<strong>输出：</strong>"35427"
<strong>解释：</strong>"35427" 本身就是一个奇数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= num.length <= 10<sup>5</sup></code></li>
	<li><code>num</code> 仅由数字组成且不含前导零</li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学
- 字符串

## 提示

1. In what order should you iterate through the digits?
2. If an odd number exists, where must the number start from?

## 示例

```
"52"
"4206"
"35427"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestOddNumber(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestOddNumber(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestOddNumber(self, num: str) -> str:
        
```

### C

```c
char* largestOddNumber(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestOddNumber(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {string}
 */
var largestOddNumber = function(num) {
    
};
```

### TypeScript

```typescript
function largestOddNumber(num: string): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return String
     */
    function largestOddNumber($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestOddNumber(_ num: String) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestOddNumber(num: String): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestOddNumber(String num) {
    
  }
}
```

### Go

```golang
func largestOddNumber(num string) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {String}
def largest_odd_number(num)
    
end
```

### Scala

```scala
object Solution {
    def largestOddNumber(num: String): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_odd_number(num: String) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-odd-number num)
  (-> string? string?)
  )
```

### Erlang

```erlang
-spec largest_odd_number(Num :: unicode:unicode_binary()) -> unicode:unicode_binary().
largest_odd_number(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_odd_number(num :: String.t) :: String.t
  def largest_odd_number(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestOddNumber(num: String): String {

    }
}
```

