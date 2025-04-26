# 面试题 08.12. 八皇后

## 题目描述

<p>设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。</p>

<p><strong>注意：</strong>本题相对原题做了扩展</p>

<p><strong>示例：</strong></p>

<pre>
<strong> 输入</strong>：4
<strong> 输出</strong>：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
<strong> 解释：</strong>4 皇后问题存在如下两个不同的解法。
[
&nbsp;[".Q..", &nbsp;// 解法 1
&nbsp; "...Q",
&nbsp; "Q...",
&nbsp; "..Q."],

&nbsp;["..Q.", &nbsp;// 解法 2
&nbsp; "Q...",
&nbsp; "...Q",
&nbsp; ".Q.."]
]
</pre>


## 难度

Hard

## 标签

- 数组
- 回溯

## 提示

1. 我们知道每一行都有一个皇后。你能试试所有的可能性吗？
2. 每行都必须有个皇后。从最后一行开始。有8个不同的列你可以放皇后。你能挨个试试吗？
3. 把它拆分成更小的子问题。第8行的皇后必定在第1、2、3、4、5、6、7或8列。当一个皇后在第8行第3列，你能输出所有可能的八皇后位置吗？然后你需要做的就是检查将一个皇后放在第7行的所有情况。

## 示例

```
4
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

