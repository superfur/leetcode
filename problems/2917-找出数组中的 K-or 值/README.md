# 2917. 找出数组中的 K-or 值

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数 <code>k</code> 。让我们通过扩展标准的按位或来介绍 <strong>K-or</strong> 操作。在 K-or 操作中，如果在 <code>nums</code> 中，至少存在 <code>k</code> 个元素的第 <code>i</code> 位值为 1 ，那么 K-or 中的第 <code>i</code> 位的值是 1 。</p>

<p>返回 <code>nums</code> 的 <strong>K-or</strong> 值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,12,9,8,9,15], k = 4
<strong>输出：</strong>9
<strong>解释：</strong>
用二进制表示 numbers：
</pre>

<table style="text-indent:10px; margin-bottom=20px;">
	<tbody>
		<tr>
			<th><b>Number</b></th>
			<th>Bit 3</th>
			<th>Bit 2</th>
			<th>Bit 1</th>
			<th>Bit 0</th>
		</tr>
		<tr>
			<td><b>7</b></td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td><b>12</b></td>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td><b>9</b></td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td><b>8</b></td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td><b>9</b></td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td><b>15</b></td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td><b>Result = 9</b></td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<pre>
位 0 在 7, 9, 9, 15 中为 1。位 3 在 12, 9, 8, 9, 15 中为 1。 只有位 0 和 3 满足。结果是 (1001)<sub>2</sub> = 9。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,12,1,11,4,5], k = 6
<strong>输出：</strong>0
<strong>解释：</strong>没有位在所有 6 个数字中都为 1，如 k = 6 所需要的。所以，答案为 0。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [10,8,5,9,11,6,8], k = 1
<strong>输出：</strong>15
<strong>解释：</strong>因为 k == 1 ，数组的 1-or 等于其中所有元素按位或运算的结果。因此，答案为 10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>0 &lt;= nums[i] &lt; 2<sup>31</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组

## 提示

1. Fix a <code>bit</code> from the range <code>[0, 31]</code>, then count the number of elements of <code>nums</code> that have <code>bit</code> set in them.
2. <code>bit</code> is set in integer <code>x</code> if and only if <code>2<sup>bit</sup> AND x == 2<sup>bit</sup></code>, where <code>AND</code> is the bitwise <code>AND</code> operation.

## 示例

```
[7,12,9,8,9,15]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findKOr(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int findKOr(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findKOr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int findKOr(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindKOr(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKOr = function(nums, k) {
    
};
```

### TypeScript

```typescript
function findKOr(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function findKOr($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findKOr(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findKOr(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findKOr(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func findKOr(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_k_or(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def findKOr(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_k_or(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-k-or nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_k_or(Nums :: [integer()], K :: integer()) -> integer().
find_k_or(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_k_or(nums :: [integer], k :: integer) :: integer
  def find_k_or(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findKOr(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

