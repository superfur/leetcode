# 3238. 求出胜利玩家的数目

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，表示在一个游戏中的玩家数目。同时给你一个二维整数数组&nbsp;<code>pick</code>&nbsp;，其中&nbsp;<code>pick[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;表示玩家&nbsp;<code>x<sub>i</sub></code>&nbsp;获得了一个颜色为&nbsp;<code>y<sub>i</sub></code>&nbsp;的球。</p>

<p>如果玩家 <code>i</code>&nbsp;获得的球中任何一种颜色球的数目 <strong>严格大于</strong>&nbsp;<code>i</code>&nbsp;个，那么我们说玩家 <code>i</code>&nbsp;是胜利玩家。换句话说：</p>

<ul>
	<li>如果玩家 0 获得了任何的球，那么玩家 0 是胜利玩家。</li>
	<li>如果玩家 1 获得了至少 2 个相同颜色的球，那么玩家 1 是胜利玩家。</li>
	<li>...</li>
	<li>如果玩家 <code>i</code>&nbsp;获得了至少&nbsp;<code>i + 1</code>&nbsp;个相同颜色的球，那么玩家 <code>i</code>&nbsp;是胜利玩家。</li>
</ul>

<p>请你返回游戏中 <strong>胜利玩家</strong>&nbsp;的数目。</p>

<p><strong>注意</strong>，可能有多个玩家是胜利玩家。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>玩家 0 和玩家 1 是胜利玩家，玩家 2 和玩家 3 不是胜利玩家。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, pick = [[1,1],[1,2],[1,3],[1,4]]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>没有胜利玩家。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, pick = [[1,1],[2,4],[2,4],[2,4]]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<p>玩家 2 是胜利玩家，因为玩家 2 获得了 3 个颜色为 4 的球。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10</code></li>
	<li><code>1 &lt;= pick.length &lt;= 100</code></li>
	<li><code>pick[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub> &lt;= n - 1 </code></li>
	<li><code>0 &lt;= y<sub>i</sub> &lt;= 10</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Keep track of the number of balls of each color for each user using hashing.
2. Find the maximum color that occurred for each player.

## 示例

```
4
[[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]
5
[[1,1],[1,2],[1,3],[1,4]]
5
[[1,1],[2,4],[2,4],[2,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int winningPlayerCount(int n, vector<vector<int>>& pick) {
        
    }
};
```

### Java

```java
class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        
    }
}
```

### Python

```python
class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        
```

### C

```c
int winningPlayerCount(int n, int** pick, int pickSize, int* pickColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WinningPlayerCount(int n, int[][] pick) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} pick
 * @return {number}
 */
var winningPlayerCount = function(n, pick) {
    
};
```

### TypeScript

```typescript
function winningPlayerCount(n: number, pick: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $pick
     * @return Integer
     */
    function winningPlayerCount($n, $pick) {
        
    }
}
```

### Swift

```swift
class Solution {
    func winningPlayerCount(_ n: Int, _ pick: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun winningPlayerCount(n: Int, pick: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int winningPlayerCount(int n, List<List<int>> pick) {
    
  }
}
```

### Go

```golang
func winningPlayerCount(n int, pick [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} pick
# @return {Integer}
def winning_player_count(n, pick)
    
end
```

### Scala

```scala
object Solution {
    def winningPlayerCount(n: Int, pick: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn winning_player_count(n: i32, pick: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (winning-player-count n pick)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec winning_player_count(N :: integer(), Pick :: [[integer()]]) -> integer().
winning_player_count(N, Pick) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec winning_player_count(n :: integer, pick :: [[integer]]) :: integer
  def winning_player_count(n, pick) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func winningPlayerCount(n: Int64, pick: Array<Array<Int64>>): Int64 {

    }
}
```

