# 1140. 石子游戏 II

## 题目描述

<p>Alice&nbsp;和 Bob 继续他们的石子游戏。许多堆石子&nbsp;<strong>排成一行</strong>，每堆都有正整数颗石子&nbsp;<code>piles[i]</code>。游戏以谁手中的石子最多来决出胜负。</p>

<p>Alice&nbsp;和 Bob 轮流进行，Alice 先开始。最初，<code>M = 1</code>。</p>

<p>在每个玩家的回合中，该玩家可以拿走剩下的&nbsp;<strong>前</strong>&nbsp;<code>X</code>&nbsp;堆的所有石子，其中&nbsp;<code>1 &lt;= X &lt;= 2M</code>。然后，令&nbsp;<code>M = max(M, X)</code>。</p>

<p>游戏一直持续到所有石子都被拿走。</p>

<p>假设 Alice 和 Bob 都发挥出最佳水平，返回 Alice 可以得到的最大数量的石头。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>piles = [2,7,9,4,4]
<strong>输出：</strong>10
<strong>解释：</strong>如果一开始 Alice 取了一堆，Bob 取了两堆，然后 Alice 再取两堆。Alice 可以得到 2 + 4 + 4 = 10 堆。
如果 Alice 一开始拿走了两堆，那么 Bob 可以拿走剩下的三堆。在这种情况下，Alice 得到 2 + 7 = 9 堆。返回 10，因为它更大。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong>piles = [1,2,3,4,5,100]
<strong>输出：</strong>104
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= piles.length &lt;= 100</code></li>
	<li><meta charset="UTF-8" /><code>1 &lt;= piles[i]&nbsp;&lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划
- 博弈
- 前缀和

## 提示

1. Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.

## 示例

```
[2,7,9,4,4]
[1,2,3,4,5,100]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        
    }
};
```

### Java

```java
class Solution {
    public int stoneGameII(int[] piles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
```

### C

```c
int stoneGameII(int* piles, int pilesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int StoneGameII(int[] piles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} piles
 * @return {number}
 */
var stoneGameII = function(piles) {
    
};
```

### TypeScript

```typescript
function stoneGameII(piles: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @return Integer
     */
    function stoneGameII($piles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGameII(_ piles: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGameII(piles: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int stoneGameII(List<int> piles) {
    
  }
}
```

### Go

```golang
func stoneGameII(piles []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} piles
# @return {Integer}
def stone_game_ii(piles)
    
end
```

### Scala

```scala
object Solution {
    def stoneGameII(piles: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game_ii(piles: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game-ii piles)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec stone_game_ii(Piles :: [integer()]) -> integer().
stone_game_ii(Piles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game_ii(piles :: [integer]) :: integer
  def stone_game_ii(piles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGameII(piles: Array<Int64>): Int64 {

    }
}
```

