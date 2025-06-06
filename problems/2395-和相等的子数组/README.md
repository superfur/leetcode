# 2395. 和相等的子数组

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，判断是否存在&nbsp;<strong>两个</strong>&nbsp;长度为&nbsp;<code>2</code>&nbsp;的子数组且它们的&nbsp;<strong>和</strong>&nbsp;相等。注意，这两个子数组起始位置的下标必须&nbsp;<strong>不相同</strong>&nbsp;。</p>

<p>如果这样的子数组存在，请返回&nbsp;<code>true</code>，否则返回&nbsp;<code>false</code><em>&nbsp;</em>。</p>

<p><strong>子数组</strong> 是一个数组中一段连续非空的元素组成的序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [4,2,4]
<b>输出：</b>true
<b>解释：</b>元素为 [4,2] 和 [2,4] 的子数组有相同的和 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,4,5]
<b>输出：</b>false
<b>解释：</b>没有长度为 2 的两个子数组和相等。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [0,0,0]
<b>输出：</b>true
<b>解释：</b>子数组 [nums[0],nums[1]] 和 [nums[1],nums[2]] 的和相等，都为 0 。
注意即使子数组的元素相同，这两个子数组也视为不相同的子数组，因为它们在原数组中的起始位置不同。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Use a counter to keep track of the subarray sums.
2. Use a hashset to check if any two sums are equal.

## 示例

```
[4,2,4]
[1,2,3,4,5]
[0,0,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool findSubarrays(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean findSubarrays(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
```

### C

```c
bool findSubarrays(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool FindSubarrays(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var findSubarrays = function(nums) {
    
};
```

### TypeScript

```typescript
function findSubarrays(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function findSubarrays($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findSubarrays(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findSubarrays(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool findSubarrays(List<int> nums) {
    
  }
}
```

### Go

```golang
func findSubarrays(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def find_subarrays(nums)
    
end
```

### Scala

```scala
object Solution {
    def findSubarrays(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_subarrays(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (find-subarrays nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec find_subarrays(Nums :: [integer()]) -> boolean().
find_subarrays(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_subarrays(nums :: [integer]) :: boolean
  def find_subarrays(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findSubarrays(nums: Array<Int64>): Bool {

    }
}
```

