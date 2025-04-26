# 877. 石子游戏

## 题目描述

<p>Alice 和 Bob 用几堆石子在做游戏。一共有偶数堆石子，<strong>排成一行</strong>；每堆都有 <strong>正</strong> 整数颗石子，数目为 <code>piles[i]</code>&nbsp;。</p>

<p>游戏以谁手中的石子最多来决出胜负。石子的 <strong>总数</strong> 是 <strong>奇数</strong> ，所以没有平局。</p>

<p>Alice 和 Bob 轮流进行，<strong>Alice 先开始</strong> 。 每回合，玩家从行的 <strong>开始</strong> 或 <strong>结束</strong> 处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中 <strong>石子最多</strong> 的玩家 <strong>获胜</strong> 。</p>

<p>假设 Alice 和 Bob 都发挥出最佳水平，当 Alice 赢得比赛时返回&nbsp;<code>true</code>&nbsp;，当 Bob 赢得比赛时返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>piles = [5,3,4,5]
<strong>输出：</strong>true
<strong>解释：</strong>
Alice 先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果 Bob 拿走前 3 颗，那么剩下的是 [4,5]，Alice 拿走后 5 颗赢得 10 分。
如果 Bob 拿走后 5 颗，那么剩下的是 [3,4]，Alice 拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对 Alice 来说是一个胜利的举动，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>piles = [3,7,2,3]
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= piles.length &lt;= 500</code></li>
	<li><code>piles.length</code> 是 <strong>偶数</strong></li>
	<li><code>1 &lt;= piles[i] &lt;= 500</code></li>
	<li><code>sum(piles[i])</code>&nbsp;是 <strong>奇数</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划
- 博弈

## 示例

```
[5,3,4,5]
[3,7,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool stoneGame(vector<int>& piles) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean stoneGame(int[] piles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
```

### C

```c
bool stoneGame(int* piles, int pilesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool StoneGame(int[] piles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} piles
 * @return {boolean}
 */
var stoneGame = function(piles) {
    
};
```

### TypeScript

```typescript
function stoneGame(piles: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $piles
     * @return Boolean
     */
    function stoneGame($piles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGame(_ piles: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGame(piles: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool stoneGame(List<int> piles) {
    
  }
}
```

### Go

```golang
func stoneGame(piles []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} piles
# @return {Boolean}
def stone_game(piles)
    
end
```

### Scala

```scala
object Solution {
    def stoneGame(piles: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game(piles: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game piles)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec stone_game(Piles :: [integer()]) -> boolean().
stone_game(Piles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game(piles :: [integer]) :: boolean
  def stone_game(piles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGame(piles: Array<Int64>): Bool {

    }
}
```

