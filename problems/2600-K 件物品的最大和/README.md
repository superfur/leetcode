# 2600. K 件物品的最大和

## 题目描述

<p>袋子中装有一些物品，每个物品上都标记着数字 <code>1</code> 、<code>0</code> 或 <code>-1</code> 。</p>

<p>给你四个非负整数 <code>numOnes</code> 、<code>numZeros</code> 、<code>numNegOnes</code> 和 <code>k</code> 。</p>

<p>袋子最初包含：</p>

<ul>
	<li><code>numOnes</code> 件标记为 <code>1</code> 的物品。</li>
	<li><code>numZeros</code> 件标记为 <code>0</code> 的物品。</li>
	<li><code>numNegOnes</code> 件标记为 <code>-1</code> 的物品。</li>
</ul>

<p>现计划从这些物品中恰好选出 <code>k</code> 件物品。返回所有可行方案中，物品上所标记数字之和的最大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2
<strong>输出：</strong>2
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 2 件标记为 1 的物品，得到的数字之和为 2 。
可以证明 2 是所有可行方案中的最大值。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4
<strong>输出：</strong>3
<strong>解释：</strong>袋子中的物品分别标记为 {1, 1, 1, 0, 0} 。取 3 件标记为 1 的物品，1 件标记为 0 的物品，得到的数字之和为 3 。
可以证明 3 是所有可行方案中的最大值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= numOnes, numZeros, numNegOnes &lt;= 50</code></li>
	<li><code>0 &lt;= k &lt;= numOnes + numZeros + numNegOnes</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数学

## 提示

1. It is always optimal to take items with the number 1 written on them as much as possible.
2. If k > numOnes, after taking all items with the number 1, it is always optimal to take items with the number 0 written on them as much as possible.
3. If k > numOnes + numZeroes we are forced to take k - numOnes - numZeroes -1s.

## 示例

```
3
2
0
2
3
2
0
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kItemsWithMaximumSum(self, numOnes, numZeros, numNegOnes, k):
        """
        :type numOnes: int
        :type numZeros: int
        :type numNegOnes: int
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
```

### C

```c
int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} numOnes
 * @param {number} numZeros
 * @param {number} numNegOnes
 * @param {number} k
 * @return {number}
 */
var kItemsWithMaximumSum = function(numOnes, numZeros, numNegOnes, k) {
    
};
```

### TypeScript

```typescript
function kItemsWithMaximumSum(numOnes: number, numZeros: number, numNegOnes: number, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $numOnes
     * @param Integer $numZeros
     * @param Integer $numNegOnes
     * @param Integer $k
     * @return Integer
     */
    function kItemsWithMaximumSum($numOnes, $numZeros, $numNegOnes, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kItemsWithMaximumSum(_ numOnes: Int, _ numZeros: Int, _ numNegOnes: Int, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
    
  }
}
```

### Go

```golang
func kItemsWithMaximumSum(numOnes int, numZeros int, numNegOnes int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} num_ones
# @param {Integer} num_zeros
# @param {Integer} num_neg_ones
# @param {Integer} k
# @return {Integer}
def k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k)
    
end
```

### Scala

```scala
object Solution {
    def kItemsWithMaximumSum(numOnes: Int, numZeros: Int, numNegOnes: Int, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_items_with_maximum_sum(num_ones: i32, num_zeros: i32, num_neg_ones: i32, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (k-items-with-maximum-sum numOnes numZeros numNegOnes k)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_items_with_maximum_sum(NumOnes :: integer(), NumZeros :: integer(), NumNegOnes :: integer(), K :: integer()) -> integer().
k_items_with_maximum_sum(NumOnes, NumZeros, NumNegOnes, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_items_with_maximum_sum(num_ones :: integer, num_zeros :: integer, num_neg_ones :: integer, k :: integer) :: integer
  def k_items_with_maximum_sum(num_ones, num_zeros, num_neg_ones, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kItemsWithMaximumSum(numOnes: Int64, numZeros: Int64, numNegOnes: Int64, k: Int64): Int64 {

    }
}
```

