# 3379. 转换数组

## 题目描述

<p>给你一个整数数组 <code>nums</code>，它表示一个循环数组。请你遵循以下规则创建一个大小&nbsp;<strong>相同&nbsp;</strong>的新数组 <code>result</code>&nbsp;：</p>
对于每个下标&nbsp;<code>i</code>（其中 <code>0 &lt;= i &lt; nums.length</code>），独立执行以下操作：

<ul>
	<li>如果 <code>nums[i] &gt; 0</code>：从下标&nbsp;<code>i</code> 开始，向&nbsp;<strong>右&nbsp;</strong>移动 <code>nums[i]</code> 步，在循环数组中落脚的下标对应的值赋给 <code>result[i]</code>。</li>
	<li>如果 <code>nums[i] &lt; 0</code>：从下标&nbsp;<code>i</code> 开始，向&nbsp;<strong>左&nbsp;</strong>移动 <code>abs(nums[i])</code> 步，在循环数组中落脚的下标对应的值赋给 <code>result[i]</code>。</li>
	<li>如果 <code>nums[i] == 0</code>：将 <code>nums[i]</code> 的值赋给 <code>result[i]</code>。</li>
</ul>

<p>返回新数组 <code>result</code>。</p>

<p><strong>注意：</strong>由于 <code>nums</code> 是循环数组，向右移动超过最后一个元素时将回到开头，向左移动超过第一个元素时将回到末尾。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,-2,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">[1,1,1,3]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>nums[0]</code> 等于 3，向右移动 3 步到 <code>nums[3]</code>，因此 <code>result[0]</code> 为 1。</li>
	<li>对于 <code>nums[1]</code> 等于 -2，向左移动 2 步到 <code>nums[3]</code>，因此 <code>result[1]</code> 为 1。</li>
	<li>对于 <code>nums[2]</code> 等于 1，向右移动 1 步到 <code>nums[3]</code>，因此 <code>result[2]</code> 为 1。</li>
	<li>对于 <code>nums[3]</code> 等于 1，向右移动 1 步到 <code>nums[0]</code>，因此 <code>result[3]</code> 为 3。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [-1,4,-1]</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,-1,4]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>nums[0]</code> 等于 -1，向左移动 1 步到 <code>nums[2]</code>，因此 <code>result[0]</code> 为 -1。</li>
	<li>对于 <code>nums[1]</code> 等于 4，向右移动 4 步到 <code>nums[2]</code>，因此 <code>result[1]</code> 为 -1。</li>
	<li>对于 <code>nums[2]</code> 等于 -1，向左移动 1 步到 <code>nums[1]</code>，因此 <code>result[2]</code> 为 4。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Simulate the operations as described in the statement

## 示例

```
[3,-2,1,1]
[-1,4,-1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] constructTransformedArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructTransformedArray(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ConstructTransformedArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var constructTransformedArray = function(nums) {
    
};
```

### TypeScript

```typescript
function constructTransformedArray(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function constructTransformedArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func constructTransformedArray(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun constructTransformedArray(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> constructTransformedArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func constructTransformedArray(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def construct_transformed_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def constructTransformedArray(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn construct_transformed_array(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (construct-transformed-array nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec construct_transformed_array(Nums :: [integer()]) -> [integer()].
construct_transformed_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec construct_transformed_array(nums :: [integer]) :: [integer]
  def construct_transformed_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func constructTransformedArray(nums: Array<Int64>): Array<Int64> {

    }
}
```

