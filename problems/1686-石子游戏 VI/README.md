# 1686. 石子游戏 VI

## 题目描述

<p>Alice 和 Bob 轮流玩一个游戏，Alice 先手。</p>

<p>一堆石子里总共有 <code>n</code> 个石子，轮到某个玩家时，他可以 <strong>移出</strong> 一个石子并得到这个石子的价值。Alice 和 Bob 对石子价值有 <strong>不一样的的评判标准</strong> 。双方都知道对方的评判标准。</p>

<p>给你两个长度为 <code>n</code> 的整数数组 <code>aliceValues</code> 和 <code>bobValues</code> 。<code>aliceValues[i]</code> 和 <code>bobValues[i]</code> 分别表示 Alice 和 Bob 认为第 <code>i</code> 个石子的价值。</p>

<p>所有石子都被取完后，得分较高的人为胜者。如果两个玩家得分相同，那么为平局。两位玩家都会采用 <b>最优策略</b> 进行游戏。</p>

<p>请你推断游戏的结果，用如下的方式表示：</p>

<ul>
	<li>如果 Alice 赢，返回 <code>1</code> 。</li>
	<li>如果 Bob 赢，返回 <code>-1</code> 。</li>
	<li>如果游戏平局，返回 <code>0</code> 。</li>
</ul>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>aliceValues = [1,3], bobValues = [2,1]
<b>输出：</b>1
<strong>解释：</strong>
如果 Alice 拿石子 1 （下标从 0开始），那么 Alice 可以得到 3 分。
Bob 只能选择石子 0 ，得到 2 分。
Alice 获胜。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>aliceValues = [1,2], bobValues = [3,1]
<b>输出：</b>0
<strong>解释：</strong>
Alice 拿石子 0 ， Bob 拿石子 1 ，他们得分都为 1 分。
打平。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>aliceValues = [2,4,3], bobValues = [1,6,7]
<b>输出：</b>-1
<strong>解释：</strong>
不管 Alice 怎么操作，Bob 都可以得到比 Alice 更高的得分。
比方说，Alice 拿石子 1 ，Bob 拿石子 2 ， Alice 拿石子 0 ，Alice 会得到 6 分而 Bob 得分为 7 分。
Bob 会获胜。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == aliceValues.length == bobValues.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= aliceValues[i], bobValues[i] <= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 博弈
- 排序
- 堆（优先队列）

## 提示

1. When one takes the stone, they not only get the points, but they take them away from the other player too.
2. Greedily choose the stone with the maximum aliceValues[i] + bobValues[i].

## 示例

```
[1,3]
[2,1]
[1,2]
[3,1]
[2,4,3]
[1,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int stoneGameVI(vector<int>& aliceValues, vector<int>& bobValues) {
        
    }
};
```

### Java

```java
class Solution {
    public int stoneGameVI(int[] aliceValues, int[] bobValues) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        
```

### C

```c
int stoneGameVI(int* aliceValues, int aliceValuesSize, int* bobValues, int bobValuesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int StoneGameVI(int[] aliceValues, int[] bobValues) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} aliceValues
 * @param {number[]} bobValues
 * @return {number}
 */
var stoneGameVI = function(aliceValues, bobValues) {
    
};
```

### TypeScript

```typescript
function stoneGameVI(aliceValues: number[], bobValues: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $aliceValues
     * @param Integer[] $bobValues
     * @return Integer
     */
    function stoneGameVI($aliceValues, $bobValues) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGameVI(_ aliceValues: [Int], _ bobValues: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGameVI(aliceValues: IntArray, bobValues: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int stoneGameVI(List<int> aliceValues, List<int> bobValues) {
    
  }
}
```

### Go

```golang
func stoneGameVI(aliceValues []int, bobValues []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} alice_values
# @param {Integer[]} bob_values
# @return {Integer}
def stone_game_vi(alice_values, bob_values)
    
end
```

### Scala

```scala
object Solution {
    def stoneGameVI(aliceValues: Array[Int], bobValues: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game_vi(alice_values: Vec<i32>, bob_values: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game-vi aliceValues bobValues)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec stone_game_vi(AliceValues :: [integer()], BobValues :: [integer()]) -> integer().
stone_game_vi(AliceValues, BobValues) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game_vi(alice_values :: [integer], bob_values :: [integer]) :: integer
  def stone_game_vi(alice_values, bob_values) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGameVI(aliceValues: Array<Int64>, bobValues: Array<Int64>): Int64 {

    }
}
```

