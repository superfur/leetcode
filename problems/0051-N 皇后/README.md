# 51. N 皇后

## 题目描述

<p>按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。</p>

<p><strong>n&nbsp;皇后问题</strong> 研究的是如何将 <code>n</code>&nbsp;个皇后放置在 <code>n×n</code> 的棋盘上，并且使皇后彼此之间不能相互攻击。</p>

<p>给你一个整数 <code>n</code> ，返回所有不同的&nbsp;<strong>n<em>&nbsp;</em>皇后问题</strong> 的解决方案。</p>

<div class="original__bRMd">
<div>
<p>每一种解法包含一个不同的&nbsp;<strong>n 皇后问题</strong> 的棋子放置方案，该方案中 <code>'Q'</code> 和 <code>'.'</code> 分别代表了皇后和空位。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong>解释：</strong>如上图所示，4 皇后问题存在两个不同的解法。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[["Q"]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 9</code></li>
</ul>
</div>
</div>


## 难度

Hard

## 标签

- 数组
- 回溯

## 示例

```
4
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<String>> solveNQueens(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
```

### Python3

```python3
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
char*** solveNQueens(int n, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<string>> SolveNQueens(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {string[][]}
 */
var solveNQueens = function(n) {
    
};
```

### TypeScript

```typescript
function solveNQueens(n: number): string[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return String[][]
     */
    function solveNQueens($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func solveNQueens(_ n: Int) -> [[String]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun solveNQueens(n: Int): List<List<String>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<String>> solveNQueens(int n) {
    
  }
}
```

### Go

```golang
func solveNQueens(n int) [][]string {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {String[][]}
def solve_n_queens(n)
    
end
```

### Scala

```scala
object Solution {
    def solveNQueens(n: Int): List[List[String]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        
    }
}
```

### Racket

```racket
(define/contract (solve-n-queens n)
  (-> exact-integer? (listof (listof string?)))
  )
```

### Erlang

```erlang
-spec solve_n_queens(N :: integer()) -> [[unicode:unicode_binary()]].
solve_n_queens(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec solve_n_queens(n :: integer) :: [[String.t]]
  def solve_n_queens(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func solveNQueens(n: Int64): ArrayList<ArrayList<String>> {

    }
}
```

