# 3256. 放三个车的价值之和最大 I

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二维整数数组&nbsp;<code>board</code>&nbsp;，它表示一个国际象棋棋盘，其中&nbsp;<code>board[i][j]</code>&nbsp;表示格子 <code>(i, j)</code>&nbsp;的 <strong>价值</strong>&nbsp;。</p>

<p>处于 <strong>同一行</strong>&nbsp;或者 <strong>同一列</strong>&nbsp;车会互相 <strong>攻击</strong>&nbsp;。你需要在棋盘上放三个车，确保它们两两之间都&nbsp;<b>无法互相攻击</b>&nbsp;。</p>

<p>请你返回满足上述条件下，三个车所在格子 <strong>值</strong>&nbsp;之和 <strong>最大</strong>&nbsp;为多少。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>board = </span>[[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]</p>

<p><b>输出：</b>4</p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/08/rooks2.png" style="width: 294px; height: 450px;" /></p>

<p>我们可以将车分别放在格子&nbsp;<code>(0, 2)</code>&nbsp;，<code>(1, 3)</code>&nbsp;和&nbsp;<code>(2, 1)</code>&nbsp;处，价值之和为&nbsp;<code>1 + 1 + 2 = 4</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>board = [[1,2,3],[4,5,6],[7,8,9]]</span></p>

<p><span class="example-io"><b>输出：</b>15</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将车分别放在格子&nbsp;<code>(0, 0)</code>&nbsp;，<code>(1, 1)</code>&nbsp;和&nbsp;<code>(2, 2)</code>&nbsp;处，价值之和为&nbsp;<code>1 + 5 + 9 = 15</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>board = [[1,1,1],[1,1,1],[1,1,1]]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>我们可以将车分别放在格子&nbsp;<code>(0, 2)</code>&nbsp;，<code>(1, 1)</code>&nbsp;和&nbsp;<code>(2, 0)</code>&nbsp;处，价值之和为&nbsp;<code>1 + 1 + 1 = 3</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= m == board.length &lt;= 100</code></li>
	<li><code>3 &lt;= n == board[i].length &lt;= 100</code></li>
	<li><code>-10<sup>9</sup> &lt;= board[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 枚举
- 矩阵

## 提示

1. Store the largest 3 values for each row.
2. Select any 3 rows and brute force all combinations.

## 示例

```
[[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]
[[1,2,3],[4,5,6],[7,8,9]]
[[1,1,1],[1,1,1],[1,1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public long maximumValueSum(int[][] board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumValueSum(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        
```

### C

```c
long long maximumValueSum(int** board, int boardSize, int* boardColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaximumValueSum(int[][] board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} board
 * @return {number}
 */
var maximumValueSum = function(board) {
    
};
```

### TypeScript

```typescript
function maximumValueSum(board: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $board
     * @return Integer
     */
    function maximumValueSum($board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumValueSum(_ board: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumValueSum(board: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumValueSum(List<List<int>> board) {
    
  }
}
```

### Go

```golang
func maximumValueSum(board [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} board
# @return {Integer}
def maximum_value_sum(board)
    
end
```

### Scala

```scala
object Solution {
    def maximumValueSum(board: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_value_sum(board: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-value-sum board)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_value_sum(Board :: [[integer()]]) -> integer().
maximum_value_sum(Board) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_value_sum(board :: [[integer]]) :: integer
  def maximum_value_sum(board) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumValueSum(board: Array<Array<Int64>>): Int64 {

    }
}
```

