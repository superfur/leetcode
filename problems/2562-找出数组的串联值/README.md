# 2562. 找出数组的串联值

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组&nbsp;<code>nums</code> 。</p>

<p>现定义两个数字的 <strong>串联</strong>&nbsp;是由这两个数值串联起来形成的新数字。</p>

<ul>
	<li>例如，<code>15</code><span style="">&nbsp;和&nbsp;</span><code>49</code>&nbsp;的串联是&nbsp;<code>1549</code> 。</li>
</ul>

<p><code>nums</code>&nbsp;的 <strong>串联值</strong>&nbsp;最初等于 <code>0</code> 。执行下述操作直到&nbsp;<code>nums</code>&nbsp;变为空：</p>

<ul>
	<li>如果&nbsp;<code>nums</code>&nbsp;的长度大于 1，分别选中 <code>nums</code> 中的第一个元素和最后一个元素，将二者串联得到的值加到&nbsp;<code>nums</code>&nbsp;的 <strong>串联值</strong> 上，然后从&nbsp;<code>nums</code>&nbsp;中删除第一个和最后一个元素。例如，如果&nbsp;<code>nums</code> 是 <code>[1, 2, 4, 5, 6]</code>，将 16 添加到串联值。</li>
	<li>如果&nbsp;<code>nums</code>&nbsp;中仅存在一个元素，则将该元素的值加到&nbsp;<code>nums</code> 的串联值上，然后删除这个元素。</li>
</ul>

<p>返回执行完所有操作后<em>&nbsp;</em><code>nums</code> 的串联值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [7,52,2,4]
<b>输出：</b>596
<b>解释：</b>在执行任一步操作前，nums 为 [7,52,2,4] ，串联值为 0 。
 - 在第一步操作中：
我们选中第一个元素 7 和最后一个元素 4 。
二者的串联是 74 ，将其加到串联值上，所以串联值等于 74 。
接着我们从 nums 中移除这两个元素，所以 nums 变为 [52,2] 。
 - 在第二步操作中： 
我们选中第一个元素 52 和最后一个元素 2 。 
二者的串联是 522 ，将其加到串联值上，所以串联值等于 596 。
接着我们从 nums 中移除这两个元素，所以 nums 变为空。
由于串联值等于 596 ，所以答案就是 596 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [5,14,13,8,12]
<b>输出：</b>673
<b>解释：</b>在执行任一步操作前，nums 为 [5,14,13,8,12] ，串联值为 0 。 
- 在第一步操作中： 
我们选中第一个元素 5 和最后一个元素 12 。 
二者的串联是 512 ，将其加到串联值上，所以串联值等于 512 。 
接着我们从 nums 中移除这两个元素，所以 nums 变为 [14,13,8] 。
- 在第二步操作中：
我们选中第一个元素 14 和最后一个元素 8 。
二者的串联是 148 ，将其加到串联值上，所以串联值等于 660 。
接着我们从 nums 中移除这两个元素，所以 nums 变为 [13] 。 
- 在第三步操作中：
nums 只有一个元素，所以我们选中 13 并将其加到串联值上，所以串联值等于 673 。
接着我们从 nums 中移除这个元素，所以 nums 变为空。 
由于串联值等于 673 ，所以答案就是 673 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 双指针
- 模拟

## 提示

1. Consider simulating the process to calculate the answer
2. iterate until the array becomes empty. In each iteration, concatenate the first element to the last element and add their concatenation value to the answer.
3. Don’t forget to handle cases when one element is left in the end, not two elements.

## 示例

```
[7,52,2,4]
[5,14,13,8,12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long findTheArrayConcVal(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long findTheArrayConcVal(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
```

### C

```c
long long findTheArrayConcVal(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long FindTheArrayConcVal(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findTheArrayConcVal = function(nums) {
    
};
```

### TypeScript

```typescript
function findTheArrayConcVal(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findTheArrayConcVal($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findTheArrayConcVal(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findTheArrayConcVal(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int findTheArrayConcVal(List<int> nums) {
    
  }
}
```

### Go

```golang
func findTheArrayConcVal(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_the_array_conc_val(nums)
    
end
```

### Scala

```scala
object Solution {
    def findTheArrayConcVal(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_the_array_conc_val(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (find-the-array-conc-val nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_the_array_conc_val(Nums :: [integer()]) -> integer().
find_the_array_conc_val(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_the_array_conc_val(nums :: [integer]) :: integer
  def find_the_array_conc_val(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findTheArrayConcVal(nums: Array<Int64>): Int64 {

    }
}
```

