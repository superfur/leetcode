# 2827. 范围中美丽整数的数目

## 题目描述

<p>给你正整数&nbsp;<code>low</code>&nbsp;，<code>high</code>&nbsp;和&nbsp;<code>k</code>&nbsp;。</p>

<p>如果一个数满足以下两个条件，那么它是 <strong>美丽的</strong>&nbsp;：</p>

<ul>
	<li>偶数数位的数目与奇数数位的数目相同。</li>
	<li>这个整数可以被&nbsp;<code>k</code>&nbsp;整除。</li>
</ul>

<p>请你返回范围&nbsp;<code>[low, high]</code>&nbsp;中美丽整数的数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>low = 10, high = 20, k = 3
<b>输出：</b>2
<b>解释：</b>给定范围中有 2 个美丽数字：[12,18]
- 12 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。
- 18 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 3 整除。
以下是一些不是美丽整数的例子：
- 16 不是美丽整数，因为它不能被 k = 3 整除。
- 15 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。
给定范围内总共有 2 个美丽整数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>low = 1, high = 10, k = 1
<b>输出：</b>1
<b>解释：</b>给定范围中有 1 个美丽数字：[10]
- 10 是美丽整数，因为它有 1 个奇数数位和 1 个偶数数位，而且可以被 k = 1 整除。
给定范围内总共有 1 个美丽整数。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>low = 5, high = 5, k = 2
<b>输出：</b>0
<b>解释：</b>给定范围中有 0 个美丽数字。
- 5 不是美丽整数，因为它的奇数数位和偶数数位的数目不相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt; low &lt;= high &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt; k &lt;= 20</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划

## 提示

1. <div class="_1l1MA">The intended solution uses Dynamic Programming.</div>
2. <div class="_1l1MA">Let <code> f(n) </code> denote number of beautiful integers in the range <code> [1…n] </code>, then the answer is <code> f(r) - f(l-1) </code>.</div>

## 示例

```
10
20
3
1
10
1
5
5
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfBeautifulIntegers(int low, int high, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfBeautifulIntegers(int low, int high, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfBeautifulIntegers(self, low, high, k):
        """
        :type low: int
        :type high: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
```

### C

```c
int numberOfBeautifulIntegers(int low, int high, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfBeautifulIntegers(int low, int high, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} low
 * @param {number} high
 * @param {number} k
 * @return {number}
 */
var numberOfBeautifulIntegers = function(low, high, k) {
    
};
```

### TypeScript

```typescript
function numberOfBeautifulIntegers(low: number, high: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $low
     * @param Integer $high
     * @param Integer $k
     * @return Integer
     */
    function numberOfBeautifulIntegers($low, $high, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfBeautifulIntegers(_ low: Int, _ high: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfBeautifulIntegers(low: Int, high: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfBeautifulIntegers(int low, int high, int k) {
    
  }
}
```

### Go

```golang
func numberOfBeautifulIntegers(low int, high int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} low
# @param {Integer} high
# @param {Integer} k
# @return {Integer}
def number_of_beautiful_integers(low, high, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfBeautifulIntegers(low: Int, high: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_beautiful_integers(low: i32, high: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-beautiful-integers low high k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_beautiful_integers(Low :: integer(), High :: integer(), K :: integer()) -> integer().
number_of_beautiful_integers(Low, High, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_beautiful_integers(low :: integer, high :: integer, k :: integer) :: integer
  def number_of_beautiful_integers(low, high, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfBeautifulIntegers(low: Int64, high: Int64, k: Int64): Int64 {

    }
}
```

