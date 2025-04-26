# 1015. 可被 K 整除的最小整数

## 题目描述

<p>给定正整数 <code>k</code>&nbsp;，你需要找出可以被 <code>k</code>&nbsp;整除的、仅包含数字 <code><strong>1</strong></code> 的最 <strong>小</strong> 正整数 <code>n</code>&nbsp;的长度。</p>

<p>返回 <code>n</code>&nbsp;的长度。如果不存在这样的 <code>n</code>&nbsp;，就返回-1。</p>

<p><strong>注意：</strong> <code>n</code> 可能不符合 64 位带符号整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>k = 1
<strong>输出：</strong>1
<strong>解释：</strong>最小的答案是 n = 1，其长度为 1。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>k = 2
<strong>输出：</strong>-1
<strong>解释：</strong>不存在可被 2 整除的正整数 n 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>k = 3
<strong>输出：</strong>3
<strong>解释：</strong>最小的答案是 n = 111，其长度为 3。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 哈希表
- 数学

## 提示

1. 11111 = 1111 * 10 + 1
We only need to store remainders modulo K.
2. If we never get a remainder of 0, why would that happen, and how would we know that?

## 示例

```
1
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int smallestRepunitDivByK(int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int smallestRepunitDivByK(int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestRepunitDivByK(self, k):
        """
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
```

### C

```c
int smallestRepunitDivByK(int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SmallestRepunitDivByK(int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function(k) {
    
};
```

### TypeScript

```typescript
function smallestRepunitDivByK(k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @return Integer
     */
    function smallestRepunitDivByK($k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestRepunitDivByK(_ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestRepunitDivByK(k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int smallestRepunitDivByK(int k) {
    
  }
}
```

### Go

```golang
func smallestRepunitDivByK(k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {Integer}
def smallest_repunit_div_by_k(k)
    
end
```

### Scala

```scala
object Solution {
    def smallestRepunitDivByK(k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-repunit-div-by-k k)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec smallest_repunit_div_by_k(K :: integer()) -> integer().
smallest_repunit_div_by_k(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_repunit_div_by_k(k :: integer) :: integer
  def smallest_repunit_div_by_k(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestRepunitDivByK(k: Int64): Int64 {

    }
}
```

