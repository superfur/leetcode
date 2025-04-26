# 2215. 找出两数组的不同

## 题目描述

<p>给你两个下标从 <code>0</code> 开始的整数数组 <code>nums1</code> 和 <code>nums2</code> ，请你返回一个长度为 <code>2</code> 的列表 <code>answer</code> ，其中：</p>

<ul>
	<li><code>answer[0]</code> 是 <code>nums1</code> 中所有<strong> 不 </strong>存在于 <code>nums2</code> 中的 <strong>不同</strong> 整数组成的列表。</li>
	<li><code>answer[1]</code> 是 <code>nums2</code> 中所有<strong> 不 </strong>存在于 <code>nums1</code> 中的 <strong>不同</strong> 整数组成的列表。</li>
</ul>

<p><strong>注意：</strong>列表中的整数可以按 <strong>任意</strong> 顺序返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3], nums2 = [2,4,6]
<strong>输出：</strong>[[1,3],[4,6]]
<strong>解释：
</strong>对于 nums1 ，nums1[1] = 2 出现在 nums2 中下标 0 处，然而 nums1[0] = 1 和 nums1[2] = 3 没有出现在 nums2 中。因此，answer[0] = [1,3]。
对于 nums2 ，nums2[0] = 2 出现在 nums1 中下标 1 处，然而 nums2[1] = 4 和 nums2[2] = 6 没有出现在 nums2 中。因此，answer[1] = [4,6]。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,3,3], nums2 = [1,1,2,2]
<strong>输出：</strong>[[3],[]]
<strong>解释：
</strong>对于 nums1 ，nums1[2] 和 nums1[3] 没有出现在 nums2 中。由于 nums1[2] == nums1[3] ，二者的值只需要在 answer[0] 中出现一次，故 answer[0] = [3]。
nums2 中的每个整数都在 nums1 中出现，因此，answer[1] = [] 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>-1000 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. For each integer in nums1, check if it exists in nums2.
2. Do the same for each integer in nums2.

## 示例

```
[1,2,3]
[2,4,6]
[1,2,3,3]
[1,1,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findDifference(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[][]}
 */
var findDifference = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function findDifference(nums1: number[], nums2: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer[][]
     */
    function findDifference($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDifference(_ nums1: [Int], _ nums2: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDifference(nums1: IntArray, nums2: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> findDifference(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func findDifference(nums1 []int, nums2 []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[][]}
def find_difference(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def findDifference(nums1: Array[Int], nums2: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_difference(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (find-difference nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec find_difference(Nums1 :: [integer()], Nums2 :: [integer()]) -> [[integer()]].
find_difference(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_difference(nums1 :: [integer], nums2 :: [integer]) :: [[integer]]
  def find_difference(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDifference(nums1: Array<Int64>, nums2: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

