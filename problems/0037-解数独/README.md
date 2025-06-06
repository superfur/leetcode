# 37. 解数独

## 题目描述

<p>编写一个程序，通过填充空格来解决数独问题。</p>

<p>数独的解法需<strong> 遵循如下规则</strong>：</p>

<ol>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一行只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一列只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一个以粗实线分隔的&nbsp;<code>3x3</code>&nbsp;宫内只能出现一次。（请参考示例图）</li>
</ol>

<p>数独部分空格内已填入了数字，空白格用&nbsp;<code>'.'</code>&nbsp;表示。</p>

<p>&nbsp;</p>

<div class="top-view__1vxA">
<div class="original__bRMd">
<div>
<p><strong>示例 1：</strong></p>
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png" style="height:250px; width:250px" />
<pre>
<strong>输入：</strong>board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
<strong>输出：</strong>[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
<strong>解释：</strong>输入的数独如上图所示，唯一有效的解决方案如下所示：

<img src=" https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714_solutionsvg.png" style="height:250px; width:250px" />
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> 是一位数字或者 <code>'.'</code></li>
	<li>题目数据 <strong>保证</strong> 输入数独仅有一个解</li>
</ul>
</div>
</div>
</div>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 回溯
- 矩阵

## 示例

```
[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public void solveSudoku(char[][] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
```

### Python3

```python3
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
```

### C

```c
void solveSudoku(char** board, int boardSize, int* boardColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public void SolveSudoku(char[][] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    
};
```

### TypeScript

```typescript
/**
 Do not return anything, modify board in-place instead.
 */
function solveSudoku(board: string[][]): void {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[][] $board
     * @return NULL
     */
    function solveSudoku(&$board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func solveSudoku(_ board: inout [[Character]]) {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun solveSudoku(board: Array<CharArray>): Unit {
        
    }
}
```

### Dart

```dart
class Solution {
  void solveSudoku(List<List<String>> board) {
    
  }
}
```

### Go

```golang
func solveSudoku(board [][]byte)  {
    
}
```

### Ruby

```ruby
# @param {Character[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
def solve_sudoku(board)
    
end
```

### Scala

```scala
object Solution {
    def solveSudoku(board: Array[Array[Char]]): Unit = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        
    }
}
```

### Cangjie

```cangjie
class Solution {
    func solveSudoku(board: Array<Array<Rune>>): Unit {

    }
}
```

