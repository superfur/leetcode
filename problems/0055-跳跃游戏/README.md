# 55. 跳跃游戏

## 题目描述

<p>给你一个非负整数数组&nbsp;<code>nums</code> ，你最初位于数组的 <strong>第一个下标</strong> 。数组中的每个元素代表你在该位置可以跳跃的最大长度。</p>

<p>判断你是否能够到达最后一个下标，如果可以，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,1,1,4]
<strong>输出：</strong>true
<strong>解释：</strong>可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1,0,4]
<strong>输出：</strong>false
<strong>解释：</strong>无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 示例

```
[2,3,1,1,4]
[3,2,1,0,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canJump(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
```

### C

```c
bool canJump(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanJump(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    
};
```

### TypeScript

```typescript
function canJump(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canJump($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canJump(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canJump(List<int> nums) {
    
  }
}
```

### Go

```golang
func canJump(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def can_jump(nums)
    
end
```

### Scala

```scala
object Solution {
    def canJump(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_jump(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-jump nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_jump(Nums :: [integer()]) -> boolean().
can_jump(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_jump(nums :: [integer]) :: boolean
  def can_jump(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canJump(nums: Array<Int64>): Bool {

    }
}
```

