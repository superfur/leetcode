# 3010. 将数组分成最小总代价的子数组 I

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>一个数组的 <strong>代价</strong>&nbsp;是它的 <strong>第一个</strong>&nbsp;元素。比方说，<code>[1,2,3]</code>&nbsp;的代价是&nbsp;<code>1</code>&nbsp;，<code>[3,4,1]</code>&nbsp;的代价是&nbsp;<code>3</code>&nbsp;。</p>

<p>你需要将&nbsp;<code>nums</code>&nbsp;分成&nbsp;<code>3</code>&nbsp;个&nbsp;<strong>连续且没有交集</strong>&nbsp;的子数组。</p>

<p>请你返回这些<span data-keyword="subarray">子数组</span>的 <strong>最小</strong>&nbsp;代价&nbsp;<b>总和</b>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,12]
<b>输出：</b>6
<b>解释：</b>最佳分割成 3 个子数组的方案是：[1] ，[2] 和 [3,12] ，总代价为 1 + 2 + 3 = 6 。
其他得到 3 个子数组的方案是：
- [1] ，[2,3] 和 [12] ，总代价是 1 + 2 + 12 = 15 。
- [1,2] ，[3] 和 [12] ，总代价是 1 + 3 + 12 = 16 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,4,3]
<b>输出：</b>12
<b>解释：</b>最佳分割成 3 个子数组的方案是：[5] ，[4] 和 [3] ，总代价为 5 + 4 + 3 = 12 。
12 是所有分割方案里的最小总代价。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [10,3,1,1]
<b>输出：</b>12
<b>解释：</b>最佳分割成 3 个子数组的方案是：[10,3] ，[1] 和 [1] ，总代价为 10 + 1 + 1 = 12 。
12 是所有分割方案里的最小总代价。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举
- 排序

## 示例

```
[1,2,3,12]
[5,4,3]
[10,3,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCost(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCost(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumCost(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCost(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumCost = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumCost(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumCost($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumCost(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Nums :: [integer()]) -> integer().
minimum_cost(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(nums :: [integer]) :: integer
  def minimum_cost(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(nums: Array<Int64>): Int64 {

    }
}
```

