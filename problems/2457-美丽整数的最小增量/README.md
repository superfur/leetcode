# 2457. 美丽整数的最小增量

## 题目描述

<p>给你两个正整数 <code>n</code> 和 <code>target</code> 。</p>

<p>如果某个整数每一位上的数字相加小于或等于 <code>target</code> ，则认为这个整数是一个 <strong>美丽整数</strong> 。</p>

<p>找出并返回满足 <code>n + x</code> 是 <strong>美丽整数</strong> 的最小非负整数 <code>x</code> 。生成的输入保证总可以使 <code>n</code> 变成一个美丽整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 16, target = 6
<strong>输出：</strong>4
<strong>解释：</strong>最初，n 是 16 ，且其每一位数字的和是 1 + 6 = 7 。在加 4 之后，n 变为 20 且每一位数字的和变成 2 + 0 = 2 。可以证明无法加上一个小于 4 的非负整数使 n 变成一个美丽整数。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 467, target = 6
<strong>输出：</strong>33
<strong>解释：</strong>最初，n 是 467 ，且其每一位数字的和是 4 + 6 + 7 = 17 。在加 33 之后，n 变为 500 且每一位数字的和变成 5 + 0 + 0 = 5 。可以证明无法加上一个小于 33 的非负整数使 n 变成一个美丽整数。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 1, target = 1
<strong>输出：</strong>0
<strong>解释：</strong>最初，n 是 1 ，且其每一位数字的和是 1 ，已经小于等于 target 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>12</sup></code></li>
	<li><code>1 &lt;= target &lt;= 150</code></li>
	<li>生成的输入保证总可以使 <code>n</code> 变成一个美丽整数。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. Think about each digit independently.
2. Turn the rightmost non-zero digit to zero until the digit sum is greater than target.

## 示例

```
16
6
467
6
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long makeIntegerBeautiful(long long n, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public long makeIntegerBeautiful(long n, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
```

### C

```c
long long makeIntegerBeautiful(long long n, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public long MakeIntegerBeautiful(long n, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} target
 * @return {number}
 */
var makeIntegerBeautiful = function(n, target) {
    
};
```

### TypeScript

```typescript
function makeIntegerBeautiful(n: number, target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $target
     * @return Integer
     */
    function makeIntegerBeautiful($n, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeIntegerBeautiful(_ n: Int, _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeIntegerBeautiful(n: Long, target: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeIntegerBeautiful(int n, int target) {
    
  }
}
```

### Go

```golang
func makeIntegerBeautiful(n int64, target int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} target
# @return {Integer}
def make_integer_beautiful(n, target)
    
end
```

### Scala

```scala
object Solution {
    def makeIntegerBeautiful(n: Long, target: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_integer_beautiful(n: i64, target: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (make-integer-beautiful n target)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec make_integer_beautiful(N :: integer(), Target :: integer()) -> integer().
make_integer_beautiful(N, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_integer_beautiful(n :: integer, target :: integer) :: integer
  def make_integer_beautiful(n, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeIntegerBeautiful(n: Int64, target: Int64): Int64 {

    }
}
```

