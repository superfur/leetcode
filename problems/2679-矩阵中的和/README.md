# 2679. 矩阵中的和

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>nums</code>&nbsp;。一开始你的分数为&nbsp;<code>0</code>&nbsp;。你需要执行以下操作直到矩阵变为空：</p>

<ol>
	<li>矩阵中每一行选取最大的一个数，并删除它。如果一行中有多个最大的数，选择任意一个并删除。</li>
	<li>在步骤 1 删除的所有数字中找到最大的一个数字，将它添加到你的 <strong>分数</strong>&nbsp;中。</li>
</ol>

<p>请你返回最后的 <strong>分数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
<b>输出：</b>15
<b>解释：</b>第一步操作中，我们删除 7 ，6 ，6 和 3 ，将分数增加 7 。下一步操作中，删除 2 ，4 ，5 和 2 ，将分数增加 5 。最后删除 1 ，2 ，3 和 1 ，将分数增加 3 。所以总得分为 7 + 5 + 3 = 15 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [[1]]
<b>输出：</b>1
<b>解释：</b>我们删除 1 并将分数增加 1 ，所以返回 1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 300</code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 500</code></li>
	<li><code>0 &lt;= nums[i][j] &lt;= 10<sup>3</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 矩阵
- 排序
- 模拟
- 堆（优先队列）

## 提示

1. Sort the numbers in each row in decreasing order.
2. The answer is the summation of the max number in every column after sorting the rows.

## 示例

```
[[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
[[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int matrixSum(vector<vector<int>>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int matrixSum(int[][] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        
```

### C

```c
int matrixSum(int** nums, int numsSize, int* numsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MatrixSum(int[][] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums
 * @return {number}
 */
var matrixSum = function(nums) {
    
};
```

### TypeScript

```typescript
function matrixSum(nums: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer
     */
    function matrixSum($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func matrixSum(_ nums: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun matrixSum(nums: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int matrixSum(List<List<int>> nums) {
    
  }
}
```

### Go

```golang
func matrixSum(nums [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums
# @return {Integer}
def matrix_sum(nums)
    
end
```

### Scala

```scala
object Solution {
    def matrixSum(nums: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn matrix_sum(nums: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (matrix-sum nums)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec matrix_sum(Nums :: [[integer()]]) -> integer().
matrix_sum(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec matrix_sum(nums :: [[integer]]) :: integer
  def matrix_sum(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func matrixSum(nums: Array<Array<Int64>>): Int64 {

    }
}
```

