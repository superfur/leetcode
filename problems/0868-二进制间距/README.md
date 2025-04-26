# 868. 二进制间距

## 题目描述

<p>给定一个正整数 <code>n</code>，找到并返回 <code>n</code> 的二进制表示中两个 <strong>相邻</strong> 1 之间的<strong> 最长距离 </strong>。如果不存在两个相邻的 1，返回 <code>0</code> 。</p>

<p>如果只有 <code>0</code> 将两个 <code>1</code> 分隔开（可能不存在 <code>0</code> ），则认为这两个 1 彼此 <strong>相邻</strong> 。两个 <code>1</code> 之间的距离是它们的二进制表示中位置的绝对差。例如，<code>"1001"</code> 中的两个 <code>1</code> 的距离为 3 。</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 22
<strong>输出：</strong>2
<strong>解释：</strong>22 的二进制是 "10110" 。
在 22 的二进制表示中，有三个 1，组成两对相邻的 1 。
第一对相邻的 1 中，两个 1 之间的距离为 2 。
第二对相邻的 1 中，两个 1 之间的距离为 1 。
答案取两个距离之中最大的，也就是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 8
<strong>输出：</strong>0
<strong>解释：</strong>8 的二进制是 "1000" 。
在 8 的二进制表示中没有相邻的两个 1，所以返回 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 5
<strong>输出：</strong>2
<strong>解释：</strong>5 的二进制是 "101" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 位运算

## 示例

```
22
8
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int binaryGap(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int binaryGap(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def binaryGap(self, n: int) -> int:
        
```

### C

```c
int binaryGap(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int BinaryGap(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var binaryGap = function(n) {
    
};
```

### TypeScript

```typescript
function binaryGap(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function binaryGap($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func binaryGap(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun binaryGap(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int binaryGap(int n) {
    
  }
}
```

### Go

```golang
func binaryGap(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def binary_gap(n)
    
end
```

### Scala

```scala
object Solution {
    def binaryGap(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn binary_gap(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (binary-gap n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec binary_gap(N :: integer()) -> integer().
binary_gap(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec binary_gap(n :: integer) :: integer
  def binary_gap(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func binaryGap(n: Int64): Int64 {

    }
}
```

