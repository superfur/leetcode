# 3397. 执行操作后不同元素的最大数量

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code>。</p>

<p>你可以对数组中的每个元素&nbsp;<strong>最多</strong> 执行 <strong>一次&nbsp;</strong>以下操作：</p>

<ul>
	<li>将一个在范围&nbsp;<code>[-k, k]</code> 内的整数加到该元素上。</li>
</ul>

<p>返回执行这些操作后，<code>nums</code> 中可能拥有的不同元素的&nbsp;<strong>最大&nbsp;</strong>数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,2,3,3,4], k = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">6</span></p>

<p><strong>解释：</strong></p>

<p>对前四个元素执行操作，<code>nums</code> 变为 <code>[-1, 0, 1, 2, 3, 4]</code>，可以获得 6 个不同的元素。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [4,4,4,4], k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>对 <code>nums[0]</code> 加 -1，以及对 <code>nums[1]</code> 加 1，<code>nums</code> 变为 <code>[3, 5, 4, 4]</code>，可以获得 3 个不同的元素。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序

## 提示

1. Can we use sorting here?
2. Find the minimum element which is not used for each element.

## 示例

```
[1,2,2,3,3,4]
2
[4,4,4,4]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDistinctElements(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maxDistinctElements(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDistinctElements(int[] nums, int k) {
        
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
var maxDistinctElements = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxDistinctElements(nums: number[], k: number): number {
    
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
    function maxDistinctElements($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDistinctElements(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDistinctElements(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDistinctElements(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxDistinctElements(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_distinct_elements(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxDistinctElements(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_distinct_elements(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-distinct-elements nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_distinct_elements(Nums :: [integer()], K :: integer()) -> integer().
max_distinct_elements(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_distinct_elements(nums :: [integer], k :: integer) :: integer
  def max_distinct_elements(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDistinctElements(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

