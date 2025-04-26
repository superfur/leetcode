# 3190. 使所有元素都可以被 3 整除的最少操作数

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。一次操作中，你可以将&nbsp;<code>nums</code>&nbsp;中的&nbsp;<strong>任意</strong>&nbsp;一个元素增加或者减少 1 。</p>

<p>请你返回将 <code>nums</code>&nbsp;中所有元素都可以被 3 整除的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>通过以下 3 个操作，数组中的所有元素都可以被 3 整除：</p>

<ul>
	<li>将 1 减少 1 。</li>
	<li>将 2 增加 1 。</li>
	<li>将 4 减少 1 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,6,9]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. If <code>x % 3 != 0</code> we can always increment or decrement <code>x</code> such that we only need 1 operation.
2. Add <code>min(nums[i] % 3, 3 - (num[i] % 3))</code> to the count of operations.

## 示例

```
[1,2,3,4]
[3,6,9]
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

