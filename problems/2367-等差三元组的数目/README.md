# 2367. 等差三元组的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、<strong>严格递增</strong> 的整数数组 <code>nums</code> 和一个正整数 <code>diff</code> 。如果满足下述全部条件，则三元组 <code>(i, j, k)</code> 就是一个 <strong>等差三元组</strong> ：</p>

<ul>
	<li><code>i &lt; j &lt; k</code> ，</li>
	<li><code>nums[j] - nums[i] == diff</code> 且</li>
	<li><code>nums[k] - nums[j] == diff</code></li>
</ul>

<p>返回不同 <strong>等差三元组</strong> 的数目<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,4,6,7,10], diff = 3
<strong>输出：</strong>2
<strong>解释：</strong>
(1, 2, 4) 是等差三元组：7 - 4 == 3 且 4 - 1 == 3 。
(2, 4, 5) 是等差三元组：10 - 7 == 3 且 7 - 4 == 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,6,7,8,9], diff = 2
<strong>输出：</strong>2
<strong>解释：</strong>
(0, 2, 4) 是等差三元组：8 - 6 == 2 且 6 - 4 == 2 。
(1, 3, 5) 是等差三元组：9 - 7 == 2 且 7 - 5 == 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 200</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 200</code></li>
	<li><code>1 &lt;= diff &lt;= 50</code></li>
	<li><code>nums</code> <strong>严格</strong> 递增</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 双指针
- 枚举

## 提示

1. Are the constraints small enough for brute force?
2. We can use three loops, each iterating through the array to go through every possible triplet. Be sure to not count duplicates.

## 示例

```
[0,1,4,6,7,10]
3
[4,5,6,7,8,9]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        
    }
};
```

### Java

```java
class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        
    }
}
```

### Python

```python
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
```

### C

```c
int arithmeticTriplets(int* nums, int numsSize, int diff) {
    
}
```

### C#

```csharp
public class Solution {
    public int ArithmeticTriplets(int[] nums, int diff) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} diff
 * @return {number}
 */
var arithmeticTriplets = function(nums, diff) {
    
};
```

### TypeScript

```typescript
function arithmeticTriplets(nums: number[], diff: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $diff
     * @return Integer
     */
    function arithmeticTriplets($nums, $diff) {
        
    }
}
```

### Swift

```swift
class Solution {
    func arithmeticTriplets(_ nums: [Int], _ diff: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun arithmeticTriplets(nums: IntArray, diff: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int arithmeticTriplets(List<int> nums, int diff) {
    
  }
}
```

### Go

```golang
func arithmeticTriplets(nums []int, diff int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} diff
# @return {Integer}
def arithmetic_triplets(nums, diff)
    
end
```

### Scala

```scala
object Solution {
    def arithmeticTriplets(nums: Array[Int], diff: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn arithmetic_triplets(nums: Vec<i32>, diff: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (arithmetic-triplets nums diff)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec arithmetic_triplets(Nums :: [integer()], Diff :: integer()) -> integer().
arithmetic_triplets(Nums, Diff) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec arithmetic_triplets(nums :: [integer], diff :: integer) :: integer
  def arithmetic_triplets(nums, diff) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func arithmeticTriplets(nums: Array<Int64>, diff: Int64): Int64 {

    }
}
```

