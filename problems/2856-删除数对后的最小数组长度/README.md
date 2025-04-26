# 2856. 删除数对后的最小数组长度

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的 <strong>非递减</strong> 整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以执行以下操作任意次：</p>

<ul>
	<li>选择 <strong>两个&nbsp;</strong>下标&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;，满足&nbsp;<code>nums[i] &lt; nums[j]</code>&nbsp;。</li>
	<li>将 <code>nums</code>&nbsp;中下标在&nbsp;<code>i</code> 和&nbsp;<code>j</code>&nbsp;处的元素删除。剩余元素按照原来的顺序组成新的数组，下标也重新从 <strong>0</strong>&nbsp;开始编号。</li>
</ul>

<p>请你返回一个整数，表示执行以上操作任意次后（可以执行 <strong>0</strong> 次），<code>nums</code>&nbsp;数组的 <strong>最小</strong>&nbsp;数组长度。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://pic.leetcode.cn/1716779983-AHhkVn-tcase1.gif" style="width: 160px; height: 70px;" /></p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,1,2,2,3,3]</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://pic.leetcode.cn/1716779979-GyQhVf-tcase2.gif" style="width: 240px; height: 70px;" /></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1000000000,1000000000]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>由于两个数字相等，不能删除它们。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [2,3,4,4,4]</span></p>

<p><strong>输出：</strong><span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://pic.leetcode.cn/1716779940-qRRlHk-tcase3.gif" style="width: 210px; height: 70px;" /></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code>&nbsp;是 <strong>非递减</strong>&nbsp;数组。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 双指针
- 二分查找
- 计数

## 提示

1. To minimize the length of the array, we should maximize the number of operations performed.
2. To perform <code>k</code> operations, it is optimal to use the smallest <code>k</code> values and the largest <code>k</code> values in <code>nums</code>.
3. What is the best way to make pairs from the smallest <code>k</code> values and the largest <code>k</code> values so it is possible to remove all the pairs?
4. If we consider the smallest <code>k</code> values and the largest <code>k</code> values as two separate <strong>sorted 0-indexed</strong> arrays, <code>a</code> and <code>b</code>, It is optimal to pair <code>a[i]</code> and <code>b[i]</code>. So, a <code>k</code> is valid if <code>a[i] < b[i]</code> for all <code>i</code> in the range <code>[0, k - 1]</code>.
5. The greatest possible valid <code>k</code> can be found using binary search.
6. The answer is <code>nums.length - 2 * k</code>.

## 示例

```
[1,2,3,4]
[1,1,2,2,3,3]
[1000000000,1000000000]
[2,3,4,4,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minLengthAfterRemovals(List<Integer> nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        
```

### C

```c
int minLengthAfterRemovals(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinLengthAfterRemovals(IList<int> nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minLengthAfterRemovals = function(nums) {
    
};
```

### TypeScript

```typescript
function minLengthAfterRemovals(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minLengthAfterRemovals($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minLengthAfterRemovals(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minLengthAfterRemovals(nums: List<Int>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minLengthAfterRemovals(List<int> nums) {
    
  }
}
```

### Go

```golang
func minLengthAfterRemovals(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_length_after_removals(nums)
    
end
```

### Scala

```scala
object Solution {
    def minLengthAfterRemovals(nums: List[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_length_after_removals(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-length-after-removals nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_length_after_removals(Nums :: [integer()]) -> integer().
min_length_after_removals(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_length_after_removals(nums :: [integer]) :: integer
  def min_length_after_removals(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minLengthAfterRemovals(nums: ArrayList<Int64>): Int64 {

    }
}
```

