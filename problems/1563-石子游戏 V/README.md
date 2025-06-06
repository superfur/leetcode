# 1563. 石子游戏 V

## 题目描述

<p>几块石子 <strong>排成一行</strong> ，每块石子都有一个关联值，关联值为整数，由数组 <code>stoneValue</code> 给出。</p>

<p>游戏中的每一轮：Alice 会将这行石子分成两个 <strong>非空行</strong>（即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。</p>

<p>只 <strong>剩下一块石子</strong> 时，游戏结束。Alice 的分数最初为 <strong><code>0</code></strong> 。</p>

<p>返回 <strong>Alice 能够获得的最大分数</strong><em> 。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>stoneValue = [6,2,3,4,5,5]
<strong>输出：</strong>18
<strong>解释：</strong>在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>stoneValue = [7,7,7,7,7,7,7]
<strong>输出：</strong>28
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>stoneValue = [4]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= stoneValue.length &lt;= 500</code></li>
	<li><code>1 &lt;=&nbsp;stoneValue[i] &lt;= 10^6</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 博弈

## 提示

1. We need to try all possible divisions for the current row to get the max score.
2. As calculating all possible divisions will lead us to calculate some sub-problems more than once, we need to think of dynamic programming.

## 示例

```
[6,2,3,4,5,5]
[7,7,7,7,7,7,7]
[4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int stoneGameV(vector<int>& stoneValue) {
        
    }
};
```

### Java

```java
class Solution {
    public int stoneGameV(int[] stoneValue) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
```

### C

```c
int stoneGameV(int* stoneValue, int stoneValueSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int StoneGameV(int[] stoneValue) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stoneValue
 * @return {number}
 */
var stoneGameV = function(stoneValue) {
    
};
```

### TypeScript

```typescript
function stoneGameV(stoneValue: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stoneValue
     * @return Integer
     */
    function stoneGameV($stoneValue) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGameV(_ stoneValue: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGameV(stoneValue: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int stoneGameV(List<int> stoneValue) {
    
  }
}
```

### Go

```golang
func stoneGameV(stoneValue []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stone_value
# @return {Integer}
def stone_game_v(stone_value)
    
end
```

### Scala

```scala
object Solution {
    def stoneGameV(stoneValue: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game_v(stone_value: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game-v stoneValue)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec stone_game_v(StoneValue :: [integer()]) -> integer().
stone_game_v(StoneValue) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game_v(stone_value :: [integer]) :: integer
  def stone_game_v(stone_value) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGameV(stoneValue: Array<Int64>): Int64 {

    }
}
```

