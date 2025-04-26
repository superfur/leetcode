# 2122. 还原原数组

## 题目描述

<p>Alice 有一个下标从 <strong>0</strong> 开始的数组 <code>arr</code> ，由 <code>n</code> 个正整数组成。她会选择一个任意的 <strong>正整数 </strong><code>k</code> 并按下述方式创建两个下标从 <strong>0</strong> 开始的新整数数组 <code>lower</code> 和 <code>higher</code> ：</p>

<ol>
	<li>对每个满足 <code>0 &lt;= i &lt; n</code> 的下标 <code>i</code> ，<code>lower[i] = arr[i] - k</code></li>
	<li>对每个满足 <code>0 &lt;= i &lt; n</code> 的下标 <code>i</code> ，<code>higher[i] = arr[i] + k</code></li>
</ol>

<p>不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 <code>lower</code> 和 <code>higher</code> 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。</p>

<p>给你一个由 2n 个整数组成的整数数组 <code>nums</code> ，其中 <strong>恰好</strong> <code>n</code> 个整数出现在 <code>lower</code> ，剩下的出现在 <code>higher</code> ，还原并返回 <strong>原数组</strong> <code>arr</code> 。如果出现答案不唯一的情况，返回 <strong>任一</strong> 有效数组。</p>

<p><strong>注意：</strong>生成的测试用例保证存在 <strong>至少一个</strong> 有效数组 <code>arr</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,10,6,4,8,12]
<strong>输出：</strong>[3,7,11]
<strong>解释：</strong>
如果 arr = [3,7,11] 且 k = 1 ，那么 lower = [2,6,10] 且 higher = [4,8,12] 。
组合 lower 和 higher 得到 [2,6,10,4,8,12] ，这是 nums 的一个排列。
另一个有效的数组是 arr = [5,7,9] 且 k = 3 。在这种情况下，lower = [2,4,6] 且 higher = [8,10,12] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,3,3]
<strong>输出：</strong>[2,2]
<strong>解释：</strong>
如果 arr = [2,2] 且 k = 1 ，那么 lower = [1,1] 且 higher = [3,3] 。
组合 lower 和 higher 得到 [1,1,3,3] ，这是 nums 的一个排列。
注意，数组不能是 [1,3] ，因为在这种情况下，获得 [1,1,3,3] 唯一可行的方案是 k = 0 。
这种方案是无效的，k 必须是一个正整数。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [5,435]
<strong>输出：</strong>[220]
<strong>解释：</strong>
唯一可行的组合是 arr = [220] 且 k = 215 。在这种情况下，lower = [5] 且 higher = [435] 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 * n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>生成的测试用例保证存在 <strong>至少一个</strong> 有效数组 <code>arr</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 双指针
- 枚举
- 排序

## 提示

1. If we fix the value of k, how can we check if an original array exists for the fixed k?
2. The smallest value of nums is obtained by subtracting k from the smallest value of the original array. How can we use this to reduce the search space for finding a valid k?
3. You can compute every possible k by using the smallest value of nums (as lower[i]) against every other value in nums (as the corresponding higher[i]).
4. For every computed k, greedily pair up the values in nums. This can be done sorting nums, then using a map to store previous values and searching that map for a corresponding lower[i] for the current nums[j] (as higher[i]).

## 示例

```
[2,10,6,4,8,12]
[1,1,3,3]
[5,435]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> recoverArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] recoverArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def recoverArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* recoverArray(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RecoverArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var recoverArray = function(nums) {
    
};
```

### TypeScript

```typescript
function recoverArray(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function recoverArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func recoverArray(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun recoverArray(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> recoverArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func recoverArray(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def recover_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def recoverArray(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn recover_array(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (recover-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec recover_array(Nums :: [integer()]) -> [integer()].
recover_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec recover_array(nums :: [integer]) :: [integer]
  def recover_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func recoverArray(nums: Array<Int64>): Array<Int64> {

    }
}
```

