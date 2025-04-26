# 1253. 重构 2 行二进制矩阵

## 题目描述

<p>给你一个&nbsp;<code>2</code>&nbsp;行 <code>n</code> 列的二进制数组：</p>

<ul>
	<li>矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是&nbsp;<code>0</code>&nbsp;就是&nbsp;<code>1</code>。</li>
	<li>第 <code>0</code> 行的元素之和为&nbsp;<code>upper</code>。</li>
	<li>第 <code>1</code> 行的元素之和为 <code>lower</code>。</li>
	<li>第 <code>i</code> 列（从 <code>0</code> 开始编号）的元素之和为&nbsp;<code>colsum[i]</code>，<code>colsum</code>&nbsp;是一个长度为&nbsp;<code>n</code>&nbsp;的整数数组。</li>
</ul>

<p>你需要利用&nbsp;<code>upper</code>，<code>lower</code>&nbsp;和&nbsp;<code>colsum</code>&nbsp;来重构这个矩阵，并以二维整数数组的形式返回它。</p>

<p>如果有多个不同的答案，那么任意一个都可以通过本题。</p>

<p>如果不存在符合要求的答案，就请返回一个空的二维数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>upper = 2, lower = 1, colsum = [1,1,1]
<strong>输出：</strong>[[1,1,0],[0,0,1]]
<strong>解释：</strong>[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>upper = 2, lower = 3, colsum = [2,2,1,1]
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
<strong>输出：</strong>[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= colsum.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= upper, lower &lt;= colsum.length</code></li>
	<li><code>0 &lt;= colsum[i] &lt;= 2</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 矩阵

## 提示

1. You cannot do anything about colsum[i] = 2 case or colsum[i] = 0 case. Then you put colsum[i] = 1 case to the upper row until upper has reached. Then put the rest into lower row.
2. Fill 0 and 2 first, then fill 1 in the upper row or lower row in turn but be careful about exhausting permitted 1s in each row.

## 示例

```
2
1
[1,1,1]
2
3
[2,2,1,1]
5
5
[2,1,2,0,1,0,1,2,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> reconstructMatrix(int upper, int lower, vector<int>& colsum) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> reconstructMatrix(int upper, int lower, int[] colsum) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** reconstructMatrix(int upper, int lower, int* colsum, int colsumSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> ReconstructMatrix(int upper, int lower, int[] colsum) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} upper
 * @param {number} lower
 * @param {number[]} colsum
 * @return {number[][]}
 */
var reconstructMatrix = function(upper, lower, colsum) {
    
};
```

### TypeScript

```typescript
function reconstructMatrix(upper: number, lower: number, colsum: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $upper
     * @param Integer $lower
     * @param Integer[] $colsum
     * @return Integer[][]
     */
    function reconstructMatrix($upper, $lower, $colsum) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reconstructMatrix(_ upper: Int, _ lower: Int, _ colsum: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reconstructMatrix(upper: Int, lower: Int, colsum: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> reconstructMatrix(int upper, int lower, List<int> colsum) {
    
  }
}
```

### Go

```golang
func reconstructMatrix(upper int, lower int, colsum []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} upper
# @param {Integer} lower
# @param {Integer[]} colsum
# @return {Integer[][]}
def reconstruct_matrix(upper, lower, colsum)
    
end
```

### Scala

```scala
object Solution {
    def reconstructMatrix(upper: Int, lower: Int, colsum: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reconstruct_matrix(upper: i32, lower: i32, colsum: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (reconstruct-matrix upper lower colsum)
  (-> exact-integer? exact-integer? (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec reconstruct_matrix(Upper :: integer(), Lower :: integer(), Colsum :: [integer()]) -> [[integer()]].
reconstruct_matrix(Upper, Lower, Colsum) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reconstruct_matrix(upper :: integer, lower :: integer, colsum :: [integer]) :: [[integer]]
  def reconstruct_matrix(upper, lower, colsum) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reconstructMatrix(upper: Int64, lower: Int64, colsum: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

