# 1872. 石子游戏 VIII

## 题目描述

<p>Alice 和 Bob 玩一个游戏，两人轮流操作， <strong>Alice 先手</strong> 。</p>

<p>总共有 <code>n</code> 个石子排成一行。轮到某个玩家的回合时，如果石子的数目 <strong>大于 1</strong> ，他将执行以下操作：</p>

<ol>
	<li>选择一个整数 <code>x &gt; 1</code> ，并且 <strong>移除</strong> 最左边的 <code>x</code> 个石子。</li>
	<li>将<strong> 移除</strong> 的石子价值之 <strong>和</strong> 累加到该玩家的分数中。</li>
	<li>将一个 <strong>新的石子</strong> 放在最左边，且新石子的值为被移除石子值之和。</li>
</ol>

<p>当只剩下 <strong>一个</strong> 石子时，游戏结束。</p>

<p>Alice 和 Bob 的 <strong>分数之差</strong> 为 <code>(Alice 的分数 - Bob 的分数)</code> 。 Alice 的目标是<strong> 最大化</strong> 分数差，Bob 的目标是 <strong>最小化</strong> 分数差。</p>

<p>给你一个长度为 <code>n</code> 的整数数组 <code>stones</code> ，其中 <code>stones[i]</code> 是 <strong>从左边起</strong> 第 <code>i</code> 个石子的价值。请你返回在双方都采用 <strong>最优</strong> 策略的情况下，Alice 和 Bob 的 <strong>分数之差</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>stones = [-1,2,-3,4,-5]
<b>输出：</b>5
<strong>解释：</strong>
- Alice 移除最左边的 4 个石子，得分增加 (-1) + 2 + (-3) + 4 = 2 ，并且将一个价值为 2 的石子放在最左边。stones = [2,-5] 。
- Bob 移除最左边的 2 个石子，得分增加 2 + (-5) = -3 ，并且将一个价值为 -3 的石子放在最左边。stones = [-3] 。
两者分数之差为 2 - (-3) = 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>stones = [7,-6,5,10,5,-2,-6]
<b>输出：</b>13
<b>解释：</b>
- Alice 移除所有石子，得分增加 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 ，并且将一个价值为 13 的石子放在最左边。stones = [13] 。
两者分数之差为 13 - 0 = 13 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>stones = [-10,-12]
<b>输出：</b>-22
<strong>解释：</strong>
- Alice 只有一种操作，就是移除所有石子。得分增加 (-10) + (-12) = -22 ，并且将一个价值为 -22 的石子放在最左边。stones = [-22] 。
两者分数之差为 (-22) - 0 = -22 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == stones.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= stones[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 博弈
- 前缀和

## 提示

1. Let's note that the only thing that matters is how many stones were removed so we can maintain dp[numberOfRemovedStones]
2. dp[x] = max(sum of all elements up to y - dp[y]) for all y > x

## 示例

```
[-1,2,-3,4,-5]
[7,-6,5,10,5,-2,-6]
[-10,-12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int stoneGameVIII(vector<int>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int stoneGameVIII(int[] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        
```

### C

```c
int stoneGameVIII(int* stones, int stonesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int StoneGameVIII(int[] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var stoneGameVIII = function(stones) {
    
};
```

### TypeScript

```typescript
function stoneGameVIII(stones: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function stoneGameVIII($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGameVIII(_ stones: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGameVIII(stones: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int stoneGameVIII(List<int> stones) {
    
  }
}
```

### Go

```golang
func stoneGameVIII(stones []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def stone_game_viii(stones)
    
end
```

### Scala

```scala
object Solution {
    def stoneGameVIII(stones: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game_viii(stones: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game-viii stones)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec stone_game_viii(Stones :: [integer()]) -> integer().
stone_game_viii(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game_viii(stones :: [integer]) :: integer
  def stone_game_viii(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGameVIII(stones: Array<Int64>): Int64 {

    }
}
```

