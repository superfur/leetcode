# 1296. 划分数组为连续数字的集合

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;和一个正整数&nbsp;<code>k</code>，请你判断是否可以把这个数组划分成一些由&nbsp;<code>k</code>&nbsp;个连续数字组成的集合。<br />
如果可以，请返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,3,4,4,5,6], k = 4
<strong>输出：</strong>true
<strong>解释：</strong>数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
<strong>输出：</strong>true
<strong>解释：</strong>数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4], k = 3
<strong>输出：</strong>false
<strong>解释：</strong>数组不能分成几个大小为 3 的子数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>此题目与 846 重复：<a href="https://leetcode-cn.com/problems/hand-of-straights/" target="_blank">https://leetcode-cn.com/problems/hand-of-straights/</a></p>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 排序

## 提示

1. If the smallest number in the possible-to-split array is V, then numbers V+1, V+2, ... V+k-1 must contain there as well.
2. You can iteratively find k sets and remove them from array until it becomes empty.
3. Failure to do so would mean that array is unsplittable.

## 示例

```
[1,2,3,3,4,4,5,6]
4
[3,2,1,2,3,4,3,4,5,9,10,11]
3
[1,2,3,4]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPossibleDivide(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPossibleDivide(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
```

### C

```c
bool isPossibleDivide(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPossibleDivide(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var isPossibleDivide = function(nums, k) {
    
};
```

### TypeScript

```typescript
function isPossibleDivide(nums: number[], k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Boolean
     */
    function isPossibleDivide($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPossibleDivide(_ nums: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPossibleDivide(nums: IntArray, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPossibleDivide(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func isPossibleDivide(nums []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def is_possible_divide(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def isPossibleDivide(nums: Array[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_possible_divide(nums: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-possible-divide nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec is_possible_divide(Nums :: [integer()], K :: integer()) -> boolean().
is_possible_divide(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_possible_divide(nums :: [integer], k :: integer) :: boolean
  def is_possible_divide(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPossibleDivide(nums: Array<Int64>, k: Int64): Bool {

    }
}
```

