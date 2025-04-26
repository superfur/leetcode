# 1889. 装包裹的最小浪费空间

## 题目描述

<p>给你 <code>n</code> 个包裹，你需要把它们装在箱子里，<strong>每个箱子装一个包裹</strong>。总共有 <code>m</code> 个供应商提供 <strong>不同尺寸</strong> 的箱子（每个规格都有无数个箱子）。如果一个包裹的尺寸 <strong>小于等于</strong> 一个箱子的尺寸，那么这个包裹就可以放入这个箱子之中。</p>

<p>包裹的尺寸用一个整数数组 <code>packages</code> 表示，其中 <code>packages[i]</code> 是第 <code>i</code> 个包裹的尺寸。供应商用二维数组 <code>boxes</code> 表示，其中 <code>boxes[j]</code> 是第 <code>j</code> 个供应商提供的所有箱子尺寸的数组。</p>

<p>你想要选择 <strong>一个供应商</strong> 并只使用该供应商提供的箱子，使得 <strong>总浪费空间最小</strong> 。对于每个装了包裹的箱子，我们定义 <strong>浪费的</strong> 空间等于 <code>箱子的尺寸 - 包裹的尺寸</code> 。<strong>总浪费空间</strong> 为 <strong>所有</strong> 箱子中浪费空间的总和。</p>

<ul>
	<li>比方说，如果你想要用尺寸数组为 <code>[4,8]</code> 的箱子装下尺寸为 <code>[2,3,5]</code> 的包裹，你可以将尺寸为 <code>2</code> 和 <code>3</code> 的两个包裹装入两个尺寸为 <code>4</code> 的箱子中，同时把尺寸为 <code>5</code> 的包裹装入尺寸为 <code>8</code> 的箱子中。总浪费空间为 <code>(4-2) + (4-3) + (8-5) = 6</code> 。</li>
</ul>

<p>请你选择 <strong>最优</strong> 箱子供应商，使得 <strong>总浪费空间最小</strong> 。如果 <strong>无法</strong> 将所有包裹放入箱子中，请你返回 <code>-1</code> 。由于答案可能会 <strong>很大</strong> ，请返回它对<strong> </strong><code>10<sup>9</sup> + 7</code> <b>取余</b> 的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>packages = [2,3,5], boxes = [[4,8],[2,8]]
<b>输出：</b>6
<b>解释：</b>选择第一个供应商最优，用两个尺寸为 4 的箱子和一个尺寸为 8 的箱子。
总浪费空间为 (4-2) + (4-3) + (8-5) = 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]
<b>输出：</b>-1
<b>解释：</b>没有箱子能装下尺寸为 5 的包裹。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]
<b>输出：</b>9
<b>解释：</b>选择第三个供应商最优，用两个尺寸为 5 的箱子，两个尺寸为 10 的箱子和两个尺寸为 14 的箱子。
总浪费空间为 (5-3) + (5-5) + (10-8) + (10-10) + (14-11) + (14-12) = 9 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == packages.length</code></li>
	<li><code>m == boxes.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= m <= 10<sup>5</sup></code></li>
	<li><code>1 <= packages[i] <= 10<sup>5</sup></code></li>
	<li><code>1 <= boxes[j].length <= 10<sup>5</sup></code></li>
	<li><code>1 <= boxes[j][k] <= 10<sup>5</sup></code></li>
	<li><code>sum(boxes[j].length) <= 10<sup>5</sup></code></li>
	<li><code>boxes[j]</code> 中的元素 <strong>互不相同</strong> 。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 前缀和
- 排序

## 提示

1. Given a fixed size box, is there a way to quickly query which packages (i.e., count and sizes) should end up in that box size?
2. Do we have to order the boxes a certain way to allow us to answer the query quickly?

## 示例

```
[2,3,5]
[[4,8],[2,8]]
[2,3,5]
[[1,4],[2,3],[3,4]]
[3,5,8,10,11,12]
[[12],[11,9],[10,5,14]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minWastedSpace(vector<int>& packages, vector<vector<int>>& boxes) {
        
    }
};
```

### Java

```java
class Solution {
    public int minWastedSpace(int[] packages, int[][] boxes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minWastedSpace(self, packages, boxes):
        """
        :type packages: List[int]
        :type boxes: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        
```

### C

```c
int minWastedSpace(int* packages, int packagesSize, int** boxes, int boxesSize, int* boxesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinWastedSpace(int[] packages, int[][] boxes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} packages
 * @param {number[][]} boxes
 * @return {number}
 */
var minWastedSpace = function(packages, boxes) {
    
};
```

### TypeScript

```typescript
function minWastedSpace(packages: number[], boxes: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $packages
     * @param Integer[][] $boxes
     * @return Integer
     */
    function minWastedSpace($packages, $boxes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minWastedSpace(_ packages: [Int], _ boxes: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minWastedSpace(packages: IntArray, boxes: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minWastedSpace(List<int> packages, List<List<int>> boxes) {
    
  }
}
```

### Go

```golang
func minWastedSpace(packages []int, boxes [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} packages
# @param {Integer[][]} boxes
# @return {Integer}
def min_wasted_space(packages, boxes)
    
end
```

### Scala

```scala
object Solution {
    def minWastedSpace(packages: Array[Int], boxes: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_wasted_space(packages: Vec<i32>, boxes: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-wasted-space packages boxes)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_wasted_space(Packages :: [integer()], Boxes :: [[integer()]]) -> integer().
min_wasted_space(Packages, Boxes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_wasted_space(packages :: [integer], boxes :: [[integer]]) :: integer
  def min_wasted_space(packages, boxes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minWastedSpace(packages: Array<Int64>, boxes: Array<Array<Int64>>): Int64 {

    }
}
```

