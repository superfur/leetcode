# 2770. 达到末尾下标所需的最大跳跃次数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、由 <code>n</code> 个整数组成的数组 <code>nums</code> 和一个整数 <code>target</code> 。</p>

<p>你的初始位置在下标 <code>0</code> 。在一步操作中，你可以从下标 <code>i</code> 跳跃到任意满足下述条件的下标 <code>j</code> ：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; n</code></li>
	<li><code>-target &lt;= nums[j] - nums[i] &lt;= target</code></li>
</ul>

<p>返回到达下标 <code>n - 1</code> 处所需的 <strong>最大跳跃次数</strong> 。</p>

<p>如果无法到达下标 <code>n - 1</code> ，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,6,4,1,2], target = 2
<strong>输出：</strong>3
<strong>解释：</strong>要想以最大跳跃次数从下标 0 到下标 n - 1 ，可以按下述跳跃序列执行操作：
- 从下标 0 跳跃到下标 1 。 
- 从下标 1 跳跃到下标 3 。 
- 从下标 3 跳跃到下标 5 。 
可以证明，从 0 到 n - 1 的所有方案中，不存在比 3 步更长的跳跃序列。因此，答案是 3 。 </pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,6,4,1,2], target = 3
<strong>输出：</strong>5
<strong>解释：</strong>要想以最大跳跃次数从下标 0 到下标 n - 1 ，可以按下述跳跃序列执行操作：
- 从下标 0 跳跃到下标 1 。 
- 从下标 1 跳跃到下标 2 。 
- 从下标 2 跳跃到下标 3 。 
- 从下标 3 跳跃到下标 4 。 
- 从下标 4 跳跃到下标 5 。 
可以证明，从 0 到 n - 1 的所有方案中，不存在比 5 步更长的跳跃序列。因此，答案是 5 。 </pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,3,6,4,1,2], target = 0
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明不存在从 0 到 n - 1 的跳跃序列。因此，答案是 -1 。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length == n &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= nums[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= target &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Use a dynamic programming approach.
2. Define a dynamic programming array dp of size n, where dp[i] represents the maximum number of jumps from index 0 to index i.
3. For each j iterate over all i < j. Set dp[j] = max(dp[j], dp[i] + 1) if -target <= nums[j] - nums[i] <= target.

## 示例

```
[1,3,6,4,1,2]
2
[1,3,6,4,1,2]
3
[1,3,6,4,1,2]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumJumps(vector<int>& nums, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumJumps(int[] nums, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumJumps(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
```

### C

```c
int maximumJumps(int* nums, int numsSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumJumps(int[] nums, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var maximumJumps = function(nums, target) {
    
};
```

### TypeScript

```typescript
function maximumJumps(nums: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function maximumJumps($nums, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumJumps(_ nums: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumJumps(nums: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumJumps(List<int> nums, int target) {
    
  }
}
```

### Go

```golang
func maximumJumps(nums []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def maximum_jumps(nums, target)
    
end
```

### Scala

```scala
object Solution {
    def maximumJumps(nums: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_jumps(nums: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-jumps nums target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_jumps(Nums :: [integer()], Target :: integer()) -> integer().
maximum_jumps(Nums, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_jumps(nums :: [integer], target :: integer) :: integer
  def maximum_jumps(nums, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumJumps(nums: Array<Int64>, target: Int64): Int64 {

    }
}
```

