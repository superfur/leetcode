# 面试题 05.01. 插入

## 题目描述

<p>给定两个整型数字 <code>N</code> 与 <code>M</code>，以及表示比特位置的 <code>i</code> 与 <code>j</code>（<code>i &lt;= j</code>，且从 0 位开始计算）。</p>

<p>编写一种方法，使 <code>M</code> 对应的二进制数字插入 <code>N</code> 对应的二进制数字的第 <code>i ~ j</code> 位区域，不足之处用 <code>0</code> 补齐。具体插入过程如图所示。</p>

<p><img alt="" src="https://pic.leetcode-cn.com/1610104070-NuLVQi-05.01.gif" style="width: 267px; height: 200px;" /></p>

<p>题目保证从 <code>i</code> 位到 <code>j</code> 位足以容纳 <code>M</code>， 例如： <code>M = 10011</code>，则 <code>i～j</code> 区域至少可容纳 5 位。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
<strong> 输出</strong>：N = 1100(10001001100)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：N = 0, M = 31(11111), i = 0, j = 4
<strong> 输出</strong>：N = 31(11111)
</pre>


## 难度

Easy

## 标签

- 位运算

## 提示

1. 把这个分成几个部分。先将精力放在清除适当的位上。
2. 要清除这些位，创建一个看起来像是一系列1，然后是0，然后是1的“位掩码”。
3. 在开始或结束时很容易创建一个0的位掩码。但是，有一堆0时，你如何在中间创建一个零位掩码？简单的做法是，为左侧创建一个位掩码，然后为右侧创建一个位掩码。然后你可以合并两边。

## 示例

```
1024
19
2
6
0
31
0
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int insertBits(int N, int M, int i, int j) {
        
    }
};
```

### Java

```java
class Solution {
    public int insertBits(int N, int M, int i, int j) {
        
    }
}
```

### Python

```python
class Solution(object):
    def insertBits(self, N, M, i, j):
        """
        :type N: int
        :type M: int
        :type i: int
        :type j: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        
```

### C

```c
int insertBits(int N, int M, int i, int j) {
    
}
```

### C#

```csharp
public class Solution {
    public int InsertBits(int N, int M, int i, int j) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} N
 * @param {number} M
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
var insertBits = function(N, M, i, j) {
    
};
```

### TypeScript

```typescript
function insertBits(N: number, M: number, i: number, j: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $N
     * @param Integer $M
     * @param Integer $i
     * @param Integer $j
     * @return Integer
     */
    function insertBits($N, $M, $i, $j) {
        
    }
}
```

### Swift

```swift
class Solution {
    func insertBits(_ N: Int, _ M: Int, _ i: Int, _ j: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun insertBits(N: Int, M: Int, i: Int, j: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int insertBits(int N, int M, int i, int j) {
    
  }
}
```

### Go

```golang
func insertBits(N int, M int, i int, j int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} m
# @param {Integer} i
# @param {Integer} j
# @return {Integer}
def insert_bits(n, m, i, j)
    
end
```

### Scala

```scala
object Solution {
    def insertBits(N: Int, M: Int, i: Int, j: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn insert_bits(n: i32, m: i32, i: i32, j: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (insert-bits N M i j)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec insert_bits(N :: integer(), M :: integer(), I :: integer(), J :: integer()) -> integer().
insert_bits(N, M, I, J) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec insert_bits(n :: integer, m :: integer, i :: integer, j :: integer) :: integer
  def insert_bits(n, m, i, j) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func insertBits(N: Int64, M: Int64, i: Int64, j: Int64): Int64 {

    }
}
```

