# 886. 可能的二分法

## 题目描述

<p>给定一组&nbsp;<code>n</code>&nbsp;人（编号为&nbsp;<code>1, 2, ..., n</code>），&nbsp;我们想把每个人分进<strong>任意</strong>大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。</p>

<p>给定整数 <code>n</code>&nbsp;和数组 <code>dislikes</code>&nbsp;，其中&nbsp;<code>dislikes[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;，表示不允许将编号为 <code>a<sub>i</sub></code>&nbsp;和&nbsp;&nbsp;<code>b<sub>i</sub></code>的人归入同一组。当可以用这种方法将所有人分进两组时，返回 <code>true</code>；否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 4, dislikes = [[1,2],[1,3],[2,4]]
<strong>输出：</strong>true
<strong>解释：</strong>group1 [1,4], group2 [2,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, dislikes = [[1,2],[1,3],[2,3]]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>0 &lt;= dislikes.length &lt;= 10<sup>4</sup></code></li>
	<li><code>dislikes[i].length == 2</code></li>
	<li><code>1 &lt;= dislikes[i][j] &lt;= n</code></li>
	<li><code>a<sub>i</sub>&nbsp;&lt; b<sub>i</sub></code></li>
	<li><code>dislikes</code>&nbsp;中每一组都 <strong>不同</strong></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 并查集
- 图

## 示例

```
4
[[1,2],[1,3],[2,4]]
3
[[1,2],[1,3],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
```

### C

```c
bool possibleBipartition(int n, int** dislikes, int dislikesSize, int* dislikesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool PossibleBipartition(int n, int[][] dislikes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} dislikes
 * @return {boolean}
 */
var possibleBipartition = function(n, dislikes) {
    
};
```

### TypeScript

```typescript
function possibleBipartition(n: number, dislikes: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $dislikes
     * @return Boolean
     */
    function possibleBipartition($n, $dislikes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func possibleBipartition(_ n: Int, _ dislikes: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun possibleBipartition(n: Int, dislikes: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool possibleBipartition(int n, List<List<int>> dislikes) {
    
  }
}
```

### Go

```golang
func possibleBipartition(n int, dislikes [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} dislikes
# @return {Boolean}
def possible_bipartition(n, dislikes)
    
end
```

### Scala

```scala
object Solution {
    def possibleBipartition(n: Int, dislikes: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn possible_bipartition(n: i32, dislikes: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (possible-bipartition n dislikes)
  (-> exact-integer? (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec possible_bipartition(N :: integer(), Dislikes :: [[integer()]]) -> boolean().
possible_bipartition(N, Dislikes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec possible_bipartition(n :: integer, dislikes :: [[integer]]) :: boolean
  def possible_bipartition(n, dislikes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func possibleBipartition(n: Int64, dislikes: Array<Array<Int64>>): Bool {

    }
}
```

