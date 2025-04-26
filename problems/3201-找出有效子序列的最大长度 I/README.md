# 3201. 找出有效子序列的最大长度 I

## 题目描述

<p>给你一个整数数组 <code>nums</code>。</p>

<p><code>nums</code> 的子序列 <code>sub</code> 的长度为 <code>x</code> ，如果其满足以下条件，则称其为 <strong>有效子序列</strong>：</p>

<ul>
	<li><code>(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2</code></li>
</ul>

<p>返回 <code>nums</code> 的 <strong>最长的有效子序列</strong> 的长度。</p>

<p>一个&nbsp;<strong>子序列</strong>&nbsp;指的是从原数组中删除一些元素（也可以不删除任何元素），剩余元素保持原来顺序组成的新数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>最长的有效子序列是 <code>[1, 2, 3, 4]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,1,1,2,1,2]</span></p>

<p><strong>输出：</strong> 6</p>

<p><strong>解释：</strong></p>

<p>最长的有效子序列是 <code>[1, 2, 1, 2, 1, 2]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>最长的有效子序列是 <code>[1, 3]</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. The possible sequence either contains all even elements, all odd elements, alternate even odd, or alternate odd even elements.
2. Considering only the parity of elements, there are only 4 possibilities and we can try all of them.
3. When selecting an element with any parity, try to select the earliest one.

## 示例

```
[1,2,3,4]
[1,2,1,1,2,1,2]
[1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
```

### C

```c
int maximumLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumLength = function(nums) {
    
};
```

### TypeScript

```typescript
function maximumLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximumLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximumLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximum_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximumLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_length(Nums :: [integer()]) -> integer().
maximum_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_length(nums :: [integer]) :: integer
  def maximum_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumLength(nums: Array<Int64>): Int64 {

    }
}
```

