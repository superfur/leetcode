# 1900. 最佳运动员的比拼回合

## 题目描述

<p><code>n</code> 名运动员参与一场锦标赛，所有运动员站成一排，并根据 <strong>最开始的</strong> 站位从 <code>1</code> 到 <code>n</code> 编号（运动员 <code>1</code> 是这一排中的第一个运动员，运动员 <code>2</code> 是第二个运动员，依此类推）。</p>

<p>锦标赛由多个回合组成（从回合 <code>1</code> 开始）。每一回合中，这一排从前往后数的第 <code>i</code> 名运动员需要与从后往前数的第 <code>i</code> 名运动员比拼，获胜者将会进入下一回合。如果当前回合中运动员数目为奇数，那么中间那位运动员将轮空晋级下一回合。</p>

<ul>
	<li>例如，当前回合中，运动员 <code>1, 2, 4, 6, 7</code> 站成一排

	<ul>
		<li>运动员 <code>1</code> 需要和运动员 <code>7</code> 比拼</li>
		<li>运动员 <code>2</code> 需要和运动员 <code>6</code> 比拼</li>
		<li>运动员 <code>4</code> 轮空晋级下一回合</li>
	</ul>
	</li>
</ul>

<p>每回合结束后，获胜者将会基于最开始分配给他们的原始顺序（升序）重新排成一排。</p>

<p>编号为 <code>firstPlayer</code> 和 <code>secondPlayer</code> 的运动员是本场锦标赛中的最佳运动员。在他们开始比拼之前，完全可以战胜任何其他运动员。而任意两个其他运动员进行比拼时，其中任意一个都有获胜的可能，因此你可以 <strong>裁定</strong> 谁是这一回合的获胜者。</p>

<p>给你三个整数 <code>n</code>、<code>firstPlayer</code> 和 <code>secondPlayer</code> 。返回一个由两个值组成的整数数组，分别表示两位最佳运动员在本场锦标赛中比拼的 <strong>最早</strong> 回合数和 <strong>最晚</strong> 回合数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 11, firstPlayer = 2, secondPlayer = 4
<strong>输出：</strong>[3,4]
<strong>解释：</strong>
一种能够产生最早回合数的情景是：
回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
回合 2：2, 3, 4, 5, 6, 11
回合 3：2, 3, 4
一种能够产生最晚回合数的情景是：
回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
回合 2：1, 2, 3, 4, 5, 6
回合 3：1, 2, 4
回合 4：2, 4
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 5, firstPlayer = 1, secondPlayer = 5
<strong>输出：</strong>[1,1]
<strong>解释：</strong>两名最佳运动员 1 和 5 将会在回合 1 进行比拼。
不存在使他们在其他回合进行比拼的可能。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 28</code></li>
	<li><code>1 &lt;= firstPlayer &lt; secondPlayer &lt;= n</code></li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 动态规划

## 提示

1. Brute force using bitmasks and simulate the rounds.
2. Calculate each state one time and save its solution.

## 示例

```
11
2
4
5
1
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        
    }
}
```

### Python

```python
class Solution(object):
    def earliestAndLatest(self, n, firstPlayer, secondPlayer):
        """
        :type n: int
        :type firstPlayer: int
        :type secondPlayer: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* earliestAndLatest(int n, int firstPlayer, int secondPlayer, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] EarliestAndLatest(int n, int firstPlayer, int secondPlayer) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} firstPlayer
 * @param {number} secondPlayer
 * @return {number[]}
 */
var earliestAndLatest = function(n, firstPlayer, secondPlayer) {
    
};
```

### TypeScript

```typescript
function earliestAndLatest(n: number, firstPlayer: number, secondPlayer: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $firstPlayer
     * @param Integer $secondPlayer
     * @return Integer[]
     */
    function earliestAndLatest($n, $firstPlayer, $secondPlayer) {
        
    }
}
```

### Swift

```swift
class Solution {
    func earliestAndLatest(_ n: Int, _ firstPlayer: Int, _ secondPlayer: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> earliestAndLatest(int n, int firstPlayer, int secondPlayer) {
    
  }
}
```

### Go

```golang
func earliestAndLatest(n int, firstPlayer int, secondPlayer int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} first_player
# @param {Integer} second_player
# @return {Integer[]}
def earliest_and_latest(n, first_player, second_player)
    
end
```

### Scala

```scala
object Solution {
    def earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn earliest_and_latest(n: i32, first_player: i32, second_player: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (earliest-and-latest n firstPlayer secondPlayer)
  (-> exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec earliest_and_latest(N :: integer(), FirstPlayer :: integer(), SecondPlayer :: integer()) -> [integer()].
earliest_and_latest(N, FirstPlayer, SecondPlayer) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec earliest_and_latest(n :: integer, first_player :: integer, second_player :: integer) :: [integer]
  def earliest_and_latest(n, first_player, second_player) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func earliestAndLatest(n: Int64, firstPlayer: Int64, secondPlayer: Int64): Array<Int64> {

    }
}
```

