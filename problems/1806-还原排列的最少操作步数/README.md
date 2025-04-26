# 1806. 还原排列的最少操作步数

## 题目描述

<p>给你一个偶数 <code>n</code>​​​​​​ ，已知存在一个长度为 <code>n</code> 的排列 <code>perm</code> ，其中 <code>perm[i] == i</code>​（下标 <strong>从 0 开始</strong> 计数）。</p>

<p>一步操作中，你将创建一个新数组 <code>arr</code> ，对于每个 <code>i</code> ：</p>

<ul>
	<li>如果 <code>i % 2 == 0</code> ，那么 <code>arr[i] = perm[i / 2]</code></li>
	<li>如果 <code>i % 2 == 1</code> ，那么 <code>arr[i] = perm[n / 2 + (i - 1) / 2]</code></li>
</ul>

<p>然后将 <code>arr</code>​​ 赋值​​给 <code>perm</code> 。</p>

<p>要想使 <code>perm</code> 回到排列初始值，至少需要执行多少步操作？返回最小的 <strong>非零</strong> 操作步数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>1
<strong>解释：</strong>最初，perm = [0,1]
第 1 步操作后，perm = [0,1]
所以，仅需执行 1 步操作</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>2
<strong>解释：</strong>最初，perm = [0,1,2,3]
第 1 步操作后，perm = [0,2,1,3]
第 2 步操作后，perm = [0,1,2,3]
所以，仅需执行 2 步操作</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 6
<strong>输出：</strong>4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 1000</code></li>
	<li><code>n</code>​​​​​​ 是一个偶数</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 模拟

## 提示

1. It is safe to assume the number of  operations isn't more than n
2. The number is small enough to apply a brute force solution.

## 示例

```
2
4
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reinitializePermutation(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int reinitializePermutation(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        
```

### C

```c
int reinitializePermutation(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReinitializePermutation(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var reinitializePermutation = function(n) {
    
};
```

### TypeScript

```typescript
function reinitializePermutation(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function reinitializePermutation($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reinitializePermutation(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reinitializePermutation(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reinitializePermutation(int n) {
    
  }
}
```

### Go

```golang
func reinitializePermutation(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def reinitialize_permutation(n)
    
end
```

### Scala

```scala
object Solution {
    def reinitializePermutation(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reinitialize_permutation(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reinitialize-permutation n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec reinitialize_permutation(N :: integer()) -> integer().
reinitialize_permutation(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reinitialize_permutation(n :: integer) :: integer
  def reinitialize_permutation(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reinitializePermutation(n: Int64): Int64 {

    }
}
```

