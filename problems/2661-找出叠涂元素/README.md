# 2661. 找出叠涂元素

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>arr</code> 和一个 <code>m x n</code> 的整数 <strong>矩阵</strong> <code>mat</code> 。<code>arr</code> 和 <code>mat</code> 都包含范围 <code>[1，m * n]</code> 内的 <strong>所有</strong> 整数。</p>

<p>从下标 <code>0</code> 开始遍历 <code>arr</code> 中的每个下标 <code>i</code> ，并将包含整数 <code>arr[i]</code> 的 <code>mat</code> 单元格涂色。</p>

<p>请你找出 <code>arr</code> 中第一个使得&nbsp;<code>mat</code> 的某一行或某一列都被涂色的元素，并返回其下标 <code>i</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="image explanation for example 1" src="https://assets.leetcode.com/uploads/2023/01/18/grid1.jpg" style="width: 321px; height: 81px;" />
<pre>
<strong>输入：</strong>arr = [1,3,4,2], mat = [[1,4],[2,3]]
<strong>输出：</strong>2
<strong>解释：</strong>遍历如上图所示，arr[2] 在矩阵中的第一行或第二列上都被涂色。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="image explanation for example 2" src="https://assets.leetcode.com/uploads/2023/01/18/grid2.jpg" style="width: 601px; height: 121px;" />
<pre>
<strong>输入：</strong>arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
<strong>输出：</strong>3
<strong>解释：</strong>遍历如上图所示，arr[3] 在矩阵中的第二列上都被涂色。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n = mat[i].length</code></li>
	<li><code>arr.length == m * n</code></li>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i], mat[r][c] &lt;= m * n</code></li>
	<li><code>arr</code> 中的所有整数 <strong>互不相同</strong></li>
	<li><code>mat</code> 中的所有整数 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 矩阵

## 提示

1. Can we use a frequency array?
2. Pre-process the positions of the values in the matrix.
3. Traverse the array and increment the corresponding row and column frequency using the pre-processed positions.
4. If the row frequency becomes equal to the number of columns, or vice-versa return the current index.

## 示例

```
[1,3,4,2]
[[1,4],[2,3]]
[2,8,7,4,1,3,5,6,9]
[[3,2,5],[1,4,6],[8,7,9]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int firstCompleteIndex(vector<int>& arr, vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int firstCompleteIndex(int[] arr, int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        """
        :type arr: List[int]
        :type mat: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
```

### C

```c
int firstCompleteIndex(int* arr, int arrSize, int** mat, int matSize, int* matColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FirstCompleteIndex(int[] arr, int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function(arr, mat) {
    
};
```

### TypeScript

```typescript
function firstCompleteIndex(arr: number[], mat: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $mat
     * @return Integer
     */
    function firstCompleteIndex($arr, $mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func firstCompleteIndex(_ arr: [Int], _ mat: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun firstCompleteIndex(arr: IntArray, mat: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int firstCompleteIndex(List<int> arr, List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func firstCompleteIndex(arr []int, mat [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer[][]} mat
# @return {Integer}
def first_complete_index(arr, mat)
    
end
```

### Scala

```scala
object Solution {
    def firstCompleteIndex(arr: Array[Int], mat: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn first_complete_index(arr: Vec<i32>, mat: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (first-complete-index arr mat)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec first_complete_index(Arr :: [integer()], Mat :: [[integer()]]) -> integer().
first_complete_index(Arr, Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec first_complete_index(arr :: [integer], mat :: [[integer]]) :: integer
  def first_complete_index(arr, mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func firstCompleteIndex(arr: Array<Int64>, mat: Array<Array<Int64>>): Int64 {

    }
}
```

