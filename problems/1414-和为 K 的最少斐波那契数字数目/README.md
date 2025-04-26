# 1414. 和为 K 的最少斐波那契数字数目

## 题目描述

<p>给你数字 <code>k</code>&nbsp;，请你返回和为&nbsp;<code>k</code>&nbsp;的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。</p>

<p>斐波那契数字定义为：</p>

<ul>
	<li>F<sub>1</sub> = 1</li>
	<li>F<sub>2</sub> = 1</li>
	<li>F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>&nbsp;， 其中 n &gt; 2 。</li>
</ul>

<p>数据保证对于给定的 <code>k</code>&nbsp;，一定能找到可行解。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>k = 7
<strong>输出：</strong>2 
<strong>解释：</strong>斐波那契数字为：1，1，2，3，5，8，13，&hellip;&hellip;
对于 k = 7 ，我们可以得到 2 + 5 = 7 。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>k = 10
<strong>输出：</strong>2 
<strong>解释：</strong>对于 k = 10 ，我们可以得到 2 + 8 = 10 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>k = 19
<strong>输出：</strong>3 
<strong>解释：</strong>对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. Generate all Fibonacci numbers up to the limit (they are few).
2. Use greedy solution, taking at every time the greatest Fibonacci number which is smaller than or equal to the current number. Subtract this Fibonacci number from the current number and repeat again the process.

## 示例

```
7
10
19
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMinFibonacciNumbers(int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMinFibonacciNumbers(int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
```

### C

```c
int findMinFibonacciNumbers(int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMinFibonacciNumbers(int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var findMinFibonacciNumbers = function(k) {
    
};
```

### TypeScript

```typescript
function findMinFibonacciNumbers(k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function findMinFibonacciNumbers($k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMinFibonacciNumbers(_ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMinFibonacciNumbers(k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMinFibonacciNumbers(int k) {
    
  }
}
```

### Go

```golang
func findMinFibonacciNumbers(k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {Integer}
def find_min_fibonacci_numbers(k)
    
end
```

### Scala

```scala
object Solution {
    def findMinFibonacciNumbers(k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_min_fibonacci_numbers(k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-min-fibonacci-numbers k)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_min_fibonacci_numbers(K :: integer()) -> integer().
find_min_fibonacci_numbers(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_min_fibonacci_numbers(k :: integer) :: integer
  def find_min_fibonacci_numbers(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMinFibonacciNumbers(k: Int64): Int64 {

    }
}
```

