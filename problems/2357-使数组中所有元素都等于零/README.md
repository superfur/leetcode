# 2357. 使数组中所有元素都等于零

## 题目描述

<p>给你一个非负整数数组 <code>nums</code> 。在一步操作中，你必须：</p>

<ul>
	<li>选出一个正整数 <code>x</code> ，<code>x</code> 需要小于或等于 <code>nums</code> 中 <strong>最小</strong> 的 <strong>非零</strong> 元素。</li>
	<li><code>nums</code> 中的每个正整数都减去 <code>x</code>。</li>
</ul>

<p>返回使 <code>nums</code> 中所有元素都等于<em> </em><code>0</code> 需要的 <strong>最少</strong> 操作数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5,0,3,5]
<strong>输出：</strong>3
<strong>解释：</strong>
第一步操作：选出 x = 1 ，之后 nums = [0,4,0,2,4] 。
第二步操作：选出 x = 2 ，之后 nums = [0,2,0,0,2] 。
第三步操作：选出 x = 2 ，之后 nums = [0,0,0,0,0] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0]
<strong>输出：</strong>0
<strong>解释：</strong>nums 中的每个元素都已经是 0 ，所以不需要执行任何操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组
- 哈希表
- 排序
- 模拟
- 堆（优先队列）

## 提示

1. It is always best to set x as the smallest non-zero element in nums.
2. Elements with the same value will always take the same number of operations to become 0. Contrarily, elements with different values will always take a different number of operations to become 0.
3. The answer is the number of unique non-zero numbers in nums.

## 示例

```
[1,5,0,3,5]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumOperations(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumOperations(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumOperations(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(nums: Array<Int64>): Int64 {

    }
}
```

