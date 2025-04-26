# 90. 子集 II

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，其中可能包含重复元素，请你返回该数组所有可能的 <span data-keyword="subset">子集</span>（幂集）。</p>

<p>解集 <strong>不能</strong> 包含重复的子集。返回的解集中，子集可以按 <strong>任意顺序</strong> 排列。</p>

<div class="original__bRMd">
<div>
<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2]
<strong>输出：</strong>[[],[1],[1,2],[1,2,2],[2],[2,2]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>[[],[0]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>
</div>
</div>


## 难度

Medium

## 标签

- 位运算
- 数组
- 回溯

## 示例

```
[1,2,2]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** subsetsWithDup(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> SubsetsWithDup(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsetsWithDup = function(nums) {
    
};
```

### TypeScript

```typescript
function subsetsWithDup(nums: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function subsetsWithDup($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subsetsWithDup(_ nums: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> subsetsWithDup(List<int> nums) {
    
  }
}
```

### Go

```golang
func subsetsWithDup(nums []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def subsets_with_dup(nums)
    
end
```

### Scala

```scala
object Solution {
    def subsetsWithDup(nums: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subsets_with_dup(nums: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (subsets-with-dup nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec subsets_with_dup(Nums :: [integer()]) -> [[integer()]].
subsets_with_dup(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subsets_with_dup(nums :: [integer]) :: [[integer]]
  def subsets_with_dup(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subsetsWithDup(nums: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

