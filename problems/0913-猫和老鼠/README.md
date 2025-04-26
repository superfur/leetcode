# 913. 猫和老鼠

## 题目描述

<p>两位玩家分别扮演猫和老鼠，在一张 <strong>无向</strong> 图上进行游戏，两人轮流行动。</p>

<p>图的形式是：<code>graph[a]</code> 是一个列表，由满足&nbsp;<code>ab</code> 是图中的一条边的所有节点 <code>b</code> 组成。</p>

<p>老鼠从节点 <code>1</code> 开始，第一个出发；猫从节点 <code>2</code> 开始，第二个出发。在节点 <code>0</code> 处有一个洞。</p>

<p>在每个玩家的行动中，他们 <strong>必须</strong> 沿着图中与所在当前位置连通的一条边移动。例如，如果老鼠在节点 <code>1</code> ，那么它必须移动到 <code>graph[1]</code> 中的任一节点。</p>

<p>此外，猫无法移动到洞中（节点 <code>0</code>）。</p>

<p>然后，游戏在出现以下三种情形之一时结束：</p>

<ul>
	<li>如果猫和老鼠出现在同一个节点，猫获胜。</li>
	<li>如果老鼠到达洞中，老鼠获胜。</li>
	<li>如果某一位置重复出现（即，玩家的位置和移动顺序都与上一次行动相同），游戏平局。</li>
</ul>

<p>给你一张图 <code>graph</code> ，并假设两位玩家都都以最佳状态参与游戏：</p>

<ul>
	<li>如果老鼠获胜，则返回&nbsp;<code>1</code>；</li>
	<li>如果猫获胜，则返回 <code>2</code>；</li>
	<li>如果平局，则返回 <code>0</code> 。</li>
</ul>
&nbsp;

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/cat1.jpg" style="width: 300px; height: 300px;" />
<pre>
<strong>输入：</strong>graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
<strong>输出：</strong>0
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/cat2.jpg" style="width: 200px; height: 200px;" />
<pre>
<strong>输入：</strong>graph = [[1,3],[0],[3],[0,2]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= graph.length &lt;= 50</code></li>
	<li><code>1&nbsp;&lt;= graph[i].length &lt; graph.length</code></li>
	<li><code>0 &lt;= graph[i][j] &lt; graph.length</code></li>
	<li><code>graph[i][j] != i</code></li>
	<li><code>graph[i]</code> 互不相同</li>
	<li>猫和老鼠在游戏中总是可以移动</li>
</ul>


## 难度

Hard

## 标签

- 图
- 拓扑排序
- 记忆化搜索
- 数学
- 动态规划
- 博弈

## 示例

```
[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
[[1,3],[0],[3],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int catMouseGame(vector<vector<int>>& graph) {
        
    }
};
```

### Java

```java
class Solution {
    public int catMouseGame(int[][] graph) {
        
    }
}
```

### Python

```python
class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        
```

### C

```c
int catMouseGame(int** graph, int graphSize, int* graphColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CatMouseGame(int[][] graph) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} graph
 * @return {number}
 */
var catMouseGame = function(graph) {
    
};
```

### TypeScript

```typescript
function catMouseGame(graph: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $graph
     * @return Integer
     */
    function catMouseGame($graph) {
        
    }
}
```

### Swift

```swift
class Solution {
    func catMouseGame(_ graph: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun catMouseGame(graph: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int catMouseGame(List<List<int>> graph) {
    
  }
}
```

### Go

```golang
func catMouseGame(graph [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} graph
# @return {Integer}
def cat_mouse_game(graph)
    
end
```

### Scala

```scala
object Solution {
    def catMouseGame(graph: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn cat_mouse_game(graph: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (cat-mouse-game graph)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec cat_mouse_game(Graph :: [[integer()]]) -> integer().
cat_mouse_game(Graph) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec cat_mouse_game(graph :: [[integer]]) :: integer
  def cat_mouse_game(graph) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func catMouseGame(graph: Array<Array<Int64>>): Int64 {

    }
}
```

