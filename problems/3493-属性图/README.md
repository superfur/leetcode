# 3493. 属性图

## 题目描述

<p>给你一个二维整数数组 <code>properties</code>，其维度为 <code>n x m</code>，以及一个整数 <code>k</code>。</p>

<p>定义一个函数 <code>intersect(a, b)</code>，它返回数组 <code>a</code> 和 <code>b</code> 中<strong> 共有的不同整数的数量 </strong>。</p>

<p>构造一个 <strong>无向图</strong>，其中每个索引 <code>i</code> 对应 <code>properties[i]</code>。如果且仅当 <code>intersect(properties[i], properties[j]) &gt;= k</code>（其中 <code>i</code> 和 <code>j</code> 的范围为 <code>[0, n - 1]</code> 且 <code>i != j</code>），节点 <code>i</code> 和节点 <code>j</code> 之间有一条边。</p>

<p>返回结果图中<strong> 连通分量 </strong>的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>生成的图有 3 个连通分量：</p>

<p><img src="https://pic.leetcode.cn/1742665594-CDVPWz-image.png" style="width: 279px; height: 171px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>生成的图有 1 个连通分量：</p>

<p><img alt="" src="https://pic.leetcode.cn/1742665565-NzYlYH-screenshot-from-2025-02-27-23-58-34.png" style="width: 219px; height: 171px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">properties = [[1,1],[1,1]], k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p><code>intersect(properties[0], properties[1]) = 1</code>，小于 <code>k</code>。因此在图中 <code>properties[0]</code> 和 <code>properties[1]</code> 之间没有边。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == properties.length &lt;= 100</code></li>
	<li><code>1 &lt;= m == properties[i].length &lt;= 100</code></li>
	<li><code>1 &lt;= properties[i][j] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= m</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图
- 数组
- 哈希表

## 提示

1. How can we optimally find the intersection of two arrays? One way is to use <code>len(set(a) & set(b))</code>.
2. For connected components, think about using DFS, BFS, or DSU.

## 示例

```
[[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]]
1
[[1,2,3],[2,3,4],[4,3,5]]
2
[[1,1],[1,1]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfComponents(int[][] properties, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfComponents(self, properties, k):
        """
        :type properties: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        
```

### C

```c
int numberOfComponents(int** properties, int propertiesSize, int* propertiesColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfComponents(int[][] properties, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} properties
 * @param {number} k
 * @return {number}
 */
var numberOfComponents = function(properties, k) {
    
};
```

### TypeScript

```typescript
function numberOfComponents(properties: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $properties
     * @param Integer $k
     * @return Integer
     */
    function numberOfComponents($properties, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfComponents(_ properties: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfComponents(properties: Array<IntArray>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfComponents(List<List<int>> properties, int k) {
    
  }
}
```

### Go

```golang
func numberOfComponents(properties [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} properties
# @param {Integer} k
# @return {Integer}
def number_of_components(properties, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfComponents(properties: Array[Array[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_components(properties: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-components properties k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_components(Properties :: [[integer()]], K :: integer()) -> integer().
number_of_components(Properties, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_components(properties :: [[integer]], k :: integer) :: integer
  def number_of_components(properties, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfComponents(properties: Array<Array<Int64>>, k: Int64): Int64 {

    }
}
```

