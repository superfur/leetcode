# 2376. 统计特殊整数

## 题目描述

<p>如果一个正整数每一个数位都是 <strong>互不相同</strong>&nbsp;的，我们称它是 <strong>特殊整数</strong> 。</p>

<p>给你一个 <strong>正</strong>&nbsp;整数&nbsp;<code>n</code>&nbsp;，请你返回区间<em>&nbsp;</em><code>[1, n]</code>&nbsp;之间特殊整数的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 20
<b>输出：</b>19
<b>解释：</b>1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 5
<b>输出：</b>5
<b>解释：</b>1 到 5 所有整数都是特殊整数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>n = 135
<b>输出：</b>110
<b>解释：</b>从 1 到 135 总共有 110 个整数是特殊整数。
不特殊的部分数字为：22 ，114 和 131 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划

## 提示

1. Try to think of dynamic programming.
2. Use the idea of digit dynamic programming to build the numbers, in addition to a bitmask that will tell which digits you have used so far on the number that you are building.

## 示例

```
20
5
135
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSpecialNumbers(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSpecialNumbers(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSpecialNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        
```

### C

```c
int countSpecialNumbers(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSpecialNumbers(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countSpecialNumbers = function(n) {
    
};
```

### TypeScript

```typescript
function countSpecialNumbers(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countSpecialNumbers($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSpecialNumbers(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSpecialNumbers(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSpecialNumbers(int n) {
    
  }
}
```

### Go

```golang
func countSpecialNumbers(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_special_numbers(n)
    
end
```

### Scala

```scala
object Solution {
    def countSpecialNumbers(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_special_numbers(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-special-numbers n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_special_numbers(N :: integer()) -> integer().
count_special_numbers(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_special_numbers(n :: integer) :: integer
  def count_special_numbers(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSpecialNumbers(n: Int64): Int64 {

    }
}
```

