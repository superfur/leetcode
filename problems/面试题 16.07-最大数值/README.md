# 面试题 16.07. 最大数值

## 题目描述

<p>编写一个方法，找出两个数字<code>a</code>和<code>b</code>中最大的那一个。不得使用if-else或其他比较运算符。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong> a = 1, b = 2
<strong>输出：</strong> 2
</pre>


## 难度

Easy

## 标签

- 位运算
- 脑筋急转弯
- 数学

## 提示

1. 如果a > b，则k为1，否则为0。如果给定k，你能返回最大值吗（没有比较或if-else逻辑）？
2. 如果当a > b时，k等于1，那么当k等于0时则相反，然后你可以返回a*k + b* (非k)。但你如何创建k？
3. 当a > b时，a – b > 0。你能得到a – b的符号位吗？
4. 你考虑过如何处理a – b中的整数溢出吗？

## 示例

```
2147483647
-2147483648
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximum(int a, int b) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximum(int a, int b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximum(self, a: int, b: int) -> int:
        
```

### C

```c
int maximum(int a, int b) {
    
}
```

### C#

```csharp
public class Solution {
    public int Maximum(int a, int b) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var maximum = function(a, b) {
    
};
```

### TypeScript

```typescript
function maximum(a: number, b: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @return Integer
     */
    function maximum($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximum(_ a: Int, _ b: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximum(a: Int, b: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximum(int a, int b) {
    
  }
}
```

### Go

```golang
func maximum(a int, b int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def maximum(a, b)
    
end
```

### Scala

```scala
object Solution {
    def maximum(a: Int, b: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum(a: i32, b: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum a b)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum(A :: integer(), B :: integer()) -> integer().
maximum(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum(a :: integer, b :: integer) :: integer
  def maximum(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximum(a: Int64, b: Int64): Int64 {

    }
}
```

