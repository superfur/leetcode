# 2905. 找出满足差值条件的下标 II

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>nums</code> ，以及整数 <code>indexDifference</code> 和整数 <code>valueDifference</code> 。</p>

<p>你的任务是从范围 <code>[0, n - 1]</code> 内找出&nbsp; <strong>2</strong> 个满足下述所有条件的下标 <code>i</code> 和 <code>j</code> ：</p>

<ul>
	<li><code>abs(i - j) &gt;= indexDifference</code> 且</li>
	<li><code>abs(nums[i] - nums[j]) &gt;= valueDifference</code></li>
</ul>

<p>返回整数数组 <code>answer</code>。如果存在满足题目要求的两个下标，则 <code>answer = [i, j]</code> ；否则，<code>answer = [-1, -1]</code> 。如果存在多组可供选择的下标对，只需要返回其中任意一组即可。</p>

<p><strong>注意：</strong><code>i</code> 和 <code>j</code> 可能 <strong>相等</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,1,4,1], indexDifference = 2, valueDifference = 4
<strong>输出：</strong>[0,3]
<strong>解释：</strong>在示例中，可以选择 i = 0 和 j = 3 。
abs(0 - 3) &gt;= 2 且 abs(nums[0] - nums[3]) &gt;= 4 。
因此，[0,3] 是一个符合题目要求的答案。
[3,0] 也是符合题目要求的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1], indexDifference = 0, valueDifference = 0
<strong>输出：</strong>[0,0]
<strong>解释：</strong>
在示例中，可以选择 i = 0 和 j = 0 。 
abs(0 - 0) &gt;= 0 且 abs(nums[0] - nums[0]) &gt;= 0 。 
因此，[0,0] 是一个符合题目要求的答案。 
[0,1]、[1,0] 和 [1,1] 也是符合题目要求的答案。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], indexDifference = 2, valueDifference = 4
<strong>输出：</strong>[-1,-1]
<strong>解释：</strong>在示例中，可以证明无法找出 2 个满足所有条件的下标。
因此，返回 [-1,-1] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= indexDifference &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= valueDifference &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针

## 提示

1. For each index <code>i >= indexDifference</code>, keep the indices <code>j<sub>1</sub></code> and <code>j<sub>2</sub></code> in the range <code>[0, i - indexDifference]</code> such that <code>nums[j<sub>1</sub>]</code> and <code>nums[j<sub>2</sub>]</code> are the minimum and maximum values in the index range.
2. Check if <code>abs(nums[i] - nums[j<sub>1</sub>]) >= valueDifference</code> or <code>abs(nums[i] - nums[j<sub>2</sub>]) >= valueDifference</code>.
3. <code>j<sub>1</sub></code> and <code>j<sub>2</sub></code> can be updated dynamically, or they can be pre-computed since they are just prefix minimum and maximum.

## 示例

```
[5,1,4,1]
2
4
[2,1]
0
0
[1,2,3]
2
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findIndices(vector<int>& nums, int indexDifference, int valueDifference) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findIndices(int[] nums, int indexDifference, int valueDifference) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findIndices(int* nums, int numsSize, int indexDifference, int valueDifference, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindIndices(int[] nums, int indexDifference, int valueDifference) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} indexDifference
 * @param {number} valueDifference
 * @return {number[]}
 */
var findIndices = function(nums, indexDifference, valueDifference) {
    
};
```

### TypeScript

```typescript
function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $indexDifference
     * @param Integer $valueDifference
     * @return Integer[]
     */
    function findIndices($nums, $indexDifference, $valueDifference) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findIndices(_ nums: [Int], _ indexDifference: Int, _ valueDifference: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findIndices(nums: IntArray, indexDifference: Int, valueDifference: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findIndices(List<int> nums, int indexDifference, int valueDifference) {
    
  }
}
```

### Go

```golang
func findIndices(nums []int, indexDifference int, valueDifference int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} index_difference
# @param {Integer} value_difference
# @return {Integer[]}
def find_indices(nums, index_difference, value_difference)
    
end
```

### Scala

```scala
object Solution {
    def findIndices(nums: Array[Int], indexDifference: Int, valueDifference: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_indices(nums: Vec<i32>, index_difference: i32, value_difference: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-indices nums indexDifference valueDifference)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_indices(Nums :: [integer()], IndexDifference :: integer(), ValueDifference :: integer()) -> [integer()].
find_indices(Nums, IndexDifference, ValueDifference) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_indices(nums :: [integer], index_difference :: integer, value_difference :: integer) :: [integer]
  def find_indices(nums, index_difference, value_difference) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findIndices(nums: Array<Int64>, indexDifference: Int64, valueDifference: Int64): Array<Int64> {

    }
}
```

