# 1674. 使数组互补的最少操作次数

## 题目描述

<p>给你一个长度为<strong> 偶数</strong> <code>n</code> 的整数数组 <code>nums</code> 和一个整数 <code>limit</code> 。每一次操作，你可以将 <code>nums</code> 中的任何整数替换为 <code>1</code> 到 <code>limit</code> 之间的另一个整数。</p>

<p>如果对于所有下标 <code>i</code>（<strong>下标从 </strong><code>0</code><strong> 开始</strong>），<code>nums[i] + nums[n - 1 - i]</code> 都等于同一个数，则数组 <code>nums</code> 是 <strong>互补的</strong> 。例如，数组 <code>[1,2,3,4]</code> 是互补的，因为对于所有下标 <code>i</code> ，<code>nums[i] + nums[n - 1 - i] = 5</code> 。</p>

<p>返回使数组 <strong>互补</strong> 的 <strong>最少</strong> 操作次数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,4,3], limit = 4
<strong>输出：</strong>1
<strong>解释：</strong>经过 1 次操作，你可以将数组 nums 变成 [1,2,<strong>2</strong>,3]（加粗元素是变更的数字）：
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,1], limit = 2
<strong>输出：</strong>2
<strong>解释：</strong>经过 2 次操作，你可以将数组 nums 变成 [<strong>2</strong>,2,2,<strong>2</strong>] 。你不能将任何数字变更为 3 ，因为 3 > limit 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,2], limit = 2
<strong>输出：</strong>0
<strong>解释：</strong>nums 已经是互补的。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>2 <= n <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= limit <= 10<sup>5</sup></code></li>
	<li><code>n</code> 是偶数。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 提示

1. Given a target sum x, each pair of nums[i] and nums[n-1-i] would either need 0, 1, or 2 modifications.
2. Can you find the optimal target sum x value such that the sum of modifications is minimized?
3. Create a difference array to efficiently sum all the modifications.

## 示例

```
[1,2,4,3]
4
[1,2,2,1]
2
[1,2,1,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMoves(int[] nums, int limit) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
```

### C

```c
int minMoves(int* nums, int numsSize, int limit) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMoves(int[] nums, int limit) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @return {number}
 */
var minMoves = function(nums, limit) {
    
};
```

### TypeScript

```typescript
function minMoves(nums: number[], limit: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @return Integer
     */
    function minMoves($nums, $limit) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMoves(_ nums: [Int], _ limit: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMoves(nums: IntArray, limit: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMoves(List<int> nums, int limit) {
    
  }
}
```

### Go

```golang
func minMoves(nums []int, limit int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer}
def min_moves(nums, limit)
    
end
```

### Scala

```scala
object Solution {
    def minMoves(nums: Array[Int], limit: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_moves(nums: Vec<i32>, limit: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-moves nums limit)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_moves(Nums :: [integer()], Limit :: integer()) -> integer().
min_moves(Nums, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_moves(nums :: [integer], limit :: integer) :: integer
  def min_moves(nums, limit) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMoves(nums: Array<Int64>, limit: Int64): Int64 {

    }
}
```

