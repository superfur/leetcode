# 面试题 08.05. 递归乘法

## 题目描述

<p>递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：A = 1, B = 10
<strong> 输出</strong>：10
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：A = 3, B = 4
<strong> 输出</strong>：12
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>保证乘法范围不会溢出</li>
</ol>


## 难度

Medium

## 标签

- 位运算
- 递归
- 数学

## 提示

1. 考虑将8乘以9看作是计算宽度为8、高度为9的矩阵中的单元数。
2. 如果你想计算8×9矩阵中的单元格数，可以先计算4×9矩阵中的单元格数，然后加倍。
3. 想想你如何处理奇数。
4. 如果不同的递归调用有重复的工作，你可以缓存它吗？
5. 如果你在做9×7（都是奇数），那么你可以换成4×7和5×7。
6. 或者，如果你在计算9×7，可以计算4×7，加倍，然后再加7。

## 示例

```
1
10
3
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int multiply(int A, int B) {
        
    }
};
```

### Java

```java
class Solution {
    public int multiply(int A, int B) {
        
    }
}
```

### Python

```python
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def multiply(self, A: int, B: int) -> int:
        
```

### C

```c
int multiply(int A, int B) {
    
}
```

### C#

```csharp
public class Solution {
    public int Multiply(int A, int B) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} A
 * @param {number} B
 * @return {number}
 */
var multiply = function(A, B) {
    
};
```

### TypeScript

```typescript
function multiply(A: number, B: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $A
     * @param Integer $B
     * @return Integer
     */
    function multiply($A, $B) {
        
    }
}
```

### Swift

```swift
class Solution {
    func multiply(_ A: Int, _ B: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun multiply(A: Int, B: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int multiply(int A, int B) {
    
  }
}
```

### Go

```golang
func multiply(A int, B int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def multiply(a, b)
    
end
```

### Scala

```scala
object Solution {
    def multiply(A: Int, B: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn multiply(a: i32, b: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (multiply A B)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec multiply(A :: integer(), B :: integer()) -> integer().
multiply(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec multiply(a :: integer, b :: integer) :: integer
  def multiply(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func multiply(A: Int64, B: Int64): Int64 {

    }
}
```

