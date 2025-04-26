# 675. 为高尔夫比赛砍树

## 题目描述

<p>你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 <code>m x n</code> 的矩阵表示， 在这个矩阵中：</p>

<ul>
	<li><code>0</code> 表示障碍，无法触碰</li>
	<li><code>1</code> 表示地面，可以行走</li>
	<li><code>比 1 大的数</code> 表示有树的单元格，可以行走，数值表示树的高度</li>
</ul>

<p>每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。</p>

<p>你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 <code>1</code>（即变为地面）。</p>

<p>你将从 <code>(0, 0)</code> 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 <code>-1</code> 。</p>

<p>可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/trees1.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>forest = [[1,2,3],[0,0,4],[7,6,5]]
<strong>输出：</strong>6
<strong>解释：</strong>沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/trees2.jpg" style="width: 242px; height: 242px;" />
<pre>
<strong>输入：</strong>forest = [[1,2,3],[0,0,0],[7,6,5]]
<strong>输出：</strong>-1
<strong>解释：</strong>由于中间一行被障碍阻塞，无法访问最下面一行中的树。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>forest = [[2,3,4],[0,0,5],[8,7,6]]
<strong>输出：</strong>6
<strong>解释：</strong>可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == forest.length</code></li>
	<li><code>n == forest[i].length</code></li>
	<li><code>1 <= m, n <= 50</code></li>
	<li><code>0 <= forest[i][j] <= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 矩阵
- 堆（优先队列）

## 示例

```
[[1,2,3],[0,0,4],[7,6,5]]
[[1,2,3],[0,0,0],[7,6,5]]
[[2,3,4],[0,0,5],[8,7,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int cutOffTree(vector<vector<int>>& forest) {
        
    }
};
```

### Java

```java
class Solution {
    public int cutOffTree(List<List<Integer>> forest) {
        
    }
}
```

### Python

```python
class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        
```

### C

```c
int cutOffTree(int** forest, int forestSize, int* forestColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CutOffTree(IList<IList<int>> forest) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} forest
 * @return {number}
 */
var cutOffTree = function(forest) {
    
};
```

### TypeScript

```typescript
function cutOffTree(forest: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $forest
     * @return Integer
     */
    function cutOffTree($forest) {
        
    }
}
```

### Swift

```swift
class Solution {
    func cutOffTree(_ forest: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun cutOffTree(forest: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int cutOffTree(List<List<int>> forest) {
    
  }
}
```

### Go

```golang
func cutOffTree(forest [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} forest
# @return {Integer}
def cut_off_tree(forest)
    
end
```

### Scala

```scala
object Solution {
    def cutOffTree(forest: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn cut_off_tree(forest: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (cut-off-tree forest)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec cut_off_tree(Forest :: [[integer()]]) -> integer().
cut_off_tree(Forest) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec cut_off_tree(forest :: [[integer]]) :: integer
  def cut_off_tree(forest) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func cutOffTree(forest: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

