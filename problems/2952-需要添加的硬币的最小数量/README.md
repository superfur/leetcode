# 2952. 需要添加的硬币的最小数量

## 题目描述

<p>给你一个下标从 <strong>0 </strong>开始的整数数组 <code>coins</code>，表示可用的硬币的面值，以及一个整数 <code>target</code> 。</p>

<p>如果存在某个 <code>coins</code> 的子序列总和为 <code>x</code>，那么整数 <code>x</code> 就是一个 <strong>可取得的金额 </strong>。</p>

<p>返回需要添加到数组中的<strong> 任意面值 </strong>硬币的 <strong>最小数量 </strong>，使范围 <code>[1, target]</code> 内的每个整数都属于 <strong>可取得的金额</strong> 。</p>

<p>数组的 <strong>子序列</strong> 是通过删除原始数组的一些（<strong>可能不删除</strong>）元素而形成的新的 <strong>非空</strong> 数组，删除过程不会改变剩余元素的相对位置。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>coins = [1,4,10], target = 19
<strong>输出：</strong>2
<strong>解释：</strong>需要添加面值为 2 和 8 的硬币各一枚，得到硬币数组 [1,2,4,8,10] 。
可以证明从 1 到 19 的所有整数都可由数组中的硬币组合得到，且需要添加到数组中的硬币数目最小为 2 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>coins = [1,4,10,5,7,19], target = 19
<strong>输出：</strong>1
<strong>解释：</strong>只需要添加一枚面值为 2 的硬币，得到硬币数组 [1,2,4,5,7,10,19] 。
可以证明从 1 到 19 的所有整数都可由数组中的硬币组合得到，且需要添加到数组中的硬币数目最小为 1 。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>coins = [1,1,1], target = 20
<strong>输出：</strong>3
<strong>解释：</strong>
需要添加面值为 4 、8 和 16 的硬币各一枚，得到硬币数组 [1,1,1,4,8,16] 。 
可以证明从 1 到 20 的所有整数都可由数组中的硬币组合得到，且需要添加到数组中的硬币数目最小为 3 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coins.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= coins[i] &lt;= target</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Sort the coins array and maintain the smallest sum that is unobtainable by induction.
2. If we don’t use any coins, the smallest integer that we cannot obtain by sum is <code>1</code>. Suppose currently, for a fixed set of the first several coins the smallest integer that we cannot obtain is <code>x + 1</code>, namely we can form all integers in the range <code>[1, x]</code> but not <code>x + 1</code>.
3. If the next unused coin’s value is NOT <code>x + 1</code> (note the array is sorted), we have to add <code>x + 1</code> to the array. After this addition, we can form all values from <code>x + 1</code> to <code>2 * x + 1</code> by adding <code>x + 1</code> in <code>[1, x]</code>'s formations. So now we can form all the numbers of <code>[1, 2 * x + 1]</code>. After this iteration the new value of <code>x</code> becomes <code>2 * x + 1</code>.

## 示例

```
[1,4,10]
19
[1,4,10,5,7,19]
19
[1,1,1]
20
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumAddedCoins(vector<int>& coins, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumAddedCoins(int[] coins, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        
```

### C

```c
int minimumAddedCoins(int* coins, int coinsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumAddedCoins(int[] coins, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} coins
 * @param {number} target
 * @return {number}
 */
var minimumAddedCoins = function(coins, target) {
    
};
```

### TypeScript

```typescript
function minimumAddedCoins(coins: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $coins
     * @param Integer $target
     * @return Integer
     */
    function minimumAddedCoins($coins, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumAddedCoins(_ coins: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumAddedCoins(coins: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumAddedCoins(List<int> coins, int target) {
    
  }
}
```

### Go

```golang
func minimumAddedCoins(coins []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} coins
# @param {Integer} target
# @return {Integer}
def minimum_added_coins(coins, target)
    
end
```

### Scala

```scala
object Solution {
    def minimumAddedCoins(coins: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_added_coins(coins: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-added-coins coins target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_added_coins(Coins :: [integer()], Target :: integer()) -> integer().
minimum_added_coins(Coins, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_added_coins(coins :: [integer], target :: integer) :: integer
  def minimum_added_coins(coins, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumAddedCoins(coins: Array<Int64>, target: Int64): Int64 {

    }
}
```

