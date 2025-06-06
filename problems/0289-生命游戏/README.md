# 289. 生命游戏

## 题目描述

<p>根据&nbsp;<a href="https://baike.baidu.com/item/%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F/2926434?fr=aladdin" target="_blank">百度百科</a>&nbsp;，&nbsp;<strong>生命游戏</strong>&nbsp;，简称为 <strong>生命</strong> ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。</p>

<p>给定一个包含 <code>m × n</code>&nbsp;个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： <code>1</code> 即为 <strong>活细胞</strong> （live），或 <code>0</code> 即为 <strong>死细胞</strong> （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：</p>

<ol>
	<li>如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；</li>
	<li>如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；</li>
	<li>如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；</li>
	<li>如果死细胞周围正好有三个活细胞，则该位置死细胞复活；</li>
</ol>

<p>下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是 <strong>同时</strong> 发生的。给你 <code>m x n</code> 网格面板 <code>board</code> 的当前状态，返回下一个状态。</p>

<p>给定当前&nbsp;<code>board</code>&nbsp;的状态，<strong>更新</strong>&nbsp;<code>board</code>&nbsp;到下一个状态。</p>

<p><strong>注意</strong> 你不需要返回任何东西。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg" />
<pre>
<strong>输入：</strong>board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
<strong>输出：</strong>[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg" />
<pre>
<strong>输入：</strong>board = [[1,1],[1,0]]
<strong>输出：</strong>[[1,1],[1,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == board.length</code></li>
	<li><code>n == board[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 25</code></li>
	<li><code>board[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。</li>
	<li>本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 模拟

## 示例

```
[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
[[1,1],[1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public void gameOfLife(int[][] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
```

### C

```c
void gameOfLife(int** board, int boardSize, int* boardColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void GameOfLife(int[][] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var gameOfLife = function(board) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify board in-place instead.
 */
function gameOfLife(board: number[][]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return NULL
     */
    function gameOfLife(&$board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func gameOfLife(_ board: inout [[Int]]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun gameOfLife(board: Array<IntArray>): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void gameOfLife(List<List<int>> board) {
    
  }
}
```

### Go

```golang
func gameOfLife(board [][]int)  {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def game_of_life(board)
    
end
```

### Scala

```scala
object Solution {
    def gameOfLife(board: Array[Array[Int]]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func gameOfLife(board: Array<Array<Int64>>): Unit {

    }
}
```

