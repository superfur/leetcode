# 1959. K 次调整数组大小浪费的最小总空间

## 题目描述

<p>你正在设计一个动态数组。给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，其中&nbsp;<code>nums[i]</code>&nbsp;是&nbsp;<code>i</code>&nbsp;时刻数组中的元素数目。除此以外，你还有一个整数 <code>k</code>&nbsp;，表示你可以 <strong>调整</strong>&nbsp;数组大小的 <strong>最多</strong>&nbsp;次数（每次都可以调整成 <strong>任意</strong>&nbsp;大小）。</p>

<p><code>t</code>&nbsp;时刻数组的大小&nbsp;<code>size<sub>t</sub></code>&nbsp;必须大于等于&nbsp;<code>nums[t]</code>&nbsp;，因为数组需要有足够的空间容纳所有元素。<code>t</code>&nbsp;时刻 <strong>浪费的空间</strong>&nbsp;为&nbsp;<code>size<sub>t</sub> - nums[t]</code>&nbsp;，<strong>总</strong>&nbsp;浪费空间为满足&nbsp;<code>0 &lt;= t &lt; nums.length</code>&nbsp;的每一个时刻&nbsp;<code>t</code>&nbsp;浪费的空间&nbsp;<strong>之和</strong>&nbsp;。</p>

<p>在调整数组大小不超过 <code>k</code>&nbsp;次的前提下，请你返回 <strong>最小总浪费空间</strong>&nbsp;。</p>

<p><strong>注意：</strong>数组最开始时可以为&nbsp;<strong>任意大小</strong>&nbsp;，且&nbsp;<strong>不计入</strong>&nbsp;调整大小的操作次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [10,20], k = 0
<b>输出：</b>10
<b>解释：</b>size = [20,20].
我们可以让数组初始大小为 20 。
总浪费空间为 (20 - 10) + (20 - 20) = 10 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [10,20,30], k = 1
<b>输出：</b>10
<b>解释：</b>size = [20,20,30].
我们可以让数组初始大小为 20 ，然后时刻 2 调整大小为 30 。
总浪费空间为 (20 - 10) + (20 - 20) + (30 - 30) = 10 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [10,20,15,30,20], k = 2
<b>输出：</b>15
<b>解释：</b>size = [10,20,20,30,30].
我们可以让数组初始大小为 10 ，时刻 1 调整大小为 20 ，时刻 3 调整大小为 30 。
总浪费空间为 (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 200</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k &lt;= nums.length - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Given a range, how can you find the minimum waste if you can't perform any resize operations?
2. Can we build our solution using dynamic programming using the current index and the number of resizing operations performed as the states?

## 示例

```
[10,20]
0
[10,20,30]
1
[10,20,15,30,20]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSpaceWastedKResizing(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSpaceWastedKResizing(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSpaceWastedKResizing(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minSpaceWastedKResizing(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSpaceWastedKResizing(int[] nums, int k) {
        
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
var minSpaceWastedKResizing = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minSpaceWastedKResizing(nums: number[], k: number): number {
    
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
    function minSpaceWastedKResizing($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSpaceWastedKResizing(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSpaceWastedKResizing(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSpaceWastedKResizing(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minSpaceWastedKResizing(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_space_wasted_k_resizing(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minSpaceWastedKResizing(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_space_wasted_k_resizing(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-space-wasted-k-resizing nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_space_wasted_k_resizing(Nums :: [integer()], K :: integer()) -> integer().
min_space_wasted_k_resizing(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_space_wasted_k_resizing(nums :: [integer], k :: integer) :: integer
  def min_space_wasted_k_resizing(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSpaceWastedKResizing(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

