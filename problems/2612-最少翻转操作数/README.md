# 2612. 最少翻转操作数

## 题目描述

<p>给定一个整数&nbsp;<code>n</code>&nbsp;和一个整数&nbsp;<code>p</code>，它们表示一个长度为 <code>n</code> 且除了下标为&nbsp;<code>p</code>&nbsp;处是 <code>1</code>&nbsp;以外，其他所有数都是 <code>0</code>&nbsp;的数组&nbsp;<code>arr</code>。同时给定一个整数数组&nbsp;<code>banned</code>&nbsp;，它包含数组中的一些限制位置。在&nbsp;<code>arr</code>&nbsp;上进行下列操作：</p>

<ul>
	<li>如果单个 1 不在&nbsp;<code>banned</code>&nbsp;中的位置上，反转大小为 <code>k</code> 的 <strong><span data-keyword="subarray-nonempty">子数组</span></strong>。</li>
</ul>

<p>返回一个包含&nbsp;<code>n</code>&nbsp;个结果的整数数组&nbsp;<code>answer</code>，其中第&nbsp;<code>i</code>&nbsp;个结果是将&nbsp;<code>1</code>&nbsp;放到位置&nbsp;<code>i</code>&nbsp;处所需的&nbsp;<strong>最少</strong>&nbsp;翻转操作次数，如果无法放到位置&nbsp;<code>i</code>&nbsp;处，此数为&nbsp;<code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 4, p = 0, banned = [1,2], k = 4</span></p>

<p><span class="example-io"><b>输出：</b>[0,-1,-1,1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>一开始 1 位于位置 0，因此我们需要在位置 0 上的操作数是 0。</li>
	<li>我们不能将 1 放置在被禁止的位置上，所以位置 1 和 2 的答案是 -1。</li>
	<li>执行大小为 4 的操作以反转整个数组。</li>
	<li>在一次操作后，1 位于位置 3，因此位置 3 的答案是 1。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 5, p = 0, banned = [2,4], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>[0,-1,-1,-1,-1]</span></p>

<p><b>解释：</b></p>

<ul>
	<li>一开始 1 位于位置 0，因此我们需要在位置 0 上的操作数是 0。</li>
	<li>我们不能在&nbsp;<code>[0, 2]</code>&nbsp;的子数组位置上执行操作，因为位置 2 在 banned 中。</li>
	<li>由于 1 不能够放置在位置 2 上，使用更多操作将 1 放置在其它位置上是不可能的。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 4, p = 2, banned = [0,1,3], k = 1</span></p>

<p><span class="example-io"><b>输出：</b>[-1,-1,0,-1]</span></p>

<p><strong>解释：</strong></p>

<p>执行大小为 1 的操作，且 1 永远不会改变位置。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= p &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned.length &lt;= n - 1</code></li>
	<li><code>0 &lt;= banned[i] &lt;= n - 1</code></li>
	<li><code>1 &lt;= k &lt;= n&nbsp;</code></li>
	<li><code>banned[i] != p</code></li>
	<li><code>banned</code>&nbsp;中的值 <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 有序集合

## 提示

1. Can we use a breadth-first search to find the minimum number of operations?
2. Find the beginning and end indices of the subarray of size k that can be reversed to bring 1 to a particular position.
3. Can we visit every index or do we need to consider the parity of k?

## 示例

```
4
0
[1,2]
4
5
0
[2,4]
3
4
2
[0,1,3]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] minReverseOperations(int n, int p, int[] banned, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minReverseOperations(self, n, p, banned, k):
        """
        :type n: int
        :type p: int
        :type banned: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minReverseOperations(self, n: int, p: int, banned: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minReverseOperations(int n, int p, int* banned, int bannedSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MinReverseOperations(int n, int p, int[] banned, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} p
 * @param {number[]} banned
 * @param {number} k
 * @return {number[]}
 */
var minReverseOperations = function(n, p, banned, k) {
    
};
```

### TypeScript

```typescript
function minReverseOperations(n: number, p: number, banned: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $p
     * @param Integer[] $banned
     * @param Integer $k
     * @return Integer[]
     */
    function minReverseOperations($n, $p, $banned, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minReverseOperations(_ n: Int, _ p: Int, _ banned: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minReverseOperations(n: Int, p: Int, banned: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minReverseOperations(int n, int p, List<int> banned, int k) {
    
  }
}
```

### Go

```golang
func minReverseOperations(n int, p int, banned []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} p
# @param {Integer[]} banned
# @param {Integer} k
# @return {Integer[]}
def min_reverse_operations(n, p, banned, k)
    
end
```

### Scala

```scala
object Solution {
    def minReverseOperations(n: Int, p: Int, banned: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_reverse_operations(n: i32, p: i32, banned: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (min-reverse-operations n p banned k)
  (-> exact-integer? exact-integer? (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_reverse_operations(N :: integer(), P :: integer(), Banned :: [integer()], K :: integer()) -> [integer()].
min_reverse_operations(N, P, Banned, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_reverse_operations(n :: integer, p :: integer, banned :: [integer], k :: integer) :: [integer]
  def min_reverse_operations(n, p, banned, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minReverseOperations(n: Int64, p: Int64, banned: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

