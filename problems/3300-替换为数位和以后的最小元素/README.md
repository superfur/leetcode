# 3300. 替换为数位和以后的最小元素

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>请你将 <code>nums</code>&nbsp;中每一个元素都替换为它的各个数位之 <strong>和</strong>&nbsp;。</p>

<p>请你返回替换所有元素以后 <code>nums</code>&nbsp;中的 <strong>最小</strong>&nbsp;元素。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [10,12,13,14]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;替换后变为&nbsp;<code>[1, 3, 4, 5]</code>&nbsp;，最小元素为 1 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<p><code>nums</code>&nbsp;替换后变为&nbsp;<code>[1, 2, 3, 4]</code>&nbsp;，最小元素为 1 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [999,19,199]</span></p>

<p><span class="example-io"><b>输出：</b>10</span></p>

<p><strong>解释：</strong></p>

<p><code>nums</code>&nbsp;替换后变为&nbsp;<code>[27, 10, 19]</code>&nbsp;，最小元素为 10 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. Convert to string and calculate the sum for each element.

## 示例

```
[10,12,13,14]
[1,2,3,4]
[999,19,199]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minElement(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minElement(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minElement(self, nums: List[int]) -> int:
        
```

### C

```c
int minElement(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinElement(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minElement = function(nums) {
    
};
```

### TypeScript

```typescript
function minElement(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minElement($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minElement(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minElement(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minElement(List<int> nums) {
    
  }
}
```

### Go

```golang
func minElement(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_element(nums)
    
end
```

### Scala

```scala
object Solution {
    def minElement(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_element(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-element nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_element(Nums :: [integer()]) -> integer().
min_element(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_element(nums :: [integer]) :: integer
  def min_element(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minElement(nums: Array<Int64>): Int64 {

    }
}
```

