# 3245. 交替组 III

## 题目描述

<p>给你一个整数数组 <code>colors</code> 和一个二维整数数组 <code>queries</code> 。<code>colors</code>表示一个由红色和蓝色瓷砖组成的环，第 <code>i</code>&nbsp;块瓷砖的颜色为&nbsp;<code>colors[i]</code>&nbsp;：</p>

<ul>
	<li><code>colors[i] == 0</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;块瓷砖的颜色是 <strong>红色</strong>&nbsp;。</li>
	<li><code>colors[i] == 1</code>&nbsp;表示第 <code>i</code>&nbsp;块瓷砖的颜色是 <strong>蓝色</strong>&nbsp;。</li>
</ul>

<p>环中连续若干块瓷砖的颜色如果是 <strong>交替</strong>&nbsp;颜色（也就是说这组瓷砖中除了第一块和最后一块瓷砖以外，中间瓷砖的颜色与它<strong>&nbsp;左边</strong>&nbsp;和 <strong>右边</strong>&nbsp;的颜色都不同），那么它被称为一个 <strong>交替组</strong>。</p>

<p>你需要处理两种类型的查询：</p>

<ul>
	<li><code>queries[i] = [1, size<sub>i</sub>]</code>，确定大小为<code>size<sub>i</sub></code>的<strong> </strong><strong>交替组</strong> 的数量。</li>
	<li><code>queries[i] = [2, index<sub>i</sub>, color<sub>i</sub>]</code>，将<code>colors[index<sub>i</sub>]</code>更改为<code>color<sub>i</sub></code>。</li>
</ul>

<p>返回数组 <code>answer</code>，数组中按顺序包含第一种类型查询的结果。</p>

<p><b>注意</b>&nbsp;，由于&nbsp;<code>colors</code>&nbsp;表示一个 <strong>环</strong>&nbsp;，<strong>第一块</strong>&nbsp;瓷砖和 <strong>最后一块</strong>&nbsp;瓷砖是相邻的。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]</span></p>

<p><strong>输出：</strong><span class="example-io">[2]</span></p>

<p><strong>解释：</strong></p>

<p>第一次查询：</p>

<p>将 <code>colors[1]</code> 改为 0。</p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-20-25.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>

<p>第二次查询：</p>

<p>统计大小为 4 的交替组的数量：</p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-25-02-2.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-24-12.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]</span></p>

<p><strong>输出：</strong><span class="example-io">[2,0]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-35-50.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>

<p>第一次查询：</p>

<p>统计大小为 3 的交替组的数量。</p>

<p><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-37-13.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /><img alt="" data-darkreader-inline-bgcolor="" data-darkreader-inline-bgimage="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-from-2024-06-03-20-36-40.png" style="width: 150px; height: 150px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; --darkreader-inline-bgimage: initial; --darkreader-inline-bgcolor: #181a1b;" /></p>

<p>第二次查询：<code>colors</code>不变。</p>

<p>第三次查询：不存在大小为 5 的交替组。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>4 &lt;= colors.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= colors[i] &lt;= 1</code></li>
	<li><code>1 &lt;= queries.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>queries[i][0] == 1</code> 或 <code>queries[i][0] == 2</code></li>
	<li>对于所有的<code>i</code>：
	<ul>
		<li><code>queries[i][0] == 1</code>： <code>queries[i].length == 2</code>, <code>3 &lt;= queries[i][1] &lt;= colors.length - 1</code></li>
		<li><code>queries[i][0] == 2</code>： <code>queries[i].length == 3</code>, <code>0 &lt;= queries[i][1] &lt;= colors.length - 1</code>, <code>0 &lt;= queries[i][2] &lt;= 1</code></li>
	</ul>
	</li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 数组

## 提示

1. Try using a segment tree to store the maximal alternating groups.
2. Store the sizes of these maximal alternating groups in another data structure.
3. Find the count of the alternating groups of size <code>k</code> with having the count of maximal alternating groups with size greater than or equal to <code>k</code> and the sum of their sizes.

## 示例

```
[0,1,1,0,1]
[[2,1,0],[1,4]]
[0,0,1,0,1,1]
[[1,3],[2,3,0],[1,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numberOfAlternatingGroups(vector<int>& colors, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> numberOfAlternatingGroups(int[] colors, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfAlternatingGroups(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numberOfAlternatingGroups(int* colors, int colorsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> NumberOfAlternatingGroups(int[] colors, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} colors
 * @param {number[][]} queries
 * @return {number[]}
 */
var numberOfAlternatingGroups = function(colors, queries) {
    
};
```

### TypeScript

```typescript
function numberOfAlternatingGroups(colors: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $colors
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function numberOfAlternatingGroups($colors, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfAlternatingGroups(_ colors: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfAlternatingGroups(colors: IntArray, queries: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numberOfAlternatingGroups(List<int> colors, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func numberOfAlternatingGroups(colors []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} colors
# @param {Integer[][]} queries
# @return {Integer[]}
def number_of_alternating_groups(colors, queries)
    
end
```

### Scala

```scala
object Solution {
    def numberOfAlternatingGroups(colors: Array[Int], queries: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_alternating_groups(colors: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-alternating-groups colors queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec number_of_alternating_groups(Colors :: [integer()], Queries :: [[integer()]]) -> [integer()].
number_of_alternating_groups(Colors, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_alternating_groups(colors :: [integer], queries :: [[integer]]) :: [integer]
  def number_of_alternating_groups(colors, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfAlternatingGroups(colors: Array<Int64>, queries: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

