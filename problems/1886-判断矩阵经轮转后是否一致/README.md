# 1886. 判断矩阵经轮转后是否一致

## 题目描述

<p>给你两个大小为 <code>n x n</code> 的二进制矩阵 <code>mat</code> 和 <code>target</code> 。现<strong> 以 90 度顺时针轮转 </strong>矩阵 <code>mat</code> 中的元素 <strong>若干次</strong> ，如果能够使 <code>mat</code> 与 <code>target</code> 一致，返回 <code>true</code> ；否则，返回<em> </em><code>false</code><em> 。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px;" />
<pre>
<strong>输入：</strong>mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong>输出：</strong>true
<strong>解释：</strong>顺时针轮转 90 度一次可以使 mat 和 target 一致。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px;" />
<pre>
<strong>输入：</strong>mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong>输出：</strong>false
<strong>解释：</strong>无法通过轮转矩阵中的元素使 equal 与 target 一致。
</pre>

<p><strong>示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px;" />
<pre>
<strong>输入：</strong>mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong>输出：</strong>true
<strong>解释：</strong>顺时针轮转 90 度两次可以使 mat 和 target 一致。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == mat.length == target.length</code></li>
	<li><code>n == mat[i].length == target[i].length</code></li>
	<li><code>1 <= n <= 10</code></li>
	<li><code>mat[i][j]</code> 和 <code>target[i][j]</code> 不是 <code>0</code> 就是 <code>1</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. What is the maximum number of rotations you have to check?
2. Is there a formula you can use to rotate a matrix 90 degrees?

## 示例

```
[[0,1],[1,0]]
[[1,0],[0,1]]
[[0,1],[1,1]]
[[1,0],[0,1]]
[[0,0,0],[0,1,0],[1,1,1]]
[[1,1,1],[0,1,0],[0,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool findRotation(vector<vector<int>>& mat, vector<vector<int>>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
```

### C

```c
bool findRotation(int** mat, int matSize, int* matColSize, int** target, int targetSize, int* targetColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool FindRotation(int[][] mat, int[][] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number[][]} target
 * @return {boolean}
 */
var findRotation = function(mat, target) {
    
};
```

### TypeScript

```typescript
function findRotation(mat: number[][], target: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer[][] $target
     * @return Boolean
     */
    function findRotation($mat, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findRotation(_ mat: [[Int]], _ target: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findRotation(mat: Array<IntArray>, target: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool findRotation(List<List<int>> mat, List<List<int>> target) {
    
  }
}
```

### Go

```golang
func findRotation(mat [][]int, target [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer[][]} target
# @return {Boolean}
def find_rotation(mat, target)
    
end
```

### Scala

```scala
object Solution {
    def findRotation(mat: Array[Array[Int]], target: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_rotation(mat: Vec<Vec<i32>>, target: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (find-rotation mat target)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec find_rotation(Mat :: [[integer()]], Target :: [[integer()]]) -> boolean().
find_rotation(Mat, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_rotation(mat :: [[integer]], target :: [[integer]]) :: boolean
  def find_rotation(mat, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findRotation(mat: Array<Array<Int64>>, target: Array<Array<Int64>>): Bool {

    }
}
```

