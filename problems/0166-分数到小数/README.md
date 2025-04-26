# 166. 分数到小数

## 题目描述

<p>给定两个整数，分别表示分数的分子&nbsp;<code>numerator</code> 和分母 <code>denominator</code>，以 <strong>字符串形式返回小数</strong> 。</p>

<p>如果小数部分为循环小数，则将循环的部分括在括号内。</p>

<p>如果存在多个答案，只需返回 <strong>任意一个</strong> 。</p>

<p>对于所有给定的输入，<strong>保证</strong> 答案字符串的长度小于 <code>10<sup>4</sup></code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numerator = 1, denominator = 2
<strong>输出：</strong>"0.5"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numerator = 2, denominator = 1
<strong>输出：</strong>"2"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>numerator = 4, denominator = 333
<strong>输出：</strong>"0.(012)"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;=&nbsp;numerator, denominator &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>denominator != 0</code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学
- 字符串

## 提示

1. No scary math, just apply elementary math knowledge. Still remember how to perform a <i>long division</i>?
2. Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
3. Notice that once the remainder starts repeating, so does the divided result.
4. Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

## 示例

```
1
2
2
1
4
333
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        
    }
};
```

### Java

```java
class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
```

### C

```c
char* fractionToDecimal(int numerator, int denominator) {
    
}
```

### C#

```csharp
public class Solution {
    public string FractionToDecimal(int numerator, int denominator) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    
};
```

### TypeScript

```typescript
function fractionToDecimal(numerator: number, denominator: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $numerator
     * @param Integer $denominator
     * @return String
     */
    function fractionToDecimal($numerator, $denominator) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fractionToDecimal(_ numerator: Int, _ denominator: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fractionToDecimal(numerator: Int, denominator: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String fractionToDecimal(int numerator, int denominator) {
    
  }
}
```

### Go

```golang
func fractionToDecimal(numerator int, denominator int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} numerator
# @param {Integer} denominator
# @return {String}
def fraction_to_decimal(numerator, denominator)
    
end
```

### Scala

```scala
object Solution {
    def fractionToDecimal(numerator: Int, denominator: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (fraction-to-decimal numerator denominator)
  (-> exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec fraction_to_decimal(Numerator :: integer(), Denominator :: integer()) -> unicode:unicode_binary().
fraction_to_decimal(Numerator, Denominator) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec fraction_to_decimal(numerator :: integer, denominator :: integer) :: String.t
  def fraction_to_decimal(numerator, denominator) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fractionToDecimal(numerator: Int64, denominator: Int64): String {

    }
}
```

