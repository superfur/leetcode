# 357. 统计各位数字都不同的数字个数

## 题目描述

给你一个整数 <code>n</code> ，统计并返回各位数字都不同的数字 <code>x</code> 的个数，其中 <code>0 &lt;= x &lt; 10<sup>n</sup></code><sup>&nbsp;</sup>。
<div class="original__bRMd">
<div>
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>91
<strong>解释：</strong>答案应为除去 <code>11、22、33、44、55、66、77、88、99 </code>外，在 0 ≤ x &lt; 100 范围内的所有数字。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 0
<strong>输出：</strong>1
</pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 8</code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 动态规划
- 回溯

## 提示

1. A direct way is to use the backtracking approach.
2. Backtracking should contains three states which are (the current number, number of steps to get that number and a bitmask which represent which number is marked as visited so far in the current number). Start with state (0,0,0) and count all valid number till we reach number of steps equals to 10<sup>n</sup>.
3. This problem can also be solved using a dynamic programming approach and some knowledge of combinatorics.
4. Let f(k) = count of numbers with unique digits with length equals k.
5. f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2) [The first factor is 9 because a number cannot start with 0].

## 示例

```
2
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        
```

### C

```c
int countNumbersWithUniqueDigits(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountNumbersWithUniqueDigits(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    
};
```

### TypeScript

```typescript
function countNumbersWithUniqueDigits(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countNumbersWithUniqueDigits($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countNumbersWithUniqueDigits(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countNumbersWithUniqueDigits(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countNumbersWithUniqueDigits(int n) {
    
  }
}
```

### Go

```golang
func countNumbersWithUniqueDigits(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_numbers_with_unique_digits(n)
    
end
```

### Scala

```scala
object Solution {
    def countNumbersWithUniqueDigits(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-numbers-with-unique-digits n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_numbers_with_unique_digits(N :: integer()) -> integer().
count_numbers_with_unique_digits(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_numbers_with_unique_digits(n :: integer) :: integer
  def count_numbers_with_unique_digits(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countNumbersWithUniqueDigits(n: Int64): Int64 {

    }
}
```

