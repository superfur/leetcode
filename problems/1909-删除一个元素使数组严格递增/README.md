# 1909. 删除一个元素使数组严格递增

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，如果 <strong>恰好</strong> 删除 <strong>一个</strong> 元素后，数组 <strong>严格递增</strong> ，那么请你返回 <code>true</code> ，否则返回 <code>false</code> 。如果数组本身已经是严格递增的，请你也返回 <code>true</code> 。</p>

<p>数组 <code>nums</code> 是 <strong>严格递增</strong> 的定义为：对于任意下标的 <code>1 &lt;= i &lt; nums.length</code> 都满足 <code>nums[i - 1] &lt; nums[i]</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,2,<strong>10</strong>,5,7]
<b>输出：</b>true
<b>解释：</b>从 nums 中删除下标 2 处的 10 ，得到 [1,2,5,7] 。
[1,2,5,7] 是严格递增的，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,3,1,2]
<b>输出：</b>false
<b>解释：</b>
[3,1,2] 是删除下标 0 处元素后得到的结果。
[2,1,2] 是删除下标 1 处元素后得到的结果。
[2,3,2] 是删除下标 2 处元素后得到的结果。
[2,3,1] 是删除下标 3 处元素后得到的结果。
没有任何结果数组是严格递增的，所以返回 false 。</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [1,1,1]
<b>输出：</b>false
<b>解释：</b>删除任意元素后的结果都是 [1,1] 。
[1,1] 不是严格递增的，所以返回 false 。
</pre>

<p><strong>示例 4：</strong></p>

<pre><b>输入：</b>nums = [1,2,3]
<b>输出：</b>true
<b>解释：</b>[1,2,3] 已经是严格递增的，所以返回 true 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. For each index i in nums remove this index.
2. If the array becomes sorted return true, otherwise revert to the original array and try different index.

## 示例

```
[1,2,10,5,7]
[2,3,1,2]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canBeIncreasing(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
```

### C

```c
bool canBeIncreasing(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanBeIncreasing(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canBeIncreasing = function(nums) {
    
};
```

### TypeScript

```typescript
function canBeIncreasing(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canBeIncreasing($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canBeIncreasing(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canBeIncreasing(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canBeIncreasing(List<int> nums) {
    
  }
}
```

### Go

```golang
func canBeIncreasing(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def can_be_increasing(nums)
    
end
```

### Scala

```scala
object Solution {
    def canBeIncreasing(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_be_increasing(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-be-increasing nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_be_increasing(Nums :: [integer()]) -> boolean().
can_be_increasing(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_be_increasing(nums :: [integer]) :: boolean
  def can_be_increasing(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canBeIncreasing(nums: Array<Int64>): Bool {

    }
}
```

