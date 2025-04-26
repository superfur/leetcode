# 2485. 找出中枢整数

## 题目描述

<p>给你一个正整数 <code>n</code> ，找出满足下述条件的<strong> 中枢整数</strong> <code>x</code> ：</p>

<ul>
	<li><code>1</code> 和 <code>x</code> 之间的所有元素之和等于 <code>x</code> 和 <code>n</code> 之间所有元素之和。</li>
</ul>

<p>返回中枢整数<em> </em><code>x</code> 。如果不存在中枢整数，则返回 <code>-1</code> 。题目保证对于给定的输入，至多存在一个中枢整数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 8
<strong>输出：</strong>6
<strong>解释：</strong>6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
<strong>解释：</strong>1 是中枢整数，因为 1 = 1 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明不存在满足题目要求的整数。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数学
- 前缀和

## 提示

1. Can you use brute force to check every number from 1 to n if any of them is the pivot integer?
2. If you know the sum of [1: pivot], how can you efficiently calculate the sum of the other parts?

## 示例

```
8
1
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int pivotInteger(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int pivotInteger(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def pivotInteger(self, n: int) -> int:
        
```

### C

```c
int pivotInteger(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int PivotInteger(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    
};
```

### TypeScript

```typescript
function pivotInteger(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function pivotInteger($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pivotInteger(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pivotInteger(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int pivotInteger(int n) {
    
  }
}
```

### Go

```golang
func pivotInteger(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def pivot_integer(n)
    
end
```

### Scala

```scala
object Solution {
    def pivotInteger(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (pivot-integer n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec pivot_integer(N :: integer()) -> integer().
pivot_integer(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pivot_integer(n :: integer) :: integer
  def pivot_integer(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pivotInteger(n: Int64): Int64 {

    }
}
```

