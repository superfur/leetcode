# 3086. 拾起 K 个 1 需要的最少行动次数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二进制数组 <code>nums</code>，其长度为 <code>n</code> ；另给你一个 <strong>正整数 </strong><code>k</code> 以及一个 <strong>非负整数 </strong><code>maxChanges</code> 。</p>

<p>Alice 在玩一个游戏，游戏的目标是让&nbsp;Alice 使用 <strong>最少 </strong>数量的 <strong>行动 </strong>次数从 <code>nums</code> 中拾起 <code>k</code> 个 1 。游戏开始时，Alice 可以选择数组 <code>[0, n - 1]</code> 范围内的任何索引&nbsp;<code>aliceIndex</code> 站立。如果 <code>nums[aliceIndex] == 1</code> ，Alice 会拾起一个 1 ，并且 <code>nums[aliceIndex]</code> 变成<code>0</code>（这<strong> 不算 </strong>作一次行动）。之后，Alice 可以执行 <strong>任意数量</strong> 的 <strong>行动</strong>（<strong>包括</strong><strong>零次</strong>），在每次行动中&nbsp;Alice 必须 <strong>恰好 </strong>执行以下动作之一：</p>

<ul>
	<li>选择任意一个下标 <code>j != aliceIndex</code> 且满足 <code>nums[j] == 0</code> ，然后将 <code>nums[j]</code> 设置为 <code>1</code> 。这个动作最多可以执行 <code>maxChanges</code> 次。</li>
	<li>选择任意两个相邻的下标 <code>x</code> 和 <code>y</code>（<code>|x - y| == 1</code>）且满足 <code>nums[x] == 1</code>, <code>nums[y] == 0</code> ，然后交换它们的值（将 <code>nums[y] = 1</code> 和 <code>nums[x] = 0</code>）。如果 <code>y == aliceIndex</code>，在这次行动后&nbsp;Alice 拾起一个 1 ，并且 <code>nums[y]</code> 变成 <code>0</code> 。</li>
</ul>

<p>返回&nbsp;Alice 拾起 <strong>恰好 </strong><code>k</code> 个 1 所需的 <strong>最少 </strong>行动次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [1,1,0,0,0,1,1,0,0,1], k = 3, maxChanges = 1</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">3</span></p>

<p><strong>解释：</strong>如果游戏开始时&nbsp;Alice 在 <code>aliceIndex == 1</code> 的位置上，按照以下步骤执行每个动作，他可以利用 <code>3</code> 次行动拾取 <code>3</code> 个 1 ：</p>

<ul>
	<li>游戏开始时&nbsp;Alice 拾取了一个 1 ，<code>nums[1]</code> 变成了 <code>0</code>。此时 <code>nums</code> 变为 <code>[1,<strong><u>0</u></strong>,0,0,0,1,1,0,0,1]</code> 。</li>
	<li>选择 <code>j == 2</code> 并执行第一种类型的动作。<code>nums</code> 变为 <code>[1,<strong><u>0</u></strong>,1,0,0,1,1,0,0,1]</code></li>
	<li>选择 <code>x == 2</code> 和 <code>y == 1</code> ，并执行第二种类型的动作。<code>nums</code> 变为 <code>[1,<strong><u>1</u></strong>,0,0,0,1,1,0,0,1]</code> 。由于 <code>y == aliceIndex</code>，Alice 拾取了一个 1 ，<code>nums</code> 变为&nbsp; <code>[1,<strong><u>0</u></strong>,0,0,0,1,1,0,0,1]</code> 。</li>
	<li>选择 <code>x == 0</code> 和 <code>y == 1</code> ，并执行第二种类型的动作。<code>nums</code> 变为 <code>[0,<strong><u>1</u></strong>,0,0,0,1,1,0,0,1]</code> 。由于 <code>y == aliceIndex</code>，Alice 拾取了一个 1 ，<code>nums</code> 变为&nbsp; <code>[0,<strong><u>0</u></strong>,0,0,0,1,1,0,0,1]</code> 。</li>
</ul>

