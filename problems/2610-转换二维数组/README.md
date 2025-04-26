# 2610. 转换二维数组

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。请你创建一个满足以下条件的二维数组：</p>

<ul>
	<li>二维数组应该 <strong>只</strong> 包含数组 <code>nums</code> 中的元素。</li>
	<li>二维数组中的每一行都包含 <strong>不同</strong> 的整数。</li>
	<li>二维数组的行数应尽可能 <strong>少</strong> 。</li>
</ul>

<p>返回结果数组。如果存在多种答案，则返回其中任何一种。</p>

<p>请注意，二维数组的每一行上可以存在不同数量的元素。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,4,1,2,3,1]
<strong>输出：</strong>[[1,3,4,2],[1,3],[1]]
<strong>解释：</strong>根据题目要求可以创建包含以下几行元素的二维数组：
- 1,3,4,2
- 1,3
- 1
nums 中的所有元素都有用到，并且每一行都由不同的整数组成，所以这是一个符合题目要求的答案。
可以证明无法创建少于三行且符合题目要求的二维数组。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>[[4,3,2,1]]
<strong>解释：</strong>nums 中的所有元素都不同，所以我们可以将其全部保存在二维数组中的第一行。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 提示

1. Process the elements in the array one by one in any order and only create a new row in the matrix when we cannot put it into the existing rows
2. We can simply iterate over the existing rows of the matrix to see if we can place each element.

## 示例

```
[1,3,4,1,2,3,1]
[2,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> findMatrix(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findMatrix(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> FindMatrix(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function(nums) {
    
};
```

### TypeScript

```typescript
function findMatrix(nums: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function findMatrix($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMatrix(_ nums: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMatrix(nums: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> findMatrix(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMatrix(nums []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def find_matrix(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMatrix(nums: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_matrix(nums: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (find-matrix nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec find_matrix(Nums :: [integer()]) -> [[integer()]].
find_matrix(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_matrix(nums :: [integer]) :: [[integer]]
  def find_matrix(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMatrix(nums: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

