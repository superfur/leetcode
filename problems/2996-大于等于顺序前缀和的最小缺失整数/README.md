# 2996. 大于等于顺序前缀和的最小缺失整数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>如果一个前缀&nbsp;<code>nums[0..i]</code>&nbsp;满足对于&nbsp;<code>1 &lt;= j &lt;= i</code>&nbsp;的所有元素都有&nbsp;<code>nums[j] = nums[j - 1] + 1</code>&nbsp;，那么我们称这个前缀是一个 <strong>顺序前缀</strong> 。特殊情况是，只包含&nbsp;<code>nums[0]</code>&nbsp;的前缀也是一个 <strong>顺序前缀</strong> 。</p>

<p>请你返回 <code>nums</code>&nbsp;中没有出现过的 <strong>最小</strong>&nbsp;整数&nbsp;<code>x</code>&nbsp;，满足&nbsp;<code>x</code>&nbsp;大于等于&nbsp;<strong>最长</strong> 顺序前缀的和。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,2,5]
<b>输出：</b>6
<b>解释：</b>nums 的最长顺序前缀是 [1,2,3] ，和为 6 ，6 不在数组中，所以 6 是大于等于最长顺序前缀和的最小整数。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,4,5,1,12,14,13]
<b>输出：</b>15
<b>解释：</b>nums 的最长顺序前缀是 [3,4,5] ，和为 12 ，12、13 和 14 都在数组中，但 15 不在，所以 15 是大于等于最长顺序前缀和的最小整数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. To find the longest sequential prefix, iterate from left to right. For a fixed <code>i</code>, if <code>nums[i] != nums[i - 1] + 1</code> then the longest sequential prefix ends at <code>i - 1</code>.

## 示例

```
[1,2,3,2,5]
[3,4,5,1,12,14,13]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int missingInteger(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int missingInteger(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
```

### C

```c
int missingInteger(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MissingInteger(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingInteger = function(nums) {
    
};
```

### TypeScript

```typescript
function missingInteger(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingInteger($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func missingInteger(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun missingInteger(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int missingInteger(List<int> nums) {
    
  }
}
```

### Go

```golang
func missingInteger(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def missing_integer(nums)
    
end
```

### Scala

```scala
object Solution {
    def missingInteger(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (missing-integer nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec missing_integer(Nums :: [integer()]) -> integer().
missing_integer(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec missing_integer(nums :: [integer]) :: integer
  def missing_integer(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func missingInteger(nums: Array<Int64>): Int64 {

    }
}
```

