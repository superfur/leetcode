# 3194. 最小元素和最大元素的最小平均值

## 题目描述

<p>你有一个初始为空的浮点数数组 <code>averages</code>。另给你一个包含 <code>n</code> 个整数的数组 <code>nums</code>，其中 <code>n</code> 为偶数。</p>

<p>你需要重复以下步骤 <code>n / 2</code> 次：</p>

<ul>
	<li>从 <code>nums</code> 中移除<strong> 最小 </strong>的元素 <code>minElement</code> 和<strong> 最大 </strong>的元素 <code>maxElement</code>。</li>
	<li>将 <code>(minElement + maxElement) / 2</code> 加入到 <code>averages</code> 中。</li>
</ul>

<p>返回 <code>averages</code> 中的 <strong>最小 </strong>元素。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [7,8,3,4,15,13,4,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">5.5</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>步骤</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[7,8,3,4,15,13,4,1]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[7,8,3,4,13,4]</td>
			<td>[8]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[7,8,4,4]</td>
			<td>[8,8]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[7,4]</td>
			<td>[8,8,6]</td>
		</tr>
		<tr>
			<td>4</td>
			<td>[]</td>
			<td>[8,8,6,5.5]</td>
		</tr>
	</tbody>
</table>
返回 averages 中最小的元素，即 5.5。</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,9,8,3,10,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">5.5</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>步骤</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,9,8,3,10,5]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[9,8,3,5]</td>
			<td>[5.5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[8,5]</td>
			<td>[5.5,6]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[]</td>
			<td>[5.5,6,6.5]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,7,8,9]</span></p>

<p><strong>输出：</strong> <span class="example-io">5.0</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>步骤</th>
			<th>nums</th>
			<th>averages</th>
		</tr>
		<tr>
			<td>0</td>
			<td>[1,2,3,7,8,9]</td>
			<td>[]</td>
		</tr>
		<tr>
			<td>1</td>
			<td>[2,3,7,8]</td>
			<td>[5]</td>
		</tr>
		<tr>
			<td>2</td>
			<td>[3,7]</td>
			<td>[5,5]</td>
		</tr>
		<tr>
			<td>3</td>
			<td>[]</td>
			<td>[5,5,5]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == nums.length &lt;= 50</code></li>
	<li><code>n</code> 为偶数。</li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 排序

## 提示

1. If <code>nums</code> is sorted, then the elements of <code>averages</code> are <code>(nums[i] + nums[n - i - 1]) / 2</code>  for all <code>i < n / 2</code>.

## 示例

```
[7,8,3,4,15,13,4,1]
[1,9,8,3,10,5]
[1,2,3,7,8,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    double minimumAverage(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public double minimumAverage(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        
```

### Python3

```python3
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
```

### C

```c
double minimumAverage(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public double MinimumAverage(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumAverage = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumAverage(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Float
     */
    function minimumAverage($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumAverage(_ nums: [Int]) -> Double {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumAverage(nums: IntArray): Double {
        
    }
}
```

### Dart

```dart
class Solution {
  double minimumAverage(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumAverage(nums []int) float64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Float}
def minimum_average(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumAverage(nums: Array[Int]): Double = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_average(nums: Vec<i32>) -> f64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-average nums)
  (-> (listof exact-integer?) flonum?)
  )
```

### Erlang

```erlang
-spec minimum_average(Nums :: [integer()]) -> float().
minimum_average(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_average(nums :: [integer]) :: float
  def minimum_average(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumAverage(nums: Array<Int64>): Float64 {

    }
}
```

