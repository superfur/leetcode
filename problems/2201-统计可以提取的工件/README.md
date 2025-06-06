# 2201. 统计可以提取的工件

## 题目描述

<p>存在一个 <code>n x n</code> 大小、下标从 <strong>0</strong> 开始的网格，网格中埋着一些工件。给你一个整数 <code>n</code> 和一个下标从 <strong>0</strong> 开始的二维整数数组 <code>artifacts</code> ，<code>artifacts</code> 描述了矩形工件的位置，其中 <code>artifacts[i] = [r1<sub>i</sub>, c1<sub>i</sub>, r2<sub>i</sub>, c2<sub>i</sub>]</code> 表示第 <code>i</code> 个工件在子网格中的填埋情况：</p>

<ul>
	<li><code>(r1<sub>i</sub>, c1<sub>i</sub>)</code> 是第 <code>i</code> 个工件 <strong>左上</strong> 单元格的坐标，且</li>
	<li><code>(r2<sub>i</sub>, c2<sub>i</sub>)</code> 是第 <code>i</code> 个工件 <strong>右下</strong> 单元格的坐标。</li>
</ul>

<p>你将会挖掘网格中的一些单元格，并清除其中的填埋物。如果单元格中埋着工件的一部分，那么该工件这一部分将会裸露出来。如果一个工件的所有部分都都裸露出来，你就可以提取该工件。</p>

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>dig</code> ，其中 <code>dig[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> 表示你将会挖掘单元格 <code>(r<sub>i</sub>, c<sub>i</sub>)</code> ，返回你可以提取的工件数目。</p>

<p>生成的测试用例满足：</p>

<ul>
	<li>不存在重叠的两个工件。</li>
	<li>每个工件最多只覆盖 <code>4</code> 个单元格。</li>
	<li><code>dig</code> 中的元素互不相同。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/16/untitled-diagram.jpg" style="width: 216px; height: 216px;">
<pre><strong>输入：</strong>n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
<strong>输出：</strong>1
<strong>解释：</strong> 
不同颜色表示不同的工件。挖掘的单元格用 'D' 在网格中进行标记。
有 1 个工件可以提取，即红色工件。
蓝色工件在单元格 (1,1) 的部分尚未裸露出来，所以无法提取该工件。
因此，返回 1 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/09/16/untitled-diagram-1.jpg" style="width: 216px; height: 216px;">
<pre><strong>输入：</strong>n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
<strong>输出：</strong>2
<strong>解释：</strong>红色工件和蓝色工件的所有部分都裸露出来（用 'D' 标记），都可以提取。因此，返回 2 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= artifacts.length, dig.length &lt;= min(n<sup>2</sup>, 10<sup>5</sup>)</code></li>
	<li><code>artifacts[i].length == 4</code></li>
	<li><code>dig[i].length == 2</code></li>
	<li><code>0 &lt;= r1<sub>i</sub>, c1<sub>i</sub>, r2<sub>i</sub>, c2<sub>i</sub>, r<sub>i</sub>, c<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>r1<sub>i</sub> &lt;= r2<sub>i</sub></code></li>
	<li><code>c1<sub>i</sub> &lt;= c2<sub>i</sub></code></li>
	<li>不存在重叠的两个工件</li>
	<li>每个工件 <strong>最多</strong> 只覆盖 <code>4</code> 个单元格</li>
	<li><code>dig</code> 中的元素互不相同</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 模拟

## 提示

1. Check if each coordinate of each artifact has been excavated. How can we do this quickly without iterating over the dig array every time?
2. Consider marking all excavated cells in a 2D boolean array.

## 示例

```
2
[[0,0,0,0],[0,1,1,1]]
[[0,0],[0,1]]
2
[[0,0,0,0],[0,1,1,1]]
[[0,0],[0,1],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int digArtifacts(int n, vector<vector<int>>& artifacts, vector<vector<int>>& dig) {
        
    }
};
```

### Java

```java
class Solution {
    public int digArtifacts(int n, int[][] artifacts, int[][] dig) {
        
    }
}
```

### Python

```python
class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
```

### C

```c
int digArtifacts(int n, int** artifacts, int artifactsSize, int* artifactsColSize, int** dig, int digSize, int* digColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DigArtifacts(int n, int[][] artifacts, int[][] dig) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} artifacts
 * @param {number[][]} dig
 * @return {number}
 */
var digArtifacts = function(n, artifacts, dig) {
    
};
```

### TypeScript

```typescript
function digArtifacts(n: number, artifacts: number[][], dig: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $artifacts
     * @param Integer[][] $dig
     * @return Integer
     */
    function digArtifacts($n, $artifacts, $dig) {
        
    }
}
```

### Swift

```swift
class Solution {
    func digArtifacts(_ n: Int, _ artifacts: [[Int]], _ dig: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun digArtifacts(n: Int, artifacts: Array<IntArray>, dig: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int digArtifacts(int n, List<List<int>> artifacts, List<List<int>> dig) {
    
  }
}
```

### Go

```golang
func digArtifacts(n int, artifacts [][]int, dig [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} artifacts
# @param {Integer[][]} dig
# @return {Integer}
def dig_artifacts(n, artifacts, dig)
    
end
```

### Scala

```scala
object Solution {
    def digArtifacts(n: Int, artifacts: Array[Array[Int]], dig: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn dig_artifacts(n: i32, artifacts: Vec<Vec<i32>>, dig: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (dig-artifacts n artifacts dig)
  (-> exact-integer? (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec dig_artifacts(N :: integer(), Artifacts :: [[integer()]], Dig :: [[integer()]]) -> integer().
dig_artifacts(N, Artifacts, Dig) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec dig_artifacts(n :: integer, artifacts :: [[integer]], dig :: [[integer]]) :: integer
  def dig_artifacts(n, artifacts, dig) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func digArtifacts(n: Int64, artifacts: Array<Array<Int64>>, dig: Array<Array<Int64>>): Int64 {

    }
}
```

