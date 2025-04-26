# 2681. 英雄的力量

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，它表示英雄的能力值。如果我们选出一部分英雄，这组英雄的 <strong>力量</strong>&nbsp;定义为：</p>

<ul>
	<li><code>i<sub>0</sub></code>&nbsp;，<code>i<sub>1</sub></code>&nbsp;，<span style="">... </span><code><span style="">i<sub>k</sub></span></code><span style="">&nbsp;</span>表示这组英雄在数组中的下标。那么这组英雄的力量为&nbsp;<code><font face="monospace">max(nums[</font>i<sub>0</sub><font face="monospace">],nums[</font>i<sub>1</sub><font face="monospace">] ... nums[</font><span style="font-size:10.8333px">i<sub>k</sub></span><font face="monospace">])<sup>2</sup> * min(nums[</font>i<sub>0</sub><font face="monospace">],nums[</font>i<sub>1</sub><font face="monospace">] ... nums[</font><span style="font-size:10.8333px">i<sub>k</sub></span><font face="monospace">])</font></code> 。</li>
</ul>

<p>请你返回所有可能的 <strong>非空</strong> 英雄组的 <strong>力量</strong> 之和。由于答案可能非常大，请你将结果对&nbsp;<code>10<sup>9 </sup>+ 7</code>&nbsp;<strong>取余。</strong></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [2,1,4]
<b>输出：</b>141
<b>解释：</b>
第 1&nbsp;组：[2] 的力量为 2<sup>2</sup>&nbsp;* 2 = 8 。
第 2&nbsp;组：[1] 的力量为 1<sup>2</sup> * 1 = 1 。
第 3&nbsp;组：[4] 的力量为 4<sup>2</sup> * 4 = 64 。
第 4&nbsp;组：[2,1] 的力量为 2<sup>2</sup> * 1 = 4 。
第 5 组：[2,4] 的力量为 4<sup>2</sup> * 2 = 32 。
第 6&nbsp;组：[1,4] 的力量为 4<sup>2</sup> * 1 = 16 。
第​ ​​​​​​7&nbsp;组：[2,1,4] 的力量为 4<sup>2</sup>​​​​​​​ * 1 = 16 。
所有英雄组的力量之和为 8 + 1 + 64 + 4 + 32 + 16 + 16 = 141 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,1,1]
<b>输出：</b>7
<b>解释：</b>总共有 7 个英雄组，每一组的力量都是 1 。所以所有英雄组的力量之和为 7 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 前缀和
- 排序

## 提示

1. Try something with sorting the array.
2. For a pair of array elements nums[i] and nums[j] (i < j), the power would be nums[i]*nums[j]^2 regardless of how many elements in between are included.
3. The number of subsets with the above as power will correspond to 2^(j-i-1).
4. Try collecting the terms for nums[0], nums[1], …, nums[j-1] when computing the power of heroes ending at index j to get the power in a single pass.

## 示例

```
[2,1,4]
[1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOfPower(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOfPower(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOfPower(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        
```

### C

```c
int sumOfPower(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOfPower(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfPower = function(nums) {
    
};
```

### TypeScript

```typescript
function sumOfPower(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumOfPower($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOfPower(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOfPower(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOfPower(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumOfPower(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_of_power(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumOfPower(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_of_power(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-of-power nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_of_power(Nums :: [integer()]) -> integer().
sum_of_power(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_of_power(nums :: [integer]) :: integer
  def sum_of_power(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOfPower(nums: Array<Int64>): Int64 {

    }
}
```

