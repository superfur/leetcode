# 330. 按要求补齐数组

## 题目描述

<p>给定一个已排序的正整数数组 <code>nums</code>&nbsp;<em>，</em>和一个正整数&nbsp;<code>n</code><em> 。</em>从&nbsp;<code>[1, n]</code>&nbsp;区间内选取任意个数字补充到&nbsp;nums&nbsp;中，使得&nbsp;<code>[1, n]</code>&nbsp;区间内的任何数字都可以用&nbsp;nums&nbsp;中某几个数字的和来表示。</p>

<p>请返回 <em>满足上述要求的最少需要补充的数字个数</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入: </strong>nums = <code>[1,3]</code>, n = <code>6</code>
<strong>输出: </strong>1 
<strong>解释:</strong>
根据 nums&nbsp;里现有的组合&nbsp;<code>[1], [3], [1,3]</code>，可以得出&nbsp;<code>1, 3, 4</code>。
现在如果我们将&nbsp;<code>2</code>&nbsp;添加到&nbsp;nums 中，&nbsp;组合变为: <code>[1], [2], [3], [1,3], [2,3], [1,2,3]</code>。
其和可以表示数字&nbsp;<code>1, 2, 3, 4, 5, 6</code>，能够覆盖&nbsp;<code>[1, 6]</code>&nbsp;区间里所有的数。
所以我们最少需要添加一个数字。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入: </strong>nums = <code>[1,5,10]</code>, n = <code>20</code>
<strong>输出:</strong> 2
<strong>解释: </strong>我们需要添加&nbsp;<code>[2,4]</code>。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<strong>输入: </strong>nums = <code>[1,2,2]</code>, n = <code>5</code>
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code>&nbsp;按 <strong>升序排列</strong></li>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组

## 示例

```
[1,3]
6
[1,5,10]
20
[1,2,2]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minPatches(vector<int>& nums, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int minPatches(int[] nums, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
```

### C

```c
int minPatches(int* nums, int numsSize, int n) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinPatches(int[] nums, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number}
 */
var minPatches = function(nums, n) {
    
};
```

### TypeScript

```typescript
function minPatches(nums: number[], n: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $n
     * @return Integer
     */
    function minPatches($nums, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minPatches(_ nums: [Int], _ n: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minPatches(nums: IntArray, n: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minPatches(List<int> nums, int n) {
    
  }
}
```

### Go

```golang
func minPatches(nums []int, n int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} n
# @return {Integer}
def min_patches(nums, n)
    
end
```

### Scala

```scala
object Solution {
    def minPatches(nums: Array[Int], n: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_patches(nums: Vec<i32>, n: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-patches nums n)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_patches(Nums :: [integer()], N :: integer()) -> integer().
min_patches(Nums, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_patches(nums :: [integer], n :: integer) :: integer
  def min_patches(nums, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minPatches(nums: Array<Int64>, n: Int64): Int64 {

    }
}
```

