# 1785. 构成特定和需要添加的最少元素

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，和两个整数 <code>limit</code> 与 <code>goal</code> 。数组 <code>nums</code> 有一条重要属性：<code>abs(nums[i]) <= limit</code> 。</p>

<p>返回使数组元素总和等于 <code>goal</code> 所需要向数组中添加的 <strong>最少元素数量</strong> ，添加元素 <strong>不应改变</strong> 数组中 <code>abs(nums[i]) <= limit</code> 这一属性。</p>

<p>注意，如果 <code>x >= 0</code> ，那么 <code>abs(x)</code> 等于 <code>x</code> ；否则，等于 <code>-x</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,-1,1], limit = 3, goal = -4
<strong>输出：</strong>2
<strong>解释：</strong>可以将 -2 和 -3 添加到数组中，数组的元素总和变为 1 - 1 + 1 - 2 - 3 = -4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,-10,9,1], limit = 100, goal = 0
<strong>输出：</strong>1
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= limit <= 10<sup>6</sup></code></li>
	<li><code>-limit <= nums[i] <= limit</code></li>
	<li><code>-10<sup>9</sup> <= goal <= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Try thinking about the problem as if the array is empty. Then you only need to form goal using elements whose absolute value is <= limit.
2. You can greedily set all of the elements except one to limit or -limit, so the number of elements you need is ceil(abs(goal)/ limit).
3. You can "normalize" goal by offsetting it by the sum of the array. For example, if the goal is 5 and the sum is -3, then it's exactly the same as if the goal is 8 and the array is empty.
4. The answer is ceil(abs(goal-sum)/limit) = (abs(goal-sum)+limit-1) / limit.

## 示例

```
[1,-1,1]
3
-4
[1,-10,9,1]
100
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        
    }
};
```

### Java

```java
class Solution {
    public int minElements(int[] nums, int limit, int goal) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minElements(self, nums, limit, goal):
        """
        :type nums: List[int]
        :type limit: int
        :type goal: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
```

### C

```c
int minElements(int* nums, int numsSize, int limit, int goal) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinElements(int[] nums, int limit, int goal) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} limit
 * @param {number} goal
 * @return {number}
 */
var minElements = function(nums, limit, goal) {
    
};
```

### TypeScript

```typescript
function minElements(nums: number[], limit: number, goal: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $limit
     * @param Integer $goal
     * @return Integer
     */
    function minElements($nums, $limit, $goal) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minElements(_ nums: [Int], _ limit: Int, _ goal: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minElements(nums: IntArray, limit: Int, goal: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minElements(List<int> nums, int limit, int goal) {
    
  }
}
```

### Go

```golang
func minElements(nums []int, limit int, goal int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} limit
# @param {Integer} goal
# @return {Integer}
def min_elements(nums, limit, goal)
    
end
```

### Scala

```scala
object Solution {
    def minElements(nums: Array[Int], limit: Int, goal: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_elements(nums: Vec<i32>, limit: i32, goal: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-elements nums limit goal)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_elements(Nums :: [integer()], Limit :: integer(), Goal :: integer()) -> integer().
min_elements(Nums, Limit, Goal) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_elements(nums :: [integer], limit :: integer, goal :: integer) :: integer
  def min_elements(nums, limit, goal) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minElements(nums: Array<Int64>, limit: Int64, goal: Int64): Int64 {

    }
}
```

