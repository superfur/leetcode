# LCR 107. 01 矩阵

## 题目描述

<p>给定一个由 <code>0</code> 和 <code>1</code> 组成的矩阵 <code>mat</code>&nbsp;，请输出一个大小相同的矩阵，其中每一个格子是 <code>mat</code> 中对应位置元素到最近的 <code>0</code> 的距离。</p>

<p>两个相邻元素间的距离为 <code>1</code> 。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<p><img alt="" src="https://pic.leetcode-cn.com/1626667201-NCWmuP-image.png" style="width: 150px; " /></p>

<pre>
<strong>输入：</strong>mat =<strong> </strong>[[0,0,0],[0,1,0],[0,0,0]]
<strong>输出：</strong>[[0,0,0],[0,1,0],[0,0,0]]
</pre>

<p><b>示例 2：</b></p>

<p><img alt="" src="https://pic.leetcode-cn.com/1626667205-xFxIeK-image.png" style="width: 150px; " /></p>

<pre>
<strong>输入：</strong>mat =<b> </b>[[0,0,0],[0,1,0],[1,1,1]]
<strong>输出：</strong>[[0,0,0],[0,1,0],[1,2,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>4</sup></code></li>
	<li><code>mat[i][j] is either 0 or 1.</code></li>
	<li><code>mat</code> 中至少有一个 <code>0&nbsp;</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 542&nbsp;题相同：<a href="https://leetcode-cn.com/problems/01-matrix/">https://leetcode-cn.com/problems/01-matrix/</a></p>


## 难度

Medium

## 标签

- 广度优先搜索
- 数组
- 动态规划
- 矩阵

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {

    }
};
```

### Java

```java
class Solution {
    public int[][] updateMatrix(int[][] mat) {

    }
}
```

### Python

```python
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** updateMatrix(int** mat, int matSize, int* matColSize, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public int[][] UpdateMatrix(int[][] mat) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function(mat) {

};
```

### TypeScript

```typescript
function updateMatrix(mat: number[][]): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[][]
     */
    function updateMatrix($mat) {

    }
}
```

### Swift

```swift
class Solution {
    func updateMatrix(_ mat: [[Int]]) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {

    }
}
```

### Go

```golang
func updateMatrix(mat [][]int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer[][]}
def update_matrix(mat)

end
```

### Scala

```scala
object Solution {
    def updateMatrix(mat: Array[Array[Int]]): Array[Array[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn update_matrix(mat: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (update-matrix mat)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))

  )
```

### Erlang

```erlang
-spec update_matrix(Mat :: [[integer()]]) -> [[integer()]].
update_matrix(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec update_matrix(mat :: [[integer]]) :: [[integer]]
  def update_matrix(mat) do

  end
end
```

