# 3161. 物块放置查询

## 题目描述

<p>有一条无限长的数轴，原点在 0 处，沿着 x 轴 <strong>正</strong>&nbsp;方向无限延伸。</p>

<p>给你一个二维数组&nbsp;<code>queries</code>&nbsp;，它包含两种操作：</p>

<ol>
	<li>操作类型 1 ：<code>queries[i] = [1, x]</code>&nbsp;。在距离原点 <code>x</code>&nbsp;处建一个障碍物。数据保证当操作执行的时候，位置 <code>x</code>&nbsp;处 <strong>没有</strong>&nbsp;任何障碍物。</li>
	<li>操作类型 2 ：<code>queries[i] = [2, x, sz]</code>&nbsp;。判断在数轴范围&nbsp;<code>[0, x]</code>&nbsp;内是否可以放置一个长度为&nbsp;<code>sz</code>&nbsp;的物块，这个物块需要&nbsp;<strong>完全</strong>&nbsp;放置在范围&nbsp;<code>[0, x]</code>&nbsp;内。如果物块与任何障碍物有重合，那么这个物块&nbsp;<strong>不能</strong>&nbsp;被放置，但物块可以与障碍物刚好接触。注意，你只是进行查询，并&nbsp;<strong>不是</strong>&nbsp;真的放置这个物块。每个查询都是相互独立的。</li>
</ol>

<p>请你返回一个 boolean 数组<code>results</code>&nbsp;，如果第&nbsp;<code>i</code> 个操作类型 2 的操作你可以放置物块，那么&nbsp;<code>results[i]</code>&nbsp;为&nbsp;<code>true</code>&nbsp;，否则为 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]</span></p>

<p><span class="example-io"><b>输出：</b>[false,true,true]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/22/example0block.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 309px; height: 129px;" /></strong></p>

<p>查询 0 ，在&nbsp;<code>x = 2</code>&nbsp;处放置一个障碍物。在&nbsp;<code>x = 3</code>&nbsp;之前任何大小不超过 2 的物块都可以被放置。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>queries = </span>[[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]<!-- notionvc: 4a471445-5af1-4d72-b11b-94d351a2c8e9 --></p>

<p><b>输出：</b>[true,true,false]</p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/22/example1block.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 310px; height: 130px;" /></strong></p>

<ul>
	<li>查询 0 在&nbsp;<code>x = 7</code>&nbsp;处放置一个障碍物。在&nbsp;<code>x = 7</code>&nbsp;之前任何大小不超过 7 的物块都可以被放置。</li>
	<li>查询 2 在&nbsp;<code>x = 2</code>&nbsp;处放置一个障碍物。现在，在&nbsp;<code>x = 7</code>&nbsp;之前任何大小不超过 5 的物块可以被放置，<code>x = 2</code>&nbsp;之前任何大小不超过 2 的物块可以被放置。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= queries.length &lt;= 15 * 10<sup>4</sup></code></li>
	<li><code>2 &lt;= queries[i].length &lt;= 3</code></li>
	<li><code>1 &lt;= queries[i][0] &lt;= 2</code></li>
	<li><code>1 &lt;= x, sz &lt;= min(5 * 10<sup>4</sup>, 3 * queries.length)</code></li>
	<li>输入保证操作 1 中，<code>x</code>&nbsp;处不会有障碍物。</li>
	<li>输入保证至少有一个操作类型 2 。</li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找

## 提示

1. Let <code>d[x]</code> be the distance of the next obstacle after <code>x</code>.
2. For each query of type 2, we just need to check if <code>max(d[0], d[1], d[2], …d[x - sz]) > sz</code>.
3. Use segment tree to maintain <code>d[x]</code>.

## 示例

```
[[1,2],[2,3,3],[2,3,1],[2,2,2]]
[[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> getResults(vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> getResults(int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getResults(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* getResults(int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> GetResults(int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var getResults = function(queries) {
    
};
```

### TypeScript

```typescript
function getResults(queries: number[][]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function getResults($queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getResults(_ queries: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getResults(queries: Array<IntArray>): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> getResults(List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func getResults(queries [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} queries
# @return {Boolean[]}
def get_results(queries)
    
end
```

### Scala

```scala
object Solution {
    def getResults(queries: Array[Array[Int]]): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (get-results queries)
  (-> (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec get_results(Queries :: [[integer()]]) -> [boolean()].
get_results(Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_results(queries :: [[integer]]) :: [boolean]
  def get_results(queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getResults(queries: Array<Array<Int64>>): ArrayList<Bool> {

    }
}
```

