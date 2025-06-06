# 3424. 将数组变相同的最小代价

## 题目描述

<p>给你两个长度都为 <code>n</code>&nbsp;的整数数组&nbsp;<code>arr</code> 和&nbsp;<code>brr</code>&nbsp;以及一个整数&nbsp;<code>k</code>&nbsp;。你可以对 <code>arr</code>&nbsp;执行以下操作任意次：</p>

<ul>
	<li>将&nbsp;<code>arr</code>&nbsp;分割成若干个&nbsp;<strong>连续的</strong>&nbsp;子数组，并将这些子数组按任意顺序重新排列。这个操作的代价为&nbsp;<code>k</code>&nbsp;。</li>
	<li>
	<p>选择 <code>arr</code>&nbsp;中的任意一个元素，将它增加或者减少一个正整数&nbsp;<code>x</code>&nbsp;。这个操作的代价为 <code>x</code>&nbsp;。</p>
	</li>
</ul>

<p>请你返回将 <code>arr</code>&nbsp;变为 <code>brr</code>&nbsp;的 <strong>最小</strong>&nbsp;总代价。</p>

<p><strong>子数组</strong>&nbsp;是一个数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>arr = [-7,9,5], brr = [7,-2,-5], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>13</span></p>

<p><b>解释：</b></p>

<ul>
	<li>将&nbsp;<code>arr</code>&nbsp;分割成两个连续子数组：<code>[-7]</code> 和&nbsp;<code>[9, 5]</code>&nbsp;然后将它们重新排列成&nbsp;<code>[9, 5, -7]</code>&nbsp;，代价为 2 。</li>
	<li>将&nbsp;<code>arr[0]</code>&nbsp;减小 2 ，数组变为&nbsp;<code>[7, 5, -7]</code>&nbsp;，操作代价为 2 。</li>
	<li>将&nbsp;<code>arr[1]</code>&nbsp;减小 7 ，数组变为&nbsp;<code>[7, -2, -7]</code>&nbsp;，操作代价为 7 。</li>
	<li>将&nbsp;<code>arr[2]</code>&nbsp;增加 2 ，数组变为&nbsp;<code>[7, -2, -5]</code>&nbsp;，操作代价为 2 。</li>
</ul>

<p>将两个数组变相等的总代价为&nbsp;<code>2 + 2 + 7 + 2 = 13</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>arr = [2,1], brr = [2,1], k = 0</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>由于数组已经相等，不需要进行任何操作，所以总代价为 0 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length == brr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= k &lt;= 2 * 10<sup>10</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= brr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. What does Operation 1 (rearranging subarrays) actually accomplish?
2. Calculate <code>sum(abs(arr[i] - brr[i]))</code> if you do not use Operation 1.
3. Calculate <code>sum(abs(arr[i] - brr[i]))</code> after sorting both arrays if you use Operation 1.

## 示例

```
[-7,9,5]
[7,-2,-5]
2
[2,1]
[2,1]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minCost(vector<int>& arr, vector<int>& brr, long long k) {
        
    }
};
```

### Java

```java
class Solution {
    public long minCost(int[] arr, int[] brr, long k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minCost(self, arr, brr, k):
        """
        :type arr: List[int]
        :type brr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        
```

### C

```c
long long minCost(int* arr, int arrSize, int* brr, int brrSize, long long k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinCost(int[] arr, int[] brr, long k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number[]} brr
 * @param {number} k
 * @return {number}
 */
var minCost = function(arr, brr, k) {
    
};
```

### TypeScript

```typescript
function minCost(arr: number[], brr: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[] $brr
     * @param Integer $k
     * @return Integer
     */
    function minCost($arr, $brr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minCost(_ arr: [Int], _ brr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minCost(arr: IntArray, brr: IntArray, k: Long): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minCost(List<int> arr, List<int> brr, int k) {
    
  }
}
```

### Go

```golang
func minCost(arr []int, brr []int, k int64) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer[]} brr
# @param {Integer} k
# @return {Integer}
def min_cost(arr, brr, k)
    
end
```

### Scala

```scala
object Solution {
    def minCost(arr: Array[Int], brr: Array[Int], k: Long): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_cost(arr: Vec<i32>, brr: Vec<i32>, k: i64) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (min-cost arr brr k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_cost(Arr :: [integer()], Brr :: [integer()], K :: integer()) -> integer().
min_cost(Arr, Brr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_cost(arr :: [integer], brr :: [integer], k :: integer) :: integer
  def min_cost(arr, brr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minCost(arr: Array<Int64>, brr: Array<Int64>, k: Int64): Int64 {

    }
}
```