<p>请注意，Alice 也可能执行其他的 <code>3</code> 次行动序列达成拾取 <code>3</code> 个 1 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;"><!-- 以下是示例内容的中文翻译，同时保留了原有的HTML格式和注释 -->
<p><strong>输入：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">nums = [0,0,0,0], k = 2, maxChanges = 3</span></p>

<p><strong>输出：</strong><span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;">4</span></p>

<p><strong>解释：</strong>如果游戏开始时&nbsp;Alice 在 <code>aliceIndex == 0</code> 的位置上，按照以下步骤执行每个动作，他可以利用 <code>4</code> 次行动拾取 <code>2</code> 个 1 ：</p>

<ul>
	<li>选择 <code>j == 1</code> 并执行第一种类型的动作。<code>nums</code> 变为 <code>[<strong><u>0</u></strong>,1,0,0]</code> 。</li>
	<li>选择 <code>x == 1</code> 和 <code>y == 0</code> ，并执行第二种类型的动作。<code>nums</code> 变为 <code>[<strong><u>1</u></strong>,0,0,0]</code> 。由于 <code>y == aliceIndex</code>，Alice 拾起了一个 1 ，<code>nums</code> 变为 <code>[<strong><u>0</u></strong>,0,0,0]</code> 。</li>
	<li>再次选择 <code>j == 1</code> 并执行第一种类型的动作。<code>nums</code> 变为 <code>[<strong><u>0</u></strong>,1,0,0]</code> 。</li>
	<li>再次选择 <code>x == 1</code> 和 <code>y == 0</code> ，并执行第二种类型的动作。<code>nums</code> 变为 <code>[<strong><u>1</u></strong>,0,0,0]</code> 。由于<code>y == aliceIndex</code>，Alice 拾起了一个 1 ，<code>nums</code> 变为 <code>[<strong><u>0</u></strong>,0,0,0]</code> 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= maxChanges &lt;= 10<sup>5</sup></code></li>
	<li><code>maxChanges + sum(nums) &gt;= k</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 前缀和
- 滑动窗口

## 提示

1. Ones created using a change require <code>2</code> moves. Hence except for the immediate neighbors of the index where we move all the ones, we should try to use change operations.
2. For some subset of ones, it is always better to move the ones to the median position.
3. We only need to be concerned with the indices where <code>nums[i] == 1</code>.

## 示例

```
[1,1,0,0,0,1,1,0,0,1]
3
1
[0,0,0,0]
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumMoves(vector<int>& nums, int k, int maxChanges) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumMoves(int[] nums, int k, int maxChanges) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumMoves(self, nums, k, maxChanges):
        """
        :type nums: List[int]
        :type k: int
        :type maxChanges: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        
```

### C

```c
long long minimumMoves(int* nums, int numsSize, int k, int maxChanges) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumMoves(int[] nums, int k, int maxChanges) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} maxChanges
 * @return {number}
 */
var minimumMoves = function(nums, k, maxChanges) {
    
};
```

### TypeScript

```typescript
function minimumMoves(nums: number[], k: number, maxChanges: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $maxChanges
     * @return Integer
     */
    function minimumMoves($nums, $k, $maxChanges) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumMoves(_ nums: [Int], _ k: Int, _ maxChanges: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumMoves(nums: IntArray, k: Int, maxChanges: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumMoves(List<int> nums, int k, int maxChanges) {
    
  }
}
```

### Go

```golang
func minimumMoves(nums []int, k int, maxChanges int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} max_changes
# @return {Integer}
def minimum_moves(nums, k, max_changes)
    
end
```

### Scala

```scala
object Solution {
    def minimumMoves(nums: Array[Int], k: Int, maxChanges: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_moves(nums: Vec<i32>, k: i32, max_changes: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-moves nums k maxChanges)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_moves(Nums :: [integer()], K :: integer(), MaxChanges :: integer()) -> integer().
minimum_moves(Nums, K, MaxChanges) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_moves(nums :: [integer], k :: integer, max_changes :: integer) :: integer
  def minimum_moves(nums, k, max_changes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumMoves(nums: Array<Int64>, k: Int64, maxChanges: Int64): Int64 {

    }
}
```

