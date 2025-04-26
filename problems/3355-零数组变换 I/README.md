# 3355. 零数组变换 I

## 题目描述

<p>给定一个长度为 <code>n</code> 的整数数组 <code>nums</code> 和一个二维数组 <code>queries</code>，其中 <code>queries[i] = [l<sub>i</sub>, r<sub>i</sub>]</code>。</p>

<p>对于每个查询&nbsp;<code>queries[i]</code>：</p>

<ul>
	<li>在&nbsp;<code>nums</code>&nbsp;的下标范围&nbsp;<code>[l<sub>i</sub>, r<sub>i</sub>]</code>&nbsp;内选择一个下标 <span data-keyword="subset">子集</span>。</li>
	<li>将选中的每个下标对应的元素值减 1。</li>
</ul>

<p><strong>零数组&nbsp;</strong>是指所有元素都等于 0 的数组。</p>

<p>如果在按顺序处理所有查询后，可以将 <code>nums</code> 转换为&nbsp;<strong>零数组&nbsp;</strong>，则返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,0,1], queries = [[0,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>对于 i = 0：</strong>

	<ul>
		<li>选择下标子集 <code>[0, 2]</code> 并将这些下标处的值减 1。</li>
		<li>数组将变为 <code>[0, 0, 0]</code>，这是一个零数组。</li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,3,2,1], queries = [[1,3],[0,2]]</span></p>

<p><strong>输出：</strong> <span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>对于 i = 0：</strong>&nbsp;

	<ul>
		<li>选择下标子集 <code>[1, 2, 3]</code> 并将这些下标处的值减 1。</li>
		<li>数组将变为 <code>[4, 2, 1, 0]</code>。</li>
	</ul>
	</li>
	<li><strong>对于 i = 1：</strong>
	<ul>
		<li>选择下标子集 <code>[0, 1, 2]</code> 并将这些下标处的值减 1。</li>
		<li>数组将变为 <code>[3, 1, 0, 0]</code>，这不是一个零数组。</li>
	</ul>
	</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= l<sub>i</sub> &lt;= r<sub>i</sub> &lt; nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. Can we use difference array and prefix sum to check if an index can be made zero?

## 示例

```
[1,0,1]
[[0,2]]
[4,3,2,1]
[[1,3],[0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
```

### C

```c
bool isZeroArray(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsZeroArray(int[] nums, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {boolean}
 */
var isZeroArray = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function isZeroArray(nums: number[], queries: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Boolean
     */
    function isZeroArray($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isZeroArray(_ nums: [Int], _ queries: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isZeroArray(nums: IntArray, queries: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isZeroArray(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func isZeroArray(nums []int, queries [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Boolean}
def is_zero_array(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def isZeroArray(nums: Array[Int], queries: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_zero_array(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-zero-array nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec is_zero_array(Nums :: [integer()], Queries :: [[integer()]]) -> boolean().
is_zero_array(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_zero_array(nums :: [integer], queries :: [[integer]]) :: boolean
  def is_zero_array(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isZeroArray(nums: Array<Int64>, queries: Array<Array<Int64>>): Bool {

    }
}
```

