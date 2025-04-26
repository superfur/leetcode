# 1406. 石子游戏 III

## 题目描述

<p>Alice 和 Bob 继续他们的石子游戏。几堆石子 <strong>排成一行</strong> ，每堆石子都对应一个得分，由数组 <code>stoneValue</code> 给出。</p>

<p>Alice 和 Bob 轮流取石子，<strong>Alice</strong> 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 <strong>1、2 或 3 堆石子</strong> 。比赛一直持续到所有石头都被拿走。</p>

<p>每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 <strong>0</strong> 。</p>

<p>比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。</p>

<p>假设 Alice 和 Bob 都采取 <strong>最优策略</strong> 。</p>

<p>如果 Alice 赢了就返回 <code>"Alice"</code> <em>，</em>Bob 赢了就返回<em> </em><code>"Bob"</code><em>，</em>分数相同返回 <code>"Tie"</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>values = [1,2,3,7]
<strong>输出：</strong>"Bob"
<strong>解释：</strong>Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>values = [1,2,3,-9]
<strong>输出：</strong>"Alice"
<strong>解释：</strong>Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
注意，他们都应该采取 <strong>最优策略 </strong>，所以在这里 Alice 将选择能够使她获胜的方案。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>values = [1,2,3,6]
<strong>输出：</strong>"Tie"
<strong>解释：</strong>Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= stoneValue.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-1000&nbsp;&lt;= stoneValue[i] &lt;= 1000</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 博弈

## 提示

1. The game can be mapped to minmax game. Alice tries to maximize the total score and Bob tries to minimize it.
2. Use dynamic programming to simulate the game. If the total score was 0 the game is "Tie", and if it has positive value then "Alice" wins, otherwise "Bob" wins.

## 示例

```
[1,2,3,7]
[1,2,3,-9]
[1,2,3,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string stoneGameIII(vector<int>& stoneValue) {
        
    }
};
```

### Java

```java
class Solution {
    public String stoneGameIII(int[] stoneValue) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
```

### C

```c
char* stoneGameIII(int* stoneValue, int stoneValueSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string StoneGameIII(int[] stoneValue) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stoneValue
 * @return {string}
 */
var stoneGameIII = function(stoneValue) {
    
};
```

### TypeScript

```typescript
function stoneGameIII(stoneValue: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return String
     */
    function stoneGameIII($stoneValue) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGameIII(_ stoneValue: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGameIII(stoneValue: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String stoneGameIII(List<int> stoneValue) {
    
  }
}
```

### Go

```golang
func stoneGameIII(stoneValue []int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stone_value
# @return {String}
def stone_game_iii(stone_value)
    
end
```

### Scala

```scala
object Solution {
    def stoneGameIII(stoneValue: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game_iii(stone_value: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game-iii stoneValue)
  (-> (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec stone_game_iii(StoneValue :: [integer()]) -> unicode:unicode_binary().
stone_game_iii(StoneValue) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game_iii(stone_value :: [integer]) :: String.t
  def stone_game_iii(stone_value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGameIII(stoneValue: Array<Int64>): String {

    }
}
```

