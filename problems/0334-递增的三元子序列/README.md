# 334. 递增的三元子序列

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> ，判断这个数组中是否存在长度为 <code>3</code> 的递增子序列。</p>

<p>如果存在这样的三元组下标 <code>(i, j, k)</code>&nbsp;且满足 <code>i &lt; j &lt; k</code> ，使得&nbsp;<code>nums[i] &lt; nums[j] &lt; nums[k]</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5]
<strong>输出：</strong>true
<strong>解释：</strong>任何 i &lt; j &lt; k 的三元组都满足题意
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [5,4,3,2,1]
<strong>输出：</strong>false
<strong>解释：</strong>不存在满足题意的三元组</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,1,5,0,4,6]
<strong>输出：</strong>true
<strong>解释：</strong>三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 &lt; nums[4] == 4 &lt; nums[5] == 6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能实现时间复杂度为 <code>O(n)</code> ，空间复杂度为 <code>O(1)</code> 的解决方案吗？</p>


## 难度

Medium

## 标签

- 贪心
- 数组

## 示例

```
[1,2,3,4,5]
[5,4,3,2,1]
[2,1,5,0,4,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean increasingTriplet(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
```

### C

```c
bool increasingTriplet(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IncreasingTriplet(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    
};
```

### TypeScript

```typescript
function increasingTriplet(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function increasingTriplet($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func increasingTriplet(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun increasingTriplet(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool increasingTriplet(List<int> nums) {
    
  }
}
```

### Go

```golang
func increasingTriplet(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def increasing_triplet(nums)
    
end
```

### Scala

```scala
object Solution {
    def increasingTriplet(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn increasing_triplet(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (increasing-triplet nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec increasing_triplet(Nums :: [integer()]) -> boolean().
increasing_triplet(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec increasing_triplet(nums :: [integer]) :: boolean
  def increasing_triplet(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func increasingTriplet(nums: Array<Int64>): Bool {

    }
}
```

