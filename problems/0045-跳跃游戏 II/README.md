# 45. 跳跃游戏 II

## 题目描述

<p>给定一个长度为 <code>n</code> 的 <strong>0 索引</strong>整数数组 <code>nums</code>。初始位置为 <code>nums[0]</code>。</p>

<p>每个元素 <code>nums[i]</code> 表示从索引 <code>i</code> 向后跳转的最大长度。换句话说，如果你在 <code>nums[i]</code> 处，你可以跳转到任意 <code>nums[i + j]</code> 处:</p>

<ul>
	<li><code>0 &lt;= j &lt;= nums[i]</code>&nbsp;</li>
	<li><code>i + j &lt; n</code></li>
</ul>

<p>返回到达&nbsp;<code>nums[n - 1]</code> 的最小跳跃次数。生成的测试用例可以到达 <code>nums[n - 1]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,3,1,1,4]
<strong>输出:</strong> 2
<strong>解释:</strong> 跳到最后一个位置的最小跳跃数是 <code>2</code>。
&nbsp;    从下标为 0 跳到下标为 1 的位置，跳&nbsp;<code>1</code>&nbsp;步，然后跳&nbsp;<code>3</code>&nbsp;步到达数组的最后一个位置。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [2,3,0,1,4]
<strong>输出:</strong> 2
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
	<li>题目保证可以到达&nbsp;<code>nums[n-1]</code></li>
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
[2,3,0,1,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int jump(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int jump(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def jump(self, nums: List[int]) -> int:
        
```

### C

```c
int jump(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Jump(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var jump = function(nums) {
    
};
```

### TypeScript

```typescript
function jump(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function jump($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func jump(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun jump(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int jump(List<int> nums) {
    
  }
}
```

### Go

```golang
func jump(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def jump(nums)
    
end
```

### Scala

```scala
object Solution {
    def jump(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (jump nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec jump(Nums :: [integer()]) -> integer().
jump(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec jump(nums :: [integer]) :: integer
  def jump(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func jump(nums: Array<Int64>): Int64 {

    }
}
```

