# 3012. 通过操作使数组长度最小

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，它只包含 <strong>正</strong>&nbsp;整数。</p>

<p>你的任务是通过进行以下操作&nbsp;<strong>任意次</strong>&nbsp;（可以是 0 次）&nbsp;<strong>最小化</strong>&nbsp;<code>nums</code>&nbsp;的长度：</p>

<ul>
	<li>在 <code>nums</code>&nbsp;中选择 <strong>两个不同</strong>&nbsp;的下标&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;，满足&nbsp;<code>nums[i] &gt; 0</code>&nbsp;且&nbsp;<code>nums[j] &gt; 0</code>&nbsp;。</li>
	<li>将结果&nbsp;<code>nums[i] % nums[j]</code>&nbsp;插入&nbsp;<code>nums</code>&nbsp;的结尾。</li>
	<li>将 <code>nums</code>&nbsp;中下标为&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;的元素删除。</li>
</ul>

<p>请你返回一个整数，它表示进行任意次操作以后<em>&nbsp;</em><code>nums</code>&nbsp;的 <strong>最小长度</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,3,1]
<b>输出：</b>1
<b>解释：</b>使数组长度最小的一种方法是：
操作 1 ：选择下标 2 和 1 ，插入 nums[2] % nums[1] 到数组末尾，得到 [1,4,3,1,3] ，然后删除下标为 2 和 1 的元素。
nums 变为 [1,1,3] 。
操作 2 ：选择下标 1 和 2 ，插入 nums[1] % nums[2] 到数组末尾，得到 [1,1,3,1] ，然后删除下标为 1 和 2 的元素。
nums 变为 [1,1] 。
操作 3 ：选择下标 1 和 0 ，插入 nums[1] % nums[0] 到数组末尾，得到 [1,1,0] ，然后删除下标为 1 和 0 的元素。
nums 变为 [0] 。
nums 的长度无法进一步减小，所以答案为 1 。
1 是可以得到的最小长度。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,5,5,10,5]
<b>输出：</b>2
<b>解释：</b>使数组长度最小的一种方法是：
操作 1 ：选择下标 0 和 3 ，插入 nums[0] % nums[3] 到数组末尾，得到 [5,5,5,10,5,5] ，然后删除下标为 0 和 3 的元素。
nums 变为 [5,5,5,5] 。
操作 2 ：选择下标 2 和 3 ，插入 nums[2] % nums[3] 到数组末尾，得到 [5,5,5,5,0] ，然后删除下标为 2 和 3 的元素。
nums 变为 [5,5,0] 。
操作 3 ：选择下标 0 和 1 ，插入 nums[0] % nums[1] 到数组末尾，得到 [5,5,0,0] ，然后删除下标为 0 和 1 的元素。
nums 变为 [0,0] 。
nums 的长度无法进一步减小，所以答案为 2 。
2 是可以得到的最小长度。</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [2,3,4]
<b>输出：</b>1
<b>解释：</b>使数组长度最小的一种方法是：
操作 1 ：选择下标 1 和 2 ，插入 nums[1] % nums[2] 到数组末尾，得到 [2,3,4,3] ，然后删除下标为 1 和 2 的元素。
nums 变为 [2,3] 。
操作 2 ：选择下标 1 和 0 ，插入 nums[1] % nums[0] 到数组末尾，得到 [2,3,1] ，然后删除下标为 1 和 0 的元素。
nums 变为 [1] 。
nums 的长度无法进一步减小，所以答案为 1 。
1 是可以得到的最小长度。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 数论

## 提示

1. The problem can be solved by considering different cases.
2. Let the minimum value in <code>nums</code> be <code>x</code>; we can consider the following cases:
3. If <code>x</code> occurs once: The minimum length of <code>nums</code> achievable in this case is <code>1</code>, since every other value, <code>y</code>, can be paired with <code>x</code>, resulting in deleting <code>x</code> and <code>y</code>, and inserting <code>x % y == x</code>, since <code>x < y</code>. So, only <code>x</code> remains after the operations.
4. If there is a value <code>y</code> in <code>nums</code> such that <code>y % x</code> is not equal to <code>0</code>: The minimum achievable length in this case is <code>1</code> as well, because inserting <code>y % x</code> creates a new minimum, since <code>y % x < x</code>, returning to the first case.
5. If neither of the previous cases holds, and <code>x</code> occurs <code>cnt</code> times: The minimum length of <code>nums</code> achievable in this case is <code>ceil(cnt / 2)</code>.

## 示例

```
[1,4,3,1]
[5,5,5,10,5]
[2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumArrayLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumArrayLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumArrayLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumArrayLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumArrayLength = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumArrayLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumArrayLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumArrayLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumArrayLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumArrayLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumArrayLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_array_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumArrayLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_array_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-array-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_array_length(Nums :: [integer()]) -> integer().
minimum_array_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_array_length(nums :: [integer]) :: integer
  def minimum_array_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumArrayLength(nums: Array<Int64>): Int64 {

    }
}
```

