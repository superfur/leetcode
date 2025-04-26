# 2134. 最少交换次数来组合所有的 1 II

## 题目描述

<p><strong>交换</strong> 定义为选中一个数组中的两个 <strong>互不相同</strong> 的位置并交换二者的值。</p>

<p><strong>环形</strong> 数组是一个数组，可以认为 <strong>第一个</strong> 元素和 <strong>最后一个</strong> 元素 <strong>相邻</strong> 。</p>

<p>给你一个 <strong>二进制环形</strong> 数组 <code>nums</code> ，返回在 <strong>任意位置</strong> 将数组中的所有 <code>1</code> 聚集在一起需要的最少交换次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [0,1,0,1,1,0,0]
<strong>输出：</strong>1
<strong>解释：</strong>这里列出一些能够将所有 1 聚集在一起的方案：
[0,<strong><em>0</em></strong>,<em><strong>1</strong></em>,1,1,0,0] 交换 1 次。
[0,1,<em><strong>1</strong></em>,1,<em><strong>0</strong></em>,0,0] 交换 1 次。
[1,1,0,0,0,0,1] 交换 2 次（利用数组的环形特性）。
无法在交换 0 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [0,1,1,1,0,0,1,1,0]
<strong>输出：</strong>2
<strong>解释：</strong>这里列出一些能够将所有 1 聚集在一起的方案：
[1,1,1,0,0,0,0,1,1] 交换 2 次（利用数组的环形特性）。
[1,1,1,1,1,0,0,0,0] 交换 2 次。
无法在交换 0 次或 1 次的情况下将数组中的所有 1 聚集在一起。
因此，需要的最少交换次数为 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,0,0,1]
<strong>输出：</strong>0
<strong>解释：</strong>得益于数组的环形特性，所有的 1 已经聚集在一起。
因此，需要的最少交换次数为 0 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>nums[i]</code> 为 <code>0</code> 或者 <code>1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 提示

1. Notice that the number of 1’s to be grouped together is fixed. It is the number of 1's the whole array has.
2. Call this number total. We should then check for every subarray of size total (possibly wrapped around), how many swaps are required to have the subarray be all 1’s.
3. The number of swaps required is the number of 0’s in the subarray.
4. To eliminate the circular property of the array, we can append the original array to itself. Then, we check each subarray of length total.
5. How do we avoid recounting the number of 0’s in the subarray each time? The Sliding Window technique can help.

## 示例

```
[0,1,0,1,1,0,0]
[0,1,1,1,0,0,1,1,0]
[1,1,0,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSwaps(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSwaps(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSwaps(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
```

### C

```c
int minSwaps(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSwaps(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minSwaps = function(nums) {
    
};
```

### TypeScript

```typescript
function minSwaps(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minSwaps($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSwaps(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSwaps(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSwaps(List<int> nums) {
    
  }
}
```

### Go

```golang
func minSwaps(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_swaps(nums)
    
end
```

### Scala

```scala
object Solution {
    def minSwaps(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_swaps(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-swaps nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_swaps(Nums :: [integer()]) -> integer().
min_swaps(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_swaps(nums :: [integer]) :: integer
  def min_swaps(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSwaps(nums: Array<Int64>): Int64 {

    }
}
```

