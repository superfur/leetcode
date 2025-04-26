# 2747. 统计没有收到请求的服务器数目

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，表示服务器的总数目，再给你一个下标从 <strong>0</strong>&nbsp;开始的 <strong>二维</strong>&nbsp;整数数组&nbsp;<code>logs</code>&nbsp;，其中&nbsp;<code>logs[i] = [server_id, time]</code>&nbsp;表示 id 为&nbsp;<code>server_id</code>&nbsp;的服务器在&nbsp;<code>time</code>&nbsp;时收到了一个请求。</p>

<p>同时给你一个整数&nbsp;<code>x</code>&nbsp;和一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>queries</code>&nbsp; 。</p>

<p>请你返回一个长度等于&nbsp;<code>queries.length</code>&nbsp;的数组&nbsp;<code>arr</code>&nbsp;，其中&nbsp;<code>arr[i]</code>&nbsp;表示在时间区间&nbsp;<code>[queries[i] - x, queries[i]]</code>&nbsp;内没有收到请求的服务器数目。</p>

<p>注意时间区间是个闭区间。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 3, logs = [[1,3],[2,6],[1,5]], x = 5, queries = [10,11]
<b>输出：</b>[1,2]
<b>解释：</b>
对于 queries[0]：id 为 1 和 2 的服务器在区间 [5, 10] 内收到了请求，所以只有服务器 3 没有收到请求。
对于 queries[1]：id 为 2 的服务器在区间 [6,11] 内收到了请求，所以 id 为 1 和 3 的服务器在这个时间段内没有收到请求。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, logs = [[2,4],[2,1],[1,2],[3,1]], x = 2, queries = [3,4]
<b>输出：</b>[0,1]
<b>解释：</b>
对于 queries[0]：区间 [1, 3] 内所有服务器都收到了请求。
对于 queries[1]：只有 id 为 3 的服务器在区间 [2,4] 内没有收到请求。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>logs[i].length == 2</code></li>
	<li><code>1 &lt;= logs[i][0] &lt;= n</code></li>
	<li><code>1 &lt;= logs[i][1] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= x &lt;= 10<sup>5</sup></code></li>
	<li><code>x &lt;&nbsp;queries[i]&nbsp;&lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序
- 滑动窗口

## 提示

1. Can we use sorting and two-pointer approach here?
2. Sort the queries array and logs array based on time in increasing order.
3. For every window of size x, use sliding window and two-pointer approach to find the answer to the queries.

## 示例

```
3
[[1,3],[2,6],[1,5]]
5
[10,11]
3
[[2,4],[2,1],[1,2],[3,1]]
2
[3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countServers(self, n, logs, x, queries):
        """
        :type n: int
        :type logs: List[List[int]]
        :type x: int
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countServers(int n, int** logs, int logsSize, int* logsColSize, int x, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] CountServers(int n, int[][] logs, int x, int[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} logs
 * @param {number} x
 * @param {number[]} queries
 * @return {number[]}
 */
var countServers = function(n, logs, x, queries) {
    
};
```

### TypeScript

```typescript
function countServers(n: number, logs: number[][], x: number, queries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $logs
     * @param Integer $x
     * @param Integer[] $queries
     * @return Integer[]
     */
    function countServers($n, $logs, $x, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countServers(_ n: Int, _ logs: [[Int]], _ x: Int, _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countServers(n: Int, logs: Array<IntArray>, x: Int, queries: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countServers(int n, List<List<int>> logs, int x, List<int> queries) {
    
  }
}
```

### Go

```golang
func countServers(n int, logs [][]int, x int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} logs
# @param {Integer} x
# @param {Integer[]} queries
# @return {Integer[]}
def count_servers(n, logs, x, queries)
    
end
```

### Scala

```scala
object Solution {
    def countServers(n: Int, logs: Array[Array[Int]], x: Int, queries: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_servers(n: i32, logs: Vec<Vec<i32>>, x: i32, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-servers n logs x queries)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer? (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_servers(N :: integer(), Logs :: [[integer()]], X :: integer(), Queries :: [integer()]) -> [integer()].
count_servers(N, Logs, X, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_servers(n :: integer, logs :: [[integer]], x :: integer, queries :: [integer]) :: [integer]
  def count_servers(n, logs, x, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countServers(n: Int64, logs: Array<Array<Int64>>, x: Int64, queries: Array<Int64>): Array<Int64> {

    }
}
```

