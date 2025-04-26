# 2369. 检查数组是否存在有效划分

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，你必须将数组划分为一个或多个 <strong>连续</strong> 子数组。</p>

<p>如果获得的这些子数组中每个都能满足下述条件<strong> 之一</strong> ，则可以称其为数组的一种 <strong>有效</strong> 划分：</p>

<ol>
	<li>子数组 <strong>恰</strong> 由 <code>2</code> 个相等元素组成，例如，子数组 <code>[2,2]</code> 。</li>
	<li>子数组 <strong>恰</strong> 由 <code>3</code> 个相等元素组成，例如，子数组 <code>[4,4,4]</code> 。</li>
	<li>子数组 <strong>恰</strong> 由 <code>3</code> 个连续递增元素组成，并且相邻元素之间的差值为 <code>1</code> 。例如，子数组 <code>[3,4,5]</code> ，但是子数组 <code>[1,3,5]</code> 不符合要求。</li>
</ol>

<p>如果数组 <strong>至少</strong> 存在一种有效划分，返回 <code>true</code><em> </em>，否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,4,4,5,6]
<strong>输出：</strong>true
<strong>解释：</strong>数组可以划分成子数组 [4,4] 和 [4,5,6] 。
这是一种有效划分，所以返回 true 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,2]
<strong>输出：</strong>false
<strong>解释：</strong>该数组不存在有效划分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. How can you reduce the problem to checking if there is a valid partition for a smaller array?
2. Use dynamic programming to reduce the problem until you have an empty array.

## 示例

```
[4,4,4,5,6]
[1,1,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validPartition(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validPartition(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
```

### C

```c
bool validPartition(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidPartition(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function(nums) {
    
};
```

### TypeScript

```typescript
function validPartition(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function validPartition($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validPartition(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validPartition(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validPartition(List<int> nums) {
    
  }
}
```

### Go

```golang
func validPartition(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def valid_partition(nums)
    
end
```

### Scala

```scala
object Solution {
    def validPartition(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_partition(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (valid-partition nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec valid_partition(Nums :: [integer()]) -> boolean().
valid_partition(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_partition(nums :: [integer]) :: boolean
  def valid_partition(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validPartition(nums: Array<Int64>): Bool {

    }
}
```

