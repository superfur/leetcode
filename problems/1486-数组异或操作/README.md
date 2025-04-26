# 1486. 数组异或操作

## 题目描述

<p>给你两个整数，<code>n</code> 和 <code>start</code> 。</p>

<p>数组 <code>nums</code> 定义为：<code>nums[i] = start + 2*i</code>（下标从 0 开始）且 <code>n == nums.length</code> 。</p>

<p>请返回 <code>nums</code> 中所有元素按位异或（<strong>XOR</strong>）后得到的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 5, start = 0
<strong>输出：</strong>8
<strong>解释：</strong>数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     &quot;^&quot; 为按位异或 XOR 运算符。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 4, start = 3
<strong>输出：</strong>8
<strong>解释：</strong>数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 1, start = 7
<strong>输出：</strong>7
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 10, start = 5
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= start &lt;= 1000</code></li>
	<li><code>n == nums.length</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数学

## 提示

1. Simulate the process, create an array nums and return the Bitwise XOR of all elements of it.

## 示例

```
5
0
4
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int xorOperation(int n, int start) {
        
    }
};
```

### Java

```java
class Solution {
    public int xorOperation(int n, int start) {
        
    }
}
```

### Python

```python
class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
```

### C

```c
int xorOperation(int n, int start) {
    
}
```

### C#

```csharp
public class Solution {
    public int XorOperation(int n, int start) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} start
 * @return {number}
 */
var xorOperation = function(n, start) {
    
};
```

### TypeScript

```typescript
function xorOperation(n: number, start: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $start
     * @return Integer
     */
    function xorOperation($n, $start) {
        
    }
}
```

### Swift

```swift
class Solution {
    func xorOperation(_ n: Int, _ start: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun xorOperation(n: Int, start: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int xorOperation(int n, int start) {
    
  }
}
```

### Go

```golang
func xorOperation(n int, start int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} start
# @return {Integer}
def xor_operation(n, start)
    
end
```

### Scala

```scala
object Solution {
    def xorOperation(n: Int, start: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn xor_operation(n: i32, start: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (xor-operation n start)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec xor_operation(N :: integer(), Start :: integer()) -> integer().
xor_operation(N, Start) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec xor_operation(n :: integer, start :: integer) :: integer
  def xor_operation(n, start) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func xorOperation(n: Int64, start: Int64): Int64 {

    }
}
```

