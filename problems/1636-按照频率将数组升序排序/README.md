# 1636. 按照频率将数组升序排序

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，请你将数组按照每个值的频率 <strong>升序</strong> 排序。如果有多个值的频率相同，请你按照数值本身将它们 <strong>降序</strong> 排序。 </p>

<p>请你返回排序后的数组。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,1,2,2,2,3]
<b>输出：</b>[3,1,1,2,2,2]
<b>解释：</b>'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,3,1,3,2]
<b>输出：</b>[1,3,3,2,2]
<b>解释：</b>'2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>nums = [-1,1,-6,4,5,-6,1,4,1]
<b>输出：</b>[5,-1,4,4,-6,-6,1,1,1]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. Count the frequency of each value.
2. Use a custom comparator to compare values by their frequency. If two values have the same frequency, compare their values.

## 示例

```
[1,1,2,2,2,3]
[2,3,1,3,2]
[-1,1,-6,4,5,-6,1,4,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] frequencySort(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* frequencySort(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FrequencySort(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var frequencySort = function(nums) {
    
};
```

### TypeScript

```typescript
function frequencySort(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function frequencySort($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func frequencySort(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun frequencySort(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> frequencySort(List<int> nums) {
    
  }
}
```

### Go

```golang
func frequencySort(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def frequency_sort(nums)
    
end
```

### Scala

```scala
object Solution {
    def frequencySort(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn frequency_sort(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (frequency-sort nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec frequency_sort(Nums :: [integer()]) -> [integer()].
frequency_sort(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec frequency_sort(nums :: [integer]) :: [integer]
  def frequency_sort(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func frequencySort(nums: Array<Int64>): Array<Int64> {

    }
}
```

