# 2439. 最小化数组中的最大值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>nums</code>&nbsp;，它含有&nbsp;<code>n</code>&nbsp;个非负整数。</p>

<p>每一步操作中，你需要：</p>

<ul>
	<li>选择一个满足&nbsp;<code>1 &lt;= i &lt; n</code>&nbsp;的整数 <code>i</code>&nbsp;，且&nbsp;<code>nums[i] &gt; 0</code>&nbsp;。</li>
	<li>将&nbsp;<code>nums[i]</code>&nbsp;减 1 。</li>
	<li>将&nbsp;<code>nums[i - 1]</code>&nbsp;加 1 。</li>
</ul>

<p>你可以对数组执行 <strong>任意</strong>&nbsp;次上述操作，请你返回可以得到的 <code>nums</code>&nbsp;数组中<b>&nbsp;最大值</b>&nbsp;<strong>最小</strong> 为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,7,1,6]
<b>输出：</b>5
<strong>解释：</strong>
一串最优操作是：
1. 选择 i = 1 ，nums 变为 [4,6,1,6] 。
2. 选择 i = 3 ，nums 变为 [4,6,2,5] 。
3. 选择 i = 1 ，nums 变为 [5,5,2,5] 。
nums 中最大值为 5 。无法得到比 5 更小的最大值。
所以我们返回 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [10,1]
<b>输出：</b>10
<strong>解释：</strong>
最优解是不改动 nums ，10 是最大值，所以返回 10 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找
- 动态规划
- 前缀和

## 提示

1. Try a binary search approach.
2. Perform a binary search over the minimum value that can be achieved for the maximum number of the array.
3. In each binary search iteration, iterate through the array backwards, greedily decreasing the current element until it is within the limit.

## 示例

```
[3,7,1,6]
[10,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeArrayValue(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeArrayValue(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
```

### C

```c
int minimizeArrayValue(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeArrayValue(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeArrayValue = function(nums) {
    
};
```

### TypeScript

```typescript
function minimizeArrayValue(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimizeArrayValue($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeArrayValue(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeArrayValue(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeArrayValue(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimizeArrayValue(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimize_array_value(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimizeArrayValue(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_array_value(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-array-value nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_array_value(Nums :: [integer()]) -> integer().
minimize_array_value(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_array_value(nums :: [integer]) :: integer
  def minimize_array_value(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeArrayValue(nums: Array<Int64>): Int64 {

    }
}
```

