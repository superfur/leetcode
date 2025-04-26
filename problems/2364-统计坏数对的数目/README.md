# 2364. 统计坏数对的数目

## 题目描述

<p>给你一个下标从<strong>&nbsp;0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。如果 <code>i &lt; j</code>&nbsp;且&nbsp;<code>j - i != nums[j] - nums[i]</code>&nbsp;，那么我们称&nbsp;<code>(i, j)</code>&nbsp;是一个 <strong>坏</strong><strong>数对</strong>&nbsp;。</p>

<p>请你返回 <code>nums</code>&nbsp;中 <strong>坏数对</strong>&nbsp;的总数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [4,1,3,3]
<b>输出：</b>5
<b>解释：</b>数对 (0, 1) 是坏数对，因为 1 - 0 != 1 - 4 。
数对 (0, 2) 是坏数对，因为 2 - 0 != 3 - 4, 2 != -1 。
数对 (0, 3) 是坏数对，因为 3 - 0 != 3 - 4, 3 != -1 。
数对 (1, 2) 是坏数对，因为 2 - 1 != 3 - 1, 1 != 2 。
数对 (2, 3) 是坏数对，因为 3 - 2 != 3 - 3, 1 != 0 。
总共有 5 个坏数对，所以我们返回 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,4,5]
<b>输出：</b>0
<strong>解释：</strong>没有坏数对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 计数

## 提示

1. Would it be easier to count the number of pairs that are not bad pairs?
2. Notice that (j - i != nums[j] - nums[i]) is the same as (nums[i] - i != nums[j] - j).
3. Keep a counter of nums[i] - i. To be efficient, use a HashMap.

## 示例

```
[4,1,3,3]
[1,2,3,4,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long countBadPairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
```

### C

```c
long long countBadPairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountBadPairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countBadPairs = function(nums) {
    
};
```

### TypeScript

```typescript
function countBadPairs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countBadPairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countBadPairs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countBadPairs(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countBadPairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func countBadPairs(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_bad_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def countBadPairs(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_bad_pairs(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-bad-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_bad_pairs(Nums :: [integer()]) -> integer().
count_bad_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_bad_pairs(nums :: [integer]) :: integer
  def count_bad_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countBadPairs(nums: Array<Int64>): Int64 {

    }
}
```

