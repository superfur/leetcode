# 2560. 打家劫舍 IV

## 题目描述

<p>沿街有一排连续的房屋。每间房屋内都藏有一定的现金。现在有一位小偷计划从这些房屋中窃取现金。</p>

<p>由于相邻的房屋装有相互连通的防盗系统，所以小偷 <strong>不会窃取相邻的房屋</strong> 。</p>

<p>小偷的 <strong>窃取能力</strong> 定义为他在窃取过程中能从单间房屋中窃取的 <strong>最大金额</strong> 。</p>

<p>给你一个整数数组 <code>nums</code> 表示每间房屋存放的现金金额。形式上，从左起第 <code>i</code> 间房屋中放有 <code>nums[i]</code> 美元。</p>

<p>另给你一个整数&nbsp;<code>k</code> ，表示窃贼将会窃取的 <strong>最少</strong> 房屋数。小偷总能窃取至少 <code>k</code> 间房屋。</p>

<p>返回小偷的 <strong>最小</strong> 窃取能力。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,5,9], k = 2
<strong>输出：</strong>5
<strong>解释：</strong>
小偷窃取至少 2 间房屋，共有 3 种方式：
- 窃取下标 0 和 2 处的房屋，窃取能力为 max(nums[0], nums[2]) = 5 。
- 窃取下标 0 和 3 处的房屋，窃取能力为 max(nums[0], nums[3]) = 9 。
- 窃取下标 1 和 3 处的房屋，窃取能力为 max(nums[1], nums[3]) = 9 。
因此，返回 min(5, 9, 9) = 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,7,9,3,1], k = 2
<strong>输出：</strong>2
<strong>解释：</strong>共有 7 种窃取方式。窃取能力最小的情况所对应的方式是窃取下标 0 和 4 处的房屋。返回 max(nums[0], nums[4]) = 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= (nums.length + 1)/2</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Can we use binary search to find the minimum value of a non-contiguous subsequence of a given size k?
2. Initialize the search range with the minimum and maximum elements of the input array.
3. Use a check function to determine if it is possible to select k non-consecutive elements that are less than or equal to the current "guess" value.
4. Adjust the search range based on the outcome of the check function, until the range converges and the minimum value is found.

## 示例

```
[2,3,5,9]
2
[2,7,9,3,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minCapability(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minCapability(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minCapability(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinCapability(int[] nums, int k) {
        
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
var minCapability = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minCapability(nums: number[], k: number): number {
    
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
    function minCapability($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCapability(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCapability(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCapability(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minCapability(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_capability(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minCapability(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_capability(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-capability nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_capability(Nums :: [integer()], K :: integer()) -> integer().
min_capability(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_capability(nums :: [integer], k :: integer) :: integer
  def min_capability(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCapability(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

