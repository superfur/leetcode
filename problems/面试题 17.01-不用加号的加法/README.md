# 面试题 17.01. 不用加号的加法

## 题目描述

<p>设计一个函数把两个数字相加。不得使用 + 或者其他算术运算符。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>a = 1, b = 1
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>a</code>,&nbsp;<code>b</code>&nbsp;均可能是负数或 0</li>
	<li>结果不会溢出 32 位整数</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数学

## 提示

1. 手动（慢慢地）完成二进制加法，尝试真正理解发生了什么。
2. 你可以把二进制加法看成是对数字的每一位进行迭代、两位进行加和，并在必要时进位。你也可以对操作进行分组。如果首先对每位相加（不进位）会怎样？之后，你可以再处理进位。
3. 只关注上面的一个步骤。如果你“忘记”进位，那么加法操作会是什么样子?
4. 仅相加步骤就可以做如下转化：1 + 1 -> 0，1 + 0 -> 1，0 + 1 -> 1，0 + 0 -> 0。没有+号要怎么做?
5. 可以使用XOR执行加法步骤。
6. 现在关注进位。在什么情况下两个值会进位？如何使用进位？
7. 进位在1 + 1时发生。如何将进位应用到数值中？
8. 可以用AND运算来计算进位。如何使用它？
9. 你可能需要不止一次地执行加法/进位操作。将进位加到和中可能会产生新的进位值

## 示例

```
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int add(int a, int b) {
        
    }
};
```

### Java

```java
class Solution {
    public int add(int a, int b) {
        
    }
}
```

### Python

```python
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def add(self, a: int, b: int) -> int:
        
```

### C

```c
int add(int a, int b) {
    
}
```

### C#

```csharp
public class Solution {
    public int Add(int a, int b) {
        
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
var add = function(a, b) {
    
};
```

### TypeScript

```typescript
function add(a: number, b: number): number {
    
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
    function add($a, $b) {
        
    }
}
```

### Swift

```swift
class Solution {
    func add(_ a: Int, _ b: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun add(a: Int, b: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int add(int a, int b) {
    
  }
}
```

### Go

```golang
func add(a int, b int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def add(a, b)
    
end
```

### Scala

```scala
object Solution {
    def add(a: Int, b: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn add(a: i32, b: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (add a b)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec add(A :: integer(), B :: integer()) -> integer().
add(A, B) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec add(a :: integer, b :: integer) :: integer
  def add(a, b) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func add(a: Int64, b: Int64): Int64 {

    }
}
```

