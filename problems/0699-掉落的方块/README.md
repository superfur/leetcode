# 699. 掉落的方块

## 题目描述

<p>在二维平面上的 x 轴上，放置着一些方块。</p>

<p>给你一个二维整数数组 <code>positions</code> ，其中 <code>positions[i] = [left<sub>i</sub>, sideLength<sub>i</sub>]</code> 表示：第 <code>i</code> 个方块边长为 <code>sideLength<sub>i</sub></code> ，其左侧边与 x 轴上坐标点&nbsp;<code>left<sub>i</sub></code> 对齐。</p>

<p>每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 <strong>另一个正方形的顶边</strong> 或者是 <strong>x 轴上</strong> 。一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。</p>

<p>在每个方块掉落后，你必须记录目前所有已经落稳的 <strong>方块堆叠的最高高度</strong> 。</p>

<p>返回一个整数数组 <code>ans</code> ，其中 <code>ans[i]</code> 表示在第 <code>i</code> 块方块掉落后堆叠的最高高度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/fallingsq1-plane.jpg" style="width: 500px; height: 505px;" />
<pre>
<strong>输入：</strong>positions = [[1,2],[2,3],[6,1]]
<strong>输出：</strong>[2,5,5]
<strong>解释：</strong>
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
因此，返回 [2, 5, 5] 作为答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>positions = [[100,100],[200,100]]
<strong>输出：</strong>[100,100]
<strong>解释：</strong>
第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
因此，返回 [100, 100] 作为答案。
注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= positions.length &lt;= 1000</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= 10<sup>8</sup></code></li>
	<li><code>1 &lt;= sideLength<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 数组
- 有序集合

## 提示

1. If positions = [[10, 20], [20, 30]], this is the same as [[1, 2], [2, 3]].  Currently, the values of positions are very large.  Can you generalize this approach so as to make the values in positions manageable?

## 示例

```
[[1,2],[2,3],[6,1]]
[[100,100],[200,100]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> fallingSquares(vector<vector<int>>& positions) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fallingSquares(int** positions, int positionsSize, int* positionsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FallingSquares(int[][] positions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} positions
 * @return {number[]}
 */
var fallingSquares = function(positions) {
    
};
```

### TypeScript

```typescript
function fallingSquares(positions: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $positions
     * @return Integer[]
     */
    function fallingSquares($positions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fallingSquares(_ positions: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fallingSquares(positions: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> fallingSquares(List<List<int>> positions) {
    
  }
}
```

### Go

```golang
func fallingSquares(positions [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} positions
# @return {Integer[]}
def falling_squares(positions)
    
end
```

### Scala

```scala
object Solution {
    def fallingSquares(positions: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn falling_squares(positions: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (falling-squares positions)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec falling_squares(Positions :: [[integer()]]) -> [integer()].
falling_squares(Positions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec falling_squares(positions :: [[integer]]) :: [integer]
  def falling_squares(positions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fallingSquares(positions: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

