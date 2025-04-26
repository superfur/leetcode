# 1269. 停在原地的方案数

## 题目描述

<p>有一个长度为 <code>arrLen</code> 的数组，开始有一个指针在索引 <code>0</code> 处。</p>

<p>每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。</p>

<p>给你两个整数 <code>steps</code> 和 <code>arrLen</code> ，请你计算并返回：在恰好执行 <code>steps</code> 次操作以后，指针仍然指向索引 <code>0</code> 处的方案数。</p>

<p>由于答案可能会很大，请返回方案数 <strong>模</strong> <code>10^9 + 7</code> 后的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>steps = 3, arrLen = 2
<strong>输出：</strong>4
<strong>解释：</strong>3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动
</pre>

<p><strong>示例  2：</strong></p>

<pre>
<strong>输入：</strong>steps = 2, arrLen = 4
<strong>输出：</strong>2
<strong>解释：</strong>2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>steps = 4, arrLen = 2
<strong>输出：</strong>8
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= steps <= 500</code></li>
	<li><code>1 <= arrLen <= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 提示

1. Try with Dynamic programming, dp(pos,steps): number of ways to back pos = 0 using exactly "steps" moves.
2. Notice that the computational complexity does not depend of "arrlen".

## 示例

```
3
2
2
4
4
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numWays(int steps, int arrLen) {
        
    }
};
```

### Java

```java
class Solution {
    public int numWays(int steps, int arrLen) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
```

### C

```c
int numWays(int steps, int arrLen) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumWays(int steps, int arrLen) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} steps
 * @param {number} arrLen
 * @return {number}
 */
var numWays = function(steps, arrLen) {
    
};
```

### TypeScript

```typescript
function numWays(steps: number, arrLen: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $steps
     * @param Integer $arrLen
     * @return Integer
     */
    function numWays($steps, $arrLen) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numWays(_ steps: Int, _ arrLen: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numWays(steps: Int, arrLen: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numWays(int steps, int arrLen) {
    
  }
}
```

### Go

```golang
func numWays(steps int, arrLen int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} steps
# @param {Integer} arr_len
# @return {Integer}
def num_ways(steps, arr_len)
    
end
```

### Scala

```scala
object Solution {
    def numWays(steps: Int, arrLen: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_ways(steps: i32, arr_len: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-ways steps arrLen)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_ways(Steps :: integer(), ArrLen :: integer()) -> integer().
num_ways(Steps, ArrLen) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_ways(steps :: integer, arr_len :: integer) :: integer
  def num_ways(steps, arr_len) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numWays(steps: Int64, arrLen: Int64): Int64 {

    }
}
```

