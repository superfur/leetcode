# 2902. 和带限制的子多重集合的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的非负整数数组&nbsp;<code>nums</code>&nbsp;和两个整数&nbsp;<code>l</code> 和&nbsp;<code>r</code>&nbsp;。</p>

<p>请你返回&nbsp;<code>nums</code>&nbsp;中子多重集合的和在闭区间&nbsp;<code>[l, r]</code>&nbsp;之间的 <strong>子多重集合的数目</strong> 。</p>

<p>由于答案可能很大，请你将答案对&nbsp;<code>10<sup>9 </sup>+ 7</code>&nbsp;取余后返回。</p>

<p><strong>子多重集合</strong> 指的是从数组中选出一些元素构成的 <strong>无序</strong>&nbsp;集合，每个元素 <code>x</code>&nbsp;出现的次数可以是&nbsp;<code>0, 1, ..., occ[x]</code>&nbsp;次，其中&nbsp;<code>occ[x]</code>&nbsp;是元素&nbsp;<code>x</code>&nbsp;在数组中的出现次数。</p>

<p><b>注意：</b></p>

<ul>
	<li>如果两个子多重集合中的元素排序后一模一样，那么它们两个是相同的&nbsp;<strong>子多重集合</strong>&nbsp;。</li>
	<li><strong>空</strong>&nbsp;集合的和是 <code>0</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,2,3], l = 6, r = 6
<b>输出：</b>1
<b>解释：</b>唯一和为 6 的子集合是 {1, 2, 3} 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,4,2,7], l = 1, r = 5
<b>输出：</b>7
<b>解释：</b>和在闭区间 [1, 5] 之间的子多重集合为 {1} ，{2} ，{4} ，{2, 2} ，{1, 2} ，{1, 4} 和 {1, 2, 2} 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,1,3,5,2], l = 3, r = 5
<b>输出：</b>9
<b>解释：</b>和在闭区间 [3, 5] 之间的子多重集合为 {3} ，{5} ，{1, 2} ，{1, 3} ，{2, 2} ，{2, 3} ，{1, 1, 2} ，{1, 1, 3} 和 {1, 2, 2} 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>nums</code> 的和不超过&nbsp;<code>2 * 10<sup>4</sup></code> 。</li>
	<li><code>0 &lt;= l &lt;= r &lt;= 2 * 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 动态规划
- 滑动窗口

## 提示

1. Since the sum of <code>nums</code>is at most <code>20000</code>, the number of distinct elements of nums is <code>200</code>.
2. Let <code>dp[x]</code> be the number of submultisets of <code>nums</code> with sum <code>x</code>.
3. The answer to the problem is <code>dp[l] + dp[l+1] + … + dp[r]</code>.
4. Use coin change dp to transition between states.

## 示例

```
[1,2,2,3]
6
6
[2,1,4,2,7]
1
5
[1,2,1,3,5,2]
3
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countSubMultisets(vector<int>& nums, int l, int r) {
        
    }
};
```

### Java

```java
class Solution {
    public int countSubMultisets(List<Integer> nums, int l, int r) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countSubMultisets(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
        
```

### C

```c
int countSubMultisets(int* nums, int numsSize, int l, int r) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountSubMultisets(IList<int> nums, int l, int r) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var countSubMultisets = function(nums, l, r) {
    
};
```

### TypeScript

```typescript
function countSubMultisets(nums: number[], l: number, r: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $l
     * @param Integer $r
     * @return Integer
     */
    function countSubMultisets($nums, $l, $r) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countSubMultisets(_ nums: [Int], _ l: Int, _ r: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countSubMultisets(nums: List<Int>, l: Int, r: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countSubMultisets(List<int> nums, int l, int r) {
    
  }
}
```

### Go

```golang
func countSubMultisets(nums []int, l int, r int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def count_sub_multisets(nums, l, r)
    
end
```

### Scala

```scala
object Solution {
    def countSubMultisets(nums: List[Int], l: Int, r: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_sub_multisets(nums: Vec<i32>, l: i32, r: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-sub-multisets nums l r)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_sub_multisets(Nums :: [integer()], L :: integer(), R :: integer()) -> integer().
count_sub_multisets(Nums, L, R) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_sub_multisets(nums :: [integer], l :: integer, r :: integer) :: integer
  def count_sub_multisets(nums, l, r) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countSubMultisets(nums: ArrayList<Int64>, l: Int64, r: Int64): Int64 {

    }
}
```

