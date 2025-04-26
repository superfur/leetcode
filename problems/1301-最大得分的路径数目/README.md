# 1301. 最大得分的路径数目

## 题目描述

<p>给你一个正方形字符数组&nbsp;<code>board</code>&nbsp;，你从数组最右下方的字符&nbsp;<code>&#39;S&#39;</code>&nbsp;出发。</p>

<p>你的目标是到达数组最左上角的字符&nbsp;<code>&#39;E&#39;</code> ，数组剩余的部分为数字字符&nbsp;<code>1, 2, ..., 9</code>&nbsp;或者障碍 <code>&#39;X&#39;</code>。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。</p>

<p>一条路径的 「得分」 定义为：路径上所有数字的和。</p>

<p>请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对&nbsp;<strong><code>10^9 + 7</code></strong> <strong>取余</strong>。</p>

<p>如果没有任何路径可以到达终点，请返回&nbsp;<code>[0, 0]</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>board = [&quot;E23&quot;,&quot;2X2&quot;,&quot;12S&quot;]
<strong>输出：</strong>[7,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>board = [&quot;E12&quot;,&quot;1X1&quot;,&quot;21S&quot;]
<strong>输出：</strong>[4,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>board = [&quot;E11&quot;,&quot;XXX&quot;,&quot;11S&quot;]
<strong>输出：</strong>[0,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= board.length == board[i].length &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵

## 提示

1. Use dynamic programming to find the path with the max score.
2. Use another dynamic programming array to count the number of paths with max score.

## 示例

```
["E23","2X2","12S"]
["E12","1X1","21S"]
["E11","XXX","11S"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] pathsWithMaxScore(List<String> board) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* pathsWithMaxScore(char** board, int boardSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] PathsWithMaxScore(IList<string> board) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} board
 * @return {number[]}
 */
var pathsWithMaxScore = function(board) {
    
};
```

### TypeScript

```typescript
function pathsWithMaxScore(board: string[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $board
     * @return Integer[]
     */
    function pathsWithMaxScore($board) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pathsWithMaxScore(_ board: [String]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pathsWithMaxScore(board: List<String>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> pathsWithMaxScore(List<String> board) {
    
  }
}
```

### Go

```golang
func pathsWithMaxScore(board []string) []int {
    
}
```

### Ruby

```ruby
# @param {String[]} board
# @return {Integer[]}
def paths_with_max_score(board)
    
end
```

### Scala

```scala
object Solution {
    def pathsWithMaxScore(board: List[String]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn paths_with_max_score(board: Vec<String>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (paths-with-max-score board)
  (-> (listof string?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec paths_with_max_score(Board :: [unicode:unicode_binary()]) -> [integer()].
paths_with_max_score(Board) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec paths_with_max_score(board :: [String.t]) :: [integer]
  def paths_with_max_score(board) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pathsWithMaxScore(board: ArrayList<String>): Array<Int64> {

    }
}
```

