# 2545. 根据第 K 场考试的分数排序

## 题目描述

<p>班里有 <code>m</code> 位学生，共计划组织 <code>n</code> 场考试。给你一个下标从 <strong>0</strong> 开始、大小为 <code>m x n</code> 的整数矩阵 <code>score</code> ，其中每一行对应一位学生，而 <code>score[i][j]</code> 表示第 <code>i</code> 位学生在第 <code>j</code> 场考试取得的分数。矩阵 <code>score</code> 包含的整数&nbsp;<strong>互不相同</strong>&nbsp;。</p>

<p>另给你一个整数 <code>k</code> 。请你按第 <code>k</code> 场考试分数从高到低完成对这些学生（矩阵中的行）的排序。</p>

<p>返回排序后的矩阵。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/30/example1.png" style="width: 600px; height: 136px;" /></p>

<pre>
<strong>输入：</strong>score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], k = 2
<strong>输出：</strong>[[7,5,11,2],[10,6,9,1],[4,8,3,15]]
<strong>解释：</strong>在上图中，S 表示学生，E 表示考试。
- 下标为 1 的学生在第 2 场考试取得的分数为 11 ，这是考试的最高分，所以 TA 需要排在第一。
- 下标为 0 的学生在第 2 场考试取得的分数为 9 ，这是考试的第二高分，所以 TA 需要排在第二。
- 下标为 2 的学生在第 2 场考试取得的分数为 3 ，这是考试的最低分，所以 TA 需要排在第三。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/30/example2.png" style="width: 486px; height: 121px;" /></p>

<pre>
<strong>输入：</strong>score = [[3,4],[5,6]], k = 0
<strong>输出：</strong>[[5,6],[3,4]]
<strong>解释：</strong>在上图中，S 表示学生，E 表示考试。
- 下标为 1 的学生在第 0 场考试取得的分数为 5 ，这是考试的最高分，所以 TA 需要排在第一。
- 下标为 0 的学生在第 0 场考试取得的分数为 3 ，这是考试的最低分，所以 TA 需要排在第二。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == score.length</code></li>
	<li><code>n == score[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 250</code></li>
	<li><code>1 &lt;= score[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>score</code> 由 <strong>不同</strong> 的整数组成</li>
	<li><code>0 &lt;= k &lt; n</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 排序

## 提示

1. Find the row with the highest score in the kth exam and swap it with the first row.
2. After fixing the first row, perform the same operation for the rest of the rows, and the matrix's rows will get sorted one by one.

## 示例

```
[[10,6,9,1],[7,5,11,2],[4,8,3,15]]
2
[[3,4],[5,6]]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> sortTheStudents(vector<vector<int>>& score, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] sortTheStudents(int[][] score, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** sortTheStudents(int** score, int scoreSize, int* scoreColSize, int k, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] SortTheStudents(int[][] score, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} score
 * @param {number} k
 * @return {number[][]}
 */
var sortTheStudents = function(score, k) {
    
};
```

### TypeScript

```typescript
function sortTheStudents(score: number[][], k: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $score
     * @param Integer $k
     * @return Integer[][]
     */
    function sortTheStudents($score, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sortTheStudents(_ score: [[Int]], _ k: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sortTheStudents(score: Array<IntArray>, k: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> sortTheStudents(List<List<int>> score, int k) {
    
  }
}
```

### Go

```golang
func sortTheStudents(score [][]int, k int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} score
# @param {Integer} k
# @return {Integer[][]}
def sort_the_students(score, k)
    
end
```

### Scala

```scala
object Solution {
    def sortTheStudents(score: Array[Array[Int]], k: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sort_the_students(score: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (sort-the-students score k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec sort_the_students(Score :: [[integer()]], K :: integer()) -> [[integer()]].
sort_the_students(Score, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sort_the_students(score :: [[integer]], k :: integer) :: [[integer]]
  def sort_the_students(score, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sortTheStudents(score: Array<Array<Int64>>, k: Int64): Array<Array<Int64>> {

    }
}
```

