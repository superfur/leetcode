# 3046. 分割数组

## 题目描述

<p>给你一个长度为 <strong>偶数 </strong>的整数数组 <code>nums</code> 。你需要将这个数组分割成 <code>nums1</code> 和 <code>nums2</code> 两部分，要求：</p>

<ul>
	<li><code>nums1.length == nums2.length == nums.length / 2</code> 。</li>
	<li><code>nums1</code> 应包含 <strong>互不相同</strong><strong> </strong>的元素。</li>
	<li><code>nums2</code>也应包含<strong> 互不相同</strong> 的元素。</li>
</ul>

<p>如果能够分割数组就返回 <code>true</code> ，否则返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2,2,3,4]
<strong>输出：</strong>true
<strong>解释：</strong>分割 nums 的可行方案之一是 nums1 = [1,2,3] 和 nums2 = [1,2,4] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1]
<strong>输出：</strong>false
<strong>解释：</strong>分割 nums 的唯一可行方案是 nums1 = [1,1] 和 nums2 = [1,1] 。但 nums1 和 nums2 都不是由互不相同的元素构成。因此，返回 false 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums.length % 2 == 0</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. It’s impossible if the same number occurs more than twice. So just check the frequency of each value.

## 示例

```
[1,1,2,2,3,4]
[1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPossibleToSplit(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPossibleToSplit(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPossibleToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        
```

### C

```c
bool isPossibleToSplit(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPossibleToSplit(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isPossibleToSplit = function(nums) {
    
};
```

### TypeScript

```typescript
function isPossibleToSplit(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isPossibleToSplit($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPossibleToSplit(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPossibleToSplit(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPossibleToSplit(List<int> nums) {
    
  }
}
```

### Go

```golang
func isPossibleToSplit(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def is_possible_to_split(nums)
    
end
```

### Scala

```scala
object Solution {
    def isPossibleToSplit(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_possible_to_split(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-possible-to-split nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_possible_to_split(Nums :: [integer()]) -> boolean().
is_possible_to_split(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_possible_to_split(nums :: [integer]) :: boolean
  def is_possible_to_split(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPossibleToSplit(nums: Array<Int64>): Bool {

    }
}
```

