# 2056. 棋盘上有效移动组合的数目

## 题目描述

<p>有一个&nbsp;<code>8 x 8</code>&nbsp;的棋盘，它包含&nbsp;<code>n</code>&nbsp;个棋子（棋子包括车，后和象三种）。给你一个长度为 <code>n</code>&nbsp;的字符串数组&nbsp;<code>pieces</code>&nbsp;，其中&nbsp;<code>pieces[i]</code>&nbsp;表示第 <code>i</code>&nbsp;个棋子的类型（车，后或象）。除此以外，还给你一个长度为 <code>n</code>&nbsp;的二维整数数组&nbsp;<code>positions</code>&nbsp;，其中 <code>positions[i] = [r<sub>i</sub>, c<sub>i</sub>]</code>&nbsp;表示第 <code>i</code>&nbsp;个棋子现在在棋盘上的位置为&nbsp;<code>(r<sub>i</sub>, c<sub>i</sub>)</code>&nbsp;，棋盘下标从 <strong>1</strong>&nbsp;开始。</p>

<p>每个棋子的移动中，首先选择移动的 <strong>方向</strong>&nbsp;，然后选择 <strong>移动的步数</strong>&nbsp;，同时你要确保移动过程中棋子不能移到棋盘以外的地方。棋子需按照以下规则移动：</p>

<ul>
	<li>车可以 <strong>水平或者竖直</strong>&nbsp;从&nbsp;<code>(r, c)</code>&nbsp;沿着方向&nbsp;<code>(r+1, c)</code>，<code>(r-1, c)</code>，<code>(r, c+1)</code>&nbsp;或者&nbsp;<code>(r, c-1)</code>&nbsp;移动。</li>
	<li>后可以 <strong>水平竖直或者斜对角</strong>&nbsp;从&nbsp;<code>(r, c)</code> 沿着方向&nbsp;<code>(r+1, c)</code>，<code>(r-1, c)</code>，<code>(r, c+1)</code>，<code>(r, c-1)</code>，<code>(r+1, c+1)</code>，<code>(r+1, c-1)</code>，<code>(r-1, c+1)</code>，<code>(r-1, c-1)</code>&nbsp;移动。</li>
	<li>象可以 <strong>斜对角</strong>&nbsp;从&nbsp;<code>(r, c)</code>&nbsp;沿着方向&nbsp;<code>(r+1, c+1)</code>，<code>(r+1, c-1)</code>，<code>(r-1, c+1)</code>，<code>(r-1, c-1)</code>&nbsp;移动。</li>
</ul>

<p>你必须同时 <strong>移动</strong> 棋盘上的每一个棋子。<strong>移动组合</strong>&nbsp;包含所有棋子的 <strong>移动</strong>&nbsp;。每一秒，每个棋子都沿着它们选择的方向往前移动 <strong>一步</strong>&nbsp;，直到它们到达目标位置。所有棋子从时刻 <code>0</code>&nbsp;开始移动。如果在某个时刻，两个或者更多棋子占据了同一个格子，那么这个移动组合 <strong>不有效</strong>&nbsp;。</p>

<p>请你返回 <strong>有效</strong>&nbsp;移动组合的数目。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>初始时，<strong>不会有两个棋子</strong>&nbsp;在 <strong>同一个位置 。</strong></li>
	<li>有可能在一个移动组合中，有棋子不移动。</li>
	<li>如果两个棋子 <strong>直接相邻</strong>&nbsp;且两个棋子下一秒要互相占据对方的位置，可以将它们在同一秒内 <strong>交换位置</strong>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a1.png" style="width: 215px; height: 215px;" /></p>

<pre>
<b>输入：</b>pieces = ["rook"], positions = [[1,1]]
<b>输出：</b>15
<b>解释：</b>上图展示了棋子所有可能的移动。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a2.png" style="width: 215px; height: 215px;" /></p>

<pre>
<b>输入：</b>pieces = ["queen"], positions = [[1,1]]
<b>输出：</b>22
<b>解释：</b>上图展示了棋子所有可能的移动。
</pre>

<p><strong>示例 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a3.png" style="width: 214px; height: 215px;" /></p>

<pre>
<b>输入：</b>pieces = ["bishop"], positions = [[4,3]]
<b>输出：</b>12
<b>解释：</b>上图展示了棋子所有可能的移动。
</pre>

