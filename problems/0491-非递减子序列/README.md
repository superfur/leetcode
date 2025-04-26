# 491. 非递减子序列

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，找出并返回所有该数组中不同的递增子序列，递增子序列中 <strong>至少有两个元素</strong> 。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,6,7,7]
<strong>输出：</strong>[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,4,3,2,1]
<strong>输出：</strong>[[4,4]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 15</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表
- 回溯

## 示例

```
[4,6,7,7]
[4,4,3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> findSubsequences(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findSubsequences(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> FindSubsequences(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findSubsequences = function(nums) {
    
};
```

### TypeScript

```typescript
function findSubsequences(nums: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function findSubsequences($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSubsequences(_ nums: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSubsequences(nums: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> findSubsequences(List<int> nums) {
    
  }
}
```

### Go

```golang
func findSubsequences(nums []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def find_subsequences(nums)
    
end
```

### Scala

```scala
object Solution {
    def findSubsequences(nums: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_subsequences(nums: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (find-subsequences nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec find_subsequences(Nums :: [integer()]) -> [[integer()]].
find_subsequences(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_subsequences(nums :: [integer]) :: [[integer]]
  def find_subsequences(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSubsequences(nums: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

