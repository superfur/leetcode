# 面试题 16.24. 数对和

## 题目描述

<p>设计一个算法，找出数组中两数之和为指定值的所有整数对。一个数只能属于一个数对。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,6,5], target = 11
<strong>输出：</strong>[[5,6]]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,6,5,6], target = 11
<strong>输出：</strong>[[5,6],[5,6]]</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length &lt;= 100000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i], target &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 计数
- 排序

## 提示

1. 从蛮力解法开始。运行复杂度是什么？解决这个问题的最佳时间是什么？
2. 我们可以用散列表使它更快吗?
3. 如果数组有序呢？
4. 如果我们对数组进行排序，那么就可以对数字进行重复的二进制搜索。如果数组是有序的呢？我们能否在O(N)时间和O(1)空间中求解这个问题？

## 示例

```
[5]
1
[]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> pairSums(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> pairSums(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def pairSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def pairSums(self, nums: List[int], target: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** pairSums(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> PairSums(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var pairSums = function(nums, target) {
    
};
```

### TypeScript

```typescript
function pairSums(nums: number[], target: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer[][]
     */
    function pairSums($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func pairSums(_ nums: [Int], _ target: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun pairSums(nums: IntArray, target: Int): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> pairSums(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func pairSums(nums []int, target int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[][]}
def pair_sums(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def pairSums(nums: Array[Int], target: Int): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn pair_sums(nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (pair-sums nums target)
  (-> (listof exact-integer?) exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec pair_sums(Nums :: [integer()], Target :: integer()) -> [[integer()]].
pair_sums(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec pair_sums(nums :: [integer], target :: integer) :: [[integer]]
  def pair_sums(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func pairSums(nums: Array<Int64>, target: Int64): ArrayList<ArrayList<Int64>> {

    }
}
```

