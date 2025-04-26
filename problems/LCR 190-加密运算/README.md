# LCR 190. 加密运算

## 题目描述

<p>计算机安全专家正在开发一款高度安全的加密通信软件，需要在进行数据传输时对数据进行加密和解密操作。假定 <code>dataA</code> 和 <code>dataB</code> 分别为随机抽样的两次通信的数据量：</p>

<ul>
	<li>正数为发送量</li>
	<li>负数为接受量</li>
	<li>0 为数据遗失</li>
</ul>

<p>请不使用四则运算符的情况下实现一个函数计算两次通信的数据量之和（三种情况均需被统计），以确保在数据传输过程中的高安全性和保密性。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>dataA = 5, dataB = -1
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>dataA</code>&nbsp;和 <code>dataB</code>&nbsp;均可能是负数或 0</li>
	<li>结果不会溢出 32 位整数</li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 位运算
- 数学

## 示例

```
5
-1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int encryptionCalculate(int dataA, int dataB) {
        
    }
};
```

### Java

```java
class Solution {
    public int encryptionCalculate(int dataA, int dataB) {
        
    }
}
```

### Python

```python
class Solution(object):
    def encryptionCalculate(self, dataA, dataB):
        """
        :type dataA: int
        :type dataB: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        
```

### C

```c
int encryptionCalculate(int dataA, int dataB) {
    
}
```

### C#

```csharp
public class Solution {
    public int EncryptionCalculate(int dataA, int dataB) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} dataA
 * @param {number} dataB
 * @return {number}
 */
var encryptionCalculate = function(dataA, dataB) {
    
};
```

### TypeScript

```typescript
function encryptionCalculate(dataA: number, dataB: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $dataA
     * @param Integer $dataB
     * @return Integer
     */
    function encryptionCalculate($dataA, $dataB) {
        
    }
}
```

### Swift

```swift
class Solution {
    func encryptionCalculate(_ dataA: Int, _ dataB: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun encryptionCalculate(dataA: Int, dataB: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int encryptionCalculate(int dataA, int dataB) {
    
  }
}
```

### Go

```golang
func encryptionCalculate(dataA int, dataB int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} data_a
# @param {Integer} data_b
# @return {Integer}
def encryption_calculate(data_a, data_b)
    
end
```

### Scala

```scala
object Solution {
    def encryptionCalculate(dataA: Int, dataB: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn encryption_calculate(data_a: i32, data_b: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (encryption-calculate dataA dataB)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec encryption_calculate(DataA :: integer(), DataB :: integer()) -> integer().
encryption_calculate(DataA, DataB) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec encryption_calculate(data_a :: integer, data_b :: integer) :: integer
  def encryption_calculate(data_a, data_b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func encryptionCalculate(dataA: Int64, dataB: Int64): Int64 {

    }
}
```

