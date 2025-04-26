# 1248. 统计「优美子数组」

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 和一个整数 <code>k</code>。如果某个连续子数组中恰好有 <code>k</code> 个奇数数字，我们就认为这个子数组是「<strong>优美子数组</strong>」。</p>

<p>请返回这个数组中 <strong>「优美子数组」</strong> 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2,1,1], k = 3
<strong>输出：</strong>2
<strong>解释：</strong>包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,6], k = 1
<strong>输出：</strong>0
<strong>解释：</strong>数列中不包含任何奇数，所以不存在优美子数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2,1,2,2,1,2,2,2], k = 2
<strong>输出：</strong>16
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10^5</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 前缀和
- 滑动窗口

## 提示

1. After replacing each even by zero and every odd by one can we use prefix sum to find answer ?
2. Can we use two pointers to count number of sub-arrays ?
3. Can we store the indices of odd numbers and for each k indices count the number of sub-arrays that contains them ?

## 示例

```
[1,1,2,1,1]
3
[2,4,6]
1
[2,2,2,1,2,2,1,2,2,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int numberOfSubarrays(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSubarrays(int[] nums, int k) {
        
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
var numberOfSubarrays = function(nums, k) {
    
};
```

### TypeScript

```typescript
function numberOfSubarrays(nums: number[], k: number): number {
    
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
    function numberOfSubarrays($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSubarrays(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSubarrays(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSubarrays(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func numberOfSubarrays(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def number_of_subarrays(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSubarrays(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-subarrays nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_subarrays(Nums :: [integer()], K :: integer()) -> integer().
number_of_subarrays(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_subarrays(nums :: [integer], k :: integer) :: integer
  def number_of_subarrays(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSubarrays(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

