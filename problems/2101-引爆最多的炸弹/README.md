# 2101. 引爆最多的炸弹

## 题目描述

<p>给你一个炸弹列表。一个炸弹的 <strong>爆炸范围</strong>&nbsp;定义为以炸弹为圆心的一个圆。</p>

<p>炸弹用一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>bombs</code>&nbsp;表示，其中&nbsp;<code>bombs[i] = [x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub>]</code>&nbsp;。<code>x<sub>i</sub></code> 和&nbsp;<code>y<sub>i</sub></code>&nbsp;表示第 <code>i</code>&nbsp;个炸弹的 X 和 Y 坐标，<code>r<sub>i</sub></code>&nbsp;表示爆炸范围的 <strong>半径</strong>&nbsp;。</p>

<p>你需要选择引爆 <strong>一个&nbsp;</strong>炸弹。当这个炸弹被引爆时，<strong>所有</strong> 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。</p>

<p>给你数组&nbsp;<code>bombs</code>&nbsp;，请你返回在引爆&nbsp;<strong>一个</strong>&nbsp;炸弹的前提下，<strong>最多</strong>&nbsp;能引爆的炸弹数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-3.png" style="width: 300px; height: 300px;"></p>

<pre><b>输入：</b>bombs = [[2,1,3],[6,1,4]]
<b>输出：</b>2
<strong>解释：</strong>
上图展示了 2 个炸弹的位置和爆炸范围。
如果我们引爆左边的炸弹，右边的炸弹不会被影响。
但如果我们引爆右边的炸弹，两个炸弹都会爆炸。
所以最多能引爆的炸弹数目是 max(1, 2) = 2 。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-2.png" style="width: 300px; height: 300px;"></p>

<pre><b>输入：</b>bombs = [[1,1,5],[10,10,5]]
<b>输出：</b>1
<strong>解释：
</strong>引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/desmos-eg1.png" style="width: 300px; height: 300px;"></p>

<pre><b>输入：</b>bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
<b>输出：</b>5
<strong>解释：</strong>
最佳引爆炸弹为炸弹 0 ，因为：
- 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。
- 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。
- 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。
所以总共有 5 个炸弹被引爆。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= bombs.length&nbsp;&lt;= 100</code></li>
	<li><code>bombs[i].length == 3</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 几何
- 数组
- 数学

## 提示

1. How can we model the relationship between different bombs? Can "graphs" help us?
2. Bombs are nodes and are connected to other bombs in their range by directed edges.
3. If we know which bombs will be affected when any bomb is detonated, how can we find the total number of bombs that will be detonated if we start from a fixed bomb?
4. Run a Depth First Search (DFS) from every node, and all the nodes it reaches are the bombs that will be detonated.

## 示例

```
[[2,1,3],[6,1,4]]
[[1,1,5],[10,10,5]]
[[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumDetonation(vector<vector<int>>& bombs) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumDetonation(int[][] bombs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
```

### C

```c
int maximumDetonation(int** bombs, int bombsSize, int* bombsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumDetonation(int[][] bombs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function(bombs) {
    
};
```

### TypeScript

```typescript
function maximumDetonation(bombs: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $bombs
     * @return Integer
     */
    function maximumDetonation($bombs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumDetonation(_ bombs: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumDetonation(bombs: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumDetonation(List<List<int>> bombs) {
    
  }
}
```

### Go

```golang
func maximumDetonation(bombs [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} bombs
# @return {Integer}
def maximum_detonation(bombs)
    
end
```

### Scala

```scala
object Solution {
    def maximumDetonation(bombs: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-detonation bombs)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_detonation(Bombs :: [[integer()]]) -> integer().
maximum_detonation(Bombs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_detonation(bombs :: [[integer]]) :: integer
  def maximum_detonation(bombs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumDetonation(bombs: Array<Array<Int64>>): Int64 {

    }
}
```

