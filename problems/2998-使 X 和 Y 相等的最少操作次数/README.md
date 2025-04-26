# 2998. 使 X 和 Y 相等的最少操作次数

## 题目描述

<p>给你两个正整数&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;。</p>

<p>一次操作中，你可以执行以下四种操作之一：</p>

<ol>
	<li>如果 <code>x</code>&nbsp;是 <code>11</code>&nbsp;的倍数，将&nbsp;<code>x</code>&nbsp;除以&nbsp;<code>11</code>&nbsp;。</li>
	<li>如果 <code>x</code>&nbsp;是 <code>5</code>&nbsp;的倍数，将 <code>x</code>&nbsp;除以 <code>5</code>&nbsp;。</li>
	<li>将&nbsp;<code>x</code> 减&nbsp;<code>1</code>&nbsp;。</li>
	<li>将&nbsp;<code>x</code>&nbsp;加&nbsp;<code>1</code>&nbsp;。</li>
</ol>

<p>请你返回让 <code>x</code>&nbsp;和 <code>y</code>&nbsp;相等的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>x = 26, y = 1
<b>输出：</b>3
<b>解释</b><strong>：</strong>我们可以通过以下操作将 26 变为 1 ：
1. 将 x 减 1
2. 将 x 除以 5
3. 将 x 除以 5
将 26 变为 1 最少需要 3 次操作。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>x = 54, y = 2
<b>输出：</b>4
<b>解释：</b>我们可以通过以下操作将 54 变为 2 ：
1. 将 x 加 1
2. 将 x 除以 11
3. 将 x 除以 5
4. 将 x 加 1
将 54 变为 2 最少需要 4 次操作。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>x = 25, y = 30
<b>输出：</b>5
<b>解释：</b>我们可以通过以下操作将 25 变为 30 ：
1. 将 x 加 1
2. 将 x 加 1
3. 将 x 加 1
4. 将 x 加 1
5. 将 x 加 1
将 25 变为 30 最少需要 5 次操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x, y &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 记忆化搜索
- 动态规划

## 提示

1. The only way to make <code>x</code> larger is to increase it by <code>1</code> so if <code>y >= x</code> the answer is <code>y - x</code>.
2. For <code>y < x</code>, <code>x - y</code> is always a candidate answer since we can repeatedly decrease <code>x</code> by one to reach <code>y</code>.
3. We can also increase <code>x</code> and then use the division operations. For example, if <code>x = 10</code> and <code>y = 1</code>, we can increment <code>x</code> by <code>1</code> then divide it by <code>11</code>.
4. Find an upper bound <code>U</code> on the maximum value of <code>x</code> we will reach an optimal solution. Since all values of <code>x</code> will be in the range <code>[1, U]</code>, we can use BFS to find the answer.
5. One possible upper bound on <code>x</code> is <code>U = x + (x - y) </code>. To reach any number strictly greater than <code>U</code> from <code>x</code>, we will need more than <code>x - y</code> operations which is not optimal since we can always reach <code>y</code> in <code>x - y</code> operations.

## 示例

```
26
1
54
2
25
30
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperationsToMakeEqual(int x, int y) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperationsToMakeEqual(int x, int y) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperationsToMakeEqual(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
```

### C

```c
int minimumOperationsToMakeEqual(int x, int y) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperationsToMakeEqual(int x, int y) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var minimumOperationsToMakeEqual = function(x, y) {
    
};
```

### TypeScript

```typescript
function minimumOperationsToMakeEqual(x: number, y: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function minimumOperationsToMakeEqual($x, $y) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperationsToMakeEqual(_ x: Int, _ y: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperationsToMakeEqual(x: Int, y: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperationsToMakeEqual(int x, int y) {
    
  }
}
```

### Go

```golang
func minimumOperationsToMakeEqual(x int, y int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def minimum_operations_to_make_equal(x, y)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperationsToMakeEqual(x: Int, y: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations_to_make_equal(x: i32, y: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations-to-make-equal x y)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations_to_make_equal(X :: integer(), Y :: integer()) -> integer().
minimum_operations_to_make_equal(X, Y) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations_to_make_equal(x :: integer, y :: integer) :: integer
  def minimum_operations_to_make_equal(x, y) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperationsToMakeEqual(x: Int64, y: Int64): Int64 {

    }
}
```

