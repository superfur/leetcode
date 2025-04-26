# 747. 至少是其他数字两倍的最大数

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，其中总是存在 <strong>唯一的</strong> 一个最大整数 。</p>

<p>请你找出数组中的最大元素并检查它是否 <strong>至少是数组中每个其他数字的两倍</strong> 。如果是，则返回 <strong>最大元素的下标</strong> ，否则返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,6,1,0]
<strong>输出：</strong>1
<strong>解释：</strong>6 是最大的整数，对于数组中的其他整数，6 至少是数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>-1
<strong>解释：</strong>4 没有超过 3 的两倍大，所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> 中的最大元素是唯一的</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`.

Scan through the array again.  If we find some `x != m` with `m < 2*x`, we should return `-1`.

Otherwise, we should return `maxIndex`.

## 示例

```
[3,6,1,0]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int dominantIndex(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
```

### C

```c
int dominantIndex(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DominantIndex(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var dominantIndex = function(nums) {
    
};
```

### TypeScript

```typescript
function dominantIndex(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function dominantIndex($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func dominantIndex(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dominantIndex(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int dominantIndex(List<int> nums) {
    
  }
}
```

### Go

```golang
func dominantIndex(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def dominant_index(nums)
    
end
```

### Scala

```scala
object Solution {
    def dominantIndex(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn dominant_index(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (dominant-index nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec dominant_index(Nums :: [integer()]) -> integer().
dominant_index(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec dominant_index(nums :: [integer]) :: integer
  def dominant_index(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func dominantIndex(nums: Array<Int64>): Int64 {

    }
}
```

