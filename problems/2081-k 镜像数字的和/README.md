# 2081. k 镜像数字的和

## 题目描述

<p>一个 <strong>k 镜像数字</strong>&nbsp;指的是一个在十进制和 k 进制下从前往后读和从后往前读都一样的&nbsp;<strong>没有前导 0</strong>&nbsp;的&nbsp;<strong>正</strong>&nbsp;整数。</p>

<ul>
	<li>比方说，<code>9</code>&nbsp;是一个 2 镜像数字。<code>9</code>&nbsp;在十进制下为&nbsp;<code>9</code>&nbsp;，二进制下为&nbsp;<code>1001</code>&nbsp;，两者从前往后读和从后往前读都一样。</li>
	<li>相反地，<code>4</code>&nbsp;不是一个 2 镜像数字。<code>4</code>&nbsp;在二进制下为&nbsp;<code>100</code>&nbsp;，从前往后和从后往前读不相同。</li>
</ul>

<p>给你进制&nbsp;<code>k</code>&nbsp;和一个数字&nbsp;<code>n</code>&nbsp;，请你返回 k 镜像数字中 <strong>最小</strong> 的 <code>n</code>&nbsp;个数 <strong>之和</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre><b>输入：</b>k = 2, n = 5
<b>输出：</b>25
<strong>解释：
</strong>最小的 5 个 2 镜像数字和它们的二进制表示如下：
  十进制       二进制
    1          1
    3          11
    5          101
    7          111
    9          1001
它们的和为 1 + 3 + 5 + 7 + 9 = 25 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>k = 3, n = 7
<b>输出：</b>499
<strong>解释：
</strong>7 个最小的 3 镜像数字和它们的三进制表示如下：
  十进制       三进制
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
它们的和为 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>k = 7, n = 17
<b>输出：</b>20379000
<b>解释：</b>17 个最小的 7 镜像数字分别为：
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= k &lt;= 9</code></li>
	<li><code>1 &lt;= n &lt;= 30</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 枚举

## 提示

1. Since we need to reduce search space, instead of checking if every number is a palindrome in base-10, can we try to "generate" the palindromic numbers?
2. If you are provided with a d digit number, how can you generate a palindrome with 2*d or 2*d - 1 digit?
3. Try brute-forcing and checking if the palindrome you generated is a "k-Mirror" number.

## 示例

```
2
5
3
7
7
17
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long kMirror(int k, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public long kMirror(int k, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kMirror(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
```

### C

```c
long long kMirror(int k, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public long KMirror(int k, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} k
 * @param {number} n
 * @return {number}
 */
var kMirror = function(k, n) {
    
};
```

### TypeScript

```typescript
function kMirror(k: number, n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $k
     * @param Integer $n
     * @return Integer
     */
    function kMirror($k, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kMirror(_ k: Int, _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kMirror(k: Int, n: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int kMirror(int k, int n) {
    
  }
}
```

### Go

```golang
func kMirror(k int, n int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @param {Integer} n
# @return {Integer}
def k_mirror(k, n)
    
end
```

### Scala

```scala
object Solution {
    def kMirror(k: Int, n: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_mirror(k: i32, n: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (k-mirror k n)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_mirror(K :: integer(), N :: integer()) -> integer().
k_mirror(K, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_mirror(k :: integer, n :: integer) :: integer
  def k_mirror(k, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kMirror(k: Int64, n: Int64): Int64 {

    }
}
```

