# 3066. 超过阈值的最少操作数 II

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你可以对&nbsp;<code>nums</code>&nbsp;执行一些操作，在一次操作中，你可以：</p>

<ul>
	<li>选择 <code>nums</code>&nbsp;中 <strong>最小</strong> 的两个整数&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;。</li>
	<li>将&nbsp;<code>x</code> 和&nbsp;<code>y</code> 从&nbsp;<code>nums</code>&nbsp;中删除。</li>
	<li>将&nbsp;<code>min(x, y) * 2 + max(x, y)</code>&nbsp;添加到数组中的任意位置。</li>
</ul>

<p><b>注意，</b>只有当&nbsp;<code>nums</code>&nbsp;<strong>至少</strong> 包含两个元素时，你才可以执行以上操作。</p>

<p>你需要使数组中的所有元素都 <strong>大于或等于</strong>&nbsp;<code>k</code>&nbsp;，请你返回需要的&nbsp;<strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><b>输入：</b>nums = [2,11,10,1,3], k = 10</p>

<p><b>输出：</b>2</p>

<p><b>解释：</b></p>

<ol>
	<li>第一次操作中，我们删除元素 1 和 2 ，然后添加 <code>1 * 2 + 2</code> 到 <code>nums</code> 中，<code>nums</code> 变为 <code>[4, 11, 10, 3]</code> 。</li>
	<li>第二次操作中，我们删除元素 3 和 4 ，然后添加 <code>3 * 2 + 4</code> 到 <code>nums</code> 中，<code>nums</code> 变为 <code>[10, 11, 10]</code> 。</li>
</ol>

<p>此时，数组中的所有元素都大于等于 10 ，所以我们停止操作。</p>

<p>可以证明使数组中所有元素都大于等于 10 需要的最少操作次数为 2 。</p>

<p>&nbsp;</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><b>输入：</b>nums = [1,1,2,4,9], k = 20</p>

<p><b>输出：</b>4</p>

<p><b>解释：</b></p>

<ol>
	<li>第一次操作后，<code>nums</code> 变为 <code>[2, 4, 9, 3]</code>。</li>
	<li>第二次操作后，<code>nums</code> 变为 <code>[7, 4, 9]</code>。</li>
	<li>第三次操作后，<code>nums</code> 变为 <code>[15, 9]</code>。</li>
	<li>第四次操作后，<code>nums</code> 变为 <code>[33]</code>。</li>
</ol>

<p>此时，<code>nums</code> 中的所有元素都大于等于 20 ，所以我们停止操作。</p>

<p>可以证明使数组中所有元素都大于等于 20 需要的最少操作次数为 4 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li>输入保证答案一定存在，也就是说，在进行某些次数的操作后，数组中所有元素都大于等于&nbsp;<code>k</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 模拟
- 堆（优先队列）

## 提示

1. Use priority queue to keep track of minimum elements.
2. Remove the minimum two elements, perform the operation, and insert the resulting number into the priority queue.

## 示例

```
[2,11,10,1,3]
10
[1,1,2,4,9]
20
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

