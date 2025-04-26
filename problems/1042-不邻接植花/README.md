# 1042. 不邻接植花

## 题目描述

<p>有 <code>n</code> 个花园，按从&nbsp;<code>1</code>&nbsp;到 <code>n</code> 标记。另有数组 <code>paths</code> ，其中 <code>paths[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;描述了花园&nbsp;<code>x<sub>i</sub></code> 到花园&nbsp;<code>y<sub>i</sub></code> 的双向路径。在每个花园中，你打算种下四种花之一。</p>

<p>另外，所有花园 <strong>最多</strong> 有 <strong>3</strong> 条路径可以进入或离开.</p>

<p>你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。</p>

<p><em>以数组形式返回 <strong>任一</strong> 可行的方案作为答案&nbsp;<code>answer</code>，其中&nbsp;<code>answer[i]</code>&nbsp;为在第&nbsp;<code>(i+1)</code>&nbsp;个花园中种植的花的种类。花的种类用 &nbsp;1、2、3、4 表示。保证存在答案。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, paths = [[1,2],[2,3],[3,1]]
<strong>输出：</strong>[1,2,3]
<strong>解释：</strong>
花园 1 和 2 花的种类不同。
花园 2 和 3 花的种类不同。
花园 3 和 1 花的种类不同。
因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 4, paths = [[1,2],[3,4]]
<strong>输出：</strong>[1,2,1,2]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
<strong>输出：</strong>[1,2,3,4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= paths.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>paths[i].length == 2</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li>每个花园 <strong>最多</strong> 有 <strong>3</strong> 条路径可以进入或离开</li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图

## 提示

1. Since each garden is connected to at most 3 gardens, there's always an available color for each garden.  For example, if one garden is next to gardens with colors 1, 3, 4,  then color #2 is available.

## 示例

```
3
[[1,2],[2,3],[3,1]]
4
[[1,2],[3,4]]
4
[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> gardenNoAdj(int n, vector<vector<int>>& paths) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] gardenNoAdj(int n, int[][] paths) {
        
    }
}
```

### Python

```python
class Solution(object):
    def gardenNoAdj(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* gardenNoAdj(int n, int** paths, int pathsSize, int* pathsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GardenNoAdj(int n, int[][] paths) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} paths
 * @return {number[]}
 */
var gardenNoAdj = function(n, paths) {
    
};
```

### TypeScript

```typescript
function gardenNoAdj(n: number, paths: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $paths
     * @return Integer[]
     */
    function gardenNoAdj($n, $paths) {
        
    }
}
```

### Swift

```swift
class Solution {
    func gardenNoAdj(_ n: Int, _ paths: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun gardenNoAdj(n: Int, paths: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> gardenNoAdj(int n, List<List<int>> paths) {
    
  }
}
```

### Go

```golang
func gardenNoAdj(n int, paths [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} paths
# @return {Integer[]}
def garden_no_adj(n, paths)
    
end
```

### Scala

```scala
object Solution {
    def gardenNoAdj(n: Int, paths: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn garden_no_adj(n: i32, paths: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (garden-no-adj n paths)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec garden_no_adj(N :: integer(), Paths :: [[integer()]]) -> [integer()].
garden_no_adj(N, Paths) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec garden_no_adj(n :: integer, paths :: [[integer]]) :: [integer]
  def garden_no_adj(n, paths) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func gardenNoAdj(n: Int64, paths: Array<Array<Int64>>): Array<Int64> {

    }
}
```

