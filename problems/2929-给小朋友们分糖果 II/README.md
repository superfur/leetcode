# 2929. 给小朋友们分糖果 II

## 题目描述

<p>给你两个正整数&nbsp;<code>n</code> 和&nbsp;<code>limit</code>&nbsp;。</p>

<p>请你将 <code>n</code>&nbsp;颗糖果分给 <code>3</code>&nbsp;位小朋友，确保没有任何小朋友得到超过 <code>limit</code>&nbsp;颗糖果，请你返回满足此条件下的&nbsp;<strong>总方案数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 5, limit = 2
<b>输出：</b>3
<b>解释：</b>总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, limit = 3
<b>输出：</b>10
<b>解释：</b>总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0, 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 组合数学
- 枚举

## 提示

1. We can enumerate the number of candies of one particular child, let it be <code>i</code> which means <code>0 <= i <= min(limit, n)</code>.
2. Suppose the 2nd child gets <code>j</code> candies. Then <code>0 <= j <= limit</code> and <code>i + j <= n</code>.
3. The 3rd child will hence get <code>n - i - j</code> candies and we should have <code>0 <= n - i - j <= limit</code>.
4. After some transformations, for each <code>i</code>, we have <code>max(0, n - i - limit) <= j <= min(limit, n - i)</code>, each <code>j</code> corresponding to a solution.
So the number of solutions for some <code>i</code> is <code>max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)</code>. Sum the expression for every <code>i</code> in <code>[0, min(n, limit)]</code>.

## 示例

```
5
2
3
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long distributeCandies(int n, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public long distributeCandies(int n, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distributeCandies(self, n, limit):
        """
        :type n: int
        :type limit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
```

### C

```c
long long distributeCandies(int n, int limit) {
    
}
```

### C#

```csharp
public class Solution {
    public long DistributeCandies(int n, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} limit
 * @return {number}
 */
var distributeCandies = function(n, limit) {
    
};
```

### TypeScript

```typescript
function distributeCandies(n: number, limit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $limit
     * @return Integer
     */
    function distributeCandies($n, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distributeCandies(_ n: Int, _ limit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distributeCandies(n: Int, limit: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int distributeCandies(int n, int limit) {
    
  }
}
```

### Go

```golang
func distributeCandies(n int, limit int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
    
end
```

### Scala

```scala
object Solution {
    def distributeCandies(n: Int, limit: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distribute_candies(n: i32, limit: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (distribute-candies n limit)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec distribute_candies(N :: integer(), Limit :: integer()) -> integer().
distribute_candies(N, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distribute_candies(n :: integer, limit :: integer) :: integer
  def distribute_candies(n, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distributeCandies(n: Int64, limit: Int64): Int64 {

    }
}
```

