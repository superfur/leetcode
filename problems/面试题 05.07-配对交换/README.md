# 面试题 05.07. 配对交换

## 题目描述

<p>配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位 0 与位 1 交换，位 2 与位 3 交换，以此类推）。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：num = 2（或者 0b10）
<strong> 输出：</strong>1 (或者 0b01)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：num = 3
<strong> 输出</strong>：3
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li><code>num</code>&nbsp;的范围在[0, 2<sup>30</sup> - 1]之间，不会发生整数溢出。</li>
</ol>


## 难度

Easy

## 标签

- 位运算

## 提示

1. 交换每一对意味着把偶数位移到左边，奇数位移到右边。你能把这个问题分成几个部分吗？
2. 你能创建一个代表偶数位的数字吗？那么你可以将偶数位移过一位吗？
3. 二进制的1010等价于十进制的10，也相当于十六进制的0xA。那么二进制的101010...在十六进制中是什么？也就是说，你要如何表示1在奇数位上的1和0交替序列？如果反过来呢（1在偶数位）？
4. 尝试用掩码0xaaaaaaaa和0x55555555提取偶数位和奇数位。然后尝试移动偶数位和奇数位来创建正确的数字。

## 示例

```
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int exchangeBits(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int exchangeBits(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def exchangeBits(self, num: int) -> int:
        
```

### C

```c
int exchangeBits(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int ExchangeBits(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var exchangeBits = function(num) {
    
};
```

### TypeScript

```typescript
function exchangeBits(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function exchangeBits($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func exchangeBits(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun exchangeBits(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int exchangeBits(int num) {
    
  }
}
```

### Go

```golang
func exchangeBits(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def exchange_bits(num)
    
end
```

### Scala

```scala
object Solution {
    def exchangeBits(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn exchange_bits(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (exchange-bits num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec exchange_bits(Num :: integer()) -> integer().
exchange_bits(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec exchange_bits(num :: integer) :: integer
  def exchange_bits(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func exchangeBits(num: Int64): Int64 {

    }
}
```

