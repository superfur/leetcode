# 3233. 统计不是特殊数字的数字数量

## 题目描述

<p>给你两个<strong> 正整数 </strong><code>l</code> 和 <code>r</code>。对于任何数字 <code>x</code>，<code>x</code> 的所有正因数（除了 <code>x</code> 本身）被称为 <code>x</code> 的 <strong>真因数</strong>。</p>

<p><span class="text-only" data-eleid="13" style="white-space: pre;">如果一个数字恰好仅有两个</span> <strong>真因数</strong>，则称该数字为 <strong>特殊数字</strong>。例如：</p>

<ul>
	<li>数字 4 是<strong> 特殊数字</strong>，因为它的真因数为 1 和 2。</li>
	<li>数字 6 不是 <strong>特殊数字</strong>，因为它的真因数为 1、2 和 3。</li>
</ul>

<p>返回区间 <code>[l, r]</code> 内<strong> 不是 特殊数字 </strong>的数字数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">l = 5, r = 7</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>区间 <code>[5, 7]</code> 内不存在特殊数字。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">l = 4, r = 16</span></p>

<p><strong>输出：</strong> <span class="reset-io">11</span></p>

<p><strong>解释：</strong></p>

<p>区间 <code>[4, 16]</code> 内的特殊数字为 4 和 9。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= l &lt;= r &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 数论

## 提示

1. A special number must be a square of a prime number.
2. We need to find all primes in the range <code>[sqrt(l), sqrt(r)]</code>.
3. Use sieve to find primes till <code>sqrt(10<sup>9</sup>)</code>.

## 示例

```
5
7
4
16
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nonSpecialCount(int l, int r) {
        
    }
};
```

### Java

```java
class Solution {
    public int nonSpecialCount(int l, int r) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nonSpecialCount(self, l, r):
        """
        :type l: int
        :type r: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        
```

### C

```c
int nonSpecialCount(int l, int r) {
    
}
```

### C#

```csharp
public class Solution {
    public int NonSpecialCount(int l, int r) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var nonSpecialCount = function(l, r) {
    
};
```

### TypeScript

```typescript
function nonSpecialCount(l: number, r: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function nonSpecialCount($l, $r) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nonSpecialCount(_ l: Int, _ r: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nonSpecialCount(l: Int, r: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nonSpecialCount(int l, int r) {
    
  }
}
```

### Go

```golang
func nonSpecialCount(l int, r int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def non_special_count(l, r)
    
end
```

### Scala

```scala
object Solution {
    def nonSpecialCount(l: Int, r: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn non_special_count(l: i32, r: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (non-special-count l r)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec non_special_count(L :: integer(), R :: integer()) -> integer().
non_special_count(L, R) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec non_special_count(l :: integer, r :: integer) :: integer
  def non_special_count(l, r) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nonSpecialCount(l: Int64, r: Int64): Int64 {

    }
}
```

