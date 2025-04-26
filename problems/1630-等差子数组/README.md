# 1630. 等差子数组

## 题目描述

<p>如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 <strong>等差数列</strong> 。更正式地，数列 <code>s</code> 是等差数列，只需要满足：对于每个有效的 <code>i</code> ， <code>s[i+1] - s[i] == s[1] - s[0]</code> 都成立。</p>

<p>例如，下面这些都是 <strong>等差数列</strong> ：</p>

<pre>1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9</pre>

<p>下面的数列 <strong>不是等差数列</strong> ：</p>

<pre>1, 1, 2, 5, 7</pre>

<p>给你一个由 <code>n</code> 个整数组成的数组 <code>nums</code>，和两个由 <code>m</code> 个整数组成的数组 <code>l</code> 和 <code>r</code>，后两个数组表示 <code>m</code> 组范围查询，其中第 <code>i</code> 个查询对应范围 <code>[l[i], r[i]]</code> 。所有数组的下标都是 <strong>从 0 开始</strong> 的。</p>

<p>返回<em> </em><code>boolean</code> 元素构成的答案列表 <code>answer</code> 。如果子数组 <code>nums[l[i]], nums[l[i]+1], ... , nums[r[i]]</code> 可以 <strong>重新排列</strong> 形成 <strong>等差数列</strong> ，<code>answer[i]</code> 的值就是 <code>true</code>；否则<code>answer[i]</code> 的值就是 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = <code>[4,6,5,9,3,7]</code>, l = <code>[0,0,2]</code>, r = <code>[2,3,5]</code>
<strong>输出：</strong><code>[true,false,true]</code>
<strong>解释：</strong>
第 0 个查询，对应子数组 [4,6,5] 。可以重新排列为等差数列 [6,5,4] 。
第 1 个查询，对应子数组 [4,6,5,9] 。无法重新排列形成等差数列。
第 2 个查询，对应子数组 <code>[5,9,3,7] 。</code>可以重新排列为等差数列 <code>[3,5,7,9] 。</code></pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
<strong>输出：</strong>[false,true,false,false,true,true]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>m == l.length</code></li>
	<li><code>m == r.length</code></li>
	<li><code>2 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= m &lt;= 500</code></li>
	<li><code>0 &lt;= l[i] &lt; r[i] &lt; n</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. To check if a given sequence is arithmetic, just check that the difference between every two consecutive elements is the same.
2. If and only if a set of numbers can make an arithmetic sequence, then its sorted version makes an arithmetic sequence. So to check a set of numbers, sort it, and check if that sequence is arithmetic.
3. For each query, get the corresponding set of numbers which will be the sub-array represented by the query, sort it, and check if the result sequence is arithmetic.

## 示例

```
[4,6,5,9,3,7]
[0,0,2]
[2,3,5]
[-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
[0,1,6,4,8,7]
[4,4,9,7,9,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* checkArithmeticSubarrays(int* nums, int numsSize, int* l, int lSize, int* r, int rSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<bool> CheckArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {
    
};
```

### TypeScript

```typescript
function checkArithmeticSubarrays(nums: number[], l: number[], r: number[]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $l
     * @param Integer[] $r
     * @return Boolean[]
     */
    function checkArithmeticSubarrays($nums, $l, $r) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkArithmeticSubarrays(_ nums: [Int], _ l: [Int], _ r: [Int]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkArithmeticSubarrays(nums: IntArray, l: IntArray, r: IntArray): List<Boolean> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> checkArithmeticSubarrays(List<int> nums, List<int> l, List<int> r) {
    
  }
}
```

### Go

```golang
func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} l
# @param {Integer[]} r
# @return {Boolean[]}
def check_arithmetic_subarrays(nums, l, r)
    
end
```

### Scala

```scala
object Solution {
    def checkArithmeticSubarrays(nums: Array[Int], l: Array[Int], r: Array[Int]): List[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_arithmetic_subarrays(nums: Vec<i32>, l: Vec<i32>, r: Vec<i32>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (check-arithmetic-subarrays nums l r)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?) (listof boolean?))
  )
```

### Erlang

```erlang
-spec check_arithmetic_subarrays(Nums :: [integer()], L :: [integer()], R :: [integer()]) -> [boolean()].
check_arithmetic_subarrays(Nums, L, R) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_arithmetic_subarrays(nums :: [integer], l :: [integer], r :: [integer]) :: [boolean]
  def check_arithmetic_subarrays(nums, l, r) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkArithmeticSubarrays(nums: Array<Int64>, l: Array<Int64>, r: Array<Int64>): ArrayList<Bool> {

    }
}
```

