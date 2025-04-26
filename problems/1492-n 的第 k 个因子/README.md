# 1492. n 的第 k 个因子

## 题目描述

<p>给你两个正整数&nbsp;<code>n</code> 和&nbsp;<code>k</code>&nbsp;。</p>

<p>如果正整数 <code>i</code> 满足 <code>n % i == 0</code> ，那么我们就说正整数 <code>i</code> 是整数 <code>n</code>&nbsp;的因子。</p>

<p>考虑整数 <code>n</code>&nbsp;的所有因子，将它们 <strong>升序排列</strong>&nbsp;。请你返回第 <code>k</code>&nbsp;个因子。如果 <code>n</code>&nbsp;的因子数少于 <code>k</code>&nbsp;，请你返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 12, k = 3
<strong>输出：</strong>3
<strong>解释：</strong>因子列表包括 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 7, k = 2
<strong>输出：</strong>7
<strong>解释：</strong>因子列表包括 [1, 7] ，第 2 个因子是 7 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4, k = 4
<strong>输出：</strong>-1
<strong>解释：</strong>因子列表包括 [1, 2, 4] ，只有 3 个因子，所以我们应该返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= n &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你可以设计时间复杂度小于 O(n) 的算法来解决此问题吗？</p>


## 难度

Medium

## 标签

- 数学
- 数论

## 提示

1. The factors of n will be always in the range [1, n].
2. Keep a list of all factors sorted.  Loop i from 1 to n and add i if n % i == 0. Return the kth factor if it exist in this list.

## 示例

```
12
3
7
2
4
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kthFactor(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kthFactor(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
```

### C

```c
int kthFactor(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KthFactor(int n, int k) {
        
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
var kthFactor = function(n, k) {
    
};
```

### TypeScript

```typescript
function kthFactor(n: number, k: number): number {
    
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
    function kthFactor($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthFactor(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthFactor(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kthFactor(int n, int k) {
    
  }
}
```

### Go

```golang
func kthFactor(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def kth_factor(n, k)
    
end
```

### Scala

```scala
object Solution {
    def kthFactor(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_factor(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (kth-factor n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec kth_factor(N :: integer(), K :: integer()) -> integer().
kth_factor(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_factor(n :: integer, k :: integer) :: integer
  def kth_factor(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthFactor(n: Int64, k: Int64): Int64 {

    }
}
```

