# 1787. 使所有区间的异或结果为零

## 题目描述

<p>给你一个整数数组 <code>nums</code>​​​ 和一个整数 <code>k</code>​​​​​ 。区间 <code>[left, right]</code>（<code>left <= right</code>）的 <strong>异或结果</strong> 是对下标位于 <code>left</code> 和 <code>right</code>（包括 <code>left</code> 和 <code>right</code> ）之间所有元素进行 <code>XOR</code> 运算的结果：<code>nums[left] XOR nums[left+1] XOR ... XOR nums[right]</code> 。</p>

<p>返回数组中 <strong>要更改的最小元素数</strong> ，以使所有长度为 <code>k</code> 的区间异或结果等于零。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,0,3,0], k = 1
<strong>输出：</strong>3
<strong>解释：</strong>将数组 [<strong>1</strong>,<strong>2</strong>,0,<strong>3</strong>,0] 修改为 [<strong>0</strong>,<strong>0</strong>,0,<strong>0</strong>,0]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,5,2,1,7,3,4,7], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>将数组 [3,4,<strong>5</strong>,<strong>2</strong>,<strong>1</strong>,7,3,4,7] 修改为 [3,4,<strong>7</strong>,<strong>3</strong>,<strong>4</strong>,7,3,4,7]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,4,1,2,5,1,2,6], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>将数组[1,2,<strong>4,</strong>1,2,<strong>5</strong>,1,2,<strong>6</strong>] 修改为 [1,2,<strong>3</strong>,1,2,<strong>3</strong>,1,2,<strong>3</strong>]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k <= nums.length <= 2000</code></li>
	<li><code>​​​​​​0 <= nums[i] < 2<sup>10</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划

## 提示

1. Let's note that for the XOR of all segments with size K to be equal to zeros, nums[i] has to be equal to nums[i+k]
2. Basically, we need to make the first K elements have XOR = 0 and then modify them.

## 示例

```
[1,2,0,3,0]
1
[3,4,5,2,1,7,3,4,7]
3
[1,2,4,1,2,5,1,2,6]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minChanges(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minChanges(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minChanges(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minChanges(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinChanges(int[] nums, int k) {
        
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
var minChanges = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minChanges(nums: number[], k: number): number {
    
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
    function minChanges($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minChanges(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minChanges(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minChanges(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minChanges(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_changes(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minChanges(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_changes(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-changes nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_changes(Nums :: [integer()], K :: integer()) -> integer().
min_changes(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_changes(nums :: [integer], k :: integer) :: integer
  def min_changes(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minChanges(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

