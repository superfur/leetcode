# 2659. 将数组清空

## 题目描述

<p>给你一个包含若干 <strong>互不相同</strong>&nbsp;整数的数组&nbsp;<code>nums</code>&nbsp;，你需要执行以下操作 <strong>直到</strong><strong>数组为空</strong>&nbsp;：</p>

<ul>
	<li>如果数组中第一个元素是当前数组中的 <strong>最小值</strong>&nbsp;，则删除它。</li>
	<li>否则，将第一个元素移动到数组的 <strong>末尾</strong>&nbsp;。</li>
</ul>

<p>请你返回需要多少个操作使<em>&nbsp;</em><code>nums</code><em>&nbsp;</em>为空。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,4,-1]
<b>输出：</b>5
</pre>

<table style="border: 2px solid black; border-collapse: collapse;">
	<thead>
		<tr>
			<th style="border: 2px solid black; padding: 5px;">Operation</th>
			<th style="border: 2px solid black; padding: 5px;">Array</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">1</td>
			<td style="border: 2px solid black; padding: 5px;">[4, -1, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">2</td>
			<td style="border: 2px solid black; padding: 5px;">[-1, 3, 4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">3</td>
			<td style="border: 2px solid black; padding: 5px;">[3, 4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">4</td>
			<td style="border: 2px solid black; padding: 5px;">[4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">5</td>
			<td style="border: 2px solid black; padding: 5px;">[]</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,4,3]
<b>输出：</b>5
</pre>

<table style="border: 2px solid black; border-collapse: collapse;">
	<thead>
		<tr>
			<th style="border: 2px solid black; padding: 5px;">Operation</th>
			<th style="border: 2px solid black; padding: 5px;">Array</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">1</td>
			<td style="border: 2px solid black; padding: 5px;">[2, 4, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">2</td>
			<td style="border: 2px solid black; padding: 5px;">[4, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">3</td>
			<td style="border: 2px solid black; padding: 5px;">[3, 4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">4</td>
			<td style="border: 2px solid black; padding: 5px;">[4]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">5</td>
			<td style="border: 2px solid black; padding: 5px;">[]</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3]
<b>输出：</b>3
</pre>

<table style="border: 2px solid black; border-collapse: collapse;">
	<thead>
		<tr>
			<th style="border: 2px solid black; padding: 5px;">Operation</th>
			<th style="border: 2px solid black; padding: 5px;">Array</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">1</td>
			<td style="border: 2px solid black; padding: 5px;">[2, 3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">2</td>
			<td style="border: 2px solid black; padding: 5px;">[3]</td>
		</tr>
		<tr>
			<td style="border: 2px solid black; padding: 5px;">3</td>
			<td style="border: 2px solid black; padding: 5px;">[]</td>
		</tr>
	</tbody>
</table>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9&nbsp;</sup>&lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code>&nbsp;中的元素 <strong>互不相同</strong>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 树状数组
- 线段树
- 数组
- 二分查找
- 有序集合
- 排序

## 提示

1. Understand the order in which the indices are removed from the array.
2. We don’t really need to delete or move the elements, only the array length matters.
3. Upon removing an index, decide how many steps it takes to move to the next one.
4. Use a data structure to speed up the calculation.

## 示例

```
[3,4,-1]
[1,2,4,3]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long countOperationsToEmptyArray(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long countOperationsToEmptyArray(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countOperationsToEmptyArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        
```

### C

```c
long long countOperationsToEmptyArray(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long CountOperationsToEmptyArray(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countOperationsToEmptyArray = function(nums) {
    
};
```

### TypeScript

```typescript
function countOperationsToEmptyArray(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countOperationsToEmptyArray($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countOperationsToEmptyArray(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countOperationsToEmptyArray(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int countOperationsToEmptyArray(List<int> nums) {
    
  }
}
```

### Go

```golang
func countOperationsToEmptyArray(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_operations_to_empty_array(nums)
    
end
```

### Scala

```scala
object Solution {
    def countOperationsToEmptyArray(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_operations_to_empty_array(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (count-operations-to-empty-array nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_operations_to_empty_array(Nums :: [integer()]) -> integer().
count_operations_to_empty_array(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_operations_to_empty_array(nums :: [integer]) :: integer
  def count_operations_to_empty_array(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countOperationsToEmptyArray(nums: Array<Int64>): Int64 {

    }
}
```

