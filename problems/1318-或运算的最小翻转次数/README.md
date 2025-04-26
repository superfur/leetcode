# 1318. 或运算的最小翻转次数

## 题目描述

<p>给你三个正整数&nbsp;<code>a</code>、<code>b</code> 和 <code>c</code>。</p>

<p>你可以对 <code>a</code> 和 <code>b</code>&nbsp;的二进制表示进行位翻转操作，返回能够使按位或运算&nbsp; &nbsp;<code>a</code> OR <code>b</code> == <code>c</code>&nbsp;&nbsp;成立的最小翻转次数。</p>

<p>「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/sample_3_1676.png" style="height: 87px; width: 260px;"></p>

<pre><strong>输入：</strong>a = 2, b = 6, c = 5
<strong>输出：</strong>3
<strong>解释：</strong>翻转后 a = 1 , b = 4 , c = 5 使得 <code>a</code> OR <code>b</code> == <code>c</code></pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>a = 4, b = 2, c = 7
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>a = 1, b = 2, c = 3
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= a &lt;= 10^9</code></li>
	<li><code>1 &lt;= b&nbsp;&lt;= 10^9</code></li>
	<li><code>1 &lt;= c&nbsp;&lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算

## 提示

1. Check the bits one by one whether they need to be flipped.

## 示例

```
2
6
5
4
2
7
1
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minFlips(int a, int b, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public int minFlips(int a, int b, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
```

### C

```c
int minFlips(int a, int b, int c) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinFlips(int a, int b, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var minFlips = function(a, b, c) {
    
};
```

### TypeScript

```typescript
function minFlips(a: number, b: number, c: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function minFlips($a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minFlips(_ a: Int, _ b: Int, _ c: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minFlips(a: Int, b: Int, c: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minFlips(int a, int b, int c) {
    
  }
}
```

### Go

```golang
func minFlips(a int, b int, c int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def min_flips(a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def minFlips(a: Int, b: Int, c: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_flips(a: i32, b: i32, c: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-flips a b c)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_flips(A :: integer(), B :: integer(), C :: integer()) -> integer().
min_flips(A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_flips(a :: integer, b :: integer, c :: integer) :: integer
  def min_flips(a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minFlips(a: Int64, b: Int64, c: Int64): Int64 {

    }
}
```

