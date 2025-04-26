# 2719. 统计整数数目

## 题目描述

<p>给你两个数字字符串&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;，以及两个整数&nbsp;<code>max_sum</code> 和&nbsp;<code>min_sum</code>&nbsp;。如果一个整数&nbsp;<code>x</code>&nbsp;满足以下条件，我们称它是一个好整数：</p>

<ul>
	<li><code>num1 &lt;= x &lt;= num2</code></li>
	<li><code>min_sum &lt;= digit_sum(x) &lt;= max_sum</code>.</li>
</ul>

<p>请你返回好整数的数目。答案可能很大，请返回答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;取余后的结果。</p>

<p>注意，<code>digit_sum(x)</code>&nbsp;表示&nbsp;<code>x</code>&nbsp;各位数字之和。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>num1 = "1", num2 = "12", min_num = 1, max_num = 8
<b>输出：</b>11
<b>解释：</b>总共有 11 个整数的数位和在 1 到 8 之间，分别是 1,2,3,4,5,6,7,8,10,11 和 12 。所以我们返回 11 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>num1 = "1", num2 = "5", min_num = 1, max_num = 5
<b>输出：</b>5
<b>解释：</b>数位和在 1 到 5 之间的 5 个整数分别为 1,2,3,4 和 5 。所以我们返回 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= num2 &lt;= 10<sup>22</sup></code></li>
	<li><code>1 &lt;= min_sum &lt;= max_sum &lt;= 400</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 字符串
- 动态规划

## 提示

1. Let f(n, l, r) denotes the number of integers from 1 to n with the sum of digits between l and r.
2. The answer is f(num2, min_sum, max_sum) - f(num-1, min_sum, max_sum).
3. You can calculate f(n, l, r) using digit dp.

## 示例

```
"1"
"12"
1
8
"1"
"5"
1
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int count(string num1, string num2, int min_sum, int max_sum) {
        
    }
};
```

### Java

```java
class Solution {
    public int count(String num1, String num2, int min_sum, int max_sum) {
        
    }
}
```

### Python

```python
class Solution(object):
    def count(self, num1, num2, min_sum, max_sum):
        """
        :type num1: str
        :type num2: str
        :type min_sum: int
        :type max_sum: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        
```

### C

```c
int count(char* num1, char* num2, int min_sum, int max_sum) {
    
}
```

### C#

```csharp
public class Solution {
    public int Count(string num1, string num2, int min_sum, int max_sum) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num1
 * @param {string} num2
 * @param {number} min_sum
 * @param {number} max_sum
 * @return {number}
 */
var count = function(num1, num2, min_sum, max_sum) {
    
};
```

### TypeScript

```typescript
function count(num1: string, num2: string, min_sum: number, max_sum: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num1
     * @param String $num2
     * @param Integer $min_sum
     * @param Integer $max_sum
     * @return Integer
     */
    function count($num1, $num2, $min_sum, $max_sum) {
        
    }
}
```

### Swift

```swift
class Solution {
    func count(_ num1: String, _ num2: String, _ min_sum: Int, _ max_sum: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int count(String num1, String num2, int min_sum, int max_sum) {
    
  }
}
```

### Go

```golang
func count(num1 string, num2 string, min_sum int, max_sum int) int {
    
}
```

### Ruby

```ruby
# @param {String} num1
# @param {String} num2
# @param {Integer} min_sum
# @param {Integer} max_sum
# @return {Integer}
def count(num1, num2, min_sum, max_sum)
    
end
```

### Scala

```scala
object Solution {
    def count(num1: String, num2: String, min_sum: Int, max_sum: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count(num1: String, num2: String, min_sum: i32, max_sum: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count num1 num2 min_sum max_sum)
  (-> string? string? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count(Num1 :: unicode:unicode_binary(), Num2 :: unicode:unicode_binary(), Min_sum :: integer(), Max_sum :: integer()) -> integer().
count(Num1, Num2, Min_sum, Max_sum) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count(num1 :: String.t, num2 :: String.t, min_sum :: integer, max_sum :: integer) :: integer
  def count(num1, num2, min_sum, max_sum) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func count(num1: String, num2: String, min_sum: Int64, max_sum: Int64): Int64 {

    }
}
```

