# 2570. 合并两个二维数组 - 求和法

## 题目描述

<p>给你两个 <strong>二维</strong> 整数数组 <code>nums1</code> 和 <code>nums2.</code></p>

<ul>
	<li><code>nums1[i] = [id<sub>i</sub>, val<sub>i</sub>]</code> 表示编号为 <code>id<sub>i</sub></code> 的数字对应的值等于 <code>val<sub>i</sub></code> 。</li>
	<li><code>nums2[i] = [id<sub>i</sub>, val<sub>i</sub>]</code>&nbsp;表示编号为 <code>id<sub>i</sub></code> 的数字对应的值等于 <code>val<sub>i</sub></code> 。</li>
</ul>

<p>每个数组都包含 <strong>互不相同</strong> 的 id ，并按 id 以 <strong>递增</strong> 顺序排列。</p>

<p>请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：</p>

<ul>
	<li>只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。</li>
	<li>每个 id 在结果数组中 <strong>只能出现一次</strong> ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则假定其对应的值等于 <code>0</code> 。</li>
</ul>

<p>返回结果数组。返回的数组需要按 id 以递增顺序排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
<strong>输出：</strong>[[1,6],[2,3],[3,2],[4,6]]
<strong>解释：</strong>结果数组中包含以下元素：
- id = 1 ，对应的值等于 2 + 4 = 6 。
- id = 2 ，对应的值等于 3 。
- id = 3 ，对应的值等于 2 。
- id = 4 ，对应的值等于5 + 1 = 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
<strong>输出：</strong>[[1,3],[2,4],[3,6],[4,3],[5,5]]
<strong>解释：</strong>不存在共同 id ，在结果数组中只需要包含每个 id 和其对应的值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 200</code></li>
	<li><code>nums1[i].length == nums2[j].length == 2</code></li>
	<li><code>1 &lt;= id<sub>i</sub>, val<sub>i</sub> &lt;= 1000</code></li>
	<li>数组中的 id 互不相同</li>
	<li>数据均按 id 以严格递增顺序排列</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 双指针

## 提示

1. Use a dictionary/hash map to keep track of the indices and their sum
values.

## 示例

```
[[1,2],[2,3],[4,5]]
[[1,4],[3,2],[4,1]]
[[2,4],[3,6],[5,5]]
[[1,3],[4,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> mergeArrays(vector<vector<int>>& nums1, vector<vector<int>>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** mergeArrays(int** nums1, int nums1Size, int* nums1ColSize, int** nums2, int nums2Size, int* nums2ColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] MergeArrays(int[][] nums1, int[][] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums1
 * @param {number[][]} nums2
 * @return {number[][]}
 */
var mergeArrays = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums1
     * @param Integer[][] $nums2
     * @return Integer[][]
     */
    function mergeArrays($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mergeArrays(_ nums1: [[Int]], _ nums2: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mergeArrays(nums1: Array<IntArray>, nums2: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> mergeArrays(List<List<int>> nums1, List<List<int>> nums2) {
    
  }
}
```

### Go

```golang
func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums1
# @param {Integer[][]} nums2
# @return {Integer[][]}
def merge_arrays(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def mergeArrays(nums1: Array[Array[Int]], nums2: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn merge_arrays(nums1: Vec<Vec<i32>>, nums2: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (merge-arrays nums1 nums2)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec merge_arrays(Nums1 :: [[integer()]], Nums2 :: [[integer()]]) -> [[integer()]].
merge_arrays(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec merge_arrays(nums1 :: [[integer]], nums2 :: [[integer]]) :: [[integer]]
  def merge_arrays(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mergeArrays(nums1: Array<Array<Int64>>, nums2: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

