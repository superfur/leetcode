# 3467. 将数组按照奇偶性转化

## 题目描述

<p>给你一个整数数组 <code>nums</code>。请你按照以下顺序 <strong>依次</strong>&nbsp;执行操作，转换 <code>nums</code>：</p>

<ol>
	<li>将每个偶数替换为 0。</li>
	<li>将每个奇数替换为 1。</li>
	<li>按&nbsp;<strong>非递减&nbsp;</strong>顺序排序修改后的数组。</li>
</ol>

<p>执行完这些操作后，返回结果数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [4,3,2,1]</span></p>

<p><strong>输出：</strong><span class="example-io">[0,0,1,1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将偶数（4 和 2）替换为 0，将奇数（3 和 1）替换为 1。现在，<code>nums = [0, 1, 0, 1]</code>。</li>
	<li>按非递减顺序排序 <code>nums</code>，得到 <code>nums = [0, 0, 1, 1]</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,5,1,4,2]</span></p>

<p><strong>输出：</strong><span class="example-io">[0,0,1,1,1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将偶数（4 和 2）替换为 0，将奇数（1, 5 和 1）替换为 1。现在，<code>nums = [1, 1, 1, 0, 0]</code>。</li>
	<li>按非递减顺序排序&nbsp;<code>nums</code>，得到 <code>nums = [0, 0, 1, 1, 1]</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 计数
- 排序

## 提示

1. Let <code>x</code> be the number of even numbers, and <code>y</code> be the number of odd numbers. Output <code>0</code> <code>x</code> times, followed by <code>1</code> <code>y</code> times.

## 示例

```
[4,3,2,1]
[1,5,1,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] transformArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* transformArray(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] TransformArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var transformArray = function(nums) {
    
};
```

### TypeScript

```typescript
function transformArray(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function transformArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func transformArray(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun transformArray(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> transformArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func transformArray(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def transform_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def transformArray(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn transform_array(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (transform-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec transform_array(Nums :: [integer()]) -> [integer()].
transform_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec transform_array(nums :: [integer]) :: [integer]
  def transform_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func transformArray(nums: Array<Int64>): Array<Int64> {

    }
}
```

