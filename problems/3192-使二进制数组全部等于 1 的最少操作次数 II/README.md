# 3192. 使二进制数组全部等于 1 的最少操作次数 II

## 题目描述

<p>给你一个二进制数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>你可以对数组执行以下操作&nbsp;<strong>任意</strong>&nbsp;次（也可以 0 次）：</p>

<ul>
	<li>选择数组中 <strong>任意</strong>&nbsp;一个下标 <code>i</code>&nbsp;，并将从下标 <code>i</code>&nbsp;开始一直到数组末尾 <strong>所有</strong>&nbsp;元素 <strong>反转</strong>&nbsp;。</li>
</ul>

<p><b>反转</b>&nbsp;一个元素指的是将它的值从 0 变 1 ，或者从 1 变 0 。</p>

<p>请你返回将 <code>nums</code>&nbsp;中所有元素变为 1 的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [0,1,1,0,1]</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong><br />
我们可以执行以下操作：</p>

<ul>
	<li>选择下标&nbsp;<code>i = 1</code>&nbsp;执行操作，得到<span class="example-io">&nbsp;<code>nums = [0,<u><strong>0</strong></u>,<u><strong>0</strong></u>,<u><strong>1</strong></u>,<u><strong>0</strong></u>]</code>&nbsp;。</span></li>
	<li>选择下标&nbsp;<code>i = 0</code>&nbsp;执行操作，得到<span class="example-io">&nbsp;<code>nums = [<u><strong>1</strong></u>,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<u><strong>0</strong></u>,<u><strong>1</strong></u>]</code>&nbsp;。</span></li>
	<li>选择下标&nbsp;<code>i = 4</code>&nbsp;执行操作，得到<span class="example-io">&nbsp;<code>nums = [1,1,1,0,<u><strong>0</strong></u>]</code>&nbsp;。</span></li>
	<li>选择下标&nbsp;<code>i = 3</code>&nbsp;执行操作，得到<span class="example-io">&nbsp;<code>nums = [1,1,1,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>&nbsp;。</span></li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,0,0,0]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong><br />
我们可以执行以下操作：</p>

<ul>
	<li>选择下标&nbsp;<code>i = 1</code>&nbsp;执行操作，得到<span class="example-io">&nbsp;<code>nums = [1,<u><strong>1</strong></u>,<u><strong>1</strong></u>,<u><strong>1</strong></u>]</code>&nbsp;。</span></li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 动态规划

## 提示

1. The only way to change <code>nums[0]</code> to 1 is by performing an operation with index <code>i = 0</code>.
2. Iterate from left to right and perform an operation at each index i where nums[i] is 0, and keep track of how many operations are currently performed on the suffix.

## 示例

```
[0,1,1,0,1]
[1,0,0,0]
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

