# 3432. 统计元素和差值为偶数的分区方案

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p><strong>分区</strong>&nbsp;是指将数组按照下标&nbsp;<code>i</code>&nbsp;（<code>0 &lt;= i &lt; n - 1</code>）划分成两个 <strong>非空</strong> 子数组，其中：</p>

<ul>
	<li>左子数组包含区间&nbsp;<code>[0, i]</code>&nbsp;内的所有下标。</li>
	<li>右子数组包含区间&nbsp;<code>[i + 1, n - 1]</code>&nbsp;内的所有下标。</li>
</ul>

<p>对左子数组和右子数组先求元素 <strong>和</strong> 再做 <strong>差</strong> ，统计并返回差值为 <strong>偶数</strong> 的 <strong>分区</strong> 方案数。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><b>输入：</b><span class="example-io">nums = [10,10,3,7,6]</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><b>解释：</b></p>

<p>共有 4 个满足题意的分区方案：</p>

<ul>
	<li><code>[10]</code>、<code>[10, 3, 7, 6]</code>&nbsp;元素和的差值为&nbsp;<code>10 - 26 = -16</code>&nbsp;，是偶数。</li>
	<li><code>[10, 10]</code>、<code>[3, 7, 6]</code> 元素和的差值为&nbsp;<code>20 - 16 = 4</code>，是偶数。</li>
	<li><code>[10, 10, 3]</code>、<code>[7, 6]</code> 元素和的差值为&nbsp;<code>23 - 13 = 10</code>，是偶数。</li>
	<li><code>[10, 10, 3, 7]</code>、<code>[6]</code> 元素和的差值为&nbsp;<code>30 - 6 = 24</code>，是偶数。</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,2]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>不存在元素和的差值为偶数的分区方案。</p>
</div>

<p><b>示例 3：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,4,6,8]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><b>解释：</b></p>

<p>所有分区方案都满足元素和的差值为偶数。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 前缀和

## 提示

1. If the parity of the sum is even, the partition is valid; otherwise, there is no partition.

## 示例

```
[10,10,3,7,6]
[1,2,2]
[2,4,6,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPartitions(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPartitions(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        
```

### C

```c
int countPartitions(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPartitions(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countPartitions = function(nums) {
    
};
```

### TypeScript

```typescript
function countPartitions(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countPartitions($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPartitions(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPartitions(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPartitions(List<int> nums) {
    
  }
}
```

### Go

```golang
func countPartitions(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_partitions(nums)
    
end
```

### Scala

```scala
object Solution {
    def countPartitions(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_partitions(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-partitions nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_partitions(Nums :: [integer()]) -> integer().
count_partitions(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_partitions(nums :: [integer]) :: integer
  def count_partitions(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPartitions(nums: Array<Int64>): Int64 {

    }
}
```

