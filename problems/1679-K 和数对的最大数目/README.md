# 1679. K 和数对的最大数目

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。</p>

<p>每一步操作中，你需要从数组中选出和为 <code>k</code> 的两个整数，并将它们移出数组。</p>

<p>返回你可以对数组执行的最大操作数。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], k = 5
<strong>输出：</strong>2
<strong>解释：</strong>开始时 nums = [1,2,3,4]：
- 移出 1 和 4 ，之后 nums = [2,3]
- 移出 2 和 3 ，之后 nums = []
不再有和为 5 的数对，因此最多执行 2 次操作。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,4,3], k = 6
<strong>输出：</strong>1
<strong>解释：</strong>开始时 nums = [3,1,3,4,3]：
- 移出前两个 3 ，之后nums = [1,4,3]
不再有和为 6 的数对，因此最多执行 1 次操作。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= k <= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 排序

## 提示

1. The abstract problem asks to count the number of disjoint pairs with a given sum k.
2. For each possible value x, it can be paired up with k - x.
3. The number of such pairs equals to  min(count(x), count(k-x)), unless that x = k / 2, where the number of such pairs will be floor(count(x) / 2).

## 示例

```
[1,2,3,4]
5
[3,1,3,4,3]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxOperations(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maxOperations(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxOperations(int[] nums, int k) {
        
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
var maxOperations = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maxOperations(nums: number[], k: number): number {
    
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
    function maxOperations($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxOperations(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxOperations(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxOperations(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maxOperations(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_operations(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maxOperations(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_operations(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_operations(Nums :: [integer()], K :: integer()) -> integer().
max_operations(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_operations(nums :: [integer], k :: integer) :: integer
  def max_operations(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxOperations(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

