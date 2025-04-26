# 1365. 有多少小于当前数字的数字

## 题目描述

<p>给你一个数组&nbsp;<code>nums</code>，对于其中每个元素&nbsp;<code>nums[i]</code>，请你统计数组中比它小的所有数字的数目。</p>

<p>换而言之，对于每个&nbsp;<code>nums[i]</code>&nbsp;你必须计算出有效的&nbsp;<code>j</code>&nbsp;的数量，其中 <code>j</code> 满足&nbsp;<code>j != i</code> <strong>且</strong> <code>nums[j] &lt; nums[i]</code>&nbsp;。</p>

<p>以数组形式返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [8,1,2,2,3]
<strong>输出：</strong>[4,0,1,1,3]
<strong>解释：</strong> 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [6,5,4,8]
<strong>输出：</strong>[2,1,0,3]
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [7,7,7,7]
<strong>输出：</strong>[0,0,0,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 500</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数排序
- 排序

## 提示

1. Brute force for each array element.
2. In order to improve the time complexity, we can sort the array and get the answer for each array element.

## 示例

```
[8,1,2,2,3]
[6,5,4,8]
[7,7,7,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    
};
```

### TypeScript

```typescript
function smallerNumbersThanCurrent(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function smallerNumbersThanCurrent($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func smallerNumbersThanCurrent(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun smallerNumbersThanCurrent(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> smallerNumbersThanCurrent(List<int> nums) {
    
  }
}
```

### Go

```golang
func smallerNumbersThanCurrent(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def smaller_numbers_than_current(nums)
    
end
```

### Scala

```scala
object Solution {
    def smallerNumbersThanCurrent(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn smaller_numbers_than_current(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (smaller-numbers-than-current nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec smaller_numbers_than_current(Nums :: [integer()]) -> [integer()].
smaller_numbers_than_current(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec smaller_numbers_than_current(nums :: [integer]) :: [integer]
  def smaller_numbers_than_current(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func smallerNumbersThanCurrent(nums: Array<Int64>): Array<Int64> {

    }
}
```

