# 1690. 石子游戏 VII

## 题目描述

<p>石子游戏中，爱丽丝和鲍勃轮流进行自己的回合，<strong>爱丽丝先开始</strong> 。</p>

<p>有 <code>n</code> 块石子排成一排。每个玩家的回合中，可以从行中 <strong>移除</strong> 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 <strong>和</strong> 相等的得分。当没有石头可移除时，得分较高者获胜。</p>

<p>鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 <strong>减小得分的差值</strong> 。爱丽丝的目标是最大限度地 <strong>扩大得分的差值</strong> 。</p>

<p>给你一个整数数组 <code>stones</code> ，其中 <code>stones[i]</code> 表示 <strong>从左边开始</strong> 的第 <code>i</code> 个石头的值，如果爱丽丝和鲍勃都 <strong>发挥出最佳水平</strong> ，请返回他们 <strong>得分的差值</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>stones = [5,3,1,4,2]
<strong>输出：</strong>6
<strong>解释：</strong>
- 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
- 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
- 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
- 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
- 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
得分的差值 18 - 12 = 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>stones = [7,90,5,1,100,10,10,2]
<strong>输出：</strong>122</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == stones.length</code></li>
	<li><code>2 <= n <= 1000</code></li>
	<li><code>1 <= stones[i] <= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划
- 博弈

## 提示

1. The constraints are small enough for an N^2 solution.
2. Try using dynamic programming.

## 示例

```
[5,3,1,4,2]
[7,90,5,1,100,10,10,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int stoneGameVII(vector<int>& stones) {
        
    }
};
```

### Java

```java
class Solution {
    public int stoneGameVII(int[] stones) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stoneGameVII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        
```

### C

```c
int stoneGameVII(int* stones, int stonesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int StoneGameVII(int[] stones) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} stones
 * @return {number}
 */
var stoneGameVII = function(stones) {
    
};
```

### TypeScript

```typescript
function stoneGameVII(stones: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $stones
     * @return Integer
     */
    function stoneGameVII($stones) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stoneGameVII(_ stones: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stoneGameVII(stones: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int stoneGameVII(List<int> stones) {
    
  }
}
```

### Go

```golang
func stoneGameVII(stones []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} stones
# @return {Integer}
def stone_game_vii(stones)
    
end
```

### Scala

```scala
object Solution {
    def stoneGameVII(stones: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stone_game_vii(stones: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (stone-game-vii stones)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec stone_game_vii(Stones :: [integer()]) -> integer().
stone_game_vii(Stones) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stone_game_vii(stones :: [integer]) :: integer
  def stone_game_vii(stones) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stoneGameVII(stones: Array<Int64>): Int64 {

    }
}
```

