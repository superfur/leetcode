# 3011. 判断一个数组是否可以变为有序

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始且全是 <strong>正</strong>&nbsp;整数的数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>一次 <b>操作</b>&nbsp;中，如果两个 <strong>相邻</strong>&nbsp;元素在二进制下 <span data-keyword="set-bit">设置位</span> 的数目 <strong>相同</strong>&nbsp;，那么你可以将这两个元素交换。你可以执行这个操作 <strong>任意次</strong>&nbsp;（<strong>也可以 0 次</strong>）。</p>

<p>如果你可以使数组变为非降序，请你返回&nbsp;<code>true</code> ，否则返回&nbsp;<code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [8,4,2,30,15]
<b>输出：</b>true
<b>解释：</b>我们先观察每个元素的二进制表示。 2 ，4 和 8 分别都只有一个数位为 1 ，分别为 "10" ，"100" 和 "1000" 。15 和 30 分别有 4 个数位为 1 ："1111" 和 "11110" 。
我们可以通过 4 个操作使数组非降序：
- 交换 nums[0] 和 nums[1] 。8 和 4 分别只有 1 个数位为 1 。数组变为 [4,8,2,30,15] 。
- 交换 nums[1] 和 nums[2] 。8 和 2 分别只有 1 个数位为 1 。数组变为 [4,2,8,30,15] 。
- 交换 nums[0] 和 nums[1] 。4 和 2 分别只有 1 个数位为 1 。数组变为 [2,4,8,30,15] 。
- 交换 nums[3] 和 nums[4] 。30 和 15 分别有 4 个数位为 1 ，数组变为 [2,4,8,15,30] 。
数组变成有序的，所以我们返回 true 。
注意我们还可以通过其他的操作序列使数组变得有序。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4,5]
<b>输出：</b>true
<b>解释：</b>数组已经是非降序的，所以我们返回 true 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [3,16,8,4,2]
<b>输出：</b>false
<b>解释：</b>无法通过操作使数组变为非降序。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2<sup>8</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 排序

## 提示

1. Split the array into segments. Each segment contains consecutive elements with the same number of set bits.
2. From left to right, the previous segment’s largest element should be smaller than the current segment’s smallest element.

## 示例

```
[8,4,2,30,15]
[1,2,3,4,5]
[3,16,8,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canSortArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canSortArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        
```

### C

```c
bool canSortArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanSortArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canSortArray = function(nums) {
    
};
```

### TypeScript

```typescript
function canSortArray(nums: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function canSortArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canSortArray(_ nums: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canSortArray(nums: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canSortArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func canSortArray(nums []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Boolean}
def can_sort_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def canSortArray(nums: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_sort_array(nums: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-sort-array nums)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_sort_array(Nums :: [integer()]) -> boolean().
can_sort_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_sort_array(nums :: [integer]) :: boolean
  def can_sort_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canSortArray(nums: Array<Int64>): Bool {

    }
}
```

