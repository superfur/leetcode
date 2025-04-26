# 3265. 统计近似相等数对 I

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>如果我们执行以下操作 <strong>至多一次</strong>&nbsp;可以让两个整数&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;相等，那么我们称这个数对是 <strong>近似相等</strong>&nbsp;的：</p>

<ul>
	<li>选择&nbsp;<code>x</code> <strong>或者</strong>&nbsp;<code>y</code> &nbsp;之一，将这个数字中的两个数位交换。</li>
</ul>

<p>请你返回 <code>nums</code>&nbsp;中，下标 <code>i</code>&nbsp;和 <code>j</code>&nbsp;满足&nbsp;<code>i &lt; j</code>&nbsp;且&nbsp;<code>nums[i]</code> 和&nbsp;<code>nums[j]</code> <strong>近似相等</strong>&nbsp;的数对数目。</p>

<p><b>注意</b>&nbsp;，执行操作后一个整数可以有前导 0 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,12,30,17,21]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><strong>解释：</strong></p>

<p>近似相等数对包括：</p>

<ul>
	<li>3 和 30 。交换 30 中的数位 3 和 0 ，得到 3 。</li>
	<li>12 和 21 。交换12 中的数位 1 和 2 ，得到 21 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,1,1,1,1]</span></p>

<p><span class="example-io"><b>输出：</b>10</span></p>

<p><strong>解释：</strong></p>

<p>数组中的任意两个元素都是近似相等的。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [123,231]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>我们无法通过交换 123&nbsp;或者 231 中的两个数位得到另一个数。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数
- 枚举
- 排序

## 提示

1. Since the constraint on the number of elements is small, you can check all pairs in the array.
2. For each pair, perform an operation on one of the elements and check if it becomes equal to the other.

## 示例

```
[3,12,30,17,21]
[1,1,1,1,1]
[123,231]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        
```

### C

```c
int countPairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countPairs = function(nums) {
    
};
```

### TypeScript

```typescript
function countPairs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countPairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func countPairs(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pairs(Nums :: [integer()]) -> integer().
count_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer]) :: integer
  def count_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(nums: Array<Int64>): Int64 {

    }
}
```

