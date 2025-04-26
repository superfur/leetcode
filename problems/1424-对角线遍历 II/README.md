# 1424. 对角线遍历 II

## 题目描述

<p>给你一个列表&nbsp;<code>nums</code>&nbsp;，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回&nbsp;<code>nums</code>&nbsp;中对角线上的整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/23/sample_1_1784.png" style="height: 143px; width: 158px;"></strong></p>

<pre><strong>输入：</strong>nums = [[1,2,3],[4,5,6],[7,8,9]]
<strong>输出：</strong>[1,4,2,7,5,3,8,6,9]
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/23/sample_2_1784.png" style="height: 177px; width: 230px;"></strong></p>

<pre><strong>输入：</strong>nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
<strong>输出：</strong>[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
<strong>输出：</strong>[1,4,2,5,3,8,6,9,7,10,11]
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>nums = [[1,2,3,4,5,6]]
<strong>输出：</strong>[1,2,3,4,5,6]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= nums[i].length &lt;=&nbsp;10^5</code></li>
	<li><code>1 &lt;= nums[i][j] &lt;= 10^9</code></li>
	<li><code>nums</code>&nbsp;中最多有&nbsp;<code>10^5</code>&nbsp;个数字。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序
- 堆（优先队列）

## 提示

1. Notice that numbers with equal sums of row and column indexes belong to the same diagonal.
2. Store them in tuples (sum, row, val), sort them, and then regroup the answer.

## 示例

```
[[1,2,3],[4,5,6],[7,8,9]]
[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDiagonalOrder(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindDiagonalOrder(IList<IList<int>> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var findDiagonalOrder = function(nums) {
    
};
```

### TypeScript

```typescript
function findDiagonalOrder(nums: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer[]
     */
    function findDiagonalOrder($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDiagonalOrder(_ nums: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDiagonalOrder(nums: List<List<Int>>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findDiagonalOrder(List<List<int>> nums) {
    
  }
}
```

### Go

```golang
func findDiagonalOrder(nums [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums
# @return {Integer[]}
def find_diagonal_order(nums)
    
end
```

### Scala

```scala
object Solution {
    def findDiagonalOrder(nums: List[List[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_diagonal_order(nums: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-diagonal-order nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_diagonal_order(Nums :: [[integer()]]) -> [integer()].
find_diagonal_order(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_diagonal_order(nums :: [[integer]]) :: [integer]
  def find_diagonal_order(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDiagonalOrder(nums: ArrayList<ArrayList<Int64>>): Array<Int64> {

    }
}
```

