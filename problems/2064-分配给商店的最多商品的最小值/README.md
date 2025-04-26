# 2064. 分配给商店的最多商品的最小值

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，表示有&nbsp;<code>n</code>&nbsp;间零售商店。总共有&nbsp;<code>m</code>&nbsp;种产品，每种产品的数目用一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>quantities</code>&nbsp;表示，其中&nbsp;<code>quantities[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;种商品的数目。</p>

<p>你需要将 <strong>所有商品</strong>&nbsp;分配到零售商店，并遵守这些规则：</p>

<ul>
	<li>一间商店 <strong>至多</strong>&nbsp;只能有 <strong>一种商品</strong> ，但一间商店拥有的商品数目可以为&nbsp;<strong>任意</strong>&nbsp;件。</li>
	<li>分配后，每间商店都会被分配一定数目的商品（可能为 <code>0</code>&nbsp;件）。用&nbsp;<code>x</code>&nbsp;表示所有商店中分配商品数目的最大值，你希望 <code>x</code>&nbsp;越小越好。也就是说，你想 <strong>最小化</strong>&nbsp;分配给任意商店商品数目的 <strong>最大值</strong>&nbsp;。</li>
</ul>

<p>请你返回最小的可能的&nbsp;<code>x</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 6, quantities = [11,6]
<b>输出：</b>3
<strong>解释： </strong>一种最优方案为：
- 11 件种类为 0 的商品被分配到前 4 间商店，分配数目分别为：2，3，3，3 。
- 6 件种类为 1 的商品被分配到另外 2 间商店，分配数目分别为：3，3 。
分配给所有商店的最大商品数目为 max(2, 3, 3, 3, 3, 3) = 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 7, quantities = [15,10,10]
<b>输出：</b>5
<b>解释：</b>一种最优方案为：
- 15 件种类为 0 的商品被分配到前 3 间商店，分配数目为：5，5，5 。
- 10 件种类为 1 的商品被分配到接下来 2 间商店，数目为：5，5 。
- 10 件种类为 2 的商品被分配到最后 2 间商店，数目为：5，5 。
分配给所有商店的最大商品数目为 max(5, 5, 5, 5, 5, 5, 5) = 5 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>n = 1, quantities = [100000]
<b>输出：</b>100000
<b>解释：</b>唯一一种最优方案为：
- 所有 100000 件商品 0 都分配到唯一的商店中。
分配给所有商店的最大商品数目为 max(100000) = 100000 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == quantities.length</code></li>
	<li><code>1 &lt;= m &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= quantities[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找

## 提示

1. There exists a monotonic nature such that when x is smaller than some number, there will be no way to distribute, and when x is not smaller than that number, there will always be a way to distribute.
2. If you are given a number k, where the number of products given to any store does not exceed k, could you determine if all products can be distributed?
3. Implement a function canDistribute(k), which returns true if you can distribute all products such that any store will not be given more than k products, and returns false if you cannot. Use this function to binary search for the smallest possible k.

## 示例

```
6
[11,6]
7
[15,10,10]
1
[100000]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizedMaximum(int n, vector<int>& quantities) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizedMaximum(int n, int[] quantities) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
```

### C

```c
int minimizedMaximum(int n, int* quantities, int quantitiesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizedMaximum(int n, int[] quantities) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} quantities
 * @return {number}
 */
var minimizedMaximum = function(n, quantities) {
    
};
```

### TypeScript

```typescript
function minimizedMaximum(n: number, quantities: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $quantities
     * @return Integer
     */
    function minimizedMaximum($n, $quantities) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizedMaximum(_ n: Int, _ quantities: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizedMaximum(n: Int, quantities: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizedMaximum(int n, List<int> quantities) {
    
  }
}
```

### Go

```golang
func minimizedMaximum(n int, quantities []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} quantities
# @return {Integer}
def minimized_maximum(n, quantities)
    
end
```

### Scala

```scala
object Solution {
    def minimizedMaximum(n: Int, quantities: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimized_maximum(n: i32, quantities: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimized-maximum n quantities)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimized_maximum(N :: integer(), Quantities :: [integer()]) -> integer().
minimized_maximum(N, Quantities) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimized_maximum(n :: integer, quantities :: [integer]) :: integer
  def minimized_maximum(n, quantities) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizedMaximum(n: Int64, quantities: Array<Int64>): Int64 {

    }
}
```

