# 2344. 使数组可以被整除的最少删除次数

## 题目描述

<p>给你两个正整数数组&nbsp;<code>nums</code> 和&nbsp;<code>numsDivide</code>&nbsp;。你可以从&nbsp;<code>nums</code>&nbsp;中删除任意数目的元素。</p>

<p>请你返回使 <code>nums</code>&nbsp;中 <strong>最小</strong>&nbsp;元素可以整除 <code>numsDivide</code>&nbsp;中所有元素的 <strong>最少</strong>&nbsp;删除次数。如果无法得到这样的元素，返回 <code>-1</code>&nbsp;。</p>

<p>如果&nbsp;<code>y % x == 0</code>&nbsp;，那么我们说整数&nbsp;<code>x</code>&nbsp;整除&nbsp;<code>y</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,3,2,4,3], numsDivide = [9,6,9,3,15]
<b>输出：</b>2
<b>解释：</b>
[2,3,2,4,3] 中最小元素是 2 ，它无法整除 numsDivide 中所有元素。
我们从 nums 中删除 2 个大小为 2 的元素，得到 nums = [3,4,3] 。
[3,4,3] 中最小元素为 3 ，它可以整除 numsDivide 中所有元素。
可以证明 2 是最少删除次数。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [4,3,6], numsDivide = [8,2,6,10]
<b>输出：</b>-1
<b>解释：</b>
我们想 nums 中的最小元素可以整除 numsDivide 中的所有元素。
没有任何办法可以达到这一目的。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, numsDivide.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], numsDivide[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 数论
- 排序
- 堆（优先队列）

## 提示

1. How can we find an integer x that divides all the elements of numsDivide?
2. Will finding GCD (Greatest Common Divisor) help here?

## 示例

```
[2,3,2,4,3]
[9,6,9,3,15]
[4,3,6]
[8,2,6,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& numsDivide) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[] nums, int[] numsDivide) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
```

### C

```c
int minOperations(int* nums, int numsSize, int* numsDivide, int numsDivideSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[] nums, int[] numsDivide) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} numsDivide
 * @return {number}
 */
var minOperations = function(nums, numsDivide) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[], numsDivide: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $numsDivide
     * @return Integer
     */
    function minOperations($nums, $numsDivide) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ numsDivide: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray, numsDivide: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums, List<int> numsDivide) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int, numsDivide []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} nums_divide
# @return {Integer}
def min_operations(nums, nums_divide)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: Array[Int], numsDivide: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, nums_divide: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums numsDivide)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()], NumsDivide :: [integer()]) -> integer().
min_operations(Nums, NumsDivide) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], nums_divide :: [integer]) :: integer
  def min_operations(nums, nums_divide) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: Array<Int64>, numsDivide: Array<Int64>): Int64 {

    }
}
```

