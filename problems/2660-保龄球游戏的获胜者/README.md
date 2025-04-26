# 2660. 保龄球游戏的获胜者

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的整数数组 <code>player1</code> 和 <code>player2</code> ，分别表示玩家 1 和玩家 2 击中的瓶数。</p>

<p>保龄球比赛由 <code>n</code> 轮组成，每轮的瓶数恰好为 <code>10</code> 。</p>

<p>假设玩家在第 <code>i</code> 轮中击中&nbsp;<code>x<sub>i</sub></code> 个瓶子。玩家第 <code>i</code> 轮的价值为：</p>

<ul>
	<li>如果玩家在该轮的前两轮的任何一轮中击中了 <code>10</code> 个瓶子，则为 <code>2x<sub>i</sub></code> 。</li>
	<li>否则，为&nbsp;<code>x<sub>i</sub></code> 。</li>
</ul>

<p>玩家的得分是其 <code>n</code> 轮价值的总和。</p>

<p>返回</p>

<ul>
	<li>如果玩家 1 的得分高于玩家 2 的得分，则为 <code>1</code> ；</li>
	<li>如果玩家 2 的得分高于玩家 1 的得分，则为 <code>2</code> ；</li>
	<li>如果平局，则为 <code>0</code> 。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">player1 = [5,10,3,2], player2 = [6,5,7,3]</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>玩家 1 的分数为 5 + 10 + 2*3 + 2*2 = 25。</p>

<p>玩家 2&nbsp;的分数为 6 + 5 + 7 + 3 = 21。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">player1 = [3,5,7,6], player2 = [8,10,10,2]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>玩家 1 的分数为 3 + 5 + 7 + 6 = 21。</p>

<p>玩家 2&nbsp;的分数为 8 + 10 + 2*10 + 2*2 = 42。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">player1 = [2,3], player2 = [4,1]</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>玩家 1 的分数为&nbsp;2 + 3 = 5。</p>

<p>玩家 2 的分数为&nbsp;4 + 1 = 5。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">player1 = [1,1,1,10,10,10,10], player2 = [10,10,10,10,1,1,1]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>玩家 1 的分数为 1 + 1 + 1 + 10 + 2*10 + 2*10 + 2*10 = 73。</p>

<p>玩家 2 的分数为 is 10 + 2*10 + 2*10 + 2*10 + 2*1 + 2*1 + 1 = 75。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == player1.length == player2.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= player1[i], player2[i] &lt;= 10</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Think about simulating the process to calculate the answer.
2. Iterate over each element and check the previous two elements. See if one of them is 10 and can affect the score.

## 示例

```
[5,10,3,2]
[6,5,7,3]
[3,5,7,6]
[8,10,10,2]
[2,3]
[4,1]
[1,1,1,10,10,10,10]
[10,10,10,10,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int isWinner(vector<int>& player1, vector<int>& player2) {
        
    }
};
```

### Java

```java
class Solution {
    public int isWinner(int[] player1, int[] player2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isWinner(self, player1, player2):
        """
        :type player1: List[int]
        :type player2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        
```

### C

```c
int isWinner(int* player1, int player1Size, int* player2, int player2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int IsWinner(int[] player1, int[] player2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} player1
 * @param {number[]} player2
 * @return {number}
 */
var isWinner = function(player1, player2) {
    
};
```

### TypeScript

```typescript
function isWinner(player1: number[], player2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $player1
     * @param Integer[] $player2
     * @return Integer
     */
    function isWinner($player1, $player2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isWinner(_ player1: [Int], _ player2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isWinner(player1: IntArray, player2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int isWinner(List<int> player1, List<int> player2) {
    
  }
}
```

### Go

```golang
func isWinner(player1 []int, player2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} player1
# @param {Integer[]} player2
# @return {Integer}
def is_winner(player1, player2)
    
end
```

### Scala

```scala
object Solution {
    def isWinner(player1: Array[Int], player2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_winner(player1: Vec<i32>, player2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (is-winner player1 player2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec is_winner(Player1 :: [integer()], Player2 :: [integer()]) -> integer().
is_winner(Player1, Player2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_winner(player1 :: [integer], player2 :: [integer]) :: integer
  def is_winner(player1, player2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isWinner(player1: Array<Int64>, player2: Array<Int64>): Int64 {

    }
}
```

