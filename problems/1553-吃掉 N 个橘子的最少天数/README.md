# 1553. 吃掉 N 个橘子的最少天数

## 题目描述

<p>厨房里总共有 <code>n</code>&nbsp;个橘子，你决定每一天选择如下方式之一吃这些橘子：</p>

<ul>
	<li>吃掉一个橘子。</li>
	<li>如果剩余橘子数 <code>n</code>&nbsp;能被 2 整除，那么你可以吃掉 <code>n/2</code> 个橘子。</li>
	<li>如果剩余橘子数&nbsp;<code>n</code>&nbsp;能被 3 整除，那么你可以吃掉 <code>2*(n/3)</code> 个橘子。</li>
</ul>

<p>每天你只能从以上 3 种方案中选择一种方案。</p>

<p>请你返回吃掉所有 <code>n</code>&nbsp;个橘子的最少天数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 10
<strong>输出：</strong>4
<strong>解释：</strong>你总共有 10 个橘子。
第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
你需要至少 4 天吃掉 10 个橘子。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 6
<strong>输出：</strong>3
<strong>解释：</strong>你总共有 6 个橘子。
第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
你至少需要 3 天吃掉 6 个橘子。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>n = 1
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>n = 56
<strong>输出：</strong>6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2*10^9</code></li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 动态规划

## 提示

1. In each step, choose between 2 options:
minOranges = 1 + min( (n%2) + f(n/2), (n%3) + f(n/3) )
where f(n) is the minimum number of days to eat n oranges.

## 示例

```
10
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDays(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDays(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDays(self, n: int) -> int:
        
```

### C

```c
int minDays(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDays(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var minDays = function(n) {
    
};
```

### TypeScript

```typescript
function minDays(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function minDays($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDays(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDays(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDays(int n) {
    
  }
}
```

### Go

```golang
func minDays(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def min_days(n)
    
end
```

### Scala

```scala
object Solution {
    def minDays(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_days(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-days n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_days(N :: integer()) -> integer().
min_days(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_days(n :: integer) :: integer
  def min_days(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDays(n: Int64): Int64 {

    }
}
```

