# 2934. 最大化数组末位元素的最少操作次数

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的整数数组 <code>nums1</code> 和 <code>nums2</code> ，这两个数组的长度都是 <code>n</code> 。</p>

<p>你可以执行一系列<strong> 操作（可能不执行）</strong>。</p>

<p>在每次操作中，你可以选择一个在范围 <code>[0, n - 1]</code> 内的下标 <code>i</code> ，并交换 <code>nums1[i]</code> 和 <code>nums2[i]</code> 的值。</p>

<p>你的任务是找到满足以下条件所需的 <strong>最小</strong> 操作次数：</p>

<ul>
	<li><code>nums1[n - 1]</code> 等于 <code>nums1</code> 中所有元素的 <strong>最大值</strong> ，即 <code>nums1[n - 1] = max(nums1[0], nums1[1], ..., nums1[n - 1])</code> 。</li>
	<li><code>nums2[n - 1]</code> 等于 <code>nums2</code> 中所有元素的 <strong>最大值</strong> ，即 <code>nums2[n - 1] = max(nums2[0], nums2[1], ..., nums2[n - 1])</code> 。</li>
</ul>

<p>以整数形式，表示并返回满足上述 <strong>全部</strong> 条件所需的 <strong>最小</strong> 操作次数，如果无法同时满足两个条件，则返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,2,7]，nums2 = [4,5,3]
<strong>输出：</strong>1
<strong>解释：</strong>在这个示例中，可以选择下标 i = 2 执行一次操作。
交换 nums1[2] 和 nums2[2] 的值，nums1 变为 [1,2,3] ，nums2 变为 [4,5,7] 。
同时满足两个条件。
可以证明，需要执行的最小操作次数为 1 。
因此，答案是 1 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [2,3,4,5,9]，nums2 = [8,8,4,4,4]
<strong>输出：</strong>2
<strong>解释：</strong>在这个示例中，可以执行以下操作：
首先，选择下标 i = 4 执行操作。
交换 nums1[4] 和 nums2[4] 的值，nums1 变为 [2,3,4,5,4] ，nums2 变为 [8,8,4,4,9] 。
然后，选择下标 i = 3 执行操作。
交换 nums1[3] 和 nums2[3] 的值，nums1 变为 [2,3,4,4,4] ，nums2 变为 [8,8,4,5,9] 。
同时满足两个条件。 
可以证明，需要执行的最小操作次数为 2 。 
因此，答案是 2 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums1 = [1,5,4]，nums2 = [2,5,3]
<strong>输出：</strong>-1
<strong>解释：</strong>在这个示例中，无法同时满足两个条件。
因此，答案是 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums1.length == nums2.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums1[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= nums2[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 枚举

## 提示

1. Consider how to calculate the minimum number of operations when <code>nums1[n - 1]</code> and <code>nums2[n - 1]</code> are fixed (they are not swapped).
2. For each index <code>i</code>, there are only <code>3</code> possibilities: <ul>
<li><code>nums1[i] <= nums1[n - 1] && nums2[i] <= nums2[n - 1]</code>. We don't need to swap them.</li>
<li><code>nums1[i] <= nums2[n - 1] && nums2[i] <= nums1[n - 1]</code>. We have to swap them.</li>
<li>Otherwise, there is no solution.</li>
</ul>
3. There are <code>2</code> cases to determine the minimum number of operations: <ul>
<li>The first case is the number of indices that need to be swapped when <code>nums1[n - 1]</code> and <code>nums2[n - 1]</code> are fixed.</li>
<li>The second case is <code>1 +</code> the number of indices that need to be swapped when <code>nums1[n - 1]</code> and <code>nums2[n - 1]</code> are swapped.</li>
</ul>
4. The answer is the minimum of both cases or <code>-1</code> if there is no solution in either case.

## 示例

```
[1,2,7]
[4,5,3]
[2,3,4,5,9]
[8,8,4,4,4]
[1,5,4]
[2,5,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int minOperations(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var minOperations = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function minOperations(nums1: number[], nums2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function minOperations($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func minOperations(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_operations(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
min_operations(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums1 :: [integer], nums2 :: [integer]) :: integer
  def min_operations(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

