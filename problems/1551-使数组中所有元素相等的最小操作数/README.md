# 1551. 使数组中所有元素相等的最小操作数

## 题目描述

<p>存在一个长度为 <code>n</code> 的数组 <code>arr</code> ，其中 <code>arr[i] = (2 * i) + 1</code> （ <code>0 &lt;= i &lt; n</code> ）。</p>

<p>一次操作中，你可以选出两个下标，记作 <code>x</code> 和 <code>y</code> （ <code>0 &lt;= x, y &lt; n</code> ）并使 <code>arr[x]</code> 减去 <code>1</code> 、<code>arr[y]</code> 加上 <code>1</code> （即 <code>arr[x] -=1 </code>且 <code>arr[y] += 1</code> ）。最终的目标是使数组中的所有元素都 <strong>相等</strong> 。题目测试用例将会 <strong>保证</strong> ：在执行若干步操作后，数组中的所有元素最终可以全部相等。</p>

<p>给你一个整数 <code>n</code>，即数组的长度。请你返回使数组 <code>arr</code> 中所有元素相等所需的 <strong>最小操作数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>2
<strong>解释：</strong>arr = [1, 3, 5]
第一次操作选出 x = 2 和 y = 0，使数组变为 [2, 3, 4]
第二次操作继续选出 x = 2 和 y = 0，数组将会变成 [3, 3, 3]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 6
<strong>输出：</strong>9
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10^4</code></li>
</ul>


## 难度

Medium

## 标签

- 数学

## 提示

1. Build the array arr using the given formula, define target = sum(arr) / n
2. What is the number of operations needed to convert arr so that all elements equal target ?

## 示例

```
3
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, n: int) -> int:
        
```

### C

```c
int minOperations(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    
};
```

### TypeScript

```typescript
function minOperations(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minOperations($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(int n) {
    
  }
}
```

### Go

```golang
func minOperations(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def min_operations(n)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(N :: integer()) -> integer().
min_operations(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(n :: integer) :: integer
  def min_operations(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(n: Int64): Int64 {

    }
}
```

