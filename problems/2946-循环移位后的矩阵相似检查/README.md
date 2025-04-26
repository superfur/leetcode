# 2946. 循环移位后的矩阵相似检查

## 题目描述

<p>给你一个<strong>下标从 0 开始</strong>且大小为 <code>m x n</code> 的整数矩阵 <code>mat</code> 和一个整数 <code>k</code> 。请你将矩阵中的<strong> 奇数</strong> 行循环 <strong>右</strong> 移 <code>k</code> 次，<strong>偶数</strong> 行循环 <strong>左</strong> 移 <code>k</code> 次。</p>

<p>如果初始矩阵和最终矩阵完全相同，则返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
<strong>输出：</strong>true
<strong>解释：</strong>
<img alt="" src="https://assets.leetcode.com/uploads/2023/10/29/similarmatrix.png" style="width: 500px; height: 117px;" />

初始矩阵如图一所示。
图二表示对奇数行右移一次且对偶数行左移一次后的矩阵状态。
图三是经过两次循环移位后的最终矩阵状态，与初始矩阵相同。
因此，返回 true 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[2,2],[2,2]], k = 3
<strong>输出：</strong>true
<strong>解释：</strong>由于矩阵中的所有值都相等，即使进行循环移位，矩阵仍然保持不变。因此，返回 true 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>mat = [[1,2]], k = 1
<strong>输出：</strong>false
<strong>解释：</strong>循环移位一次后，mat = [[2,1]]，与初始矩阵不相等。因此，返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= mat.length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i].length &lt;= 25</code></li>
	<li><code>1 &lt;= mat[i][j] &lt;= 25</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 矩阵
- 模拟

## 提示

1. You can reduce <code>k</code> shifts to <code>(k % n)</code> shifts as after <code>n</code> shifts the matrix will become similar to the initial matrix.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
4
[[1,2,1,2],[5,5,5,5],[6,3,6,3]]
2
[[2,2],[2,2]]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool areSimilar(vector<vector<int>>& mat, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean areSimilar(int[][] mat, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def areSimilar(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
```

### C

```c
bool areSimilar(int** mat, int matSize, int* matColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool AreSimilar(int[][] mat, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {boolean}
 */
var areSimilar = function(mat, k) {
    
};
```

### TypeScript

```typescript
function areSimilar(mat: number[][], k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Boolean
     */
    function areSimilar($mat, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func areSimilar(_ mat: [[Int]], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun areSimilar(mat: Array<IntArray>, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool areSimilar(List<List<int>> mat, int k) {
    
  }
}
```

### Go

```golang
func areSimilar(mat [][]int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} k
# @return {Boolean}
def are_similar(mat, k)
    
end
```

### Scala

```scala
object Solution {
    def areSimilar(mat: Array[Array[Int]], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn are_similar(mat: Vec<Vec<i32>>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (are-similar mat k)
  (-> (listof (listof exact-integer?)) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec are_similar(Mat :: [[integer()]], K :: integer()) -> boolean().
are_similar(Mat, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec are_similar(mat :: [[integer]], k :: integer) :: boolean
  def are_similar(mat, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func areSimilar(mat: Array<Array<Int64>>, k: Int64): Bool {

    }
}
```

