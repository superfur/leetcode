# 3041. 修改数组后最大化数组中的连续元素数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始只包含 <strong>正</strong>&nbsp;整数的数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>一开始，你可以将数组中 <strong>任意数量</strong> 元素增加 <strong>至多</strong> <code>1</code> 。</p>

<p>修改后，你可以从最终数组中选择 <strong>一个或者更多</strong>&nbsp;元素，并确保这些元素升序排序后是 <strong>连续</strong>&nbsp;的。比方说，<code>[3, 4, 5]</code> 是连续的，但是&nbsp;<code>[3, 4, 6]</code> 和&nbsp;<code>[1, 1, 2, 3]</code>&nbsp;不是连续的。<!-- notionvc: 312f8c5d-40d0-4cd1-96cc-9e96a846735b --></p>

<p>请你返回 <strong>最多</strong>&nbsp;可以选出的元素数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,5,1,1]
<b>输出：</b>3
<b>解释：</b>我们将下标 0 和 3 处的元素增加 1 ，得到结果数组 nums = [3,1,5,2,1] 。
我们选择元素 [<em><strong>3</strong></em>,<em><strong>1</strong></em>,5,<em><strong>2</strong></em>,1] 并将它们排序得到 [1,2,3] ，是连续元素。
最多可以得到 3 个连续元素。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,4,7,10]
<b>输出：</b>1
<b>解释：</b>我们可以选择的最多元素数目是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 动态规划
- 排序

## 提示

1. Sort the array and try using dynamic programming.
2. Let <code>dp[i]</code> be the length of the longest consecutive elements ending at element at index <code>i</code> in the sorted array.

## 示例

```
[2,1,5,1,1]
[1,4,7,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSelectedElements(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSelectedElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        
```

### C

```c
int maxSelectedElements(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSelectedElements(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSelectedElements = function(nums) {
    
};
```

### TypeScript

```typescript
function maxSelectedElements(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxSelectedElements($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSelectedElements(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSelectedElements(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSelectedElements(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxSelectedElements(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_selected_elements(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxSelectedElements(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_selected_elements(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-selected-elements nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_selected_elements(Nums :: [integer()]) -> integer().
max_selected_elements(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_selected_elements(nums :: [integer]) :: integer
  def max_selected_elements(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSelectedElements(nums: Array<Int64>): Int64 {

    }
}
```

