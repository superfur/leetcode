# 2169. 得到 0 的操作数

## 题目描述

<p>给你两个 <strong>非负</strong> 整数 <code>num1</code> 和 <code>num2</code> 。</p>

<p>每一步 <strong>操作</strong>&nbsp;中，如果 <code>num1 &gt;= num2</code> ，你必须用 <code>num1</code> 减 <code>num2</code> ；否则，你必须用 <code>num2</code> 减 <code>num1</code> 。</p>

<ul>
	<li>例如，<code>num1 = 5</code> 且 <code>num2 = 4</code> ，应该用&nbsp;<code>num1</code> 减 <code>num2</code> ，因此，得到 <code>num1 = 1</code> 和 <code>num2 = 4</code> 。然而，如果 <code>num1 = 4</code>且 <code>num2 = 5</code> ，一步操作后，得到 <code>num1 = 4</code> 和 <code>num2 = 1</code> 。</li>
</ul>

<p>返回使 <code>num1 = 0</code> 或 <code>num2 = 0</code> 的 <strong>操作数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num1 = 2, num2 = 3
<strong>输出：</strong>3
<strong>解释：</strong>
- 操作 1 ：num1 = 2 ，num2 = 3 。由于 num1 &lt; num2 ，num2 减 num1 得到 num1 = 2 ，num2 = 3 - 2 = 1 。
- 操作 2 ：num1 = 2 ，num2 = 1 。由于 num1 &gt; num2 ，num1 减 num2 。
- 操作 3 ：num1 = 1 ，num2 = 1 。由于 num1 == num2 ，num1 减 num2 。
此时 num1 = 0 ，num2 = 1 。由于 num1 == 0 ，不需要再执行任何操作。
所以总操作数是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>num1 = 10, num2 = 10
<strong>输出：</strong>1
<strong>解释：</strong>
- 操作 1 ：num1 = 10 ，num2 = 10 。由于 num1 == num2 ，num1 减 num2 得到 num1 = 10 - 10 = 0 。
此时 num1 = 0 ，num2 = 10 。由于 num1 == 0 ，不需要再执行任何操作。
所以总操作数是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num1, num2 &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 模拟

## 提示

1. Try simulating the process until either of the two integers is zero.
2. Count the number of operations done.

## 示例

```
2
3
10
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countOperations(int num1, int num2) {
        
    }
};
```

### Java

```java
class Solution {
    public int countOperations(int num1, int num2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOperations(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
```

### C

```c
int countOperations(int num1, int num2) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountOperations(int num1, int num2) {
        
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
var countOperations = function(num1, num2) {
    
};
```

### TypeScript

```typescript
function countOperations(num1: number, num2: number): number {
    
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
    function countOperations($num1, $num2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOperations(_ num1: Int, _ num2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOperations(num1: Int, num2: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countOperations(int num1, int num2) {
    
  }
}
```

### Go

```golang
func countOperations(num1 int, num2 int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def count_operations(num1, num2)
    
end
```

### Scala

```scala
object Solution {
    def countOperations(num1: Int, num2: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_operations(num1: i32, num2: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-operations num1 num2)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_operations(Num1 :: integer(), Num2 :: integer()) -> integer().
count_operations(Num1, Num2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_operations(num1 :: integer, num2 :: integer) :: integer
  def count_operations(num1, num2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOperations(num1: Int64, num2: Int64): Int64 {

    }
}
```

