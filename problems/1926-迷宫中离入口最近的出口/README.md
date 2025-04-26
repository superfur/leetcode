# 1926. 迷宫中离入口最近的出口

## 题目描述

<p>给你一个 <code>m x n</code> 的迷宫矩阵 <code>maze</code> （<strong>下标从 0 开始</strong>），矩阵中有空格子（用 <code>'.'</code> 表示）和墙（用 <code>'+'</code> 表示）。同时给你迷宫的入口 <code>entrance</code> ，用 <code>entrance = [entrance<sub>row</sub>, entrance<sub>col</sub>]</code> 表示你一开始所在格子的行和列。</p>

<p>每一步操作，你可以往 <strong>上</strong>，<strong>下</strong>，<strong>左</strong> 或者 <strong>右</strong> 移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离 <code>entrance</code> <strong>最近</strong> 的出口。<strong>出口</strong> 的含义是 <code>maze</code> <strong>边界</strong> 上的 <strong>空格子</strong>。<code>entrance</code> 格子 <strong>不算</strong> 出口。</p>

<p>请你返回从 <code>entrance</code> 到最近出口的最短路径的 <strong>步数</strong> ，如果不存在这样的路径，请你返回 <code>-1</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg" style="width: 333px; height: 253px;">
<pre><b>输入：</b>maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
<b>输出：</b>1
<b>解释：</b>总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。
一开始，你在入口格子 (1,2) 处。
- 你可以往左移动 2 步到达 (1,0) 。
- 你可以往上移动 1 步到达 (0,2) 。
从入口处没法到达 (2,3) 。
所以，最近的出口是 (0,2) ，距离为 1 步。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg" style="width: 253px; height: 253px;">
<pre><b>输入：</b>maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
<b>输出：</b>2
<b>解释：</b>迷宫中只有 1 个出口，在 (1,2) 处。
(1,0) 不算出口，因为它是入口格子。
初始时，你在入口与格子 (1,0) 处。
- 你可以往右移动 2 步到达 (1,2) 处。
所以，最近的出口为 (1,2) ，距离为 2 步。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg" style="width: 173px; height: 93px;">
<pre><b>输入：</b>maze = [[".","+"]], entrance = [0,0]
<b>输出：</b>-1
<b>解释：</b>这个迷宫中没有出口。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>maze.length == m</code></li>
	<li><code>maze[i].length == n</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>maze[i][j]</code> 要么是 <code>'.'</code> ，要么是 <code>'+'</code> 。</li>
	<li><code>entrance.length == 2</code></li>
	<li><code>0 &lt;= entrance<sub>row</sub> &lt; m</code></li>
	<li><code>0 &lt;= entrance<sub>col</sub> &lt; n</code></li>
	<li><code>entrance</code> 一定是空格子。</li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 矩阵

## 提示

1. Which type of traversal lets you find the distance from a point?
2. Try using a Breadth First Search.

## 示例

```
[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
[1,2]
[["+","+","+"],[".",".","."],["+","+","+"]]
[1,0]
[[".","+"]]
[0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        
    }
};
```

### Java

```java
class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        
    }
}
```

### Python

```python
class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
```

### C

```c
int nearestExit(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NearestExit(char[][] maze, int[] entrance) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} maze
 * @param {number[]} entrance
 * @return {number}
 */
var nearestExit = function(maze, entrance) {
    
};
```

### TypeScript

```typescript
function nearestExit(maze: string[][], entrance: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $maze
     * @param Integer[] $entrance
     * @return Integer
     */
    function nearestExit($maze, $entrance) {
        
    }
}
```

### Swift

```swift
class Solution {
    func nearestExit(_ maze: [[Character]], _ entrance: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun nearestExit(maze: Array<CharArray>, entrance: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int nearestExit(List<List<String>> maze, List<int> entrance) {
    
  }
}
```

### Go

```golang
func nearestExit(maze [][]byte, entrance []int) int {
    
}
```

### Ruby

```ruby
# @param {Character[][]} maze
# @param {Integer[]} entrance
# @return {Integer}
def nearest_exit(maze, entrance)
    
end
```

### Scala

```scala
object Solution {
    def nearestExit(maze: Array[Array[Char]], entrance: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nearest_exit(maze: Vec<Vec<char>>, entrance: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (nearest-exit maze entrance)
  (-> (listof (listof char?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec nearest_exit(Maze :: [[char()]], Entrance :: [integer()]) -> integer().
nearest_exit(Maze, Entrance) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nearest_exit(maze :: [[char]], entrance :: [integer]) :: integer
  def nearest_exit(maze, entrance) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func nearestExit(maze: Array<Array<Rune>>, entrance: Array<Int64>): Int64 {

    }
}
```

