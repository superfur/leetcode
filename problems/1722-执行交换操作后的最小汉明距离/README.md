# 1722. 执行交换操作后的最小汉明距离

## 题目描述

<p>给你两个整数数组 <code>source</code> 和 <code>target</code> ，长度都是 <code>n</code> 。还有一个数组 <code>allowedSwaps</code> ，其中每个 <code>allowedSwaps[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示你可以交换数组 <code>source</code> 中下标为 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code>（<strong>下标从 0 开始</strong>）的两个元素。注意，你可以按 <strong>任意</strong> 顺序 <strong>多次</strong> 交换一对特定下标指向的元素。</p>

<p>相同长度的两个数组 <code>source</code> 和 <code>target</code> 间的 <strong>汉明距离</strong> 是元素不同的下标数量。形式上，其值等于满足 <code>source[i] != target[i]</code> （<strong>下标从 0 开始</strong>）的下标 <code>i</code>（<code>0 &lt;= i &lt;= n-1</code>）的数量。</p>

<p>在对数组 <code>source</code> 执行 <strong>任意</strong> 数量的交换操作后，返回 <code>source</code> 和 <code>target</code> 间的 <strong>最小汉明距离</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
<strong>输出：</strong>1
<strong>解释：</strong>source 可以按下述方式转换：
- 交换下标 0 和 1 指向的元素：source = [<strong>2</strong>,<strong>1</strong>,3,4]
- 交换下标 2 和 3 指向的元素：source = [2,1,<strong>4</strong>,<strong>3</strong>]
source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
<strong>输出：</strong>2
<strong>解释：</strong>不能对 source 执行交换操作。
source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == source.length == target.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= source[i], target[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= allowedSwaps.length &lt;= 10<sup>5</sup></code></li>
	<li><code>allowedSwaps[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 并查集
- 数组

## 提示

1. The source array can be imagined as a graph where each index is a node and each allowedSwaps[i] is an edge.
2. Nodes within the same component can be freely swapped with each other.
3. For each component, find the number of common elements. The elements that are not in common will contribute to the total Hamming distance.

## 示例

```
[1,2,3,4]
[2,1,4,5]
[[0,1],[2,3]]
[1,2,3,4]
[1,3,2,4]
[]
[5,1,2,4,3]
[1,5,4,2,3]
[[0,4],[4,2],[1,3],[1,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumHammingDistance(vector<int>& source, vector<int>& target, vector<vector<int>>& allowedSwaps) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
```

### C

```c
int minimumHammingDistance(int* source, int sourceSize, int* target, int targetSize, int** allowedSwaps, int allowedSwapsSize, int* allowedSwapsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} source
 * @param {number[]} target
 * @param {number[][]} allowedSwaps
 * @return {number}
 */
var minimumHammingDistance = function(source, target, allowedSwaps) {
    
};
```

### TypeScript

```typescript
function minimumHammingDistance(source: number[], target: number[], allowedSwaps: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $source
     * @param Integer[] $target
     * @param Integer[][] $allowedSwaps
     * @return Integer
     */
    function minimumHammingDistance($source, $target, $allowedSwaps) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumHammingDistance(_ source: [Int], _ target: [Int], _ allowedSwaps: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumHammingDistance(source: IntArray, target: IntArray, allowedSwaps: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumHammingDistance(List<int> source, List<int> target, List<List<int>> allowedSwaps) {
    
  }
}
```

### Go

```golang
func minimumHammingDistance(source []int, target []int, allowedSwaps [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} source
# @param {Integer[]} target
# @param {Integer[][]} allowed_swaps
# @return {Integer}
def minimum_hamming_distance(source, target, allowed_swaps)
    
end
```

### Scala

```scala
object Solution {
    def minimumHammingDistance(source: Array[Int], target: Array[Int], allowedSwaps: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_hamming_distance(source: Vec<i32>, target: Vec<i32>, allowed_swaps: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-hamming-distance source target allowedSwaps)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_hamming_distance(Source :: [integer()], Target :: [integer()], AllowedSwaps :: [[integer()]]) -> integer().
minimum_hamming_distance(Source, Target, AllowedSwaps) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_hamming_distance(source :: [integer], target :: [integer], allowed_swaps :: [[integer]]) :: integer
  def minimum_hamming_distance(source, target, allowed_swaps) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumHammingDistance(source: Array<Int64>, target: Array<Int64>, allowedSwaps: Array<Array<Int64>>): Int64 {

    }
}
```

