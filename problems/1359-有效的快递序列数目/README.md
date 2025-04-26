# 1359. 有效的快递序列数目

## 题目描述

<p>给你&nbsp;<code>n</code>&nbsp;笔订单，每笔订单都需要快递服务。</p>

<p>计算所有有效的 取货 / 交付 可能的顺序，使 delivery(i) 总是在 pickup(i) 之后。</p>

<p>由于答案可能很大，请返回答案对 10^9 + 7 取余的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
<strong>解释：</strong>只有一种序列 (P1, D1)，物品 1 的配送服务（D1）在物品 1 的收件服务（P1）后。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>6
<strong>解释：</strong>所有可能的序列包括：
(P1,P2,D1,D2)，(P1,P2,D2,D1)，(P1,D1,P2,D2)，(P2,P1,D1,D2)，(P2,P1,D2,D1) 和 (P2,D2,P1,D1)。
(P1,D2,P2,D1) 是一个无效的序列，因为物品 2 的收件服务（P2）不应在物品 2 的配送服务（D2）之后。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3
<strong>输出：</strong>90
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. Use the permutation and combination theory to add one (P, D) pair each time until n pairs.

## 示例

```
1
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countOrders(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int countOrders(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countOrders(self, n: int) -> int:
        
```

### C

```c
int countOrders(int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountOrders(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {
    
};
```

### TypeScript

```typescript
function countOrders(n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer
     */
    function countOrders($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOrders(_ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOrders(n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countOrders(int n) {
    
  }
}
```

### Go

```golang
func countOrders(n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer}
def count_orders(n)
    
end
```

### Scala

```scala
object Solution {
    def countOrders(n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_orders(n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-orders n)
  (-> exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_orders(N :: integer()) -> integer().
count_orders(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_orders(n :: integer) :: integer
  def count_orders(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOrders(n: Int64): Int64 {

    }
}
```

