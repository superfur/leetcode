# 456. 132 模式

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，数组中共有 <code>n</code> 个整数。<strong>132 模式的子序列</strong> 由三个整数 <code>nums[i]</code>、<code>nums[j]</code> 和 <code>nums[k]</code> 组成，并同时满足：<code>i < j < k</code> 和 <code>nums[i] < nums[k] < nums[j]</code> 。</p>

<p>如果 <code>nums</code> 中存在 <strong>132 模式的子序列</strong> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>false
<strong>解释：</strong>序列中不存在 132 模式的子序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,4,2]
<strong>输出：</strong>true
<strong>解释：</strong>序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,3,2,0]
<strong>输出：</strong>true
<strong>解释：</strong>序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 2 * 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 二分查找
- 有序集合
- 单调栈

## 示例

```
[1,2,3,4]
[3,1,4,2]
[-1,3,2,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean find132pattern(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
```

### C

```c
bool find132pattern(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool Find132pattern(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var find132pattern = function(nums) {
    
};
```

### TypeScript

```typescript
function find132pattern(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function find132pattern($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func find132pattern(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun find132pattern(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool find132pattern(List<int> nums) {
    
  }
}
```

### Go

```golang
func find132pattern(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def find132pattern(nums)
    
end
```

### Scala

```scala
object Solution {
    def find132pattern(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find132pattern(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (find132pattern nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec find132pattern(Nums :: [integer()]) -> boolean().
find132pattern(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find132pattern(nums :: [integer]) :: boolean
  def find132pattern(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func find132pattern(nums: Array<Int64>): Bool {

    }
}
```

