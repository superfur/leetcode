# 3160. 所有球里面不同颜色的数目

## 题目描述

<p>给你一个整数&nbsp;<code>limit</code>&nbsp;和一个大小为 <code>n x 2</code>&nbsp;的二维数组&nbsp;<code>queries</code>&nbsp;。</p>

<p>总共有&nbsp;<code>limit + 1</code>&nbsp;个球，每个球的编号为&nbsp;<code>[0, limit]</code>&nbsp;中一个&nbsp;<strong>互不相同</strong>&nbsp;的数字。一开始，所有球都没有颜色。<code>queries</code>&nbsp;中每次操作的格式为&nbsp;<code>[x, y]</code>&nbsp;，你需要将球&nbsp;<code>x</code>&nbsp;染上颜色&nbsp;<code>y</code>&nbsp;。每次操作之后，你需要求出所有球颜色的数目。</p>

<p>请你返回一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>result</code>&nbsp;，其中&nbsp;<code>result[i]</code>&nbsp;是第 <code>i</code>&nbsp;次操作以后颜色的数目。</p>

<p><strong>注意</strong>&nbsp;，没有染色的球不算作一种颜色。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]</span></p>

<p><span class="example-io"><b>输出：</b>[1,2,2,3]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop.gif" style="width: 455px; height: 145px;" /></p>

<ul>
	<li>操作 0&nbsp;后，球 1 颜色为 4 。</li>
	<li>操作 1 后，球 1 颜色为&nbsp;4 ，球 2 颜色为 5 。</li>
	<li>操作 2 后，球 1 颜色为 3 ，球 2 颜色为 5 。</li>
	<li>操作 3 后，球 1 颜色为 3 ，球 2 颜色为 5 ，球 3 颜色为 4 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]</span></p>

<p><span class="example-io"><b>输出：</b>[1,2,2,3,4]</span></p>

<p><strong>解释：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop2.gif" style="width: 457px; height: 144px;" /></strong></p>

<ul>
	<li>操作 0&nbsp;后，球 0&nbsp;颜色为 1&nbsp;。</li>
	<li>操作 1&nbsp;后，球 0&nbsp;颜色为 1 ，球 1 颜色为 2 。</li>
	<li>操作 2&nbsp;后，球 0&nbsp;颜色为 1 ，球 1 和 2&nbsp;颜色为 2 。</li>
	<li>操作 3 后，球 0&nbsp;颜色为 1 ，球 1 和 2&nbsp;颜色为 2 ，球 3 颜色为 4 。</li>
	<li>操作 4&nbsp;后，球 0&nbsp;颜色为 1 ，球 1 和 2&nbsp;颜色为 2 ，球 3 颜色为 4 ，球 4 颜色为 5 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= limit &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= n == queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= queries[i][0] &lt;= limit</code></li>
	<li><code>1 &lt;= queries[i][1] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 模拟

## 提示

1. Use two HashMaps to maintain the color of each ball and the set of balls with each color.

## 示例

```
4
[[1,4],[2,5],[1,3],[3,4]]
4
[[0,1],[1,2],[2,2],[3,4],[4,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> queryResults(int limit, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] queryResults(int limit, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* queryResults(int limit, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] QueryResults(int limit, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} limit
 * @param {number[][]} queries
 * @return {number[]}
 */
var queryResults = function(limit, queries) {
    
};
```

### TypeScript

```typescript
function queryResults(limit: number, queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $limit
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function queryResults($limit, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func queryResults(_ limit: Int, _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun queryResults(limit: Int, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> queryResults(int limit, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func queryResults(limit int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} limit
# @param {Integer[][]} queries
# @return {Integer[]}
def query_results(limit, queries)
    
end
```

### Scala

```scala
object Solution {
    def queryResults(limit: Int, queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn query_results(limit: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (query-results limit queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec query_results(Limit :: integer(), Queries :: [[integer()]]) -> [integer()].
query_results(Limit, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec query_results(limit :: integer, queries :: [[integer]]) :: [integer]
  def query_results(limit, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func queryResults(limit: Int64, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

