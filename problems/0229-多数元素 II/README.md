# 229. 多数元素 II

## 题目描述

<p>给定一个大小为&nbsp;<em>n&nbsp;</em>的整数数组，找出其中所有出现超过&nbsp;<code>⌊ n/3 ⌋</code>&nbsp;次的元素。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,3]
<strong>输出：</strong>[3]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2]
<strong>输出：</strong>[1,2]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。</p>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数
- 排序

## 提示

1. Think about the possible number of elements that can appear more than ⌊ n/3 ⌋ times in the array.
2. It can be at most two. Why?
3. Consider using Boyer-Moore Voting Algorithm, which is efficient for finding elements that appear more than a certain threshold.

## 示例

```
[3,2,3]
[1]
[1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* majorityElement(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    
};
```

### TypeScript

```typescript
function majorityElement(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function majorityElement($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func majorityElement(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun majorityElement(nums: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> majorityElement(List<int> nums) {
    
  }
}
```

### Go

```golang
func majorityElement(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def majority_element(nums)
    
end
```

### Scala

```scala
object Solution {
    def majorityElement(nums: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (majority-element nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec majority_element(Nums :: [integer()]) -> [integer()].
majority_element(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec majority_element(nums :: [integer]) :: [integer]
  def majority_element(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func majorityElement(nums: Array<Int64>): ArrayList<Int64> {

    }
}
```

