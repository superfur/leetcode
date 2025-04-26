# 1337. 矩阵中战斗力最弱的 K 行

## 题目描述

<p>给你一个大小为 <code>m * n</code> 的矩阵 <code>mat</code>，矩阵由若干军人和平民组成，分别用 1 和 0 表示。</p>

<p>请你返回矩阵中战斗力最弱的 <code>k</code> 行的索引，按从最弱到最强排序。</p>

<p>如果第 <em><strong>i</strong></em> 行的军人数量少于第 <em><strong>j</strong></em> 行，或者两行军人数量相同但<em><strong> i</strong></em> 小于 <em><strong>j</strong></em>，那么我们认为第<em><strong> i </strong></em>行的战斗力比第<em><strong> j </strong></em>行弱。</p>

<p>军人 <strong>总是</strong> 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
<strong>输出：</strong>[2,0,3]
<strong>解释：</strong>
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
<strong>输出：</strong>[0,2]
<strong>解释：</strong> 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>2 <= n, m <= 100</code></li>
	<li><code>1 <= k <= m</code></li>
	<li><code>matrix[i][j]</code> 不是 0 就是 1</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 二分查找
- 矩阵
- 排序
- 堆（优先队列）

## 提示

1. Sort the matrix row indexes by the number of soldiers and then row indexes.

## 示例

```
[[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
3
[[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* kWeakestRows(int** mat, int matSize, int* matColSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @param {number} k
 * @return {number[]}
 */
var kWeakestRows = function(mat, k) {
    
};
```

### TypeScript

```typescript
function kWeakestRows(mat: number[][], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @param Integer $k
     * @return Integer[]
     */
    function kWeakestRows($mat, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kWeakestRows(_ mat: [[Int]], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kWeakestRows(mat: Array<IntArray>, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> kWeakestRows(List<List<int>> mat, int k) {
    
  }
}
```

### Go

```golang
func kWeakestRows(mat [][]int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @param {Integer} k
# @return {Integer[]}
def k_weakest_rows(mat, k)
    
end
```

### Scala

```scala
object Solution {
    def kWeakestRows(mat: Array[Array[Int]], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_weakest_rows(mat: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (k-weakest-rows mat k)
  (-> (listof (listof exact-integer?)) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec k_weakest_rows(Mat :: [[integer()]], K :: integer()) -> [integer()].
k_weakest_rows(Mat, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_weakest_rows(mat :: [[integer]], k :: integer) :: [integer]
  def k_weakest_rows(mat, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kWeakestRows(mat: Array<Array<Int64>>, k: Int64): Array<Int64> {

    }
}
```

