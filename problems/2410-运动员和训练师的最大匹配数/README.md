# 2410. 运动员和训练师的最大匹配数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>players</code>&nbsp;，其中&nbsp;<code>players[i]</code>&nbsp;表示第 <code>i</code>&nbsp;名运动员的 <strong>能力</strong>&nbsp;值，同时给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>trainers</code>&nbsp;，其中&nbsp;<code>trainers[j]</code>&nbsp;表示第 <code>j</code>&nbsp;名训练师的 <strong>训练能力值</strong>&nbsp;。</p>

<p>如果第 <code>i</code>&nbsp;名运动员的能力值 <strong>小于等于</strong>&nbsp;第 <code>j</code>&nbsp;名训练师的能力值，那么第&nbsp;<code>i</code>&nbsp;名运动员可以 <strong>匹配</strong>&nbsp;第&nbsp;<code>j</code>&nbsp;名训练师。除此以外，每名运动员至多可以匹配一位训练师，每位训练师最多可以匹配一位运动员。</p>

<p>请你返回满足上述要求&nbsp;<code>players</code>&nbsp;和 <code>trainers</code>&nbsp;的 <strong>最大</strong> 匹配数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>players = [4,7,9], trainers = [8,2,5,8]
<b>输出：</b>2
<b>解释：</b>
得到两个匹配的一种方案是：
- players[0] 与 trainers[0] 匹配，因为 4 &lt;= 8 。
- players[1] 与 trainers[3] 匹配，因为 7 &lt;= 8 。
可以证明 2 是可以形成的最大匹配数。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>players = [1,1,1], trainers = [10]
<b>输出：</b>1
<b>解释：</b>
训练师可以匹配所有 3 个运动员
每个运动员至多只能匹配一个训练师，所以最大答案是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= players.length, trainers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= players[i], trainers[j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 提示

1. Sort both the arrays.
2. Construct the matching greedily.

## 示例

```
[4,7,9]
[8,2,5,8]
[1,1,1]
[10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        
    }
};
```

### Java

```java
class Solution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
```

### C

```c
int matchPlayersAndTrainers(int* players, int playersSize, int* trainers, int trainersSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MatchPlayersAndTrainers(int[] players, int[] trainers) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} players
 * @param {number[]} trainers
 * @return {number}
 */
var matchPlayersAndTrainers = function(players, trainers) {
    
};
```

### TypeScript

```typescript
function matchPlayersAndTrainers(players: number[], trainers: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $players
     * @param Integer[] $trainers
     * @return Integer
     */
    function matchPlayersAndTrainers($players, $trainers) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matchPlayersAndTrainers(_ players: [Int], _ trainers: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matchPlayersAndTrainers(players: IntArray, trainers: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int matchPlayersAndTrainers(List<int> players, List<int> trainers) {
    
  }
}
```

### Go

```golang
func matchPlayersAndTrainers(players []int, trainers []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} players
# @param {Integer[]} trainers
# @return {Integer}
def match_players_and_trainers(players, trainers)
    
end
```

### Scala

```scala
object Solution {
    def matchPlayersAndTrainers(players: Array[Int], trainers: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn match_players_and_trainers(players: Vec<i32>, trainers: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (match-players-and-trainers players trainers)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec match_players_and_trainers(Players :: [integer()], Trainers :: [integer()]) -> integer().
match_players_and_trainers(Players, Trainers) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec match_players_and_trainers(players :: [integer], trainers :: [integer]) :: integer
  def match_players_and_trainers(players, trainers) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matchPlayersAndTrainers(players: Array<Int64>, trainers: Array<Int64>): Int64 {

    }
}
```

