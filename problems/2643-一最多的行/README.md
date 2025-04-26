# 2643. 一最多的行

## 题目描述

<p>给你一个大小为 <code>m x n</code> 的二进制矩阵 <code>mat</code> ，请你找出包含最多 <strong>1</strong> 的行的下标（从 <strong>0</strong> 开始）以及这一行中 <strong>1</strong> 的数目。</p>

<p>如果有多行包含最多的 1 ，只需要选择 <strong>行下标最小</strong> 的那一行。</p>

<p>返回一个由行下标和该行中 1 的数量组成的数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>mat = [[0,1],[1,0]]
<strong>输出：</strong>[0,1]
<strong>解释：</strong>两行中 1 的数量相同。所以返回下标最小的行，下标为 0 。该行 1 的数量为 1 。所以，答案为 [0,1] 。 
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>mat = [[0,0,0],[0,1,1]]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>下标为 1 的行中 1 的数量最多<code>。</code>该行 1 的数量<code>为 2 。所以，答案为</code> [1,2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>mat = [[0,0],[1,1],[0,0]]
<strong>输出：</strong>[1,2]
<strong>解释：</strong>下标为 1 的行中 1 的数量最多。该行 1 的数量<code>为 2 。所以，答案为</code> [1,2] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == mat.length</code>&nbsp;</li>
	<li><code>n == mat[i].length</code>&nbsp;</li>
	<li><code>1 &lt;= m, n &lt;= 100</code>&nbsp;</li>
	<li><code>mat[i][j]</code> 为 <code>0</code> 或 <code>1</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵

## 提示

1. Iterate through each row and keep the count of ones.

## 示例

```
[[0,1],[1,0]]
[[0,0,0],[0,1,1]]
[[0,0],[1,1],[0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> rowAndMaximumOnes(vector<vector<int>>& mat) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] rowAndMaximumOnes(int[][] mat) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rowAndMaximumOnes(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rowAndMaximumOnes(int** mat, int matSize, int* matColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RowAndMaximumOnes(int[][] mat) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var rowAndMaximumOnes = function(mat) {
    
};
```

### TypeScript

```typescript
function rowAndMaximumOnes(mat: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $mat
     * @return Integer[]
     */
    function rowAndMaximumOnes($mat) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rowAndMaximumOnes(_ mat: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rowAndMaximumOnes(mat: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> rowAndMaximumOnes(List<List<int>> mat) {
    
  }
}
```

### Go

```golang
func rowAndMaximumOnes(mat [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} mat
# @return {Integer[]}
def row_and_maximum_ones(mat)
    
end
```

### Scala

```scala
object Solution {
    def rowAndMaximumOnes(mat: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn row_and_maximum_ones(mat: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (row-and-maximum-ones mat)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec row_and_maximum_ones(Mat :: [[integer()]]) -> [integer()].
row_and_maximum_ones(Mat) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec row_and_maximum_ones(mat :: [[integer]]) :: [integer]
  def row_and_maximum_ones(mat) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rowAndMaximumOnes(mat: Array<Array<Int64>>): Array<Int64> {

    }
}
```

