# 2735. 收集巧克力

## 题目描述

<p>给你一个长度为 <code>n</code>、下标从 <strong>0</strong> 开始的整数数组 <code>nums</code>，<code>nums[i]</code> 表示收集位于下标 <code>i</code> 处的巧克力成本。每个巧克力都对应一个不同的类型，最初，位于下标 <code>i</code> 的巧克力就对应第 <code>i</code> 个类型。</p>

<p>在一步操作中，你可以用成本 <code>x</code> 执行下述行为：</p>

<ul>
	<li>同时修改所有巧克力的类型，将巧克力的类型&nbsp;<code>i<sup>th</sup></code>&nbsp;修改为类型&nbsp;<code>((i + 1) mod n)<sup>th</sup></code>。</li>
</ul>

<p>假设你可以执行任意次操作，请返回收集所有类型巧克力所需的最小成本。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [20,1,15], x = 5
<strong>输出：</strong>13
<strong>解释：</strong>最开始，巧克力的类型分别是 [0,1,2] 。我们可以用成本 1 购买第 1 个类型的巧克力。
接着，我们用成本 5 执行一次操作，巧克力的类型变更为 [1,2,0] 。我们可以用成本 1 购买第 2 个类型的巧克力。
然后，我们用成本 5 执行一次操作，巧克力的类型变更为 [2,0,1] 。我们可以用成本 1 购买第 0 个类型的巧克力。
因此，收集所有类型的巧克力需要的总成本是 (1 + 5 + 1 + 5 + 1) = 13 。可以证明这是一种最优方案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3], x = 4
<strong>输出：</strong>6
<strong>解释：</strong>我们将会按最初的成本收集全部三个类型的巧克力，而不需执行任何操作。因此，收集所有类型的巧克力需要的总成本是 1 + 2 + 3 = 6 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= x &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 枚举

## 提示

1. How many maximum rotations will be needed?
2. The array will be rotated for a max of N times, so try all possibilities as N = 1000.

## 示例

```
[20,1,15]
5
[1,2,3]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minCost(vector<int>& nums, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public long minCost(int[] nums, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        
```

### C

```c
long long minCost(int* nums, int numsSize, int x) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinCost(int[] nums, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} x
 * @return {number}
 */
var minCost = function(nums, x) {
    
};
```

### TypeScript

```typescript
function minCost(nums: number[], x: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $x
     * @return Integer
     */
    function minCost($nums, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ nums: [Int], _ x: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(nums: IntArray, x: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<int> nums, int x) {
    
  }
}
```

### Go

```golang
func minCost(nums []int, x int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_cost(nums, x)
    
end
```

### Scala

```scala
object Solution {
    def minCost(nums: Array[Int], x: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(nums: Vec<i32>, x: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost nums x)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Nums :: [integer()], X :: integer()) -> integer().
min_cost(Nums, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(nums :: [integer], x :: integer) :: integer
  def min_cost(nums, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(nums: Array<Int64>, x: Int64): Int64 {

    }
}
```

