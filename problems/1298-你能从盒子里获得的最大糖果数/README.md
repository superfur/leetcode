# 1298. 你能从盒子里获得的最大糖果数

## 题目描述

<p>给你&nbsp;<code>n</code>&nbsp;个盒子，每个盒子的格式为&nbsp;<code>[status, candies, keys, containedBoxes]</code>&nbsp;，其中：</p>

<ul>
	<li>状态字&nbsp;<code>status[i]</code>：整数，如果&nbsp;<code>box[i]</code>&nbsp;是开的，那么是 <strong>1&nbsp;</strong>，否则是 <strong>0&nbsp;</strong>。</li>
	<li>糖果数&nbsp;<code>candies[i]</code>: 整数，表示&nbsp;<code>box[i]</code> 中糖果的数目。</li>
	<li>钥匙&nbsp;<code>keys[i]</code>：数组，表示你打开&nbsp;<code>box[i]</code>&nbsp;后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。</li>
	<li>内含的盒子&nbsp;<code>containedBoxes[i]</code>：整数，表示放在&nbsp;<code>box[i]</code>&nbsp;里的盒子所对应的下标。</li>
</ul>

<p>给你一个&nbsp;<code>initialBoxes</code> 数组，表示你现在得到的盒子，你可以获得里面的糖果，也可以用盒子里的钥匙打开新的盒子，还可以继续探索从这个盒子里找到的其他盒子。</p>

<p>请你按照上述规则，返回可以获得糖果的 <strong>最大数目&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
<strong>输出：</strong>16
<strong>解释：
</strong>一开始你有盒子 0 。你将获得它里面的 7 个糖果和盒子 1 和 2。
盒子 1 目前状态是关闭的，而且你还没有对应它的钥匙。所以你将会打开盒子 2 ，并得到里面的 4 个糖果和盒子 1 的钥匙。
在盒子 1 中，你会获得 5 个糖果和盒子 3 ，但是你没法获得盒子 3 的钥匙所以盒子 3 会保持关闭状态。
你总共可以获得的糖果数目 = 7 + 4 + 5 = 16 个。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
<strong>输出：</strong>6
<strong>解释：
</strong>你一开始拥有盒子 0 。打开它你可以找到盒子 1,2,3,4,5 和它们对应的钥匙。
打开这些盒子，你将获得所有盒子的糖果，所以总糖果数为 6 个。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
<strong>输出：</strong>1
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]
<strong>输出：</strong>7
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= status.length &lt;= 1000</code></li>
	<li><code>status.length == candies.length == keys.length == containedBoxes.length == n</code></li>
	<li><code>status[i]</code> 要么是&nbsp;<code>0</code>&nbsp;要么是&nbsp;<code>1</code> 。</li>
	<li><code>1 &lt;= candies[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= keys[i].length &lt;= status.length</code></li>
	<li><code>0 &lt;= keys[i][j] &lt; status.length</code></li>
	<li><code>keys[i]</code>&nbsp;中的值都是互不相同的。</li>
	<li><code>0 &lt;= containedBoxes[i].length &lt;= status.length</code></li>
	<li><code>0 &lt;= containedBoxes[i][j] &lt; status.length</code></li>
	<li><code>containedBoxes[i]</code>&nbsp;中的值都是互不相同的。</li>
	<li>每个盒子最多被一个盒子包含。</li>
	<li><code>0 &lt;= initialBoxes.length&nbsp;&lt;= status.length</code></li>
	<li><code>0 &lt;= initialBoxes[i] &lt; status.length</code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 图
- 数组

## 提示

1. Use Breadth First Search (BFS) to traverse all possible boxes you can open. Only push to the queue the boxes the you have with their keys.

## 示例

```
[1,0,1,0]
[7,5,4,100]
[[],[],[1],[]]
[[1,2],[3],[],[]]
[0]
[1,0,0,0,0,0]
[1,1,1,1,1,1]
[[1,2,3,4,5],[],[],[],[],[]]
[[1,2,3,4,5],[],[],[],[],[]]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        """
        :type status: List[int]
        :type candies: List[int]
        :type keys: List[List[int]]
        :type containedBoxes: List[List[int]]
        :type initialBoxes: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        
```

### C

```c
int maxCandies(int* status, int statusSize, int* candies, int candiesSize, int** keys, int keysSize, int* keysColSize, int** containedBoxes, int containedBoxesSize, int* containedBoxesColSize, int* initialBoxes, int initialBoxesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxCandies(int[] status, int[] candies, int[][] keys, int[][] containedBoxes, int[] initialBoxes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    
};
```

### TypeScript

```typescript
function maxCandies(status: number[], candies: number[], keys: number[][], containedBoxes: number[][], initialBoxes: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $status
     * @param Integer[] $candies
     * @param Integer[][] $keys
     * @param Integer[][] $containedBoxes
     * @param Integer[] $initialBoxes
     * @return Integer
     */
    function maxCandies($status, $candies, $keys, $containedBoxes, $initialBoxes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxCandies(_ status: [Int], _ candies: [Int], _ keys: [[Int]], _ containedBoxes: [[Int]], _ initialBoxes: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxCandies(status: IntArray, candies: IntArray, keys: Array<IntArray>, containedBoxes: Array<IntArray>, initialBoxes: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxCandies(List<int> status, List<int> candies, List<List<int>> keys, List<List<int>> containedBoxes, List<int> initialBoxes) {
    
  }
}
```

### Go

```golang
func maxCandies(status []int, candies []int, keys [][]int, containedBoxes [][]int, initialBoxes []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} status
# @param {Integer[]} candies
# @param {Integer[][]} keys
# @param {Integer[][]} contained_boxes
# @param {Integer[]} initial_boxes
# @return {Integer}
def max_candies(status, candies, keys, contained_boxes, initial_boxes)
    
end
```

### Scala

```scala
object Solution {
    def maxCandies(status: Array[Int], candies: Array[Int], keys: Array[Array[Int]], containedBoxes: Array[Array[Int]], initialBoxes: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_candies(status: Vec<i32>, candies: Vec<i32>, keys: Vec<Vec<i32>>, contained_boxes: Vec<Vec<i32>>, initial_boxes: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-candies status candies keys containedBoxes initialBoxes)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_candies(Status :: [integer()], Candies :: [integer()], Keys :: [[integer()]], ContainedBoxes :: [[integer()]], InitialBoxes :: [integer()]) -> integer().
max_candies(Status, Candies, Keys, ContainedBoxes, InitialBoxes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_candies(status :: [integer], candies :: [integer], keys :: [[integer]], contained_boxes :: [[integer]], initial_boxes :: [integer]) :: integer
  def max_candies(status, candies, keys, contained_boxes, initial_boxes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxCandies(status: Array<Int64>, candies: Array<Int64>, keys: Array<Array<Int64>>, containedBoxes: Array<Array<Int64>>, initialBoxes: Array<Int64>): Int64 {

    }
}
```

