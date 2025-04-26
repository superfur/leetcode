# 2148. 元素计数

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，统计并返回在 <code>nums</code> 中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [11,7,2,15]
<strong>输出：</strong>2
<strong>解释：</strong>元素 7 ：严格较小元素是元素 2 ，严格较大元素是元素 11 。
元素 11 ：严格较小元素是元素 7 ，严格较大元素是元素 15 。
总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-3,3,3,90]
<strong>输出：</strong>2
<strong>解释：</strong>元素 3 ：严格较小元素是元素 -3 ，严格较大元素是元素 90 。
由于有两个元素的值为 3 ，总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 计数
- 排序

## 提示

1. All the elements in the array should be counted except for the minimum and maximum elements.
2. If the array has n elements, the answer will be n - count(min(nums)) - count(max(nums))
3. This formula will not work in case the array has all the elements equal, why?

## 示例

```
[11,7,2,15]
[-3,3,3,90]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countElements(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countElements(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countElements(self, nums: List[int]) -> int:
        
```

### C

```c
int countElements(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountElements(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countElements = function(nums) {
    
};
```

### TypeScript

```typescript
function countElements(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countElements($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countElements(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countElements(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countElements(List<int> nums) {
    
  }
}
```

### Go

```golang
func countElements(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_elements(nums)
    
end
```

### Scala

```scala
object Solution {
    def countElements(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_elements(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-elements nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_elements(Nums :: [integer()]) -> integer().
count_elements(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_elements(nums :: [integer]) :: integer
  def count_elements(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countElements(nums: Array<Int64>): Int64 {

    }
}
```

