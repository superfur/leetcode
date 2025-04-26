# 2507. 使用质因数之和替换后可以取到的最小值

## 题目描述

<p>给你一个正整数 <code>n</code> 。</p>

<p>请你将 <code>n</code> 的值替换为 <code>n</code> 的 <strong>质因数</strong> 之和，重复这一过程。</p>

<ul>
	<li>注意，如果 <code>n</code> 能够被某个质因数多次整除，则在求和时，应当包含这个质因数同样次数。</li>
</ul>

<p>返回<em> </em><code>n</code><em> </em>可以取到的最小值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 15
<strong>输出：</strong>5
<strong>解释：</strong>最开始，n = 15 。
15 = 3 * 5 ，所以 n 替换为 3 + 5 = 8 。
8 = 2 * 2 * 2 ，所以 n 替换为 2 + 2 + 2 = 6 。
6 = 2 * 3 ，所以 n 替换为 2 + 3 = 5 。
5 是 n 可以取到的最小值。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>3
<strong>解释：</strong>最开始，n = 3 。
3 是 n 可以取到的最小值。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 数论
- 模拟

## 提示

1. Every time you replace n, it will become smaller until it is a prime number, where it will keep the same value each time you replace it.
2. n decreases logarithmically, allowing you to simulate the process.
3. To find the prime factors, iterate through all numbers less than n from least to greatest and find the maximum number of times each number divides n.

## 示例

```
15
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestValue(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestValue(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestValue(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestValue(self, n: int) -> int:
        
```

### C

```c
int smallestValue(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestValue(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var smallestValue = function(n) {
    
};
```

### TypeScript

```typescript
function smallestValue(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function smallestValue($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestValue(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestValue(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestValue(int n) {
    
  }
}
```

### Go

```golang
func smallestValue(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def smallest_value(n)
    
end
```

### Scala

```scala
object Solution {
    def smallestValue(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_value(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-value n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_value(N :: integer()) -> integer().
smallest_value(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_value(n :: integer) :: integer
  def smallest_value(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestValue(n: Int64): Int64 {

    }
}
```

