# 3028. 边界上的蚂蚁

## 题目描述

<p>边界上有一只蚂蚁，它有时向 <strong>左 </strong>走，有时向 <strong>右 </strong>走。</p>

<p>给你一个 <strong>非零</strong> 整数数组 <code>nums</code> 。蚂蚁会按顺序读取 <code>nums</code> 中的元素，从第一个元素开始直到结束。每一步，蚂蚁会根据当前元素的值移动：</p>

<ul>
	<li>如果 <code>nums[i] &lt; 0</code> ，向 <strong>左</strong> 移动<!-- notionvc: 55fee232-4fc9-445f-952a-f1b979415864 --> <code>-nums[i]</code>单位。</li>
	<li>如果 <code>nums[i] &gt; 0</code> ，向 <strong>右</strong> 移动 <code>nums[i]</code>单位。</li>
</ul>

<p>返回蚂蚁 <strong>返回 </strong>到边界上的次数。</p>

<p><strong>注意：</strong></p>

<ul>
	<li>边界两侧有无限的空间。</li>
	<li>只有在蚂蚁移动了 <code>|nums[i]|</code> 单位后才检查它是否位于边界上。换句话说，如果蚂蚁只是在移动过程中穿过了边界，则不会计算在内。<!-- notionvc: 5ff95338-8634-4d02-a085-1e83c0be6fcd --></li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,-5]
<strong>输出：</strong>1
<strong>解释：</strong>第 1 步后，蚂蚁距边界右侧 2 单位远<!-- notionvc: 61ace51c-559f-4bc6-800f-0a0db2540433 -->。
第 2 步后，蚂蚁距边界右侧 5 单位远<!-- notionvc: 61ace51c-559f-4bc6-800f-0a0db2540433 -->。
第 3 步后，蚂蚁位于边界上。
所以答案是 1 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,-3,-4]
<strong>输出：</strong>0
<strong>解释：</strong>第 1 步后，蚂蚁距边界右侧 3 单位远<!-- notionvc: 61ace51c-559f-4bc6-800f-0a0db2540433 -->。
第 2 步后，蚂蚁距边界右侧 5 单位远<!-- notionvc: 61ace51c-559f-4bc6-800f-0a0db2540433 -->。
第 3 步后，蚂蚁距边界右侧 2 单位远<!-- notionvc: 61ace51c-559f-4bc6-800f-0a0db2540433 -->。
第 4 步后，蚂蚁距边界左侧 2 单位远<!-- notionvc: 61ace51c-559f-4bc6-800f-0a0db2540433 -->。
蚂蚁从未返回到边界上，所以答案是 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li><code>nums[i] != 0</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 前缀和
- 模拟

## 提示

1. Define a variable and add <code>nums[i]</code> to it in each step.

## 示例

```
[2,3,-5]
[3,2,-3,-4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int returnToBoundaryCount(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int returnToBoundaryCount(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        
```

### C

```c
int returnToBoundaryCount(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReturnToBoundaryCount(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var returnToBoundaryCount = function(nums) {
    
};
```

### TypeScript

```typescript
function returnToBoundaryCount(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function returnToBoundaryCount($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func returnToBoundaryCount(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun returnToBoundaryCount(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int returnToBoundaryCount(List<int> nums) {
    
  }
}
```

### Go

```golang
func returnToBoundaryCount(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def return_to_boundary_count(nums)
    
end
```

### Scala

```scala
object Solution {
    def returnToBoundaryCount(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn return_to_boundary_count(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (return-to-boundary-count nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec return_to_boundary_count(Nums :: [integer()]) -> integer().
return_to_boundary_count(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec return_to_boundary_count(nums :: [integer]) :: integer
  def return_to_boundary_count(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func returnToBoundaryCount(nums: Array<Int64>): Int64 {

    }
}
```

