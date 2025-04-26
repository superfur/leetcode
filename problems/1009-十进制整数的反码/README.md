# 1009. 十进制整数的反码

## 题目描述

<p>每个非负整数&nbsp;<code>N</code>&nbsp;都有其二进制表示。例如，&nbsp;<code>5</code>&nbsp;可以被表示为二进制&nbsp;<code>&quot;101&quot;</code>，<code>11</code> 可以用二进制&nbsp;<code>&quot;1011&quot;</code>&nbsp;表示，依此类推。注意，除&nbsp;<code>N = 0</code>&nbsp;外，任何二进制表示中都不含前导零。</p>

<p>二进制的反码表示是将每个&nbsp;<code>1</code>&nbsp;改为&nbsp;<code>0</code>&nbsp;且每个&nbsp;<code>0</code>&nbsp;变为&nbsp;<code>1</code>。例如，二进制数&nbsp;<code>&quot;101&quot;</code>&nbsp;的二进制反码为&nbsp;<code>&quot;010&quot;</code>。</p>

<p>给你一个十进制数&nbsp;<code>N</code>，请你返回其二进制表示的反码所对应的十进制整数。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>5
<strong>输出：</strong>2
<strong>解释：</strong>5 的二进制表示为 &quot;101&quot;，其二进制反码为 &quot;010&quot;，也就是十进制中的 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>7
<strong>输出：</strong>0
<strong>解释：</strong>7 的二进制表示为 &quot;111&quot;，其二进制反码为 &quot;000&quot;，也就是十进制中的 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>10
<strong>输出：</strong>5
<strong>解释：</strong>10 的二进制表示为 &quot;1010&quot;，其二进制反码为 &quot;0101&quot;，也就是十进制中的 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= N &lt; 10^9</code></li>
	<li>本题与 476：<a href="https://leetcode-cn.com/problems/number-complement/">https://leetcode-cn.com/problems/number-complement/</a> 相同</li>
</ol>


## 难度

Easy

## 标签

- 位运算

## 提示

1. A binary number plus its complement will equal 111....111 in binary.  Also, N = 0 is a corner case.

## 示例

```
5
7
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bitwiseComplement(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int bitwiseComplement(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
```

### C

```c
int bitwiseComplement(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int BitwiseComplement(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var bitwiseComplement = function(n) {
    
};
```

### TypeScript

```typescript
function bitwiseComplement(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function bitwiseComplement($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bitwiseComplement(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bitwiseComplement(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bitwiseComplement(int n) {
    
  }
}
```

### Go

```golang
func bitwiseComplement(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def bitwise_complement(n)
    
end
```

### Scala

```scala
object Solution {
    def bitwiseComplement(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (bitwise-complement n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec bitwise_complement(N :: integer()) -> integer().
bitwise_complement(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec bitwise_complement(n :: integer) :: integer
  def bitwise_complement(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bitwiseComplement(n: Int64): Int64 {

    }
}
```

