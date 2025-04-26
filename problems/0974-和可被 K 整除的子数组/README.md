# 974. 和可被 K 整除的子数组

## 题目描述

<p>给定一个整数数组 <code>nums</code>&nbsp;和一个整数 <code>k</code> ，返回其中元素之和可被 <code>k</code>&nbsp;整除的非空&nbsp;<strong>子数组</strong> 的数目。</p>

<p><strong>子数组</strong> 是数组中&nbsp;<strong>连续</strong>&nbsp;的部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,5,0,-2,-3,1], k = 5
<strong>输出：</strong>7
<strong>解释：
</strong>有 7 个子数组满足其元素之和可被 k = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> nums = [5], k = 9
<strong>输出:</strong> 0
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>2 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 前缀和

## 示例

```
[4,5,0,-2,-3,1]
5
[5]
9
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int subarraysDivByK(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SubarraysDivByK(int[] nums, int k) {
        
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
var subarraysDivByK = function(nums, k) {
    
};
```

### TypeScript

```typescript
function subarraysDivByK(nums: number[], k: number): number {
    
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
    function subarraysDivByK($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func subarraysDivByK(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun subarraysDivByK(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int subarraysDivByK(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func subarraysDivByK(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarrays_div_by_k(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def subarraysDivByK(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (subarrays-div-by-k nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec subarrays_div_by_k(Nums :: [integer()], K :: integer()) -> integer().
subarrays_div_by_k(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec subarrays_div_by_k(nums :: [integer], k :: integer) :: integer
  def subarrays_div_by_k(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func subarraysDivByK(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