<p><strong>示例 4:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a4.png" style="width: 216px; height: 219px;" /></p>

<pre>
<b>输入：</b>pieces = ["rook","rook"], positions = [[1,1],[8,8]]
<b>输出：</b>223
<b>解释：</b>每个车有 15 种移动，所以总共有 15 * 15 = 225 种移动组合。
但是，有两个是不有效的移动组合：
- 将两个车都移动到 (8, 1) ，会导致它们在同一个格子相遇。
- 将两个车都移动到 (1, 8) ，会导致它们在同一个格子相遇。
所以，总共有 225 - 2 = 223 种有效移动组合。
注意，有两种有效的移动组合，分别是一个车在 (1, 8) ，另一个车在 (8, 1) 。
即使棋盘状态是相同的，这两个移动组合被视为不同的，因为每个棋子移动操作是不相同的。
</pre>

<p><strong>示例 5：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a5.png" style="width: 214px; height: 213px;" /></p>

<pre>
<b>输入：</b>pieces = ["queen","bishop"], positions = [[5,7],[3,4]]
<b>输出：</b>281
<b>解释：</b>总共有 12 * 24 = 288 种移动组合。
但是，有一些不有效的移动组合：
- 如果后停在 (6, 7) ，它会阻挡象到达 (6, 7) 或者 (7, 8) 。
- 如果后停在 (5, 6) ，它会阻挡象到达 (5, 6) ，(6, 7) 或者 (7, 8) 。
- 如果象停在 (5, 2) ，它会阻挡后到达 (5, 2) 或者 (5, 1) 。
在 288 个移动组合当中，281 个是有效的。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == pieces.length </code></li>
	<li><code>n == positions.length</code></li>
	<li><code>1 &lt;= n &lt;= 4</code></li>
	<li><code>pieces</code>&nbsp;只包含字符串&nbsp;<code>"rook"</code>&nbsp;，<code>"queen"</code>&nbsp;和&nbsp;<code>"bishop"</code>&nbsp;。</li>
	<li>棋盘上最多只有一个后。</li>
	<li><code>1 &lt;= r<sub>i</sub>, c<sub>i</sub> &lt;= 8</code></li>
	<li>每一个&nbsp;<code>positions[i]</code>&nbsp;互不相同。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 字符串
- 回溯
- 模拟

## 提示

1. N is small, we can generate all possible move combinations.
2. For each possible move combination, determine which ones are valid.

## 示例

```
["rook"]
[[1,1]]
["queen"]
[[1,1]]
["bishop"]
[[4,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCombinations(vector<string>& pieces, vector<vector<int>>& positions) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCombinations(String[] pieces, int[][] positions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCombinations(self, pieces, positions):
        """
        :type pieces: List[str]
        :type positions: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        
```

### C

```c
int countCombinations(char** pieces, int piecesSize, int** positions, int positionsSize, int* positionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCombinations(string[] pieces, int[][] positions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} pieces
 * @param {number[][]} positions
 * @return {number}
 */
var countCombinations = function(pieces, positions) {
    
};
```

### TypeScript

```typescript
function countCombinations(pieces: string[], positions: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $pieces
     * @param Integer[][] $positions
     * @return Integer
     */
    function countCombinations($pieces, $positions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCombinations(_ pieces: [String], _ positions: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCombinations(pieces: Array<String>, positions: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCombinations(List<String> pieces, List<List<int>> positions) {
    
  }
}
```

### Go

```golang
func countCombinations(pieces []string, positions [][]int) int {
    
}
```

### Ruby

```ruby
# @param {String[]} pieces
# @param {Integer[][]} positions
# @return {Integer}
def count_combinations(pieces, positions)
    
end
```

### Scala

```scala
object Solution {
    def countCombinations(pieces: Array[String], positions: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_combinations(pieces: Vec<String>, positions: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-combinations pieces positions)
  (-> (listof string?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_combinations(Pieces :: [unicode:unicode_binary()], Positions :: [[integer()]]) -> integer().
count_combinations(Pieces, Positions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_combinations(pieces :: [String.t], positions :: [[integer]]) :: integer
  def count_combinations(pieces, positions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCombinations(pieces: Array<String>, positions: Array<Array<Int64>>): Int64 {

    }
}
```

