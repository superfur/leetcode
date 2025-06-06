# 1687. 从仓库到码头运输箱子

## 题目描述

<p>你有一辆货运卡车，你需要用这一辆车把一些箱子从仓库运送到码头。这辆卡车每次运输有&nbsp;<strong>箱子数目的限制</strong>&nbsp;和 <strong>总重量的限制</strong>&nbsp;。</p>

<p>给你一个箱子数组&nbsp;<code>boxes</code>&nbsp;和三个整数 <code>portsCount</code>, <code>maxBoxes</code>&nbsp;和&nbsp;<code>maxWeight</code>&nbsp;，其中&nbsp;<code>boxes[i] = [ports<sub>​​i</sub>​, weight<sub>i</sub>]</code>&nbsp;。</p>

<ul>
	<li><code>ports<sub>​​i</sub></code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;个箱子需要送达的码头，&nbsp;<code>weights<sub>i</sub></code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个箱子的重量。</li>
	<li><code>portsCount</code>&nbsp;是码头的数目。</li>
	<li><code>maxBoxes</code> 和&nbsp;<code>maxWeight</code>&nbsp;分别是卡车每趟运输箱子数目和重量的限制。</li>
</ul>

<p>箱子需要按照 <strong>数组顺序</strong>&nbsp;运输，同时每次运输需要遵循以下步骤：</p>

<ul>
	<li>卡车从&nbsp;<code>boxes</code>&nbsp;队列中按顺序取出若干个箱子，但不能违反&nbsp;<code>maxBoxes</code> 和&nbsp;<code>maxWeight</code>&nbsp;限制。</li>
	<li>对于在卡车上的箱子，我们需要 <strong>按顺序</strong>&nbsp;处理它们，卡车会通过 <strong>一趟行程</strong>&nbsp;将最前面的箱子送到目的地码头并卸货。如果卡车已经在对应的码头，那么不需要 <strong>额外行程</strong>&nbsp;，箱子也会立马被卸货。</li>
	<li>卡车上所有箱子都被卸货后，卡车需要 <strong>一趟行程</strong>&nbsp;回到仓库，从箱子队列里再取出一些箱子。</li>
</ul>

<p>卡车在将所有箱子运输并卸货后，最后必须回到仓库。</p>

<p>请你返回将所有箱子送到相应码头的&nbsp;<b>最少行程</b>&nbsp;次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
<b>输出：</b>4
<b>解释：</b>最优策略如下：
- 卡车将所有箱子装上车，到达码头 1 ，然后去码头 2 ，然后再回到码头 1 ，最后回到仓库，总共需要 4 趟行程。
所以总行程数为 4 。
注意到第一个和第三个箱子不能同时被卸货，因为箱子需要按顺序处理（也就是第二个箱子需要先被送到码头 2 ，然后才能处理第三个箱子）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
<b>输出：</b>6
<b>解释：</b>最优策略如下：
- 卡车首先运输第一个箱子，到达码头 1 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第二、第三、第四个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五个箱子，到达码头 2 ，回到仓库，总共 2 趟行程。
总行程数为 2 + 2 + 2 = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
<b>输出：</b>6
<b>解释：</b>最优策略如下：
- 卡车运输第一和第二个箱子，到达码头 1 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第三和第四个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五和第六个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
总行程数为 2 + 2 + 2 = 6 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
<b>输出：</b>14
<b>解释：</b>最优策略如下：
- 卡车运输第一个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第二个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第三和第四个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第六和第七个箱子，到达码头 3 ，然后去码头 4 ，然后回到仓库，总共 3 趟行程。
- 卡车运输第八和第九个箱子，到达码头 1 ，然后去码头 5 ，然后回到仓库，总共 3 趟行程。
总行程数为 2 + 2 + 2 + 2 + 3 + 3 = 14 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= boxes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= portsCount, maxBoxes, maxWeight &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= ports<sub>​​i</sub> &lt;= portsCount</code></li>
	<li><code>1 &lt;= weights<sub>i</sub> &lt;= maxWeight</code></li>
</ul>


## 难度

Hard

## 标签

- 线段树
- 队列
- 数组
- 动态规划
- 前缀和
- 单调队列
- 堆（优先队列）

## 提示

1. Try to think of the most basic dp which is n^2 now optimize it
2. Think of any range query data structure to optimize

## 示例

```
[[1,1],[2,1],[1,1]]
2
3
3
[[1,2],[3,3],[3,1],[3,1],[2,4]]
3
3
6
[[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]]
3
6
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int boxDelivering(vector<vector<int>>& boxes, int portsCount, int maxBoxes, int maxWeight) {
        
    }
};
```

### Java

```java
class Solution {
    public int boxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        
    }
}
```

### Python

```python
class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        
```

### C

```c
int boxDelivering(int** boxes, int boxesSize, int* boxesColSize, int portsCount, int maxBoxes, int maxWeight) {
    
}
```

### C#

```csharp
public class Solution {
    public int BoxDelivering(int[][] boxes, int portsCount, int maxBoxes, int maxWeight) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} boxes
 * @param {number} portsCount
 * @param {number} maxBoxes
 * @param {number} maxWeight
 * @return {number}
 */
var boxDelivering = function(boxes, portsCount, maxBoxes, maxWeight) {
    
};
```

### TypeScript

```typescript
function boxDelivering(boxes: number[][], portsCount: number, maxBoxes: number, maxWeight: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $boxes
     * @param Integer $portsCount
     * @param Integer $maxBoxes
     * @param Integer $maxWeight
     * @return Integer
     */
    function boxDelivering($boxes, $portsCount, $maxBoxes, $maxWeight) {
        
    }
}
```

### Swift

```swift
class Solution {
    func boxDelivering(_ boxes: [[Int]], _ portsCount: Int, _ maxBoxes: Int, _ maxWeight: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun boxDelivering(boxes: Array<IntArray>, portsCount: Int, maxBoxes: Int, maxWeight: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int boxDelivering(List<List<int>> boxes, int portsCount, int maxBoxes, int maxWeight) {
    
  }
}
```

### Go

```golang
func boxDelivering(boxes [][]int, portsCount int, maxBoxes int, maxWeight int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} boxes
# @param {Integer} ports_count
# @param {Integer} max_boxes
# @param {Integer} max_weight
# @return {Integer}
def box_delivering(boxes, ports_count, max_boxes, max_weight)
    
end
```

### Scala

```scala
object Solution {
    def boxDelivering(boxes: Array[Array[Int]], portsCount: Int, maxBoxes: Int, maxWeight: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn box_delivering(boxes: Vec<Vec<i32>>, ports_count: i32, max_boxes: i32, max_weight: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (box-delivering boxes portsCount maxBoxes maxWeight)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec box_delivering(Boxes :: [[integer()]], PortsCount :: integer(), MaxBoxes :: integer(), MaxWeight :: integer()) -> integer().
box_delivering(Boxes, PortsCount, MaxBoxes, MaxWeight) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec box_delivering(boxes :: [[integer]], ports_count :: integer, max_boxes :: integer, max_weight :: integer) :: integer
  def box_delivering(boxes, ports_count, max_boxes, max_weight) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func boxDelivering(boxes: Array<Array<Int64>>, portsCount: Int64, maxBoxes: Int64, maxWeight: Int64): Int64 {

    }
}
```

