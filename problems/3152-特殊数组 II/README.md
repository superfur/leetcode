# 3152. 特殊数组 II

## 题目描述

<p>如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 <strong>特殊数组</strong> 。</p>

<p>你有一个整数数组 <code>nums</code> 和一个二维整数矩阵 <code>queries</code>，对于 <code>queries[i] = [from<sub>i</sub>, to<sub>i</sub>]</code>，请你帮助你检查 <span data-keyword="subarray">子数组</span> <code>nums[from<sub>i</sub>..to<sub>i</sub>]</code> 是不是一个 <strong>特殊数组 </strong>。</p>

<p>返回布尔数组 <code>answer</code>，如果 <code>nums[from<sub>i</sub>..to<sub>i</sub>]</code> 是特殊数组，则 <code>answer[i]</code> 为 <code>true</code> ，否则，<code>answer[i]</code> 为 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [3,4,1,2,6], queries = [[0,4]]</span></p>

<p><strong>输出：</strong><span class="example-io">[false]</span></p>

<p><strong>解释：</strong></p>

<p>子数组是 <code>[3,4,1,2,6]</code>。2 和 6 都是偶数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [4,3,1,6], queries = [[0,2],[2,3]]</span></p>

<p><strong>输出：</strong><span class="example-io">[false,true]</span></p>

<p><strong>解释：</strong></p>

<ol>
	<li>子数组是 <code>[4,3,1]</code>。3 和 1 都是奇数。因此这个查询的答案是 <code>false</code>。</li>
	<li>子数组是 <code>[1,6]</code>。只有一对：<code>(1,6)</code>，且包含了奇偶性不同的数字。因此这个查询的答案是 <code>true</code>。</li>
</ol>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= queries[i][0] &lt;= queries[i][1] &lt;= nums.length - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 前缀和

## 提示

1. Try to split the array into some non-intersected continuous special subarrays.
2. For each query check that the first and the last elements of that query are in the same subarray or not.

## 示例

```
[3,4,1,2,6]
[[0,4]]
[4,3,1,6]
[[0,2],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> isArraySpecial(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isArraySpecial(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* isArraySpecial(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool[] IsArraySpecial(int[] nums, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var isArraySpecial = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function isArraySpecial(nums: number[], queries: number[][]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function isArraySpecial($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isArraySpecial(_ nums: [Int], _ queries: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isArraySpecial(nums: IntArray, queries: Array<IntArray>): BooleanArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> isArraySpecial(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func isArraySpecial(nums []int, queries [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Boolean[]}
def is_array_special(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def isArraySpecial(nums: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_array_special(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (is-array-special nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec is_array_special(Nums :: [integer()], Queries :: [[integer()]]) -> [boolean()].
is_array_special(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_array_special(nums :: [integer], queries :: [[integer]]) :: [boolean]
  def is_array_special(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isArraySpecial(nums: Array<Int64>, queries: Array<Array<Int64>>): Array<Bool> {

    }
}
```

