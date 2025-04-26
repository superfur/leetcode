# 632. 最小区间

## 题目描述

<p>你有&nbsp;<code>k</code>&nbsp;个 <strong>非递减排列</strong> 的整数列表。找到一个 <strong>最小 </strong>区间，使得&nbsp;<code>k</code>&nbsp;个列表中的每个列表至少有一个数包含在其中。</p>

<p>我们定义如果&nbsp;<code>b-a &lt; d-c</code>&nbsp;或者在&nbsp;<code>b-a == d-c</code>&nbsp;时&nbsp;<code>a &lt; c</code>，则区间 <code>[a,b]</code> 比 <code>[c,d]</code> 小。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
<strong>输出：</strong>[20,24]
<strong>解释：</strong> 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[1,2,3],[1,2,3]]
<strong>输出：</strong>[1,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length == k</code></li>
	<li><code>1 &lt;= k &lt;= 3500</code></li>
	<li><code>1 &lt;= nums[i].length &lt;= 50</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i][j] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 按非递减顺序排列</li>
</ul>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 贪心
- 数组
- 哈希表
- 排序
- 滑动窗口
- 堆（优先队列）

## 示例

```
[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
[[1,2,3],[1,2,3],[1,2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] smallestRange(List<List<Integer>> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallestRange(int** nums, int numsSize, int* numsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SmallestRange(IList<IList<int>> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var smallestRange = function(nums) {
    
};
```

### TypeScript

```typescript
function smallestRange(nums: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer[]
     */
    function smallestRange($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallestRange(_ nums: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallestRange(nums: List<List<Int>>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> smallestRange(List<List<int>> nums) {
    
  }
}
```

### Go

```golang
func smallestRange(nums [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums
# @return {Integer[]}
def smallest_range(nums)
    
end
```

### Scala

```scala
object Solution {
    def smallestRange(nums: List[List[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smallest_range(nums: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (smallest-range nums)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec smallest_range(Nums :: [[integer()]]) -> [integer()].
smallest_range(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smallest_range(nums :: [[integer]]) :: [integer]
  def smallest_range(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallestRange(nums: ArrayList<ArrayList<Int64>>): Array<Int64> {

    }
}
```

