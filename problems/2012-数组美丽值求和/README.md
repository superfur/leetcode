# 2012. 数组美丽值求和

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> 。对于每个下标 <code>i</code>（<code>1 &lt;= i &lt;= nums.length - 2</code>），<code>nums[i]</code> 的 <strong>美丽值</strong> 等于：</p>

<ul>
	<li><code>2</code>，对于所有 <code>0 &lt;= j &lt; i</code> 且 <code>i &lt; k &lt;= nums.length - 1</code> ，满足 <code>nums[j] &lt; nums[i] &lt; nums[k]</code></li>
	<li><code>1</code>，如果满足 <code>nums[i - 1] &lt; nums[i] &lt; nums[i + 1]</code> ，且不满足前面的条件</li>
	<li><code>0</code>，如果上述条件全部不满足</li>
</ul>

<p>返回符合 <code>1 &lt;= i &lt;= nums.length - 2</code> 的所有<em> </em><code>nums[i]</code><em> </em>的 <strong>美丽值的总和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,2,3]
<strong>输出：</strong>2
<strong>解释：</strong>对于每个符合范围 1 &lt;= i &lt;= 1 的下标 i :
- nums[1] 的美丽值等于 2
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [2,4,6,4]
<strong>输出：</strong>1
<strong>解释：</strong>对于每个符合范围 1 &lt;= i &lt;= 2 的下标 i :
- nums[1] 的美丽值等于 1
- nums[2] 的美丽值等于 0
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,2,1]
<strong>输出：</strong>0
<strong>解释：</strong>对于每个符合范围 1 &lt;= i &lt;= 1 的下标 i :
- nums[1] 的美丽值等于 0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 提示

1. Use suffix/prefix arrays.
2. prefix[i] records the maximum value in range (0, i - 1) inclusive.
3. suffix[i] records the minimum value in range (i + 1, n - 1) inclusive.

## 示例

```
[1,2,3]
[2,4,6,4]
[3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfBeauties(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfBeauties(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfBeauties(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        
```

### C

```c
int sumOfBeauties(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfBeauties(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfBeauties = function(nums) {
    
};
```

### TypeScript

```typescript
function sumOfBeauties(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfBeauties($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfBeauties(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfBeauties(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfBeauties(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumOfBeauties(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_of_beauties(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumOfBeauties(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_beauties(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-beauties nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_beauties(Nums :: [integer()]) -> integer().
sum_of_beauties(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_beauties(nums :: [integer]) :: integer
  def sum_of_beauties(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfBeauties(nums: Array<Int64>): Int64 {

    }
}
```

