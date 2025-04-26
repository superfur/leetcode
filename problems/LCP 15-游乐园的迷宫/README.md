# LCP 15. 游乐园的迷宫

## 题目描述

<p>小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 <code>N</code> 个推销点，编号 <code>0</code> 到 <code>N-1</code>，不存在三点共线的情况。每两点之间有一条直线相连。游戏没有规定起点和终点，但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 <code>N-2</code> 个点恰好一次并回到终点。访问的顺序需要满足一串给定的长度为 <code>N-2</code> 由 <code>L</code> 和 <code>R</code> 组成的字符串 <code>direction</code>，表示从起点出发之后在每个顶点上转角的方向。根据这个提示，小王希望你能够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。</p>

<p><img alt="Screenshot 2020-03-20 at 17.04.58.png" src="https://pic.leetcode-cn.com/595b60797d4a461287864a8cd05bba1d3b8760104ff83f43b902fd68477be9c3-Screenshot%202020-03-20%20at%2017.04.58.png" style="max-height:500px" /></p>

<p>（上图：A-&gt;B-&gt;C 右转； 下图：D-&gt;E-&gt;F 左转）</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>points = [[1,1],[1,4],[3,2],[2,1]], direction = "LL"</code></p>

<p>输出：<code>[0,2,1,3]</code></p>

<p>解释：[0,2,1,3] 是符合"LL"的方案之一。在 [0,2,1,3] 方案中，0-&gt;2-&gt;1 是左转方向， 2-&gt;1-&gt;3 也是左转方向 <img alt="图片.gif" src="https://pic.leetcode-cn.com/c01c1efc423b916267c2a3a170266c925c368d62afa047c267cc1020970e55d9-%E5%9B%BE%E7%89%87.gif" style="max-height:300px" /></p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>points = [[1,3],[2,4],[3,3],[2,1]], direction = "LR"</code></p>

<p>输出：<code>[0,3,1,2]</code></p>

<p>解释：[0,3,1,2] 是符合"LR"的方案之一。在 [0,3,1,2] 方案中，0-&gt;3-&gt;1 是左转方向， 3-&gt;1-&gt;2 是右转方向</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 1000 且 points[i].length == 2</code></li>
	<li><code>1 &lt;= points[i][0],points[i][1] &lt;= 10000</code></li>
	<li><code>direction.length == points.length - 2</code></li>
	<li><code>direction 只包含 "L","R"</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 几何
- 数组
- 数学

## 示例

```
[[1,1],[1,4],[3,2],[2,1]]
"LL"
[[1,3],[2,4],[3,3],[2,1]]
"LR"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> visitOrder(vector<vector<int>>& points, string direction) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] visitOrder(int[][] points, String direction) {
        
    }
}
```

### Python

```python
class Solution(object):
    def visitOrder(self, points, direction):
        """
        :type points: List[List[int]]
        :type direction: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* visitOrder(int** points, int pointsSize, int* pointsColSize, char* direction, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] VisitOrder(int[][] points, string direction) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @param {string} direction
 * @return {number[]}
 */
var visitOrder = function(points, direction) {
    
};
```

### TypeScript

```typescript
function visitOrder(points: number[][], direction: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @param String $direction
     * @return Integer[]
     */
    function visitOrder($points, $direction) {
        
    }
}
```

### Swift

```swift
class Solution {
    func visitOrder(_ points: [[Int]], _ direction: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun visitOrder(points: Array<IntArray>, direction: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> visitOrder(List<List<int>> points, String direction) {
    
  }
}
```

### Go

```golang
func visitOrder(points [][]int, direction string) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @param {String} direction
# @return {Integer[]}
def visit_order(points, direction)
    
end
```

### Scala

```scala
object Solution {
    def visitOrder(points: Array[Array[Int]], direction: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn visit_order(points: Vec<Vec<i32>>, direction: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (visit-order points direction)
  (-> (listof (listof exact-integer?)) string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec visit_order(Points :: [[integer()]], Direction :: unicode:unicode_binary()) -> [integer()].
visit_order(Points, Direction) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec visit_order(points :: [[integer]], direction :: String.t) :: [integer]
  def visit_order(points, direction) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func visitOrder(points: Array<Array<Int64>>, direction: String): Array<Int64> {

    }
}
```

