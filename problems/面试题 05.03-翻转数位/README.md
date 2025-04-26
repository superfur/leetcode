# 面试题 05.03. 翻转数位

## 题目描述

<p>给定一个32位整数 <code>num</code>，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> <code>num</code> = 1775(11011101111<sub>2</sub>)
<strong>输出:</strong> 8
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> <code>num</code> = 7(0111<sub>2</sub>)
<strong>输出:</strong> 4
</pre>


## 难度

Easy

## 标签

- 位运算
- 动态规划

## 提示

1. 先试试蛮力解法。你能尝试一切可能性吗？
2. 把0翻转到1可以合并两个1 的序列，但只有在这两个序列仅被一个0分隔时才可以。
3. 每个序列都可以通过与邻近的序列合并或者直接翻转紧挨着的0来增加其长度。你只需要找到最好的选择。
4. 尝试用线性时间、单次扫描和O(1) 空间完成它。

## 示例

```
0
2147483647
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reverseBits(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int reverseBits(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reverseBits(self, num: int) -> int:
        
```

### C

```c
int reverseBits(int num) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReverseBits(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number}
 */
var reverseBits = function(num) {
    
};
```

### TypeScript

```typescript
function reverseBits(num: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer
     */
    function reverseBits($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reverseBits(_ num: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reverseBits(num: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reverseBits(int num) {
    
  }
}
```

### Go

```golang
func reverseBits(num int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer}
def reverse_bits(num)
    
end
```

### Scala

```scala
object Solution {
    def reverseBits(num: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_bits(num: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-bits num)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec reverse_bits(Num :: integer()) -> integer().
reverse_bits(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_bits(num :: integer) :: integer
  def reverse_bits(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reverseBits(num: Int64): Int64 {

    }
}
```

