# 218. 天际线问题

## 题目描述

<p>城市的 <strong>天际线</strong> 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 <em>由这些建筑物形成的<strong> 天际线</strong></em> 。</p>

<p>每个建筑物的几何信息由数组 <code>buildings</code> 表示，其中三元组 <code>buildings[i] = [lefti, righti, heighti]</code> 表示：</p>

<ul>
	<li><code>left<sub>i</sub></code> 是第 <code>i</code> 座建筑物左边缘的 <code>x</code> 坐标。</li>
	<li><code>right<sub>i</sub></code> 是第 <code>i</code> 座建筑物右边缘的 <code>x</code> 坐标。</li>
	<li><code>height<sub>i</sub></code> 是第 <code>i</code> 座建筑物的高度。</li>
</ul>

<p>你可以假设所有的建筑都是完美的长方形，在高度为 <code>0</code>&nbsp;的绝对平坦的表面上。</p>

<p><strong>天际线</strong> 应该表示为由 “关键点” 组成的列表，格式 <code>[[x<sub>1</sub>,y<sub>1</sub>],[x<sub>2</sub>,y<sub>2</sub>],...]</code> ，并按 <strong>x 坐标 </strong>进行 <strong>排序</strong> 。<strong>关键点是水平线段的左端点</strong>。列表中最后一个点是最右侧建筑物的终点，<code>y</code> 坐标始终为 <code>0</code> ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。</p>

<p><strong>注意：</strong>输出天际线中不得有连续的相同高度的水平线。例如 <code>[...[2 3], [4 5], [7 5], [11 5], [12 7]...]</code> 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：<code>[...[2 3], [4 5], [12 7], ...]</code></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/merged.jpg" style="height: 331px; width: 800px;" />
<pre>
<strong>输入：</strong>buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
<strong>输出：</strong>[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
<strong>解释：</strong>
图 A<strong> </strong>显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>buildings = [[0,2,3],[2,5,3]]
<strong>输出：</strong>[[0,3],[5,0]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= buildings.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= left<sub>i</sub> &lt; right<sub>i</sub> &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= height<sub>i</sub> &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>buildings</code> 按 <code>left<sub>i</sub></code> 非递减排序</li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 分治
- 有序集合
- 扫描线
- 堆（优先队列）

## 示例

```
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[0,2,3],[2,5,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> getSkyline(int[][] buildings) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** getSkyline(int** buildings, int buildingsSize, int* buildingsColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> GetSkyline(int[][] buildings) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} buildings
 * @return {number[][]}
 */
var getSkyline = function(buildings) {
    
};
```

### TypeScript

```typescript
function getSkyline(buildings: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $buildings
     * @return Integer[][]
     */
    function getSkyline($buildings) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getSkyline(_ buildings: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getSkyline(buildings: Array<IntArray>): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> getSkyline(List<List<int>> buildings) {
    
  }
}
```

### Go

```golang
func getSkyline(buildings [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} buildings
# @return {Integer[][]}
def get_skyline(buildings)
    
end
```

### Scala

```scala
object Solution {
    def getSkyline(buildings: Array[Array[Int]]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_skyline(buildings: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (get-skyline buildings)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec get_skyline(Buildings :: [[integer()]]) -> [[integer()]].
get_skyline(Buildings) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_skyline(buildings :: [[integer]]) :: [[integer]]
  def get_skyline(buildings) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getSkyline(buildings: Array<Array<Int64>>): ArrayList<ArrayList<Int64>> {

    }
}
```

