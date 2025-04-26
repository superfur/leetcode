# 面试题 08.01. 三步问题

## 题目描述

<p>三步问题。有个小孩正在上楼梯，楼梯有 n 阶台阶，小孩一次可以上 1 阶、2 阶或 3 阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模 1000000007。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：n = 3 
<strong> 输出</strong>：4
<strong> 说明：</strong>有四种走法
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：n = 5
<strong> 输出</strong>：13
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>n 范围在[1, 1000000]之间</li>
</ol>


## 难度

Easy

## 标签

- 记忆化搜索
- 数学
- 动态规划

## 提示

1. 自上而下地处理这个问题。小孩的最后一跳是什么？
2. 如果知道跳到第100级台阶之前的每一级台阶的跳法数量，可以计算第100级台阶的跳法数量吗？
3. 可以通过步数99、98、97的数量，来计算100步的数量。这对应孩子最后迈1步、2步或3步。我们把它们加起来还是相乘？也就是说，它是f(100) = f(99) + f(98)+ f(97) 或者f(100) = f(99)×f(98)×f(97)吗？
4. 当“我们这样做然后那样做”时，将这些值相乘。当“我们这样做或者那样做”时，将这些值相加。
5. 这个方法的运行时间是多少？仔细想想。你能优化它吗？
6. 尝试用制表法的方式优化效率低下的递归过程。

## 示例

```
3
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int waysToStep(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int waysToStep(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToStep(self, n: int) -> int:
        
```

### C

```c
int waysToStep(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int WaysToStep(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var waysToStep = function(n) {
    
};
```

### TypeScript

```typescript
function waysToStep(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function waysToStep($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToStep(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToStep(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToStep(int n) {
    
  }
}
```

### Go

```golang
func waysToStep(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def ways_to_step(n)
    
end
```

### Scala

```scala
object Solution {
    def waysToStep(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_step(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-step n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_step(N :: integer()) -> integer().
ways_to_step(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_step(n :: integer) :: integer
  def ways_to_step(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToStep(n: Int64): Int64 {

    }
}
```

