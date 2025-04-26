# 1703. 得到连续 K 个 1 的最少相邻交换次数

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。 <code>nums</code> 仅包含 <code>0</code> 和 <code>1</code> 。每一次移动，你可以选择 <strong>相邻</strong> 两个数字并将它们交换。</p>

<p>请你返回使 <code>nums</code> 中包含 <code>k</code> 个 <strong>连续 </strong><code>1</code> 的 <strong>最少</strong> 交换次数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,0,0,1,0,1], k = 2
<b>输出：</b>1
<b>解释：</b>在第一次操作时，nums 可以变成 [1,0,0,0,<strong>1</strong>,<strong>1</strong>] 得到连续两个 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,0,0,0,0,0,1,1], k = 3
<b>输出：</b>5
<b>解释：</b>通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,<strong>1</strong>,<strong>1</strong>,<strong>1</strong>] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [1,1,0,1], k = 2
<b>输出：</b>0
<b>解释：</b>nums 已经有连续 2 个 1 了。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 要么是 <code>0</code> ，要么是 <code>1</code> 。</li>
	<li><code>1 &lt;= k &lt;= sum(nums)</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 前缀和
- 滑动窗口

## 提示

1. Choose k 1s and determine how many steps are required to move them into 1 group.
2. Maintain a sliding window of k 1s, and maintain the steps required to group them.
3. When you slide the window across, should you move the group to the right? Once you move the group to the right, it will never need to slide to the left again.

## 示例

```
[1,0,0,1,0,1]
2
[1,0,0,0,0,0,1,1]
3
[1,1,0,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMoves(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMoves(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMoves(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minMoves(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMoves(int[] nums, int k) {
        
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
var minMoves = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minMoves(nums: number[], k: number): number {
    
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
    function minMoves($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMoves(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMoves(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMoves(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minMoves(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_moves(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minMoves(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_moves(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-moves nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_moves(Nums :: [integer()], K :: integer()) -> integer().
min_moves(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_moves(nums :: [integer], k :: integer) :: integer
  def min_moves(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMoves(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

