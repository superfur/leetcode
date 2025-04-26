# 47. 全排列 II

## 题目描述

<p>给定一个可包含重复数字的序列 <code>nums</code> ，<em><strong>按任意顺序</strong></em> 返回所有不重复的全排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2]
<strong>输出：</strong>
[[1,1,2],
 [1,2,1],
 [2,1,1]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 8</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 回溯
- 排序

## 示例

```
[1,1,2]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** permuteUnique(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    
};
```

### TypeScript

```typescript
function permuteUnique(nums: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[][]
     */
    function permuteUnique($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun permuteUnique(nums: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> permuteUnique(List<int> nums) {
    
  }
}
```

### Go

```golang
func permuteUnique(nums []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[][]}
def permute_unique(nums)
    
end
```

### Scala

```scala
object Solution {
    def permuteUnique(nums: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn permute_unique(nums: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (permute-unique nums)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec permute_unique(Nums :: [integer()]) -> [[integer()]].
permute_unique(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec permute_unique(nums :: [integer]) :: [[integer]]
  def permute_unique(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func permuteUnique(nums: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

