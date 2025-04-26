# 2763. 所有子数组中不平衡数字之和

## 题目描述

<p>一个长度为 <code>n</code>&nbsp;下标从 <strong>0</strong>&nbsp;开始的整数数组 <code>arr</code>&nbsp;的 <strong>不平衡数字</strong>&nbsp;定义为，在&nbsp;<code>sarr = sorted(arr)</code>&nbsp;数组中，满足以下条件的下标数目：</p>

<ul>
	<li><code>0 &lt;= i &lt; n - 1</code>&nbsp;，和</li>
	<li><code>sarr[i+1] - sarr[i] &gt; 1</code></li>
</ul>

<p>这里，<code>sorted(arr)</code>&nbsp;表示将数组 <code>arr</code>&nbsp;排序后得到的数组。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，请你返回它所有&nbsp;<strong>子数组</strong>&nbsp;的&nbsp;<strong>不平衡数字</strong>&nbsp;之和。</p>

<p>子数组指的是一个数组中连续一段 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,3,1,4]
<b>输出：</b>3
<b>解释：</b>总共有 3 个子数组有非 0 不平衡数字：
- 子数组 [3, 1] ，不平衡数字为 1 。
- 子数组 [3, 1, 4] ，不平衡数字为 1 。
- 子数组 [1, 4] ，不平衡数字为 1 。
其他所有子数组的不平衡数字都是 0 ，所以所有子数组的不平衡数字之和为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,3,3,3,5]
<b>输出：</b>8
<b>解释：</b>总共有 7 个子数组有非 0 不平衡数字：
- 子数组 [1, 3] ，不平衡数字为 1 。
- 子数组 [1, 3, 3] ，不平衡数字为 1 。
- 子数组 [1, 3, 3, 3] ，不平衡数字为 1 。
- 子数组 [1, 3, 3, 3, 5] ，不平衡数字为 2 。
- 子数组 [3, 3, 3, 5] ，不平衡数字为 1 。
- 子数组 [3, 3, 5] ，不平衡数字为 1 。
- 子数组 [3, 5] ，不平衡数字为 1 。
其他所有子数组的不平衡数字都是 0 ，所以所有子数组的不平衡数字之和为 8 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 有序集合

## 提示

1. Iterate over all subarrays in a nested fashion. Namely, for each left endpoint, start from nums[left] and add elements nums[left + 1], nums[left + 2], etc.
2. To keep track of the imbalance value, maintain a set of added elements.
3. Increment the imbalance value whenever a new number is not adjacent (+/- 1) to other old numbers. For example, when you add 3 to [1, 5], or when you add 5 to [1, 3]. For a formal proof, consider three cases: new value is (i) largest, (ii) smallest, (iii) between two old numbers.
4. Decrement the imbalance value whenever a new number is adjacent (+/- 1) to two old numbers. For example, when you add 3 to [2, 4]. The imbalance value does not change in the case of one adjacent old number.

## 示例

```
[2,3,1,4]
[1,3,3,3,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumImbalanceNumbers(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumImbalanceNumbers(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumImbalanceNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumImbalanceNumbers(self, nums: List[int]) -> int:
        
```

### C

```c
int sumImbalanceNumbers(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumImbalanceNumbers(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sumImbalanceNumbers = function(nums) {
    
};
```

### TypeScript

```typescript
function sumImbalanceNumbers(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function sumImbalanceNumbers($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumImbalanceNumbers(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumImbalanceNumbers(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumImbalanceNumbers(List<int> nums) {
    
  }
}
```

### Go

```golang
func sumImbalanceNumbers(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def sum_imbalance_numbers(nums)
    
end
```

### Scala

```scala
object Solution {
    def sumImbalanceNumbers(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_imbalance_numbers(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-imbalance-numbers nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_imbalance_numbers(Nums :: [integer()]) -> integer().
sum_imbalance_numbers(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_imbalance_numbers(nums :: [integer]) :: integer
  def sum_imbalance_numbers(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumImbalanceNumbers(nums: Array<Int64>): Int64 {

    }
}
```

