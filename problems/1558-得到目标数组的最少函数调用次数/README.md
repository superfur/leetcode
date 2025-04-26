# 1558. 得到目标数组的最少函数调用次数

## 题目描述

<p><img alt="" src="https://assets.leetcode.com/uploads/2020/07/10/sample_2_1887.png" style="height:294px; width:573px" /></p>

<p>给你一个与 <code>nums</code>&nbsp;大小相同且初始值全为 0 的数组 <code>arr</code> ，请你调用以上函数得到整数数组 <code>nums</code>&nbsp;。</p>

<p>请你返回将 <code>arr</code>&nbsp;变成 <code>nums</code>&nbsp;的最少函数调用次数。</p>

<p>答案保证在 32 位有符号整数以内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,5]
<strong>输出：</strong>5
<strong>解释：</strong>给第二个数加 1 ：[0, 0] 变成 [0, 1] （1 次操作）。
将所有数字乘以 2 ：[0, 1] -&gt; [0, 2] -&gt; [0, 4] （2 次操作）。
给两个数字都加 1 ：[0, 4] -&gt; [1, 4] -&gt; <strong>[1, 5]</strong> （2 次操作）。
总操作次数为：1 + 2 + 2 = 5 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2]
<strong>输出：</strong>3
<strong>解释：</strong>给两个数字都加 1 ：[0, 0] -&gt; [0, 1] -&gt; [1, 1] （2 次操作）。
将所有数字乘以 2 ： [1, 1] -&gt; <strong>[2, 2]</strong> （1 次操作）。
总操作次数为： 2 + 1 = 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,2,5]
<strong>输出：</strong>6
<strong>解释：</strong>（初始）[0,0,0] -&gt; [1,0,0] -&gt; [1,0,1] -&gt; [2,0,2] -&gt; [2,1,2] -&gt; [4,2,4] -&gt; <strong>[4,2,5] </strong>（nums 数组）。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,2,4]
<strong>输出：</strong>7
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,8,16]
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 数组

## 提示

1. Work backwards: try to go from nums to arr.
2. You should try to divide by 2 as much as possible, but you can only divide by 2 if everything is even.

## 示例

```
[1,5]
[2,2]
[4,2,5]
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

