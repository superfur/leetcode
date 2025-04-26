# 2429. 最小异或

## 题目描述

<p>给你两个正整数 <code>num1</code> 和 <code>num2</code> ，找出满足下述条件的正整数 <code>x</code> ：</p>

<ul>
	<li><code>x</code> 的置位数和 <code>num2</code> 相同，且</li>
	<li><code>x XOR num1</code> 的值 <strong>最小</strong></li>
</ul>

<p>注意 <code>XOR</code> 是按位异或运算。</p>

<p>返回整数<em> </em><code>x</code> 。题目保证，对于生成的测试用例， <code>x</code> 是 <strong>唯一确定</strong> 的。</p>

<p>整数的 <strong>置位数</strong> 是其二进制表示中 <code>1</code> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num1 = 3, num2 = 5
<strong>输出：</strong>3
<strong>解释：</strong>
num1 和 num2 的二进制表示分别是 0011 和 0101 。
整数 <strong>3</strong> 的置位数与 num2 相同，且 <code>3 XOR 3 = 0</code> 是最小的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num1 = 1, num2 = 12
<strong>输出：</strong>3
<strong>解释：</strong>
num1 和 num2 的二进制表示分别是 0001 和 1100 。
整数 <strong>3</strong> 的置位数与 num2 相同，且 <code>3 XOR 1 = 2</code> 是最小的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num1, num2 &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算

## 提示

1. To arrive at a small xor, try to turn off some bits from num1
2. If there are still left bits to set, try to set them from the least significant bit

## 示例

```
3
5
1
12
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeXor(int num1, int num2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeXor(int num1, int num2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
```

### C

```c
int minimizeXor(int num1, int num2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeXor(int num1, int num2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num1
 * @param {number} num2
 * @return {number}
 */
var minimizeXor = function(num1, num2) {
    
};
```

### TypeScript

```typescript
function minimizeXor(num1: number, num2: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num1
     * @param Integer $num2
     * @return Integer
     */
    function minimizeXor($num1, $num2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeXor(_ num1: Int, _ num2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeXor(num1: Int, num2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeXor(int num1, int num2) {
    
  }
}
```

### Go

```golang
func minimizeXor(num1 int, num2 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def minimize_xor(num1, num2)
    
end
```

### Scala

```scala
object Solution {
    def minimizeXor(num1: Int, num2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_xor(num1: i32, num2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-xor num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_xor(Num1 :: integer(), Num2 :: integer()) -> integer().
minimize_xor(Num1, Num2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_xor(num1 :: integer, num2 :: integer) :: integer
  def minimize_xor(num1, num2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeXor(num1: Int64, num2: Int64): Int64 {

    }
}
```

