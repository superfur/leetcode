# 523. 连续的子数组和

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个整数&nbsp;<code>k</code> ，如果&nbsp;<code>nums</code>&nbsp;有一个 <strong>好的子数组</strong>&nbsp;返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>：</p>

<p>一个&nbsp;<strong>好的子数组</strong>&nbsp;是：</p>

<ul>
	<li>长度&nbsp;<strong>至少为 2</strong> ，且</li>
	<li>子数组元素总和为 <code>k</code> 的倍数。</li>
</ul>

<p><strong>注意</strong>：</p>

<ul>
	<li><strong>子数组</strong> 是数组中 <strong>连续</strong> 的部分。</li>
	<li>如果存在一个整数 <code>n</code> ，令整数 <code>x</code> 符合 <code>x = n * k</code> ，则称 <code>x</code> 是 <code>k</code> 的一个倍数。<code>0</code> <strong>始终</strong> 视为 <code>k</code> 的一个倍数。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [23<u>,2,4</u>,6,7], k = 6
<strong>输出：</strong>true
<strong>解释：</strong>[2,4] 是一个大小为 2 的子数组，并且和为 6 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [<u>23,2,6,4,7</u>], k = 6
<strong>输出：</strong>true
<strong>解释：</strong>[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [23,2,6,4,7], k = 13
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= sum(nums[i]) &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 前缀和

## 示例

```
[23,2,4,6,7]
6
[23,2,6,4,7]
6
[23,2,6,4,7]
13
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
```

### C

```c
bool checkSubarraySum(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CheckSubarraySum(int[] nums, int k) {
        
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
var checkSubarraySum = function(nums, k) {
    
};
```

### TypeScript

```typescript
function checkSubarraySum(nums: number[], k: number): boolean {
    
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
    function checkSubarraySum($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func checkSubarraySum(_ nums: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun checkSubarraySum(nums: IntArray, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool checkSubarraySum(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func checkSubarraySum(nums []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def check_subarray_sum(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def checkSubarraySum(nums: Array[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn check_subarray_sum(nums: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (check-subarray-sum nums k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec check_subarray_sum(Nums :: [integer()], K :: integer()) -> boolean().
check_subarray_sum(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec check_subarray_sum(nums :: [integer], k :: integer) :: boolean
  def check_subarray_sum(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func checkSubarraySum(nums: Array<Int64>, k: Int64): Bool {

    }
}
```

