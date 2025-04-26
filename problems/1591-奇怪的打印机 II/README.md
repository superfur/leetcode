# 1591. 奇怪的打印机 II

## 题目描述

<p>给你一个奇怪的打印机，它有如下两个特殊的打印规则：</p>

<ul>
	<li>每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。</li>
	<li>一旦矩形根据上面的规则使用了一种颜色，那么 <strong>相同的颜色不能再被使用&nbsp;</strong>。</li>
</ul>

<p>给你一个初始没有颜色的&nbsp;<code>m x n</code>&nbsp;的矩形&nbsp;<code>targetGrid</code>&nbsp;，其中&nbsp;<code>targetGrid[row][col]</code>&nbsp;是位置&nbsp;<code>(row, col)</code>&nbsp;的颜色。</p>

<p>如果你能按照上述规则打印出矩形<em>&nbsp;</em><code>targetGrid</code>&nbsp;，请你返回&nbsp;<code>true</code>&nbsp;，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/19/sample_1_1929.png" style="height: 138px; width: 483px;"></p>

<pre><strong>输入：</strong>targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/19/sample_2_1929.png" style="height: 290px; width: 483px;"></p>

<pre><strong>输入：</strong>targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
<strong>输出：</strong>true
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
<strong>输出：</strong>false
<strong>解释：</strong>没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>targetGrid = [[1,1,1],[3,1,3]]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == targetGrid.length</code></li>
	<li><code>n == targetGrid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 60</code></li>
	<li><code>1 &lt;= targetGrid[row][col] &lt;= 60</code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 拓扑排序
- 数组
- 矩阵

## 提示

1. Try thinking in reverse. Given the grid, how can you tell if a colour was painted last?

## 示例

```
[[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
[[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
[[1,2,1],[2,1,2],[1,2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPrintable(vector<vector<int>>& targetGrid) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPrintable(int[][] targetGrid) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPrintable(self, targetGrid):
        """
        :type targetGrid: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
```

### C

```c
bool isPrintable(int** targetGrid, int targetGridSize, int* targetGridColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPrintable(int[][] targetGrid) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} targetGrid
 * @return {boolean}
 */
var isPrintable = function(targetGrid) {
    
};
```

### TypeScript

```typescript
function isPrintable(targetGrid: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $targetGrid
     * @return Boolean
     */
    function isPrintable($targetGrid) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPrintable(_ targetGrid: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPrintable(targetGrid: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPrintable(List<List<int>> targetGrid) {
    
  }
}
```

### Go

```golang
func isPrintable(targetGrid [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} target_grid
# @return {Boolean}
def is_printable(target_grid)
    
end
```

### Scala

```scala
object Solution {
    def isPrintable(targetGrid: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_printable(target_grid: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-printable targetGrid)
  (-> (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_printable(TargetGrid :: [[integer()]]) -> boolean().
is_printable(TargetGrid) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_printable(target_grid :: [[integer]]) :: boolean
  def is_printable(target_grid) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPrintable(targetGrid: Array<Array<Int64>>): Bool {

    }
}
```

