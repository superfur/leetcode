# 面试题 04.01. 节点间通路

## 题目描述

<p>节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
<strong> 输出</strong>：true
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
<strong> 输出</strong>：true
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>节点数量n在[0, 1e5]范围内。</li>
	<li>节点编号大于等于 0 小于 n。</li>
	<li>图中可能存在自环和平行边。</li>
</ol>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图

## 提示

1. 有两个众所周知的算法可以做到这一点。其利弊是什么？

## 示例

```
3
[[0, 1], [0, 2], [1, 2], [1, 2]]
0
2
5
[[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
0
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool findWhetherExistsPath(int n, vector<vector<int>>& graph, int start, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean findWhetherExistsPath(int n, int[][] graph, int start, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findWhetherExistsPath(self, n, graph, start, target):
        """
        :type n: int
        :type graph: List[List[int]]
        :type start: int
        :type target: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        
```

### C

```c
bool findWhetherExistsPath(int n, int** graph, int graphSize, int* graphColSize, int start, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public bool FindWhetherExistsPath(int n, int[][] graph, int start, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} graph
 * @param {number} start
 * @param {number} target
 * @return {boolean}
 */
var findWhetherExistsPath = function(n, graph, start, target) {
    
};
```

### TypeScript

```typescript
function findWhetherExistsPath(n: number, graph: number[][], start: number, target: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $graph
     * @param Integer $start
     * @param Integer $target
     * @return Boolean
     */
    function findWhetherExistsPath($n, $graph, $start, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findWhetherExistsPath(_ n: Int, _ graph: [[Int]], _ start: Int, _ target: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findWhetherExistsPath(n: Int, graph: Array<IntArray>, start: Int, target: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool findWhetherExistsPath(int n, List<List<int>> graph, int start, int target) {
    
  }
}
```

### Go

```golang
func findWhetherExistsPath(n int, graph [][]int, start int, target int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} graph
# @param {Integer} start
# @param {Integer} target
# @return {Boolean}
def find_whether_exists_path(n, graph, start, target)
    
end
```

### Scala

```scala
object Solution {
    def findWhetherExistsPath(n: Int, graph: Array[Array[Int]], start: Int, target: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_whether_exists_path(n: i32, graph: Vec<Vec<i32>>, start: i32, target: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (find-whether-exists-path n graph start target)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec find_whether_exists_path(N :: integer(), Graph :: [[integer()]], Start :: integer(), Target :: integer()) -> boolean().
find_whether_exists_path(N, Graph, Start, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_whether_exists_path(n :: integer, graph :: [[integer]], start :: integer, target :: integer) :: boolean
  def find_whether_exists_path(n, graph, start, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findWhetherExistsPath(n: Int64, graph: Array<Array<Int64>>, start: Int64, target: Int64): Bool {

    }
}
```

