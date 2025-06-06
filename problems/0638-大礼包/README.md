# 638. 大礼包

## 题目描述

<p>在 LeetCode 商店中， 有 <code>n</code> 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。</p>

<p>给你一个整数数组 <code>price</code> 表示物品价格，其中 <code>price[i]</code> 是第 <code>i</code> 件物品的价格。另有一个整数数组 <code>needs</code> 表示购物清单，其中 <code>needs[i]</code> 是需要购买第 <code>i</code> 件物品的数量。</p>

<p>还有一个数组 <code>special</code> 表示大礼包，<code>special[i]</code> 的长度为 <code>n + 1</code> ，其中 <code>special[i][j]</code> 表示第 <code>i</code> 个大礼包中内含第 <code>j</code> 件物品的数量，且 <code>special[i][n]</code> （也就是数组中的最后一个整数）为第 <code>i</code> 个大礼包的价格。</p>

<p>返回<strong> 确切 </strong>满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
<strong>输出：</strong>14
<strong>解释：</strong>有 A 和 B 两种物品，价格分别为 ¥2 和 ¥5 。 
大礼包 1 ，你可以以 ¥5 的价格购买 3A 和 0B 。 
大礼包 2 ，你可以以 ¥10 的价格购买 1A 和 2B 。 
需要购买 3 个 A 和 2 个 B ， 所以付 ¥10 购买 1A 和 2B（大礼包 2），以及 ¥4 购买 2A 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
<strong>输出：</strong>11
<strong>解释：</strong>A ，B ，C 的价格分别为 ¥2 ，¥3 ，¥4 。
可以用 ¥4 购买 1A 和 1B ，也可以用 ¥9 购买 2A ，2B 和 1C 。 
需要买 1A ，2B 和 1C ，所以付 ¥4 买 1A 和 1B（大礼包 1），以及 ¥3 购买 1B ， ¥4 购买 1C 。 
不可以购买超出待购清单的物品，尽管购买大礼包 2 更加便宜。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == price.length == needs.length</code></li>
	<li><code>1 &lt;= n &lt;= 6</code></li>
	<li><code>0 &lt;= price[i], needs[i] &lt;= 10</code></li>
	<li><code>1 &lt;= special.length &lt;= 100</code></li>
	<li><code>special[i].length == n + 1</code></li>
	<li><code>0 &lt;= special[i][j] &lt;= 50</code></li>
	<li>生成的输入对于&nbsp;<code>0 &lt;= j &lt;= n - 1</code> 至少有一个&nbsp;<code>special[i][j]</code>&nbsp;非零。</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 记忆化搜索
- 数组
- 动态规划
- 回溯
- 状态压缩

## 示例

```
[2,5]
[[3,0,5],[1,2,10]]
[3,2]
[2,3,4]
[[1,1,0,4],[2,2,1,9]]
[1,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int shoppingOffers(vector<int>& price, vector<vector<int>>& special, vector<int>& needs) {
        
    }
};
```

### Java

```java
class Solution {
    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
```

### C

```c
int shoppingOffers(int* price, int priceSize, int** special, int specialSize, int* specialColSize, int* needs, int needsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ShoppingOffers(IList<int> price, IList<IList<int>> special, IList<int> needs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} price
 * @param {number[][]} special
 * @param {number[]} needs
 * @return {number}
 */
var shoppingOffers = function(price, special, needs) {
    
};
```

### TypeScript

```typescript
function shoppingOffers(price: number[], special: number[][], needs: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $price
     * @param Integer[][] $special
     * @param Integer[] $needs
     * @return Integer
     */
    function shoppingOffers($price, $special, $needs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func shoppingOffers(_ price: [Int], _ special: [[Int]], _ needs: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun shoppingOffers(price: List<Int>, special: List<List<Int>>, needs: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int shoppingOffers(List<int> price, List<List<int>> special, List<int> needs) {
    
  }
}
```

### Go

```golang
func shoppingOffers(price []int, special [][]int, needs []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} price
# @param {Integer[][]} special
# @param {Integer[]} needs
# @return {Integer}
def shopping_offers(price, special, needs)
    
end
```

### Scala

```scala
object Solution {
    def shoppingOffers(price: List[Int], special: List[List[Int]], needs: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn shopping_offers(price: Vec<i32>, special: Vec<Vec<i32>>, needs: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (shopping-offers price special needs)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec shopping_offers(Price :: [integer()], Special :: [[integer()]], Needs :: [integer()]) -> integer().
shopping_offers(Price, Special, Needs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec shopping_offers(price :: [integer], special :: [[integer]], needs :: [integer]) :: integer
  def shopping_offers(price, special, needs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func shoppingOffers(price: ArrayList<Int64>, special: ArrayList<ArrayList<Int64>>, needs: ArrayList<Int64>): Int64 {

    }
}
```

