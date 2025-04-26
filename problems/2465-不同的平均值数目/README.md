# 2465. 不同的平均值数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <strong>偶数</strong>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>只要&nbsp;<code>nums</code> <strong>不是</strong>&nbsp;空数组，你就重复执行以下步骤：</p>

<ul>
	<li>找到&nbsp;<code>nums</code>&nbsp;中的最小值，并删除它。</li>
	<li>找到&nbsp;<code>nums</code>&nbsp;中的最大值，并删除它。</li>
	<li>计算删除两数的平均值。</li>
</ul>

<p>两数 <code>a</code>&nbsp;和 <code>b</code>&nbsp;的 <strong>平均值</strong>&nbsp;为&nbsp;<code>(a + b) / 2</code>&nbsp;。</p>

<ul>
	<li>比方说，<code>2</code>&nbsp;和&nbsp;<code>3</code>&nbsp;的平均值是&nbsp;<code>(2 + 3) / 2 = 2.5</code>&nbsp;。</li>
</ul>

<p>返回上述过程能得到的 <strong>不同</strong>&nbsp;平均值的数目。</p>

<p><strong>注意</strong>&nbsp;，如果最小值或者最大值有重复元素，可以删除任意一个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [4,1,4,0,3,5]
<b>输出：</b>2
<strong>解释：</strong>
1. 删除 0 和 5 ，平均值是 (0 + 5) / 2 = 2.5 ，现在 nums = [4,1,4,3] 。
2. 删除 1 和 4 ，平均值是 (1 + 4) / 2 = 2.5 ，现在 nums = [4,3] 。
3. 删除 3 和 4 ，平均值是 (3 + 4) / 2 = 3.5 。
2.5 ，2.5 和 3.5 之中总共有 2 个不同的数，我们返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,100]
<b>输出：</b>1
<strong>解释：</strong>
删除 1 和 100 后只有一个平均值，所以我们返回 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>nums.length</code>&nbsp;是偶数。</li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 双指针
- 排序

## 提示

1. Try sorting the array.
2. Store the averages being calculated, and find the distinct ones.

## 示例

```
[4,1,4,0,3,5]
[1,100]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int distinctAverages(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int distinctAverages(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
```

### C

```c
int distinctAverages(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DistinctAverages(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var distinctAverages = function(nums) {
    
};
```

### TypeScript

```typescript
function distinctAverages(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function distinctAverages($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distinctAverages(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distinctAverages(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int distinctAverages(List<int> nums) {
    
  }
}
```

### Go

```golang
func distinctAverages(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def distinct_averages(nums)
    
end
```

### Scala

```scala
object Solution {
    def distinctAverages(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distinct_averages(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (distinct-averages nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec distinct_averages(Nums :: [integer()]) -> integer().
distinct_averages(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distinct_averages(nums :: [integer]) :: integer
  def distinct_averages(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distinctAverages(nums: Array<Int64>): Int64 {

    }
}
```

