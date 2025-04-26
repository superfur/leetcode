# 3116. 单面值组合的第 K 小金额

## 题目描述

<p>给你一个整数数组 <code>coins</code> 表示不同面额的硬币，另给你一个整数 <code>k</code> 。</p>

<p>你有无限量的每种面额的硬币。但是，你<strong> 不能 </strong>组合使用不同面额的硬币。</p>

<p>返回使用这些硬币能制造的<strong> 第 </strong><code>k<sup>th</sup></code><strong> 小</strong> 金额。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;">coins = [3,6,9], k = 3</span></p>

<p><strong>输出：</strong> <span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;">9</span></p>

<p><strong>解释：</strong>给定的硬币可以制造以下金额：<br />
3元硬币产生3的倍数：3, 6, 9, 12, 15等。<br />
6元硬币产生6的倍数：6, 12, 18, 24等。<br />
9元硬币产生9的倍数：9, 18, 27, 36等。<br />
所有硬币合起来可以产生：3, 6, <u><strong>9</strong></u>, 12, 15等。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="
    border-color: var(--border-tertiary);
    border-left-width: 2px;
    color: var(--text-secondary);
    font-size: .875rem;
    margin-bottom: 1rem;
    margin-top: 1rem;
    overflow: visible;
    padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;">coins = [5,2], k = 7</span></p>

<p><strong>输出：</strong><span class="example-io" style="
    font-family: Menlo,sans-serif;
    font-size: 0.85rem;">12</span></p>

<p><strong>解释：</strong>给定的硬币可以制造以下金额：<br />
5元硬币产生5的倍数：5, 10, 15, 20等。<br />
2元硬币产生2的倍数：2, 4, 6, 8, 10, 12等。<br />
所有硬币合起来可以产生：2, 4, 5, 6, 8, 10, <u><strong>12</strong></u>, 14, 15等。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 15</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 25</code></li>
	<li><code>1 &lt;= k &lt;= 2 * 10<sup>9</sup></code></li>
	<li><code>coins</code> 包含两两不同的整数。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 数学
- 二分查找
- 组合数学
- 数论

## 提示

1. Binary search the answer <code>x</code>.
2. Use the inclusion-exclusion principle to count the number of distinct amounts that can be made up to <code>x</code>.

## 示例

```
[3,6,9]
3
[5,2]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long findKthSmallest(vector<int>& coins, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long findKthSmallest(int[] coins, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        
```

### C

```c
long long findKthSmallest(int* coins, int coinsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long FindKthSmallest(int[] coins, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} coins
 * @param {number} k
 * @return {number}
 */
var findKthSmallest = function(coins, k) {
    
};
```

### TypeScript

```typescript
function findKthSmallest(coins: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @param Integer $k
     * @return Integer
     */
    function findKthSmallest($coins, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKthSmallest(_ coins: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKthSmallest(coins: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int findKthSmallest(List<int> coins, int k) {
    
  }
}
```

### Go

```golang
func findKthSmallest(coins []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def find_kth_smallest(coins, k)
    
end
```

### Scala

```scala
object Solution {
    def findKthSmallest(coins: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_kth_smallest(coins: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-kth-smallest coins k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_kth_smallest(Coins :: [integer()], K :: integer()) -> integer().
find_kth_smallest(Coins, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_kth_smallest(coins :: [integer], k :: integer) :: integer
  def find_kth_smallest(coins, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKthSmallest(coins: Array<Int64>, k: Int64): Int64 {

    }
}
```

