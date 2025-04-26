# 1219. 黄金矿工

## 题目描述

<p>你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为&nbsp;<code>m * n</code> 的网格 <code>grid</code> 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 <code>0</code>。</p>

<p>为了使收益最大化，矿工需要按以下规则来开采黄金：</p>

<ul>
	<li>每当矿工进入一个单元，就会收集该单元格中的所有黄金。</li>
	<li>矿工每次可以从当前位置向上下左右四个方向走。</li>
	<li>每个单元格只能被开采（进入）一次。</li>
	<li><strong>不得开采</strong>（进入）黄金数目为 <code>0</code> 的单元格。</li>
	<li>矿工可以从网格中 <strong>任意一个</strong> 有黄金的单元格出发或者是停止。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>grid = [[0,6,0],[5,8,7],[0,9,0]]
<strong>输出：</strong>24
<strong>解释：</strong>
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -&gt; 8 -&gt; 7。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
<strong>输出：</strong>28
<strong>解释：</strong>
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -&gt; 2 -&gt; 3 -&gt; 4 -&gt; 5 -&gt; 6 -&gt; 7。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length,&nbsp;grid[i].length &lt;= 15</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 100</code></li>
	<li>最多 <strong>25 </strong>个单元格中有黄金。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 回溯
- 矩阵

## 提示

1. Use recursion to try all such paths and find the one with the maximum value.

## 示例

```
[[0,6,0],[5,8,7],[0,9,0]]
[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaximumGold(vector<vector<int>>& grid) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMaximumGold(int[][] grid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
```

### C

```c
int getMaximumGold(int** grid, int gridSize, int* gridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMaximumGold(int[][] grid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var getMaximumGold = function(grid) {
    
};
```

### TypeScript

```typescript
function getMaximumGold(grid: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $grid
     * @return Integer
     */
    function getMaximumGold($grid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaximumGold(_ grid: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaximumGold(grid: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaximumGold(List<List<int>> grid) {
    
  }
}
```

### Go

```golang
func getMaximumGold(grid [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} grid
# @return {Integer}
def get_maximum_gold(grid)
    
end
```

### Scala

```scala
object Solution {
    def getMaximumGold(grid: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_maximum_gold(grid: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-maximum-gold grid)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec get_maximum_gold(Grid :: [[integer()]]) -> integer().
get_maximum_gold(Grid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_maximum_gold(grid :: [[integer]]) :: integer
  def get_maximum_gold(grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaximumGold(grid: Array<Array<Int64>>): Int64 {

    }
}
```

