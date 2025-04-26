# 2829. k-avoiding 数组的最小总和

## 题目描述

<p>给你两个整数 <code>n</code> 和 <code>k</code> 。</p>

<p>对于一个由 <strong>不同</strong> 正整数组成的数组，如果其中不存在任何求和等于 k 的不同元素对，则称其为 <strong>k-avoiding</strong> 数组。</p>

<p>返回长度为 <code>n</code> 的 <strong>k-avoiding</strong> 数组的可能的最小总和。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5, k = 4
<strong>输出：</strong>18
<strong>解释：</strong>设若 k-avoiding 数组为 [1,2,4,5,6] ，其元素总和为 18 。
可以证明不存在总和小于 18 的 k-avoiding 数组。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 6
<strong>输出：</strong>3
<strong>解释：</strong>可以构造数组 [1,2] ，其元素总和为 3 。
可以证明不存在总和小于 3 的 k-avoiding 数组。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 50</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数学

## 提示

1. <div class="_1l1MA">Try to start with the smallest possible integers.</div>
2. <div class="_1l1MA">Check if the current number can be added to the array.</div>
3. <div class="_1l1MA">To check if the current number can be added, keep track of already added numbers in a set.</div>
4. <div class="_1l1MA">If the number <code>i</code> is added to the array, then <code>i + k</code> can not be added.</div>

## 示例

```
5
4
2
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSum(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSum(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
```

### C

```c
int minimumSum(int n, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSum(int n, int k) {
        
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
var minimumSum = function(n, k) {
    
};
```

### TypeScript

```typescript
function minimumSum(n: number, k: number): number {
    
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
    function minimumSum($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSum(_ n: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSum(n: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSum(int n, int k) {
    
  }
}
```

### Go

```golang
func minimumSum(n int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def minimum_sum(n, k)
    
end
```

### Scala

```scala
object Solution {
    def minimumSum(n: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_sum(n: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-sum n k)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_sum(N :: integer(), K :: integer()) -> integer().
minimum_sum(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_sum(n :: integer, k :: integer) :: integer
  def minimum_sum(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSum(n: Int64, k: Int64): Int64 {

    }
}
```

