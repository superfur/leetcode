# 3375. 使数组的值全部为 K 的最少操作次数

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>如果一个数组中所有 <strong>严格大于</strong>&nbsp;<code>h</code>&nbsp;的整数值都 <strong>相等</strong>&nbsp;，那么我们称整数&nbsp;<code>h</code>&nbsp;是 <strong>合法的</strong>&nbsp;。</p>

<p>比方说，如果&nbsp;<code>nums = [10, 8, 10, 8]</code>&nbsp;，那么&nbsp;<code>h = 9</code>&nbsp;是一个 <strong>合法</strong>&nbsp;整数，因为所有满足&nbsp;<code>nums[i] &gt; 9</code>&nbsp;的数都等于 10 ，但是 5 不是 <strong>合法</strong>&nbsp;整数。</p>

<p>你可以对 <code>nums</code>&nbsp;执行以下操作：</p>

<ul>
	<li>选择一个整数&nbsp;<code>h</code>&nbsp;，它对于 <strong>当前</strong>&nbsp;<code>nums</code>&nbsp;中的值是合法的。</li>
	<li>对于每个下标 <code>i</code>&nbsp;，如果它满足&nbsp;<code>nums[i] &gt; h</code>&nbsp;，那么将&nbsp;<code>nums[i]</code>&nbsp;变为&nbsp;<code>h</code>&nbsp;。</li>
</ul>

<p>你的目标是将 <code>nums</code>&nbsp;中的所有元素都变为 <code>k</code>&nbsp;，请你返回 <strong>最少</strong>&nbsp;操作次数。如果无法将所有元素都变&nbsp;<code>k</code>&nbsp;，那么返回 -1 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [5,2,5,4,5], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b></p>

<p>依次选择合法整数 4 和 2 ，将数组全部变为 2 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,1,2], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><strong>解释：</strong></p>

<p>没法将所有值变为 2 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [9,7,5,3], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>依次选择合法整数 7 ，5 ，3 和 1 ，将数组全部变为 1 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100 </code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Handle the case when the array contains an integer less than <code>k</code>
2. Start by performing operations on the highest integer
3. You can perform an operation on the highest integer using the second-highest, an operation on the second-highest using the third-highest, and so forth.
4. The answer is the number of distinct integers in the array that are larger than <code>k</code>.

## 示例

```
[5,2,5,4,5]
2
[2,1,2]
2
[9,7,5,3]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minOperations(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

