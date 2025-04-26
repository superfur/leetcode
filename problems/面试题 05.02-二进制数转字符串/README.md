# 面试题 05.02. 二进制数转字符串

## 题目描述

<p>二进制数转字符串。给定一个介于 0 和 1 之间的实数（如 0.72），类型为 double，打印它的二进制表达式。如果该数字无法精确地用 32 位以内的二进制表示，则打印“ERROR”。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入</strong>：0.625
<strong>输出</strong>："0.101"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入</strong>：0.1
<strong>输出</strong>："ERROR"
<strong>提示</strong>：0.1 无法被二进制准确表示
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>32位包括输出中的 <code>"0."</code> 这两位。</li>
	<li>题目保证输入用例的小数位数最多只有 <code>6</code> 位</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数学
- 字符串

## 提示

1. 为了解决这个问题，试着想想如何用它来处理整数。
2. 像0.893这样的数字（以10为底），每个数字代表什么？那么以2为底的0.10 010中的每个数字代表什么？
3. 一个数字如0.893（以10为底）表示8×101 + 9×102 + 3×103。将此系统转换为以2为底。
4. 你将如何获得0.893中的第一个数字？如果乘以10，那么你会改变值得到8.93。如果乘以2，结果会是什么？
5. 想想那些不能用二进制精确表示的值会发生什么。

## 示例

```
0.625
0.1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string printBin(double num) {
        
    }
};
```

### Java

```java
class Solution {
    public String printBin(double num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def printBin(self, num):
        """
        :type num: float
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def printBin(self, num: float) -> str:
        
```

### C

```c
char* printBin(double num) {
    
}
```

### C#

```csharp
public class Solution {
    public string PrintBin(double num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {string}
 */
var printBin = function(num) {
    
};
```

### TypeScript

```typescript
function printBin(num: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Float $num
     * @return String
     */
    function printBin($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func printBin(_ num: Double) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun printBin(num: Double): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String printBin(double num) {
    
  }
}
```

### Go

```golang
func printBin(num float64) string {
    
}
```

### Ruby

```ruby
# @param {Float} num
# @return {String}
def print_bin(num)
    
end
```

### Scala

```scala
object Solution {
    def printBin(num: Double): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn print_bin(num: f64) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (print-bin num)
  (-> flonum? string?)
  )
```

### Erlang

```erlang
-spec print_bin(Num :: float()) -> unicode:unicode_binary().
print_bin(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec print_bin(num :: float) :: String.t
  def print_bin(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func printBin(num: Float64): String {

    }
}
```

