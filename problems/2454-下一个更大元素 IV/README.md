# 2454. 下一个更大元素 IV

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的非负整数数组&nbsp;<code>nums</code>&nbsp;。对于&nbsp;<code>nums</code>&nbsp;中每一个整数，你必须找到对应元素的&nbsp;<strong>第二大</strong>&nbsp;整数。</p>

<p>如果&nbsp;<code>nums[j]</code>&nbsp;满足以下条件，那么我们称它为&nbsp;<code>nums[i]</code>&nbsp;的&nbsp;<strong>第二大</strong>&nbsp;整数：</p>

<ul>
	<li><code>j &gt; i</code></li>
	<li><code>nums[j] &gt; nums[i]</code></li>
	<li>恰好存在 <strong>一个</strong>&nbsp;<code>k</code>&nbsp;满足 <code>i &lt; k &lt; j</code>&nbsp;且&nbsp;<code>nums[k] &gt; nums[i]</code>&nbsp;。</li>
</ul>

<p>如果不存在&nbsp;<code>nums[j]</code>&nbsp;，那么第二大整数为&nbsp;<code>-1</code>&nbsp;。</p>

<ul>
	<li>比方说，数组&nbsp;<code>[1, 2, 4, 3]</code>&nbsp;中，<code>1</code>&nbsp;的第二大整数是&nbsp;<code>4</code>&nbsp;，<code>2</code>&nbsp;的第二大整数是&nbsp;<code>3</code>&nbsp;，<code>3</code> 和&nbsp;<code>4</code>&nbsp;的第二大整数是&nbsp;<code>-1</code>&nbsp;。</li>
</ul>

<p>请你返回一个整数数组<em>&nbsp;</em><code>answer</code>&nbsp;，其中<em>&nbsp;</em><code>answer[i]</code>是<em>&nbsp;</em><code>nums[i]</code>&nbsp;的第二大整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,4,0,9,6]
<b>输出：</b>[9,6,6,-1,-1]
<strong>解释：</strong>
下标为 0 处：2 的右边，4 是大于 2 的第一个整数，9 是第二个大于 2 的整数。
下标为 1 处：4 的右边，9 是大于 4 的第一个整数，6 是第二个大于 4 的整数。
下标为 2 处：0 的右边，9 是大于 0 的第一个整数，6 是第二个大于 0 的整数。
下标为 3 处：右边不存在大于 9 的整数，所以第二大整数为 -1 。
下标为 4 处：右边不存在大于 6 的整数，所以第二大整数为 -1 。
所以我们返回 [9,6,6,-1,-1] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,3]
<b>输出：</b>[-1,-1]
<strong>解释：</strong>
由于每个数右边都没有更大的数，所以我们返回 [-1,-1] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 二分查找
- 排序
- 单调栈
- 堆（优先队列）

## 提示

1. Move forward in nums and store the value in a non-increasing stack for the first greater value.
2. Move the value in the stack to an ordered data structure for the second greater value.
3. Move value from the ordered data structure for the answer.

## 示例

```
[2,4,0,9,6]
[3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> secondGreaterElement(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] secondGreaterElement(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def secondGreaterElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* secondGreaterElement(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SecondGreaterElement(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var secondGreaterElement = function(nums) {
    
};
```

### TypeScript

```typescript
function secondGreaterElement(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function secondGreaterElement($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func secondGreaterElement(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun secondGreaterElement(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> secondGreaterElement(List<int> nums) {
    
  }
}
```

### Go

```golang
func secondGreaterElement(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def second_greater_element(nums)
    
end
```

### Scala

```scala
object Solution {
    def secondGreaterElement(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn second_greater_element(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (second-greater-element nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec second_greater_element(Nums :: [integer()]) -> [integer()].
second_greater_element(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec second_greater_element(nums :: [integer]) :: [integer]
  def second_greater_element(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func secondGreaterElement(nums: Array<Int64>): Array<Int64> {

    }
}
```

