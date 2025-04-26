# 3267. 统计近似相等数对 II

## 题目描述

<p><strong>注意：</strong>在这个问题中，操作次数增加为至多&nbsp;<strong>两次</strong>&nbsp;。</p>

<p>给你一个正整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>如果我们执行以下操作 <strong>至多<u>两次</u></strong>&nbsp;可以让两个整数&nbsp;<code>x</code> 和&nbsp;<code>y</code>&nbsp;相等，那么我们称这个数对是 <strong>近似相等</strong>&nbsp;的：</p>

<ul>
	<li>选择&nbsp;<code>x</code> <strong>或者</strong>&nbsp;<code>y</code> &nbsp;之一，将这个数字中的两个数位交换。</li>
</ul>

<p>请你返回 <code>nums</code>&nbsp;中，下标 <code>i</code>&nbsp;和 <code>j</code>&nbsp;满足&nbsp;<code>i &lt; j</code>&nbsp;且&nbsp;<code>nums[i]</code> 和&nbsp;<code>nums[j]</code> <strong>近似相等</strong>&nbsp;的数对数目。</p>

<p><b>注意</b>&nbsp;，执行操作后得到的整数可以有前导 0 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1023,2310,2130,213]</span></p>

<p><span class="example-io"><b>输出：</b>4</span></p>

<p><strong>解释：</strong></p>

<p>近似相等数对包括：</p>

<ul>
	<li>1023 和 2310 。交换 1023 中数位 1 和 2 ，然后交换数位 0 和 3 ，得到 2310 。</li>
	<li>1023 和 213 。交换 1023 中数位 1 和 0 ，然后交换数位 1 和 2 ，得到 0213 ，也就是 213 。</li>
	<li>2310 和 213 。交换 2310 中数位 2 和 0 ，然后交换数位 3 和 2 ，得到 0213 ，也就是 213 。</li>
	<li>2310 和 2130 。交换 2310 中数位 3 和 1 ，得到 2130 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,10,100]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>近似相等数对包括：</p>

<ul>
	<li>1 和 10 。交换 10 中数位 1 和 0&nbsp;，得到 01 ，也就是 1&nbsp;。</li>
	<li>1 和 100 。交换 100 中数位 1 和从左往右的第二个 0 ，得到 001 ，也就是 1 。</li>
	<li>10 和 100 。交换 100 中数位 1 和从左往右的第一个 0 ，得到 010 ，也就是 10 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 5000</code></li>
	<li><code>1 &lt;= nums[i] &lt;&nbsp;10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 计数
- 枚举
- 排序

## 提示

1. For each element, find all possible integers we can get by applying the operations.
2. Store the frequencies of all the integers in a hashmap.

## 示例

```
[1023,2310,2130,213]
[1,10,100]
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

