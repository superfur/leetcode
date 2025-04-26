# 2595. 奇偶位数

## 题目描述

<p>给你一个 <strong>正</strong> 整数 <code>n</code> 。</p>

<p>用 <code>even</code> 表示在 <code>n</code> 的二进制形式（下标从 <strong>0</strong> 开始）中值为 <code>1</code> 的偶数下标的个数。</p>

<p>用 <code>odd</code> 表示在 <code>n</code> 的二进制形式（下标从 <strong>0</strong> 开始）中值为 <code>1</code> 的奇数下标的个数。</p>

<p>请注意，在数字的二进制表示中，位下标的顺序&nbsp;<strong>从右到左</strong>。</p>

<p>返回整数数组<em> </em><code>answer</code><em> </em>，其中<em> </em><code>answer = [even, odd]</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 50</span></p>

<p><span class="example-io"><b>输出：</b>[1,2]</span></p>

<p><strong>解释：</strong></p>

<p>50 的二进制表示是&nbsp;<code>110010</code>。</p>

<p>在下标 1，4，5 对应的值为&nbsp;1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">n = 2</span></p>

<p><span class="example-io"><b>输出：</b>[0,1]</span></p>

<p><strong>解释：</strong></p>

<p>2 的二进制表示是&nbsp;<code>10</code>。</p>

<p>只有下标 1 对应的值为&nbsp;1。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算

## 提示

1. Maintain two integer variables, even and odd, to count the number of even and odd indices in the binary representation of integer n.
2. Divide n by 2 while n is positive, and if n modulo 2 is 1, add 1 to its corresponding variable.

## 示例

```
50
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> evenOddBit(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] evenOddBit(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* evenOddBit(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] EvenOddBit(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var evenOddBit = function(n) {
    
};
```

### TypeScript

```typescript
function evenOddBit(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function evenOddBit($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func evenOddBit(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun evenOddBit(n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> evenOddBit(int n) {
    
  }
}
```

### Go

```golang
func evenOddBit(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def even_odd_bit(n)
    
end
```

### Scala

```scala
object Solution {
    def evenOddBit(n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn even_odd_bit(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (even-odd-bit n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec even_odd_bit(N :: integer()) -> [integer()].
even_odd_bit(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec even_odd_bit(n :: integer) :: [integer]
  def even_odd_bit(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func evenOddBit(n: Int64): Array<Int64> {

    }
}
```

