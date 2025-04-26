# 3187. 数组中的峰值

## 题目描述

<p>数组 <code>arr</code>&nbsp;中&nbsp;<strong>大于</strong>&nbsp;前面和后面相邻元素的元素被称为 <strong>峰值</strong>&nbsp;元素。</p>

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个二维整数数组&nbsp;<code>queries</code>&nbsp;。</p>

<p>你需要处理以下两种类型的操作：</p>

<ul>
	<li><code>queries[i] = [1, l<sub>i</sub>, r<sub>i</sub>]</code>&nbsp;，求出子数组&nbsp;<code>nums[l<sub>i</sub>..r<sub>i</sub>]</code>&nbsp;中&nbsp;<strong>峰值</strong>&nbsp;元素的数目。<!-- notionvc: 73b20b7c-e1ab-4dac-86d0-13761094a9ae --></li>
	<li><code>queries[i] = [2, index<sub>i</sub>, val<sub>i</sub>]</code>&nbsp;，将&nbsp;<code>nums[index<sub>i</sub>]</code>&nbsp;变为&nbsp;<code><font face="monospace">val<sub>i</sub></font></code><font face="monospace">&nbsp;。</font></li>
</ul>

<p>请你返回一个数组&nbsp;<code>answer</code>&nbsp;，它依次包含每一个第一种操作的答案。<!-- notionvc: a9ccef22-4061-4b5a-b4cc-a2b2a0e12f30 --></p>

<p><strong>注意：</strong></p>

<ul>
	<li>子数组中 <strong>第一个</strong>&nbsp;和 <strong>最后一个</strong>&nbsp;元素都 <strong>不是</strong>&nbsp;峰值元素。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]</span></p>

<p><span class="example-io"><b>输出：</b>[0]</span></p>

<p><strong>解释：</strong></p>

<p>第一个操作：我们将&nbsp;<code>nums[3]</code>&nbsp;变为&nbsp;4 ，<code>nums</code>&nbsp;变为&nbsp;<code>[3,1,4,4,5]</code>&nbsp;。</p>

<p>第二个操作：<code>[3,1,4,4,5]</code>&nbsp;中峰值元素的数目为 0 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]</span></p>

<p><span class="example-io"><b>输出：</b>[0,1]</span></p>

<p><strong>解释：</strong></p>

<p>第一个操作：<code>nums[2]</code>&nbsp;变为 4 ，它已经是 4 了，所以保持不变。</p>

<p>第二个操作：<code>[4,1,4]</code>&nbsp;中峰值元素的数目为 0 。</p>

<p>第三个操作：第二个 4 是&nbsp;<code>[4,1,4,2,1]</code>&nbsp;中的峰值元素。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i][0] == 1</code>&nbsp;或者&nbsp;<code>queries[i][0] == 2</code></li>
	<li>对于所有的 <code>i</code>&nbsp;，都有：
	<ul>
		<li><code>queries[i][0] == 1</code>&nbsp;：<code>0 &lt;= queries[i][1] &lt;= queries[i][2] &lt;= nums.length - 1</code></li>
		<li><code>queries[i][0] == 2</code> ：<code>0 &lt;= queries[i][1] &lt;= nums.length - 1</code>, <code>1 &lt;= queries[i][2] &lt;= 10<sup>5</sup></code></li>
	</ul>
	</li>
</ul>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组

## 提示

1. Let <code>p[i]</code> be whether <code>nums[i]</code> is a peak in the original array. Namely <code>p[i] = nums[i] > nums[i - 1] && nums[i] > nums[i + 1]</code>.
2. Updating <code>nums[i]</code>, only affects <code>p[i]</code>, <code>p[i - 1]</code> and <code>p[i + 1]</code>. We can recalculate the 3 values in constant time.
3. The answer for <code>[l<sub>i</sub>, r<sub>i</sub>]</code> is <code>p[l<sub>i</sub> + 1] + p[l<sub>i</sub> + 2] + … + p[r<sub>i</sub> - 1]</code> (note that <code>l<sub>i</sub></code> and <code>r<sub>i</sub></code> are not included).
4. Use some data structures (i.e. segment tree or binary indexed tree) to maintain the subarray sum efficiently.

## 示例

```
[3,1,4,2,5]
[[2,3,4],[1,0,4]]
[4,1,4,2,1,5]
[[2,2,4],[1,0,2],[1,0,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> countOfPeaks(vector<int>& nums, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> countOfPeaks(int[] nums, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOfPeaks(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countOfPeaks(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> CountOfPeaks(int[] nums, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var countOfPeaks = function(nums, queries) {
    
};
```

### TypeScript

```typescript
function countOfPeaks(nums: number[], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function countOfPeaks($nums, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOfPeaks(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOfPeaks(nums: IntArray, queries: Array<IntArray>): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> countOfPeaks(List<int> nums, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func countOfPeaks(nums []int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Integer[]}
def count_of_peaks(nums, queries)
    
end
```

### Scala

```scala
object Solution {
    def countOfPeaks(nums: Array[Int], queries: Array[Array[Int]]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_of_peaks(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (count-of-peaks nums queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec count_of_peaks(Nums :: [integer()], Queries :: [[integer()]]) -> [integer()].
count_of_peaks(Nums, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_of_peaks(nums :: [integer], queries :: [[integer]]) :: [integer]
  def count_of_peaks(nums, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOfPeaks(nums: Array<Int64>, queries: Array<Array<Int64>>): ArrayList<Int64> {

    }
}
```

