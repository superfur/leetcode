# 376. 摆动序列

## 题目描述

<p>如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为<strong> 摆动序列 。</strong>第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。</p>

<ul>
	<li>
	<p>例如， <code>[1, 7, 4, 9, 2, 5]</code> 是一个 <strong>摆动序列</strong> ，因为差值 <code>(6, -3, 5, -7, 3)</code> 是正负交替出现的。</p>
	</li>
	<li>相反，<code>[1, 4, 7, 2, 5]</code> 和 <code>[1, 7, 4, 5, 5]</code> 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。</li>
</ul>

<p><strong>子序列</strong> 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。</p>

<p>给你一个整数数组 <code>nums</code> ，返回 <code>nums</code> 中作为 <strong>摆动序列 </strong>的 <strong>最长子序列的长度</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,7,4,9,2,5]
<strong>输出：</strong>6
<strong>解释：</strong>整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,17,5,10,13,15,10,5,16,8]
<strong>输出：</strong>7
<strong>解释：</strong>这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5,6,7,8,9]
<strong>输出：</strong>2
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 1000</code></li>
	<li><code>0 <= nums[i] <= 1000</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>你能否用 <code>O(n)</code><em> </em>时间复杂度完成此题?</p>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 示例

```
[1,7,4,9,2,5]
[1,17,5,10,13,15,10,5,16,8]
[1,2,3,4,5,6,7,8,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int wiggleMaxLength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
```

### C

```c
int wiggleMaxLength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int WiggleMaxLength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    
};
```

### TypeScript

```typescript
function wiggleMaxLength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function wiggleMaxLength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func wiggleMaxLength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun wiggleMaxLength(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int wiggleMaxLength(List<int> nums) {
    
  }
}
```

### Go

```golang
func wiggleMaxLength(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def wiggle_max_length(nums)
    
end
```

### Scala

```scala
object Solution {
    def wiggleMaxLength(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (wiggle-max-length nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec wiggle_max_length(Nums :: [integer()]) -> integer().
wiggle_max_length(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec wiggle_max_length(nums :: [integer]) :: integer
  def wiggle_max_length(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func wiggleMaxLength(nums: Array<Int64>): Int64 {

    }
}
```

