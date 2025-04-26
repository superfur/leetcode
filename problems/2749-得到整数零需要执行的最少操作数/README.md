# 2749. 得到整数零需要执行的最少操作数

## 题目描述

<p>给你两个整数：<code>num1</code> 和 <code>num2</code> 。</p>

<p>在一步操作中，你需要从范围&nbsp;<code>[0, 60]</code> 中选出一个整数 <code>i</code> ，并从 <code>num1</code> 减去 <code>2<sup>i</sup> + num2</code> 。</p>

<p>请你计算，要想使 <code>num1</code> 等于 <code>0</code> 需要执行的最少操作数，并以整数形式返回。</p>

<p>如果无法使 <code>num1</code> 等于 <code>0</code> ，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num1 = 3, num2 = -2
<strong>输出：</strong>3
<strong>解释：</strong>可以执行下述步骤使 3 等于 0 ：
- 选择 i = 2 ，并从 3 减去 2<sup>2</sup> + (-2) ，num1 = 3 - (4 + (-2)) = 1 。
- 选择 i = 2 ，并从 1 减去 2<sup>2</sup> + (-2) ，num1 = 1 - (4 + (-2)) = -1 。
- 选择 i = 0 ，并从 -1 减去 2<sup>0</sup>&nbsp;+ (-2) ，num1 = (-1) - (1 + (-2)) = 0 。
可以证明 3 是需要执行的最少操作数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num1 = 5, num2 = 7
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明，执行操作无法使 5 等于 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= num2 &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 脑筋急转弯
- 枚举

## 提示

1. If we want to make integer n equal to 0 by only subtracting powers of 2 from n, in how many operations can we achieve it?
2. We need at least - the number of bits in the binary representation of n, and at most - n.
3. Notice that, if it is possible to make num1 equal to 0, then we need at most 60 operations.
4. Iterate on the number of operations.

## 示例

```
3
-2
5
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        
    }
};
```

### Java

```java
class Solution {
    public int makeTheIntegerZero(int num1, int num2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
```

### C

```c
int makeTheIntegerZero(int num1, int num2) {
    
}
```

### C#

```csharp
public class Solution {
    public int MakeTheIntegerZero(int num1, int num2) {
        
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
var makeTheIntegerZero = function(num1, num2) {
    
};
```

### TypeScript

```typescript
function makeTheIntegerZero(num1: number, num2: number): number {
    
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
    function makeTheIntegerZero($num1, $num2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeTheIntegerZero(_ num1: Int, _ num2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeTheIntegerZero(num1: Int, num2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeTheIntegerZero(int num1, int num2) {
    
  }
}
```

### Go

```golang
func makeTheIntegerZero(num1 int, num2 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def make_the_integer_zero(num1, num2)
    
end
```

### Scala

```scala
object Solution {
    def makeTheIntegerZero(num1: Int, num2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_the_integer_zero(num1: i32, num2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (make-the-integer-zero num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec make_the_integer_zero(Num1 :: integer(), Num2 :: integer()) -> integer().
make_the_integer_zero(Num1, Num2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_the_integer_zero(num1 :: integer, num2 :: integer) :: integer
  def make_the_integer_zero(num1, num2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeTheIntegerZero(num1: Int64, num2: Int64): Int64 {

    }
}
```

