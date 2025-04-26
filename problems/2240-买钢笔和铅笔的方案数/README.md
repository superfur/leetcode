# 2240. 买钢笔和铅笔的方案数

## 题目描述

<p>给你一个整数&nbsp;<code>total</code>&nbsp;，表示你拥有的总钱数。同时给你两个整数&nbsp;<code>cost1</code> 和&nbsp;<code>cost2</code>&nbsp;，分别表示一支钢笔和一支铅笔的价格。你可以花费你部分或者全部的钱，去买任意数目的两种笔。</p>

<p>请你返回购买钢笔和铅笔的&nbsp;<strong>不同方案数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>total = 20, cost1 = 10, cost2 = 5
<b>输出：</b>9
<b>解释：</b>一支钢笔的价格为 10 ，一支铅笔的价格为 5 。
- 如果你买 0 支钢笔，那么你可以买 0 ，1 ，2 ，3 或者 4 支铅笔。
- 如果你买 1 支钢笔，那么你可以买 0 ，1 或者 2 支铅笔。
- 如果你买 2 支钢笔，那么你没法买任何铅笔。
所以买钢笔和铅笔的总方案数为 5 + 3 + 1 = 9 种。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>total = 5, cost1 = 10, cost2 = 10
<b>输出：</b>1
<b>解释：</b>钢笔和铅笔的价格都为 10 ，都比拥有的钱数多，所以你没法购买任何文具。所以只有 1 种方案：买 0 支钢笔和 0 支铅笔。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= total, cost1, cost2 &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数学
- 枚举

## 提示

1. Fix the number of pencils purchased and calculate the number of ways to buy pens.
2. Sum up the number of ways to buy pens for each amount of pencils purchased to get the answer.

## 示例

```
20
10
5
5
10
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long waysToBuyPensPencils(int total, int cost1, int cost2) {
        
    }
};
```

### Java

```java
class Solution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def waysToBuyPensPencils(self, total, cost1, cost2):
        """
        :type total: int
        :type cost1: int
        :type cost2: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        
```

### C

```c
long long waysToBuyPensPencils(int total, int cost1, int cost2) {
    
}
```

### C#

```csharp
public class Solution {
    public long WaysToBuyPensPencils(int total, int cost1, int cost2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} total
 * @param {number} cost1
 * @param {number} cost2
 * @return {number}
 */
var waysToBuyPensPencils = function(total, cost1, cost2) {
    
};
```

### TypeScript

```typescript
function waysToBuyPensPencils(total: number, cost1: number, cost2: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $total
     * @param Integer $cost1
     * @param Integer $cost2
     * @return Integer
     */
    function waysToBuyPensPencils($total, $cost1, $cost2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func waysToBuyPensPencils(_ total: Int, _ cost1: Int, _ cost2: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int waysToBuyPensPencils(int total, int cost1, int cost2) {
    
  }
}
```

### Go

```golang
func waysToBuyPensPencils(total int, cost1 int, cost2 int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer} total
# @param {Integer} cost1
# @param {Integer} cost2
# @return {Integer}
def ways_to_buy_pens_pencils(total, cost1, cost2)
    
end
```

### Scala

```scala
object Solution {
    def waysToBuyPensPencils(total: Int, cost1: Int, cost2: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways_to_buy_pens_pencils(total: i32, cost1: i32, cost2: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (ways-to-buy-pens-pencils total cost1 cost2)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ways_to_buy_pens_pencils(Total :: integer(), Cost1 :: integer(), Cost2 :: integer()) -> integer().
ways_to_buy_pens_pencils(Total, Cost1, Cost2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways_to_buy_pens_pencils(total :: integer, cost1 :: integer, cost2 :: integer) :: integer
  def ways_to_buy_pens_pencils(total, cost1, cost2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func waysToBuyPensPencils(total: Int64, cost1: Int64, cost2: Int64): Int64 {

    }
}
```

