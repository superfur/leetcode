# 3388. 统计数组中的美丽分割

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>如果数组&nbsp;<code>nums</code>&nbsp;的一个分割满足以下条件，我们称它是一个 <strong>美丽</strong>&nbsp;分割：</p>

<ol>
	<li>数组&nbsp;<code>nums</code>&nbsp;分为三段 <span data-keyword="subarray-nonempty">非空子数组</span>：<code>nums1</code>&nbsp;，<code>nums2</code>&nbsp;和&nbsp;<code>nums3</code>&nbsp;，三个数组&nbsp;<code>nums1</code>&nbsp;，<code>nums2</code>&nbsp;和&nbsp;<code>nums3</code>&nbsp;按顺序连接可以得到 <code>nums</code>&nbsp;。</li>
	<li>子数组&nbsp;<code>nums1</code>&nbsp;是子数组&nbsp;<code>nums2</code>&nbsp;的 <span data-keyword="array-prefix">前缀</span> <strong>或者</strong>&nbsp;<code>nums2</code>&nbsp;是&nbsp;<code>nums3</code>&nbsp;的 <span data-keyword="array-prefix">前缀</span>。</li>
</ol>

<p>请你返回满足以上条件的分割 <strong>数目</strong>&nbsp;。</p>

<p><strong>子数组</strong>&nbsp;指的是一个数组里一段连续 <strong>非空</strong>&nbsp;的元素。</p>

<p><strong>前缀</strong>&nbsp;指的是一个数组从头开始到中间某个元素结束的子数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,1,2,1]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b></p>

<p>美丽分割如下：</p>

<ol>
	<li><code>nums1 = [1]</code>&nbsp;，<code>nums2 = [1,2]</code>&nbsp;，<code>nums3 = [1]</code>&nbsp;。</li>
	<li><code>nums1 = [1]</code>&nbsp;，<code>nums2 = [1]</code>&nbsp;，<code>nums3 = [2,1]</code>&nbsp;。</li>
</ol>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>没有美丽分割。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5000</code></li>
	<li><code><font face="monospace">0 &lt;= nums[i] &lt;= 50</font></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Use 2D dynamic programming to find the maximum matching prefix.

## 示例

```
[1,1,2,1]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int beautifulSplits(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int beautifulSplits(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def beautifulSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        
```

### C

```c
int beautifulSplits(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int BeautifulSplits(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var beautifulSplits = function(nums) {
    
};
```

### TypeScript

```typescript
function beautifulSplits(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function beautifulSplits($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func beautifulSplits(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun beautifulSplits(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int beautifulSplits(List<int> nums) {
    
  }
}
```

### Go

```golang
func beautifulSplits(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def beautiful_splits(nums)
    
end
```

### Scala

```scala
object Solution {
    def beautifulSplits(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn beautiful_splits(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (beautiful-splits nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec beautiful_splits(Nums :: [integer()]) -> integer().
beautiful_splits(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec beautiful_splits(nums :: [integer]) :: integer
  def beautiful_splits(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func beautifulSplits(nums: Array<Int64>): Int64 {

    }
}
```

