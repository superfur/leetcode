# 2248. 多个数组求交集

## 题目描述

<p>给你一个二维整数数组 <code>nums</code> ，其中 <code>nums[i]</code> 是由 <strong>不同</strong> 正整数组成的一个非空数组，按 <strong>升序排列</strong> 返回一个数组，数组中的每个元素在 <code>nums</code>&nbsp;<strong>所有数组</strong> 中都出现过。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [[<em><strong>3</strong></em>,1,2,<em><strong>4</strong></em>,5],[1,2,<em><strong>3</strong></em>,<em><strong>4</strong></em>],[<em><strong>3</strong></em>,<em><strong>4</strong></em>,5,6]]
<strong>输出：</strong>[3,4]
<strong>解释：</strong>
nums[0] = [<em><strong>3</strong></em>,1,2,<em><strong>4</strong></em>,5]，nums[1] = [1,2,<em><strong>3</strong></em>,<em><strong>4</strong></em>]，nums[2] = [<em><strong>3</strong></em>,<em><strong>4</strong></em>,5,6]，在 nums 中每个数组中都出现的数字是 3 和 4 ，所以返回 [3,4] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[4,5,6]]
<strong>输出：</strong>[]
<strong>解释：</strong>
不存在同时出现在 nums[0] 和 nums[1] 的整数，所以返回一个空列表 [] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= sum(nums[i].length) &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i][j] &lt;= 1000</code></li>
	<li><code>nums[i]</code> 中的所有值 <strong>互不相同</strong></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数
- 排序

## 提示

1. Keep a count of the number of times each integer occurs in nums.
2. Since all integers of nums[i] are distinct, if an integer is present in each array, its count will be equal to the total number of arrays.

## 示例

```
[[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
[[1,2,3],[4,5,6]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> intersection(vector<vector<int>>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> intersection(int[][] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> Intersection(int[][] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var intersection = function(nums) {
    
};
```

### TypeScript

```typescript
function intersection(nums: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer[]
     */
    function intersection($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func intersection(_ nums: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun intersection(nums: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> intersection(List<List<int>> nums) {
    
  }
}
```

### Go

```golang
func intersection(nums [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums
# @return {Integer[]}
def intersection(nums)
    
end
```

### Scala

```scala
object Solution {
    def intersection(nums: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (intersection nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec intersection(Nums :: [[integer()]]) -> [integer()].
intersection(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec intersection(nums :: [[integer]]) :: [integer]
  def intersection(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func intersection(nums: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

