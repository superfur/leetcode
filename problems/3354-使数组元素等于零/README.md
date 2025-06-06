# 3354. 使数组元素等于零

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code> 。</p>

<p>开始时，选择一个满足 <code>nums[curr] == 0</code> 的起始位置&nbsp;<code>curr</code>&nbsp;，并选择一个移动 <strong>方向</strong>&nbsp;：向左或者向右。</p>

<p>此后，你需要重复下面的过程：</p>

<ul>
	<li>如果&nbsp;<code>curr</code>&nbsp;超过范围&nbsp;<code>[0, n - 1]</code> ，过程结束。</li>
	<li>如果&nbsp;<code>nums[curr] == 0</code> ，沿当前方向继续移动：如果向右移，则 <strong>递增</strong>&nbsp;<code>curr</code>&nbsp;；如果向左移，则 <strong>递减</strong>&nbsp;<code>curr</code>&nbsp;。</li>
	<li>如果&nbsp;<code>nums[curr] &gt; 0</code>:
	<ul>
		<li>将&nbsp;<code>nums[curr]</code>&nbsp;减&nbsp;1 。</li>
		<li><strong>反转</strong>&nbsp;移动方向（向左变向右，反之亦然）。</li>
		<li>沿新方向移动一步。</li>
	</ul>
	</li>
</ul>

<p>如果在结束整个过程后，<code>nums</code>&nbsp;中的所有元素都变为 0 ，则认为选出的初始位置和移动方向 <strong>有效</strong>&nbsp;。</p>

<p>返回可能的有效选择方案数目。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,0,2,0,3]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b></p>

<p>可能的有效选择方案如下：</p>

<ul>
	<li>选择&nbsp;<code>curr = 3</code>&nbsp;并向左移动。

	<ul>
		<li><code>[1,0,2,<strong><u>0</u></strong>,3] -&gt; [1,0,<strong><u>2</u></strong>,0,3] -&gt; [1,0,1,<strong><u>0</u></strong>,3] -&gt; [1,0,1,0,<strong><u>3</u></strong>] -&gt; [1,0,1,<strong><u>0</u></strong>,2] -&gt; [1,0,<strong><u>1</u></strong>,0,2] -&gt; [1,0,0,<strong><u>0</u></strong>,2] -&gt; [1,0,0,0,<strong><u>2</u></strong>] -&gt; [1,0,0,<strong><u>0</u></strong>,1] -&gt; [1,0,<strong><u>0</u></strong>,0,1] -&gt; [1,<strong><u>0</u></strong>,0,0,1] -&gt; [<strong><u>1</u></strong>,0,0,0,1] -&gt; [0,<strong><u>0</u></strong>,0,0,1] -&gt; [0,0,<strong><u>0</u></strong>,0,1] -&gt; [0,0,0,<strong><u>0</u></strong>,1] -&gt; [0,0,0,0,<strong><u>1</u></strong>] -&gt; [0,0,0,0,0]</code>.</li>
	</ul>
	</li>
	<li>选择&nbsp;<code>curr = 3</code>&nbsp;并向右移动。
	<ul>
		<li><code>[1,0,2,<strong><u>0</u></strong>,3] -&gt; [1,0,2,0,<strong><u>3</u></strong>] -&gt; [1,0,2,<strong><u>0</u></strong>,2] -&gt; [1,0,<strong><u>2</u></strong>,0,2] -&gt; [1,0,1,<strong><u>0</u></strong>,2] -&gt; [1,0,1,0,<strong><u>2</u></strong>] -&gt; [1,0,1,<strong><u>0</u></strong>,1] -&gt; [1,0,<strong><u>1</u></strong>,0,1] -&gt; [1,0,0,<strong><u>0</u></strong>,1] -&gt; [1,0,0,0,<strong><u>1</u></strong>] -&gt; [1,0,0,<strong><u>0</u></strong>,0] -&gt; [1,0,<strong><u>0</u></strong>,0,0] -&gt; [1,<strong><u>0</u></strong>,0,0,0] -&gt; [<strong><u>1</u></strong>,0,0,0,0] -&gt; [0,0,0,0,0].</code></li>
	</ul>
	</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,3,4,0,4,1,0]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><b>解释：</b></p>

<p>不存在有效的选择方案。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
	<li>至少存在一个元素&nbsp;<code>i</code>&nbsp;满足&nbsp;<code>nums[i] == 0</code> 。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 前缀和
- 模拟

## 提示

1. Since the constraints are very small, you can simulate the process described.

## 示例

```
[1,0,2,0,3]
[2,3,4,0,4,1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countValidSelections(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countValidSelections(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
```

### C

```c
int countValidSelections(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountValidSelections(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countValidSelections = function(nums) {
    
};
```

### TypeScript

```typescript
function countValidSelections(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countValidSelections($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countValidSelections(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countValidSelections(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countValidSelections(List<int> nums) {
    
  }
}
```

### Go

```golang
func countValidSelections(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_valid_selections(nums)
    
end
```

### Scala

```scala
object Solution {
    def countValidSelections(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_valid_selections(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-valid-selections nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_valid_selections(Nums :: [integer()]) -> integer().
count_valid_selections(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_valid_selections(nums :: [integer]) :: integer
  def count_valid_selections(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countValidSelections(nums: Array<Int64>): Int64 {

    }
}
```

