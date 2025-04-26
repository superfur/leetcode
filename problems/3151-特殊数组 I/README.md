# 3151. 特殊数组 I

## 题目描述

<p>如果数组的每一对相邻元素都是两个奇偶性不同的数字，则该数组被认为是一个 <strong>特殊数组</strong>。换句话说，每一对中的元素 <strong>必须</strong> 有一个是偶数，另一个是奇数。</p>

<p>你有一个整数数组 <code>nums</code>。如果 <code>nums</code> 是一个 <strong>特殊数组</strong> ，返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1]</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>只有一个元素，所以答案为 <code>true</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [2,1,4]</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>只有两对相邻元素： <code>(2,1)</code> 和 <code>(1,4)</code>，它们都包含了奇偶性不同的数字，因此答案为 <code>true</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [4,3,1,6]</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p><code>nums[1]</code> 和 <code>nums[2]</code> 都是奇数。因此答案为 <code>false</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Try to check the parity of each element and its previous element.

## 示例

```
[1]
[2,1,4]
[4,3,1,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isArraySpecial(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
```

### C

```c
bool isArraySpecial(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsArraySpecial(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var isArraySpecial = function(nums) {
    
};
```

### TypeScript

```typescript
function isArraySpecial(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function isArraySpecial($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isArraySpecial(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isArraySpecial(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isArraySpecial(List<int> nums) {
    
  }
}
```

### Go

```golang
func isArraySpecial(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def is_array_special(nums)
    
end
```

### Scala

```scala
object Solution {
    def isArraySpecial(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_array_special(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-array-special nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_array_special(Nums :: [integer()]) -> boolean().
is_array_special(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_array_special(nums :: [integer]) :: boolean
  def is_array_special(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isArraySpecial(nums: Array<Int64>): Bool {

    }
}
```

