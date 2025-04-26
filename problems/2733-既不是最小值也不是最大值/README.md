# 2733. 既不是最小值也不是最大值

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，数组由 <strong>不同正整数</strong> 组成，请你找出并返回数组中 <strong>任一</strong> 既不是 <strong>最小值</strong> 也不是 <strong>最大值</strong> 的数字，如果不存在这样的数字，返回 <strong><code>-1</code></strong> 。</p>

<p>返回所选整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [3,2,1,4]
<strong>输出：</strong>2
<strong>解释：</strong>在这个示例中，最小值是 1 ，最大值是 4 。因此，2 或 3 都是有效答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,2]
<strong>输出：</strong>-1
<strong>解释：</strong>由于不存在既不是最大值也不是最小值的数字，我们无法选出满足题目给定条件的数字。因此，不存在答案，返回 -1 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [2,1,3]
<strong>输出：</strong>2
<strong>解释：</strong>2 既不是最小值，也不是最大值，这个示例只有这一个有效答案。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>nums</code> 中的所有数字互不相同</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Find any value in the array that is not the minimum or the maximum value.

## 示例

```
[3,2,1,4]
[1,2]
[2,1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findNonMinOrMax(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        
```

### C

```c
int findNonMinOrMax(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindNonMinOrMax(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    
};
```

### TypeScript

```typescript
function findNonMinOrMax(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNonMinOrMax($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findNonMinOrMax(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findNonMinOrMax(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findNonMinOrMax(List<int> nums) {
    
  }
}
```

### Go

```golang
func findNonMinOrMax(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_non_min_or_max(nums)
    
end
```

### Scala

```scala
object Solution {
    def findNonMinOrMax(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_non_min_or_max(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-non-min-or-max nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_non_min_or_max(Nums :: [integer()]) -> integer().
find_non_min_or_max(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_non_min_or_max(nums :: [integer]) :: integer
  def find_non_min_or_max(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findNonMinOrMax(nums: Array<Int64>): Int64 {

    }
}
```

