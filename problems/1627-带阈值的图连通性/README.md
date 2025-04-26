# 1627. 带阈值的图连通性

## 题目描述

<p>有 <code>n</code> 座城市，编号从 <code>1</code> 到 <code>n</code> 。编号为 <code>x</code> 和 <code>y</code> 的两座城市直接连通的前提是： <code>x</code> 和 <code>y</code> 的公因数中，至少有一个 <strong>严格大于</strong> 某个阈值 <code>threshold</code> 。更正式地说，如果存在整数 <code>z</code> ，且满足以下所有条件，则编号 <code>x</code> 和 <code>y</code> 的城市之间有一条道路：</p>

<ul>
	<li><code>x % z == 0</code></li>
	<li><code>y % z == 0</code></li>
	<li><code>z > threshold</code></li>
</ul>

<p>给你两个整数 <code>n</code> 和 <code>threshold</code> ，以及一个待查询数组，请你判断每个查询<code> queries[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 指向的城市 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 是否连通（即，它们之间是否存在一条路径）。</p>

<p>返回数组 <code>answer</code> ，其中<code>answer.length == queries.length</code> 。如果第 <code>i</code> 个查询中指向的城市 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 连通，则 <code>answer[i]</code> 为 <code>true</code> ；如果不连通，则 <code>answer[i]</code> 为 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/18/ex1.jpg" style="width: 382px; height: 181px;" /></p>

<p> </p>

<pre>
<strong>输入：</strong>n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
<strong>输出：</strong>[false,false,true]
<strong>解释：</strong>每个数的因数如下：
1:   1
2:   1, 2
3:   1, <strong>3</strong>
4:   1, 2, <strong>4</strong>
5:   1, <strong>5</strong>
6:   1, 2, <strong>3</strong>, <strong>6</strong>
所有大于阈值的的因数已经加粗标识，只有城市 3 和 6 共享公约数 3 ，因此结果是： 
[1,4]   1 与 4 不连通
[2,5]   2 与 5 不连通
[3,6]   3 与 6 连通，存在路径 3--6
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/18/tmp.jpg" style="width: 532px; height: 302px;" /></p>

<p> </p>

<pre>
<strong>输入：</strong>n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
<strong>输出：</strong>[true,true,true,true,true]
<strong>解释：</strong>每个数的因数与上一个例子相同。但是，由于阈值为 0 ，所有的因数都大于阈值。因为所有的数字共享公因数 1 ，所以所有的城市都互相连通。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/16/ex3.jpg" style="width: 282px; height: 282px;" /></p>

<p> </p>

<pre>
<strong>输入：</strong>n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
<strong>输出：</strong>[false,false,false,false,false]
<strong>解释：</strong>只有城市 2 和 4 共享的公约数 2 严格大于阈值 1 ，所以只有这两座城市是连通的。
注意，同一对节点 [x, y] 可以有多个查询，并且查询 [x，y] 等同于查询 [y，x] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 10<sup>4</sup></code></li>
	<li><code>0 <= threshold <= n</code></li>
	<li><code>1 <= queries.length <= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>1 <= a<sub>i</sub>, b<sub>i</sub> <= cities</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
</ul>


## 难度

Hard

## 标签

- 并查集
- 数组
- 数学
- 数论

## 提示

1. How to build the graph of the cities?
2. Connect city i with all its multiples 2*i, 3*i, ...
3. Answer the queries using union-find data structure.

## 示例

```
6
2
[[1,4],[2,5],[3,6]]
6
0
[[4,5],[3,4],[3,2],[2,6],[1,3]]
5
1
[[4,5],[4,5],[3,2],[2,3],[3,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> areConnected(int n, int threshold, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> areConnected(int n, int threshold, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def areConnected(self, n, threshold, queries):
        """
        :type n: int
        :type threshold: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* areConnected(int n, int threshold, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> AreConnected(int n, int threshold, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} threshold
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var areConnected = function(n, threshold, queries) {
    
};
```

### TypeScript

```typescript
function areConnected(n: number, threshold: number, queries: number[][]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $threshold
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function areConnected($n, $threshold, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func areConnected(_ n: Int, _ threshold: Int, _ queries: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun areConnected(n: Int, threshold: Int, queries: Array<IntArray>): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> areConnected(int n, int threshold, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func areConnected(n int, threshold int, queries [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} threshold
# @param {Integer[][]} queries
# @return {Boolean[]}
def are_connected(n, threshold, queries)
    
end
```

### Scala

```scala
object Solution {
    def areConnected(n: Int, threshold: Int, queries: Array[Array[Int]]): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn are_connected(n: i32, threshold: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (are-connected n threshold queries)
  (-> exact-integer? exact-integer? (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec are_connected(N :: integer(), Threshold :: integer(), Queries :: [[integer()]]) -> [boolean()].
are_connected(N, Threshold, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec are_connected(n :: integer, threshold :: integer, queries :: [[integer]]) :: [boolean]
  def are_connected(n, threshold, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func areConnected(n: Int64, threshold: Int64, queries: Array<Array<Int64>>): ArrayList<Bool> {

    }
}
```

