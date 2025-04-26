# 629. K 个逆序对数组

## 题目描述

<p>对于一个整数数组&nbsp;<code>nums</code>，<strong>逆序对</strong>是一对满足 <code>0 &lt;= i &lt; j &lt; nums.length</code> 且&nbsp;<code>nums[i] &gt; nums[j]</code>的整数对&nbsp;<code>[i, j]</code>&nbsp;。</p>

<p>给你两个整数&nbsp;<code>n</code>&nbsp;和&nbsp;<code>k</code>，找出所有包含从&nbsp;<code>1</code>&nbsp;到&nbsp;<code>n</code>&nbsp;的数字，且恰好拥有&nbsp;<code>k</code>&nbsp;个 <strong>逆序对</strong> 的不同的数组的个数。由于答案可能很大，只需要返回对 <code>10<sup>9</sup>&nbsp;+ 7</code> 取余的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 0
<strong>输出：</strong>1
<strong>解释：</strong>
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 1
<strong>输出：</strong>2
<strong>解释：</strong>
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 动态规划

## 示例

```
3
0
3
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kInversePairs(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kInversePairs(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        
```

### C

```c
int kInversePairs(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KInversePairs(int n, int k) {
        
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
var kInversePairs = function(n, k) {
    
};
```

### TypeScript

```typescript
function kInversePairs(n: number, k: number): number {
    
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
    function kInversePairs($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kInversePairs(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kInversePairs(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kInversePairs(int n, int k) {
    
  }
}
```

### Go

```golang
func kInversePairs(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def k_inverse_pairs(n, k)
    
end
```

### Scala

```scala
object Solution {
    def kInversePairs(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_inverse_pairs(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (k-inverse-pairs n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_inverse_pairs(N :: integer(), K :: integer()) -> integer().
k_inverse_pairs(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_inverse_pairs(n :: integer, k :: integer) :: integer
  def k_inverse_pairs(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kInversePairs(n: Int64, k: Int64): Int64 {

    }
}
```

