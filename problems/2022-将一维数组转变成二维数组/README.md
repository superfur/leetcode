# 2022. 将一维数组转变成二维数组

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的一维整数数组&nbsp;<code>original</code>&nbsp;和两个整数&nbsp;<code>m</code>&nbsp;和&nbsp;&nbsp;<code>n</code>&nbsp;。你需要使用&nbsp;<code>original</code>&nbsp;中&nbsp;<strong>所有</strong>&nbsp;元素创建一个&nbsp;<code>m</code>&nbsp;行&nbsp;<code>n</code>&nbsp;列的二维数组。</p>

<p><code>original</code>&nbsp;中下标从 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;（都 <strong>包含</strong> ）的元素构成二维数组的第一行，下标从 <code>n</code>&nbsp;到 <code>2 * n - 1</code>&nbsp;（都 <strong>包含</strong>&nbsp;）的元素构成二维数组的第二行，依此类推。</p>

<p>请你根据上述过程返回一个<em>&nbsp;</em><code>m x n</code>&nbsp;的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img src="https://assets.leetcode.com/uploads/2021/08/26/image-20210826114243-1.png" style="width: 500px; height: 174px;">
<pre><b>输入：</b>original = [1,2,3,4], m = 2, n = 2
<b>输出：</b>[[1,2],[3,4]]
<strong>解释：
</strong>构造出的二维数组应该包含 2 行 2 列。
original 中第一个 n=2 的部分为 [1,2] ，构成二维数组的第一行。
original 中第二个 n=2 的部分为 [3,4] ，构成二维数组的第二行。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>original = [1,2,3], m = 1, n = 3
<b>输出：</b>[[1,2,3]]
<b>解释：</b>
构造出的二维数组应该包含 1 行 3 列。
将 original 中所有三个元素放入第一行中，构成要求的二维数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>original = [1,2], m = 1, n = 1
<b>输出：</b>[]
<strong>解释：
</strong>original 中有 2 个元素。
无法将 2 个元素放入到一个 1x1 的二维数组中，所以返回一个空的二维数组。
</pre>

<p><strong>示例 4：</strong></p>

<pre><b>输入：</b>original = [3], m = 1, n = 2
<b>输出：</b>[]
<strong>解释：</strong>
original 中只有 1 个元素。
无法将 1 个元素放满一个 1x2 的二维数组，所以返回一个空的二维数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= original.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= original[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m, n &lt;= 4 * 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 矩阵
- 模拟

## 提示

1. When is it possible to convert original into a 2D array and when is it impossible?
2. It is possible if and only if m * n == original.length
3. If it is possible to convert original to a 2D array, keep an index i such that original[i] is the next element to add to the 2D array.

## 示例

```
[1,2,3,4]
2
2
[1,2,3]
1
3
[1,2]
1
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] Construct2DArray(int[] original, int m, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    
};
```

### TypeScript

```typescript
function construct2DArray(original: number[], m: number, n: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $original
     * @param Integer $m
     * @param Integer $n
     * @return Integer[][]
     */
    function construct2DArray($original, $m, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func construct2DArray(_ original: [Int], _ m: Int, _ n: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun construct2DArray(original: IntArray, m: Int, n: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> construct2DArray(List<int> original, int m, int n) {
    
  }
}
```

### Go

```golang
func construct2DArray(original []int, m int, n int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} original
# @param {Integer} m
# @param {Integer} n
# @return {Integer[][]}
def construct2_d_array(original, m, n)
    
end
```

### Scala

```scala
object Solution {
    def construct2DArray(original: Array[Int], m: Int, n: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (construct2-d-array original m n)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec construct2_d_array(Original :: [integer()], M :: integer(), N :: integer()) -> [[integer()]].
construct2_d_array(Original, M, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec construct2_d_array(original :: [integer], m :: integer, n :: integer) :: [[integer]]
  def construct2_d_array(original, m, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func construct2DArray(original: Array<Int64>, m: Int64, n: Int64): Array<Array<Int64>> {

    }
}
```

