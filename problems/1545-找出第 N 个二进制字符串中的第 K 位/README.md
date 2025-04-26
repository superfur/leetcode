# 1545. 找出第 N 个二进制字符串中的第 K 位

## 题目描述

<p>给你两个正整数 <code>n</code> 和 <code>k</code>，二进制字符串  <code>S<sub>n</sub></code> 的形成规则如下：</p>

<ul>
	<li><code>S<sub>1</sub> = "0"</code></li>
	<li>当 <code>i > 1</code> 时，<code>S<sub>i</sub> = S<sub>i-1</sub> + "1" + reverse(invert(S<sub>i-1</sub>))</code></li>
</ul>

<p>其中 <code>+</code> 表示串联操作，<code>reverse(x)</code> 返回反转 <code>x</code> 后得到的字符串，而 <code>invert(x)</code> 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）。</p>

<p>例如，符合上述描述的序列的前 4 个字符串依次是：</p>

<ul>
	<li><code>S<sub>1 </sub>= "0"</code></li>
	<li><code>S<sub>2 </sub>= "0<strong>1</strong>1"</code></li>
	<li><code>S<sub>3 </sub>= "011<strong>1</strong>001"</code></li>
	<li><code>S<sub>4</sub> = "0111001<strong>1</strong>0110001"</code></li>
</ul>

<p>请你返回  <code>S<sub>n</sub></code> 的 <strong>第 <code>k</code> 位字符</strong> ，题目数据保证 <code>k</code> 一定在 <code>S<sub>n</sub></code> 长度范围以内。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 1
<strong>输出：</strong>"0"
<strong>解释：</strong>S<sub>3</sub> 为 "<strong>0</strong>111001"，其第 1 位为 "0" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 11
<strong>输出：</strong>"1"
<strong>解释：</strong>S<sub>4</sub> 为 "0111001101<strong>1</strong>0001"，其第 11 位为 "1" 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 1, k = 1
<strong>输出：</strong>"0"
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 3
<strong>输出：</strong>"1"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 20</code></li>
	<li><code>1 <= k <= 2<sup>n</sup> - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 递归
- 字符串
- 模拟

## 提示

1. Since n is small, we can simply simulate the process of constructing S1 to Sn.

## 示例

```
3
1
4
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    char findKthBit(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public char findKthBit(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
```

### C

```c
char findKthBit(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public char FindKthBit(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {character}
 */
var findKthBit = function(n, k) {
    
};
```

### TypeScript

```typescript
function findKthBit(n: number, k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function findKthBit($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKthBit(_ n: Int, _ k: Int) -> Character {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKthBit(n: Int, k: Int): Char {
        
    }
}
```

### Dart

```dart
class Solution {
  String findKthBit(int n, int k) {
    
  }
}
```

### Go

```golang
func findKthBit(n int, k int) byte {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Character}
def find_kth_bit(n, k)
    
end
```

### Scala

```scala
object Solution {
    def findKthBit(n: Int, k: Int): Char = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_kth_bit(n: i32, k: i32) -> char {
        
    }
}
```

### Racket

```racket
(define/contract (find-kth-bit n k)
  (-> exact-integer? exact-integer? char?)
  )
```

### Erlang

```erlang
-spec find_kth_bit(N :: integer(), K :: integer()) -> char().
find_kth_bit(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_kth_bit(n :: integer, k :: integer) :: char
  def find_kth_bit(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKthBit(n: Int64, k: Int64): Rune {

    }
}
```

