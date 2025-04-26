# 717. 1 比特与 2 比特字符

## 题目描述

<p>有两种特殊字符：</p>

<ul>
	<li>第一种字符可以用一比特&nbsp;<code>0</code> 表示</li>
	<li>第二种字符可以用两比特（<code>10</code>&nbsp;或&nbsp;<code>11</code>）表示</li>
</ul>

<p>给你一个以 <code>0</code> 结尾的二进制数组&nbsp;<code>bits</code>&nbsp;，如果最后一个字符必须是一个一比特字符，则返回 <code>true</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> bits = [1, 0, 0]
<strong>输出:</strong> true
<strong>解释:</strong> 唯一的解码方式是将其解析为一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入：</strong>bits = [1,1,1,0]
<strong>输出：</strong>false
<strong>解释：</strong>唯一的解码方式是将其解析为两比特字符和两比特字符。
所以最后一个字符不是一比特字符。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= bits.length &lt;= 1000</code></li>
	<li><code>bits[i]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Keep track of where the next character starts.  At the end, you want to know if you started on the last bit.

## 示例

```
[1,0,0]
[1,1,1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isOneBitCharacter(vector<int>& bits) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isOneBitCharacter(int[] bits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
```

### C

```c
bool isOneBitCharacter(int* bits, int bitsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsOneBitCharacter(int[] bits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    
};
```

### TypeScript

```typescript
function isOneBitCharacter(bits: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $bits
     * @return Boolean
     */
    function isOneBitCharacter($bits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isOneBitCharacter(_ bits: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isOneBitCharacter(bits: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isOneBitCharacter(List<int> bits) {
    
  }
}
```

### Go

```golang
func isOneBitCharacter(bits []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} bits
# @return {Boolean}
def is_one_bit_character(bits)
    
end
```

### Scala

```scala
object Solution {
    def isOneBitCharacter(bits: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-one-bit-character bits)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_one_bit_character(Bits :: [integer()]) -> boolean().
is_one_bit_character(Bits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_one_bit_character(bits :: [integer]) :: boolean
  def is_one_bit_character(bits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isOneBitCharacter(bits: Array<Int64>): Bool {

    }
}
```

