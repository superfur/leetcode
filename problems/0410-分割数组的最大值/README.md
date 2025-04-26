# 410. 分割数组的最大值

## 题目描述

<p>给定一个非负整数数组 <code>nums</code> 和一个整数&nbsp;<code>k</code> ，你需要将这个数组分成&nbsp;<code>k</code><em>&nbsp;</em>个非空的连续子数组，使得这&nbsp;<code>k</code><em>&nbsp;</em>个子数组各自和的最大值 <strong>最小</strong>。</p>

<p>返回分割后最小的和的最大值。</p>

<p><strong>子数组</strong> 是数组中连续的部份。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [7,2,5,10,8], k = 2
<strong>输出：</strong>18
<strong>解释：</strong>
一共有四种方法将 nums 分割为 2 个子数组。 
其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4,5], k = 2
<strong>输出：</strong>9
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,4,4], k = 3
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(50, nums.length)</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 二分查找
- 动态规划
- 前缀和

## 示例

```
[7,2,5,10,8]
2
[1,2,3,4,5]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int splitArray(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int splitArray(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int splitArray(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int SplitArray(int[] nums, int k) {
        
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
var splitArray = function(nums, k) {
    
};
```

### TypeScript

```typescript
function splitArray(nums: number[], k: number): number {
    
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
    function splitArray($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func splitArray(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitArray(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int splitArray(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func splitArray(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def split_array(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def splitArray(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_array(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (split-array nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec split_array(Nums :: [integer()], K :: integer()) -> integer().
split_array(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec split_array(nums :: [integer], k :: integer) :: integer
  def split_array(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func splitArray(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

