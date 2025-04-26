# 3040. 相同分数的最大操作数目 II

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，如果&nbsp;<code>nums</code>&nbsp;<strong>至少</strong>&nbsp;包含 <code>2</code>&nbsp;个元素，你可以执行以下操作中的&nbsp;<strong>任意</strong>&nbsp;一个：</p>

<ul>
	<li>选择 <code>nums</code>&nbsp;中最前面两个元素并且删除它们。</li>
	<li>选择 <code>nums</code>&nbsp;中最后两个元素并且删除它们。</li>
	<li>选择 <code>nums</code>&nbsp;中第一个和最后一个元素并且删除它们。</li>
</ul>

<p>一次操作的&nbsp;<strong>分数</strong>&nbsp;是被删除元素的和。</p>

<p>在确保<strong>&nbsp;所有操作分数相同</strong>&nbsp;的前提下，请你求出&nbsp;<strong>最多</strong>&nbsp;能进行多少次操作。</p>

<p>请你返回按照上述要求&nbsp;<strong>最多</strong>&nbsp;可以进行的操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,1,2,3,4]
<b>输出：</b>3
<b>解释：</b>我们执行以下操作：
- 删除前两个元素，分数为 3 + 2 = 5 ，nums = [1,2,3,4] 。
- 删除第一个元素和最后一个元素，分数为 1 + 4 = 5 ，nums = [2,3] 。
- 删除第一个元素和最后一个元素，分数为 2 + 3 = 5 ，nums = [] 。
由于 nums 为空，我们无法继续进行任何操作。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,6,1,4]
<b>输出：</b>2
<b>解释：</b>我们执行以下操作：
- 删除前两个元素，分数为 3 + 2 = 5 ，nums = [6,1,4] 。
- 删除最后两个元素，分数为 1 + 4 = 5 ，nums = [6] 。
至多进行 2 次操作。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 记忆化搜索
- 数组
- 动态规划

## 提示

1. After the first operation, the score of other operations is fixed.
2. For the fixed score use dynamic programming <code>dp[l][r]</code> to find a maximum number of operations on the subarray <code>nums[l..r]</code>.

## 示例

```
[3,2,1,2,3,4]
[3,2,6,1,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxOperations(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        
```

### C

```c
int maxOperations(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxOperations(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function maxOperations(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxOperations(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxOperations(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxOperations(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxOperations(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_operations(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_operations(Nums :: [integer()]) -> integer().
max_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_operations(nums :: [integer]) :: integer
  def max_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxOperations(nums: Array<Int64>): Int64 {

    }
}
```

