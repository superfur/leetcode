# 1611. 使整数变为 0 的最少操作次数

## 题目描述

<p>给你一个整数 <code>n</code>，你需要重复执行多次下述操作将其转换为 <code>0</code> ：</p>

<ul>
	<li>翻转 <code>n</code> 的二进制表示中最右侧位（第 <code>0</code> 位）。</li>
	<li>如果第 <code>(i-1)</code> 位为 <code>1</code> 且从第 <code>(i-2)</code> 位到第 <code>0</code> 位都为 <code>0</code>，则翻转 <code>n</code> 的二进制表示中的第 <code>i</code> 位。</li>
</ul>

<p>返回将 <code>n</code> 转换为 <code>0</code> 的最小操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>2
<strong>解释：</strong>3 的二进制表示为 "11"
"<strong>1</strong>1" -&gt; "<strong>0</strong>1" ，执行的是第 2 种操作，因为第 0 位为 1 。
"0<strong>1</strong>" -&gt; "0<strong>0</strong>" ，执行的是第 1 种操作。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 6
<strong>输出：</strong>4
<strong>解释：</strong>6 的二进制表示为 "110".
"<strong>1</strong>10" -&gt; "<strong>0</strong>10" ，执行的是第 2 种操作，因为第 1 位为 1 ，第 0 到 0 位为 0 。
"01<strong>0</strong>" -&gt; "01<strong>1</strong>" ，执行的是第 1 种操作。
"0<strong>1</strong>1" -&gt; "0<strong>0</strong>1" ，执行的是第 2 种操作，因为第 0 位为 1 。
"00<strong>1</strong>" -&gt; "00<strong>0</strong>" ，执行的是第 1 种操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 记忆化搜索
- 动态规划

## 提示

1. The fastest way to convert n to zero is to remove all set bits starting from the leftmost one. Try some simple examples to learn the rule of how many steps are needed to remove one set bit.
2. consider n=2^k case first, then solve for all n.

## 示例

```
3
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOneBitOperations(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOneBitOperations(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOneBitOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        
```

### C

```c
int minimumOneBitOperations(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOneBitOperations(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minimumOneBitOperations = function(n) {
    
};
```

### TypeScript

```typescript
function minimumOneBitOperations(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minimumOneBitOperations($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOneBitOperations(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOneBitOperations(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOneBitOperations(int n) {
    
  }
}
```

### Go

```golang
func minimumOneBitOperations(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def minimum_one_bit_operations(n)
    
end
```

### Scala

```scala
object Solution {
    def minimumOneBitOperations(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_one_bit_operations(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-one-bit-operations n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_one_bit_operations(N :: integer()) -> integer().
minimum_one_bit_operations(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_one_bit_operations(n :: integer) :: integer
  def minimum_one_bit_operations(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOneBitOperations(n: Int64): Int64 {

    }
}
```

