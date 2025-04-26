# 3272. 统计好整数的数目

## 题目描述

<p>给你两个 <strong>正</strong>&nbsp;整数&nbsp;<code>n</code> 和&nbsp;<code>k</code>&nbsp;。</p>

<p>如果一个整数&nbsp;<code>x</code>&nbsp;满足以下条件，那么它被称为 <strong>k</strong><strong>&nbsp;回文</strong>&nbsp;整数&nbsp;。</p>

<ul>
	<li><code>x</code>&nbsp;是一个&nbsp;<span data-keyword="palindrome-integer">回文整数 。</span></li>
	<li><code>x</code>&nbsp;能被 <code>k</code>&nbsp;整除。</li>
</ul>

<p>如果一个整数的数位重新排列后能得到一个 <strong>k 回文整数</strong>&nbsp;，那么我们称这个整数为&nbsp;<strong>好 </strong>整数。比方说，<code>k = 2</code>&nbsp;，那么&nbsp;2020 可以重新排列得到 2002 ，2002 是一个 k 回文串，所以 2020 是一个好整数。而 1010 无法重新排列数位得到一个 k 回文整数。</p>

<p>请你返回 <code>n</code>&nbsp;个数位的整数中，有多少个 <strong>好</strong>&nbsp;整数。</p>

<p><b>注意</b>&nbsp;，任何整数在重新排列数位之前或者之后 <strong>都不能</strong> 有前导 0 。比方说 1010 不能重排列得到&nbsp;101 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 3, k = 5</span></p>

<p><span class="example-io"><b>输出：</b>27</span></p>

<p><b>解释：</b></p>

<p>部分好整数如下：</p>

<ul>
	<li>551 ，因为它可以重排列得到 515 。</li>
	<li>525 ，因为它已经是一个 k 回文整数。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 1, k = 4</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>两个好整数分别是 4 和 8 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, k = 6</span></p>

<p><span class="example-io"><b>输出：</b>2468</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= k &lt;= 9</code></li>
</ul>


## 难度

Hard

## 标签

- 哈希表
- 数学
- 组合数学
- 枚举

## 提示

1. How to generate all K-palindromic strings of length <code>n</code>? Do we need to go through all <code>n</code> digits?
2. Use permutations to calculate the number of possible rearrangements.

## 示例

```
3
5
1
4
5
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countGoodIntegers(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long countGoodIntegers(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
```

### C

```c
long long countGoodIntegers(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountGoodIntegers(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var countGoodIntegers = function(n, k) {
    
};
```

### TypeScript

```typescript
function countGoodIntegers(n: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer
     */
    function countGoodIntegers($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodIntegers(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodIntegers(n: Int, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodIntegers(int n, int k) {
    
  }
}
```

### Go

```golang
func countGoodIntegers(n int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def count_good_integers(n, k)
    
end
```

### Scala

```scala
object Solution {
    def countGoodIntegers(n: Int, k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_integers(n: i32, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-integers n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_integers(N :: integer(), K :: integer()) -> integer().
count_good_integers(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_integers(n :: integer, k :: integer) :: integer
  def count_good_integers(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodIntegers(n: Int64, k: Int64): Int64 {

    }
}
```

