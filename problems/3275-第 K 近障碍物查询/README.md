# 3275. 第 K 近障碍物查询

## 题目描述

<p>有一个无限大的二维平面。</p>

<p>给你一个正整数&nbsp;<code>k</code>&nbsp;，同时给你一个二维数组&nbsp;<code>queries</code>&nbsp;，包含一系列查询：</p>

<ul>
	<li><code>queries[i] = [x, y]</code>&nbsp;：在平面上坐标&nbsp;<code>(x, y)</code>&nbsp;处建一个障碍物，数据保证之前的查询 <strong>不会</strong> 在这个坐标处建立任何障碍物。</li>
</ul>

<p>每次查询后，你需要找到离原点第 <code>k</code>&nbsp;<strong>近</strong>&nbsp;障碍物到原点的 <strong>距离</strong>&nbsp;。</p>

<p>请你返回一个整数数组&nbsp;<code>results</code>&nbsp;，其中&nbsp;<code>results[i]</code>&nbsp;表示建立第 <code>i</code>&nbsp;个障碍物以后，离原地第 <code>k</code>&nbsp;近障碍物距离原点的距离。如果少于 <code>k</code>&nbsp;个障碍物，<code>results[i] == -1</code>&nbsp;。</p>

<p><strong>注意</strong>，一开始&nbsp;<strong>没有</strong>&nbsp;任何障碍物。</p>

<p>坐标在&nbsp;<code>(x, y)</code>&nbsp;处的点距离原点的距离定义为&nbsp;<code>|x| + |y|</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>[-1,7,5,3]</span></p>

<p><strong>解释：</strong></p>

<p>最初，不存在障碍物。</p>

<ul>
	<li><code>queries[0]</code>&nbsp;之后，少于 2 个障碍物。</li>
	<li><code>queries[1]</code>&nbsp;之后，&nbsp;两个障碍物距离原点的距离分别为 3 和 7 。</li>
	<li><code>queries[2]</code>&nbsp;之后，障碍物距离原点的距离分别为 3 ，5 和 7 。</li>
	<li><code>queries[3]</code>&nbsp;之后，障碍物距离原点的距离分别为 3，3，5 和 7 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>queries = [[5,5],[4,4],[3,3]], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>[10,8,6]</span></p>

<p><b>解释：</b></p>

<ul>
	<li><code>queries[0]</code>&nbsp;之后，只有一个障碍物，距离原点距离为 10 。</li>
	<li><code>queries[1]</code>&nbsp;之后，障碍物距离原点距离分别为 8 和 10 。</li>
	<li><code>queries[2]</code>&nbsp;之后，障碍物距离原点的距离分别为 6， 8 和10 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li>所有&nbsp;<code>queries[i]</code>&nbsp;互不相同。</li>
	<li><code>-10<sup>9</sup> &lt;= queries[i][0], queries[i][1] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 堆（优先队列）

## 提示

1. Consider if there are more than <code>k</code> obstacles. Can the <code>k + 1<sup>th</sup></code> obstacle ever be the answer to any query?
2. Maintain a max heap of size <code>k</code>, thus heap will contain minimum element at the top in that queue.
3. Remove top element and insert new element from input array if current max is larger than this.

## 示例

```
[[1,2],[3,4],[2,3],[-3,0]]
2
[[5,5],[4,4],[3,3]]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> resultsArray(vector<vector<int>>& queries, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] resultsArray(int[][] queries, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def resultsArray(self, queries, k):
        """
        :type queries: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int** queries, int queriesSize, int* queriesColSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ResultsArray(int[][] queries, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} queries
 * @param {number} k
 * @return {number[]}
 */
var resultsArray = function(queries, k) {
    
};
```

### TypeScript

```typescript
function resultsArray(queries: number[][], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $queries
     * @param Integer $k
     * @return Integer[]
     */
    function resultsArray($queries, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func resultsArray(_ queries: [[Int]], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun resultsArray(queries: Array<IntArray>, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> resultsArray(List<List<int>> queries, int k) {
    
  }
}
```

### Go

```golang
func resultsArray(queries [][]int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} queries
# @param {Integer} k
# @return {Integer[]}
def results_array(queries, k)
    
end
```

### Scala

```scala
object Solution {
    def resultsArray(queries: Array[Array[Int]], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn results_array(queries: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (results-array queries k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec results_array(Queries :: [[integer()]], K :: integer()) -> [integer()].
results_array(Queries, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec results_array(queries :: [[integer]], k :: integer) :: [integer]
  def results_array(queries, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func resultsArray(queries: Array<Array<Int64>>, k: Int64): Array<Int64> {

    }
}
```

