# 1222. 可以攻击国王的皇后

## 题目描述

<p>在一个 <strong>下标从 0 开始</strong> 的 <code>8 x 8</code> 棋盘上，可能有多个黑皇后和一个白国王。</p>

<p>给你一个二维整数数组 <code>queens</code>，其中 <code>queens[i] = [xQueeni, yQueeni]</code> 表示第 <code>i</code> 个黑皇后在棋盘上的位置。还给你一个长度为 <code>2</code> 的整数数组 <code>king</code>，其中 <code>king = [xKing, yKing]</code> 表示白国王的位置。</p>

<p>返回 <em>能够直接攻击国王的黑皇后的坐标</em>。你可以以 <strong>任何顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1703052515-HqjAJq-chess1.jpg" style="width: 400px; height: 400px;" /></p>

<pre>
<strong>输入：</strong>queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
<strong>输出：</strong>[[0,1],[1,0],[3,3]]
<strong>解释：</strong>上面的图示显示了三个可以直接攻击国王的皇后和三个不能攻击国王的皇后（用红色虚线标记）。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://pic.leetcode.cn/1703052660-bPPflt-chess2.jpg" style="width: 400px; height: 400px;" /></strong></p>

<pre>
<strong>输入：</strong>queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
<strong>输出：</strong>[[2,2],[3,4],[4,4]]
<strong>解释：</strong>上面的图示显示了三个能够直接攻击国王的黑皇后和三个不能攻击国王的黑皇后（用红色虚线标记）。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><meta charset="UTF-8" /><code>1 &lt;= queens.length &lt; 64</code></li>
	<li><code>queens[i].length == king.length == 2</code></li>
	<li><code>0 &lt;= xQueen<sub>i</sub>, yQueen<sub>i</sub>, xKing, yKing &lt; 8</code></li>
	<li>所有给定的位置都是 <strong>唯一</strong> 的。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 模拟

## 提示

1. Check 8 directions around the King.
2. Find the nearest queen in each direction.

## 示例

```
[[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
[0,0]
[[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]]
[3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> queensAttacktheKing(vector<vector<int>>& queens, vector<int>& king) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> queensAttacktheKing(int[][] queens, int[] king) {
        
    }
}
```

### Python

```python
class Solution(object):
    def queensAttacktheKing(self, queens, king):
        """
        :type queens: List[List[int]]
        :type king: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** queensAttacktheKing(int** queens, int queensSize, int* queensColSize, int* king, int kingSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> QueensAttacktheKing(int[][] queens, int[] king) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} queens
 * @param {number[]} king
 * @return {number[][]}
 */
var queensAttacktheKing = function(queens, king) {
    
};
```

### TypeScript

```typescript
function queensAttacktheKing(queens: number[][], king: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $queens
     * @param Integer[] $king
     * @return Integer[][]
     */
    function queensAttacktheKing($queens, $king) {
        
    }
}
```

### Swift

```swift
class Solution {
    func queensAttacktheKing(_ queens: [[Int]], _ king: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun queensAttacktheKing(queens: Array<IntArray>, king: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> queensAttacktheKing(List<List<int>> queens, List<int> king) {
    
  }
}
```

### Go

```golang
func queensAttacktheKing(queens [][]int, king []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} queens
# @param {Integer[]} king
# @return {Integer[][]}
def queens_attackthe_king(queens, king)
    
end
```

### Scala

```scala
object Solution {
    def queensAttacktheKing(queens: Array[Array[Int]], king: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn queens_attackthe_king(queens: Vec<Vec<i32>>, king: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (queens-attackthe-king queens king)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec queens_attackthe_king(Queens :: [[integer()]], King :: [integer()]) -> [[integer()]].
queens_attackthe_king(Queens, King) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec queens_attackthe_king(queens :: [[integer]], king :: [integer]) :: [[integer]]
  def queens_attackthe_king(queens, king) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func queensAttacktheKing(queens: Array<Array<Int64>>, king: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

