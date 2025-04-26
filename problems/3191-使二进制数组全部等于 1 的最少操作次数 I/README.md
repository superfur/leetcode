# 3191. 使二进制数组全部等于 1 的最少操作次数 I

## 题目描述

<p>给你一个二进制数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以对数组执行以下操作 <strong>任意</strong>&nbsp;次（也可以 0 次）：</p>

<ul>
	<li>选择数组中 <strong>任意连续</strong>&nbsp;3 个元素，并将它们 <strong>全部反转</strong>&nbsp;。</li>
</ul>

<p><strong>反转</strong>&nbsp;一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。</p>

<p>请你返回将 <code>nums</code>&nbsp;中所有元素变为 1 的 <strong>最少</strong>&nbsp;操作次数。如果无法全部变成 1 ，返回 -1 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [0,1,1,1,0,0]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong><br />
我们可以执行以下操作：</p>

<ul>
	<li>选择下标为 0 ，1 和 2 的元素并反转，得到&nbsp;<code>nums = [<u><strong>1</strong></u>,<u><strong>0</strong></u>,<u><strong>0</strong></u>,1,0,0]</code>&nbsp;。</li>
	<li>选择下标为 1 ，2 和 3 的元素并反转，得到&nbsp;<code>nums = [1,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<strong><u>0</u></strong>,0,0]</code>&nbsp;。</li>
	<li>选择下标为 3 ，4 和 5 的元素并反转，得到&nbsp;<code>nums = [1,1,1,<strong><u>1</u></strong>,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [0,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><strong>解释：</strong><br />
无法将所有元素都变为 1 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 队列
- 数组
- 前缀和
- 滑动窗口

## 提示

1. If <code>nums[0]</code> is 0, then the only way to change it to 1 is by doing an operation on the first 3 elements of the array.
2. After Changing <code>nums[0]</code> to 1, use the same logic on the remaining array.

## 示例

```
[0,1,1,1,0,0]
[0,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
```

### C

```c
int minOperations(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()]) -> integer().
min_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: Array<Int64>): Int64 {

    }
}
```

