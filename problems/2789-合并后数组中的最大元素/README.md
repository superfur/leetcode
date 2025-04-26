# 2789. 合并后数组中的最大元素

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始、由正整数组成的数组 <code>nums</code> 。</p>

<p>你可以在数组上执行下述操作 <strong>任意</strong> 次：</p>

<ul>
	<li>选中一个同时满足&nbsp;<code>0 &lt;= i &lt; nums.length - 1</code> 和 <code>nums[i] &lt;= nums[i + 1]</code> 的整数 <code>i</code> 。将元素 <code>nums[i + 1]</code> 替换为 <code>nums[i] + nums[i + 1]</code> ，并从数组中删除元素 <code>nums[i]</code> 。</li>
</ul>

<p>返回你可以从最终数组中获得的 <strong>最大</strong> 元素的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,3,7,9,3]
<strong>输出：</strong>21
<strong>解释：</strong>我们可以在数组上执行下述操作：
- 选中 i = 0 ，得到数组 nums = [<strong><em>5</em></strong>,7,9,3] 。
- 选中 i = 1 ，得到数组 nums = [5,<em><strong>16</strong></em>,3] 。
- 选中 i = 0 ，得到数组 nums = [<em><strong>21</strong></em>,3] 。
最终数组中的最大元素是 21 。可以证明我们无法获得更大的元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [5,3,3]
<strong>输出：</strong>11
<strong>解释：</strong>我们可以在数组上执行下述操作：
- 选中 i = 1 ，得到数组 nums = [5,<em><strong>6</strong></em>] 。
- 选中 i = 0 ，得到数组 nums = [<em><strong>11</strong></em>] 。
最终数组中只有一个元素，即 11 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Start from the end of the array and keep merging elements together until it is no longer possible.
2. The answer will be the resulting element from the last merge operation.

## 示例

```
[2,3,7,9,3]
[5,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxArrayValue(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxArrayValue(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxArrayValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
```

### C

```c
long long maxArrayValue(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxArrayValue(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxArrayValue = function(nums) {
    
};
```

### TypeScript

```typescript
function maxArrayValue(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxArrayValue($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxArrayValue(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxArrayValue(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxArrayValue(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxArrayValue(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_array_value(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxArrayValue(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_array_value(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-array-value nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_array_value(Nums :: [integer()]) -> integer().
max_array_value(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_array_value(nums :: [integer]) :: integer
  def max_array_value(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxArrayValue(nums: Array<Int64>): Int64 {

    }
}
```

