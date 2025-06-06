# 面试题 17.10. 主要元素

## 题目描述

<p>数组中占比超过一半的元素称之为主要元素。给你一个<strong> 整数 </strong>数组，找出其中的主要元素。若没有，返回 <code>-1</code> 。请设计时间复杂度为 <code>O(N)</code> 、空间复杂度为 <code>O(1)</code> 的解决方案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[1,2,5,9,5,9,5,5,5]
<strong>输出：</strong>5</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>[3,2]
<strong>输出：</strong>-1</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>[2,2,1,1,1,2,2]
<strong>输出：</strong>2</pre>


## 难度

Easy

## 标签

- 数组
- 计数

## 提示

1. 从蛮力解法开始。你能检查一下每个值是否为主要元素吗?
2. 考虑蛮力解法。我们选择一个元素，然后通过计算匹配和非匹配元素的数量来验证它是否是主要元素。假设对于第一个元素，前几次检查显示 7 个不匹配的元素和 3 个匹配的元素。有必要继续检查这个元素吗?
3. 主要元素一开始看起来并不一定像主要元素。例如，有可能主要元素出现在数组的第一个元素中，然后在接下来的 8 个元素中都不再出现。但是，在这些情况下，主要元素将在数组的后面出现(实际上，在数组的后面会出现很多次)。当某个元素看起来“不太像”主要元素时，继续检查它并不一定很重要。
4. 还要注意，主要元素对于某些子数组也必须是主要元素，而且子数组不能拥有多个主要元素。
5. 试试这个:给定一个元素，开始检查它是否是一个子数组的开始，同时对于这个子数组，该元素是它的主要元素。一旦它变得“不太可能”(出现的次数少于一半)，就开始检查下一个元素(子数组之后的元素)。

## 示例

```
[3,2,3]
[2,2,1,1,1,2,2]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int majorityElement(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
```

### C

```c
int majorityElement(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MajorityElement(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    
};
```

### TypeScript

```typescript
function majorityElement(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun majorityElement(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int majorityElement(List<int> nums) {
    
  }
}
```

### Go

```golang
func majorityElement(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    
end
```

### Scala

```scala
object Solution {
    def majorityElement(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (majority-element nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec majority_element(Nums :: [integer()]) -> integer().
majority_element(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec majority_element(nums :: [integer]) :: integer
  def majority_element(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func majorityElement(nums: Array<Int64>): Int64 {

    }
}
```

