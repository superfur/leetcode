# 1567. 乘积为正数的最长子数组长度

## 题目描述

<p>给你一个整数数组 <code>nums</code>&nbsp;，请你求出乘积为正数的最长子数组的长度。</p>

<p>一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。</p>

<p>请你返回乘积为正数的最长子数组长度。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp; 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,-2,-3,4]
<strong>输出：</strong>4
<strong>解释：</strong>数组本身乘积就是正数，值为 24 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1,-2,-3,-4]
<strong>输出：</strong>3
<strong>解释：</strong>最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,-2,-3,0,1]
<strong>输出：</strong>2
<strong>解释：</strong>乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>-10^9 &lt;= nums[i]&nbsp;&lt;= 10^9</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. Split the whole array into subarrays by zeroes since a subarray with positive product cannot contain any zero.
2. If the subarray has even number of negative numbers, the whole subarray has positive product.
3. Otherwise, we have two choices, either - remove the prefix till the first negative element in this subarray, or remove the suffix starting from the last negative element in this subarray.

## 示例

```
[1,-2,-3,4]
[0,1,-2,-3,-4]
[-1,-2,-3,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaxLen(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int getMaxLen(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getMaxLen(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        
```

### C

```c
int getMaxLen(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetMaxLen(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var getMaxLen = function(nums) {
    
};
```

### TypeScript

```typescript
function getMaxLen(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function getMaxLen($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getMaxLen(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaxLen(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getMaxLen(List<int> nums) {
    
  }
}
```

### Go

```golang
func getMaxLen(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def get_max_len(nums)
    
end
```

### Scala

```scala
object Solution {
    def getMaxLen(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_max_len(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-max-len nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec get_max_len(Nums :: [integer()]) -> integer().
get_max_len(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_max_len(nums :: [integer]) :: integer
  def get_max_len(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getMaxLen(nums: Array<Int64>): Int64 {

    }
}
```

