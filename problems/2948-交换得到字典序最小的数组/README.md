# 2948. 交换得到字典序最小的数组

## 题目描述

<p>给你一个下标从 <strong>0 </strong>开始的 <strong>正整数</strong> 数组 <code>nums</code> 和一个 <strong>正整数</strong> <code>limit</code> 。</p>

<p>在一次操作中，你可以选择任意两个下标 <code>i</code> 和 <code>j</code>，<strong>如果</strong> 满足 <code>|nums[i] - nums[j]| &lt;= limit</code> ，则交换 <code>nums[i]</code> 和 <code>nums[j]</code> 。</p>

<p>返回执行任意次操作后能得到的 <strong>字典序最小的数组</strong><em> </em>。</p>

<p>如果在数组 <code>a</code> 和数组 <code>b</code> 第一个不同的位置上，数组 <code>a</code> 中的对应元素比数组 <code>b</code> 中的对应元素的字典序更小，则认为数组 <code>a</code> 就比数组 <code>b</code> 字典序更小。例如，数组 <code>[2,10,3]</code> 比数组 <code>[10,2,3]</code> 字典序更小，下标 <code>0</code> 处是两个数组第一个不同的位置，且 <code>2 &lt; 10</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,3,9,8], limit = 2
<strong>输出：</strong>[1,3,5,8,9]
<strong>解释：</strong>执行 2 次操作：
- 交换 nums[1] 和 nums[2] 。数组变为 [1,3,5,9,8] 。
- 交换 nums[3] 和 nums[4] 。数组变为 [1,3,5,8,9] 。
即便执行更多次操作，也无法得到字典序更小的数组。
注意，执行不同的操作也可能会得到相同的结果。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,7,6,18,2,1], limit = 3
<strong>输出：</strong>[1,6,7,18,1,2]
<strong>解释：</strong>执行 3 次操作：
- 交换 nums[1] 和 nums[2] 。数组变为 [1,6,7,18,2,1] 。
- 交换 nums[0] 和 nums[4] 。数组变为 [2,6,7,18,1,1] 。
- 交换 nums[0] 和 nums[5] 。数组变为 [1,6,7,18,1,2] 。
即便执行更多次操作，也无法得到字典序更小的数组。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,7,28,19,10], limit = 3
<strong>输出：</strong>[1,7,28,19,10]
<strong>解释：</strong>[1,7,28,19,10] 是字典序最小的数组，因为不管怎么选择下标都无法执行操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 并查集
- 数组
- 排序

## 提示

1. Construct a virtual graph where all elements in <code>nums</code> are nodes and the pairs satisfying the condition have an edge between them.
2. Instead of constructing all edges, we only care about the connected components.
3. Can we use DSU?
4. Sort <code>nums</code>. Now we just need to consider if the consecutive elements have an edge to check if they belong to the same connected component. Hence, all connected components become a list of position-consecutive elements after sorting.
5. For each index of <code>nums</code> from <code>0</code> to <code>nums.length - 1</code> we can change it to the current minimum value we have in its connected component and remove that value from the connected component.

## 示例

```
[1,5,3,9,8]
2
[1,7,6,18,2,1]
3
[1,7,28,19,10]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* lexicographicallySmallestArray(int* nums, int numsSize, int limit, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] LexicographicallySmallestArray(int[] nums, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number[]}
 */
var lexicographicallySmallestArray = function(nums, limit) {
    
};
```

### TypeScript

```typescript
function lexicographicallySmallestArray(nums: number[], limit: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer[]
     */
    function lexicographicallySmallestArray($nums, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lexicographicallySmallestArray(_ nums: [Int], _ limit: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lexicographicallySmallestArray(nums: IntArray, limit: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> lexicographicallySmallestArray(List<int> nums, int limit) {
    
  }
}
```

### Go

```golang
func lexicographicallySmallestArray(nums []int, limit int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer[]}
def lexicographically_smallest_array(nums, limit)
    
end
```

### Scala

```scala
object Solution {
    def lexicographicallySmallestArray(nums: Array[Int], limit: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn lexicographically_smallest_array(nums: Vec<i32>, limit: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (lexicographically-smallest-array nums limit)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec lexicographically_smallest_array(Nums :: [integer()], Limit :: integer()) -> [integer()].
lexicographically_smallest_array(Nums, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec lexicographically_smallest_array(nums :: [integer], limit :: integer) :: [integer]
  def lexicographically_smallest_array(nums, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lexicographicallySmallestArray(nums: Array<Int64>, limit: Int64): Array<Int64> {

    }
}
```

