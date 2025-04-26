# 3264. K 次乘运算后的最终数组 I

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，一个整数&nbsp;<code>k</code>&nbsp;&nbsp;和一个整数&nbsp;<code>multiplier</code>&nbsp;。</p>

<p>你需要对 <code>nums</code>&nbsp;执行 <code>k</code>&nbsp;次操作，每次操作中：</p>

<ul>
	<li>找到 <code>nums</code>&nbsp;中的 <strong>最小</strong>&nbsp;值&nbsp;<code>x</code>&nbsp;，如果存在多个最小值，选择最 <strong>前面</strong>&nbsp;的一个。</li>
	<li>将 <code>x</code>&nbsp;替换为&nbsp;<code>x * multiplier</code>&nbsp;。</li>
</ul>

<p>请你返回执行完 <code>k</code>&nbsp;次乘运算之后，最终的 <code>nums</code>&nbsp;数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [2,1,3,5,6], k = 5, multiplier = 2</span></p>

<p><span class="example-io"><b>输出：</b>[8,4,6,5,6]</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>操作</th>
			<th>结果</th>
		</tr>
		<tr>
			<td>1 次操作后</td>
			<td>[2, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>2 次操作后</td>
			<td>[4, 2, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>3 次操作后</td>
			<td>[4, 4, 3, 5, 6]</td>
		</tr>
		<tr>
			<td>4 次操作后</td>
			<td>[4, 4, 6, 5, 6]</td>
		</tr>
		<tr>
			<td>5 次操作后</td>
			<td>[8, 4, 6, 5, 6]</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b></span>nums = [1,2], k = 3, multiplier = 4</p>

<p><span class="example-io"><b>输出：</b></span>[16,8]</p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>操作</th>
			<th>结果</th>
		</tr>
		<tr>
			<td>1 次操作后</td>
			<td>[4, 2]</td>
		</tr>
		<tr>
			<td>2 次操作后</td>
			<td>[4, 8]</td>
		</tr>
		<tr>
			<td>3 次操作后</td>
			<td>[16, 8]</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>1 &lt;= multiplier &lt;= 5</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 模拟
- 堆（优先队列）

## 提示

1. Maintain sorted pairs <code>(nums[index], index)</code> in a priority queue.
2. Simulate the operation <code>k</code> times.

## 示例

```
[2,1,3,5,6]
5
2
[1,2]
3
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetFinalState(int[] nums, int k, int multiplier) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} multiplier
 * @return {number[]}
 */
var getFinalState = function(nums, k, multiplier) {
    
};
```

### TypeScript

```typescript
function getFinalState(nums: number[], k: number, multiplier: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @param Integer $multiplier
     * @return Integer[]
     */
    function getFinalState($nums, $k, $multiplier) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getFinalState(_ nums: [Int], _ k: Int, _ multiplier: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getFinalState(nums: IntArray, k: Int, multiplier: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getFinalState(List<int> nums, int k, int multiplier) {
    
  }
}
```

### Go

```golang
func getFinalState(nums []int, k int, multiplier int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} multiplier
# @return {Integer[]}
def get_final_state(nums, k, multiplier)
    
end
```

### Scala

```scala
object Solution {
    def getFinalState(nums: Array[Int], k: Int, multiplier: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_final_state(nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-final-state nums k multiplier)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_final_state(Nums :: [integer()], K :: integer(), Multiplier :: integer()) -> [integer()].
get_final_state(Nums, K, Multiplier) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_final_state(nums :: [integer], k :: integer, multiplier :: integer) :: [integer]
  def get_final_state(nums, k, multiplier) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getFinalState(nums: Array<Int64>, k: Int64, multiplier: Int64): Array<Int64> {

    }
}
```

