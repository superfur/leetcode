# 1995. 统计特殊四元组

## 题目描述

<p>给你一个 <strong>下标从 0 开始</strong> 的整数数组 <code>nums</code> ，返回满足下述条件的 <strong>不同</strong> 四元组 <code>(a, b, c, d)</code> 的 <strong>数目</strong> ：</p>

<ul>
	<li><code>nums[a] + nums[b] + nums[c] == nums[d]</code> ，且</li>
	<li><code>a &lt; b &lt; c &lt; d</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3,6]
<strong>输出：</strong>1
<strong>解释：</strong>满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [3,3,6,4,5]
<strong>输出：</strong>0
<strong>解释：</strong>[3,3,6,4,5] 中不存在满足要求的四元组。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,1,3,5]
<strong>输出：</strong>4
<strong>解释：</strong>满足要求的 4 个四元组如下：
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>4 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 枚举

## 提示

1. N is very small, how can we use that?
2. Can we check every possible quadruplet?

## 示例

```
[1,2,3,6]
[3,3,6,4,5]
[1,1,1,3,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countQuadruplets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countQuadruplets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        
```

### C

```c
int countQuadruplets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountQuadruplets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countQuadruplets = function(nums) {
    
};
```

### TypeScript

```typescript
function countQuadruplets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countQuadruplets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countQuadruplets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countQuadruplets(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countQuadruplets(List<int> nums) {
    
  }
}
```

### Go

```golang
func countQuadruplets(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_quadruplets(nums)
    
end
```

### Scala

```scala
object Solution {
    def countQuadruplets(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_quadruplets(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-quadruplets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_quadruplets(Nums :: [integer()]) -> integer().
count_quadruplets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_quadruplets(nums :: [integer]) :: integer
  def count_quadruplets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countQuadruplets(nums: Array<Int64>): Int64 {

    }
}
```

