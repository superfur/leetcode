# 587. 安装栅栏

## 题目描述

<p>给定一个数组 <code>trees</code>，其中 <code>trees[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> 表示树在花园中的位置。</p>

<p>你被要求用最短长度的绳子把整个花园围起来，因为绳子很贵。只有把&nbsp;<strong>所有的树都围起来</strong>，花园才围得很好。</p>

<p>返回<em>恰好位于围栏周边的树木的坐标</em>。</p>

<p><strong>示例 1:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/24/erect2-plane.jpg" style="width: 400px;" /></p>

<pre>
<strong>输入:</strong> points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
<strong>输出:</strong> [[1,1],[2,0],[3,3],[2,4],[4,2]]</pre>

<p><strong>示例 2:</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/04/24/erect1-plane.jpg" style="height: 393px; width: 400px;" /></p>

<pre>
<strong>输入:</strong> points = [[1,2],[2,2],[4,2]]
<strong>输出:</strong> [[4,2],[2,2],[1,2]]</pre>

<p>&nbsp;</p>

<p><strong>注意:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 3000</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub>&nbsp;&lt;= 100</code></li>
	<li>
	<p data-group="1-1">所有给定的点都是&nbsp;<strong>唯一&nbsp;</strong>的。</p>
	</li>
</ul>


## 难度

Hard

## 标签

- 几何
- 数组
- 数学

## 示例

```
[[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
[[1,2],[2,2],[4,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> outerTrees(vector<vector<int>>& trees) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] outerTrees(int[][] trees) {
        
    }
}
```

### Python

```python
class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** outerTrees(int** trees, int treesSize, int* treesColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] OuterTrees(int[][] trees) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} trees
 * @return {number[][]}
 */
var outerTrees = function(trees) {
    
};
```

### TypeScript

```typescript
function outerTrees(trees: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $trees
     * @return Integer[][]
     */
    function outerTrees($trees) {
        
    }
}
```

### Swift

```swift
class Solution {
    func outerTrees(_ trees: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun outerTrees(trees: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> outerTrees(List<List<int>> trees) {
    
  }
}
```

### Go

```golang
func outerTrees(trees [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} trees
# @return {Integer[][]}
def outer_trees(trees)
    
end
```

### Scala

```scala
object Solution {
    def outerTrees(trees: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn outer_trees(trees: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (outer-trees trees)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec outer_trees(Trees :: [[integer()]]) -> [[integer()]].
outer_trees(Trees) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec outer_trees(trees :: [[integer]]) :: [[integer]]
  def outer_trees(trees) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func outerTrees(trees: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

