# 1923. 最长公共子路径

## 题目描述

<p>一个国家由 <code>n</code> 个编号为 <code>0</code> 到 <code>n - 1</code> 的城市组成。在这个国家里，<strong>每两个</strong> 城市之间都有一条道路连接。</p>

<p>总共有 <code>m</code> 个编号为 <code>0</code> 到 <code>m - 1</code> 的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。每条路径都由一个整数数组表示，每个整数数组表示一个朋友按顺序访问过的城市序列。同一个城市在一条路径中可能 <strong>重复</strong> 出现，但同一个城市在一条路径中不会连续出现。</p>

<p>给你一个整数 <code>n</code> 和二维数组 <code>paths</code> ，其中 <code>paths[i]</code> 是一个整数数组，表示第 <code>i</code> 个朋友走过的路径，请你返回 <strong>每一个</strong> 朋友都走过的 <strong>最长公共子路径</strong> 的长度，如果不存在公共子路径，请你返回 <code>0</code> 。</p>

<p>一个 <strong>子路径</strong> 指的是一条路径中连续的城市序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 5, paths = [[0,1,<strong>2,3</strong>,4],
                     [<strong>2,3</strong>,4],
                     [4,0,1,<strong>2,3</strong>]]
<b>输出：</b>2
<b>解释：</b>最长公共子路径为 [2,3] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, paths = [[0],[1],[2]]
<b>输出：</b>0
<b>解释：</b>三条路径没有公共子路径。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>n = 5, paths = [[<strong>0</strong>,1,2,3,4],
                     [4,3,2,1,<strong>0</strong>]]
<b>输出：</b>1
<b>解释：</b>最长公共子路径为 [0]，[1]，[2]，[3] 和 [4] 。它们长度都为 1 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>m == paths.length</code></li>
	<li><code>2 <= m <= 10<sup>5</sup></code></li>
	<li><code>sum(paths[i].length) <= 10<sup>5</sup></code></li>
	<li><code>0 <= paths[i][j] < n</code></li>
	<li><code>paths[i]</code> 中同一个城市不会连续重复出现。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 后缀数组
- 哈希函数
- 滚动哈希

## 提示

1. If there is a common path with length x, there is for sure a common path of length y where y < x.
2. We can use binary search over the answer with the range [0, min(path[i].length)].
3. Using binary search, we want to verify if we have a common path of length m. We can achieve this using hashing.

## 示例

```
5
[[0,1,2,3,4],[2,3,4],[4,0,1,2,3]]
3
[[0],[1],[2]]
5
[[0,1,2,3,4],[4,3,2,1,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestCommonSubpath(int n, vector<vector<int>>& paths) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestCommonSubpath(int n, int[][] paths) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestCommonSubpath(self, n, paths):
        """
        :type n: int
        :type paths: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        
```

### C

```c
int longestCommonSubpath(int n, int** paths, int pathsSize, int* pathsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestCommonSubpath(int n, int[][] paths) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} paths
 * @return {number}
 */
var longestCommonSubpath = function(n, paths) {
    
};
```

### TypeScript

```typescript
function longestCommonSubpath(n: number, paths: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $paths
     * @return Integer
     */
    function longestCommonSubpath($n, $paths) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestCommonSubpath(_ n: Int, _ paths: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestCommonSubpath(n: Int, paths: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestCommonSubpath(int n, List<List<int>> paths) {
    
  }
}
```

### Go

```golang
func longestCommonSubpath(n int, paths [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} paths
# @return {Integer}
def longest_common_subpath(n, paths)
    
end
```

### Scala

```scala
object Solution {
    def longestCommonSubpath(n: Int, paths: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_common_subpath(n: i32, paths: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-common-subpath n paths)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_common_subpath(N :: integer(), Paths :: [[integer()]]) -> integer().
longest_common_subpath(N, Paths) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_common_subpath(n :: integer, paths :: [[integer]]) :: integer
  def longest_common_subpath(n, paths) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestCommonSubpath(n: Int64, paths: Array<Array<Int64>>): Int64 {

    }
}
```

