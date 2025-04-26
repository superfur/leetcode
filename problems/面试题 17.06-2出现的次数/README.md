# 面试题 17.06. 2出现的次数

## 题目描述

<p>编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>25
<strong>输出：</strong>9
<strong>解释：</strong>(2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)</pre>

<p>提示：</p>

<ul>
	<li><code>n &lt;= 10^9</code></li>
</ul>


## 难度

Hard

## 标签

- 递归
- 数学
- 动态规划

## 提示

1. 从蛮力解法开始。
2. 不要计算每一个数中有多少个2，要一位数一位数地想，也就是说，首先计算(对于每个数字)第 1 位中有多少个 2，然后计算(对于每个数字)第 2 位中有多少个 2，再计算(对于每个数字)第 3 位中有多少个 2，以此类推。
3. 是否有一种更快的方法来计算某一特定位在一个数值范围内有多少个 2?注意，任何位的大约 1/10 应该是 2，但这只是大概比例。如何将其表述得更准确些?

## 示例

```
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOf2sInRange(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOf2sInRange(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOf2sInRange(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        
```

### C

```c
int numberOf2sInRange(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOf2sInRange(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var numberOf2sInRange = function(n) {
    
};
```

### TypeScript

```typescript
function numberOf2sInRange(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function numberOf2sInRange($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOf2sInRange(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOf2sInRange(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOf2sInRange(int n) {
    
  }
}
```

### Go

```golang
func numberOf2sInRange(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def number_of2s_in_range(n)
    
end
```

### Scala

```scala
object Solution {
    def numberOf2sInRange(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of2s_in_range(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of2s-in-range n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of2s_in_range(N :: integer()) -> integer().
number_of2s_in_range(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of2s_in_range(n :: integer) :: integer
  def number_of2s_in_range(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOf2sInRange(n: Int64): Int64 {

    }
}
```

