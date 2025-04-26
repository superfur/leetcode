# 2176. 统计数组中相等且可以被整除的数对

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，请你返回满足&nbsp;<code>0 &lt;= i &lt; j &lt; n</code>&nbsp;，<code>nums[i] == nums[j]</code> 且&nbsp;<code>(i * j)</code>&nbsp;能被&nbsp;<code>k</code>&nbsp;整除的数对&nbsp;<code>(i, j)</code>&nbsp;的&nbsp;<strong>数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,1,2,2,2,1,3], k = 2
<b>输出：</b>4
<strong>解释：</strong>
总共有 4 对数符合所有要求：
- nums[0] == nums[6] 且 0 * 6 == 0 ，能被 2 整除。
- nums[2] == nums[3] 且 2 * 3 == 6 ，能被 2 整除。
- nums[2] == nums[4] 且 2 * 4 == 8 ，能被 2 整除。
- nums[3] == nums[4] 且 3 * 4 == 12 ，能被 2 整除。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,4], k = 1
<b>输出：</b>0
<b>解释：</b>由于数组中没有重复数值，所以没有数对 (i,j) 符合所有要求。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i], k &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. For every possible pair of indices (i, j) where i < j, check if it satisfies the given conditions.

## 示例

```
[3,1,2,2,2,1,3]
2
[1,2,3,4]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPairs(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int countPairs(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPairs(int[] nums, int k) {
        
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
var countPairs = function(nums, k) {
    
};
```

### TypeScript

```typescript
function countPairs(nums: number[], k: number): number {
    
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
    function countPairs($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPairs(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func countPairs(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_pairs(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pairs(Nums :: [integer()], K :: integer()) -> integer().
count_pairs(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer], k :: integer) :: integer
  def count_pairs(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

