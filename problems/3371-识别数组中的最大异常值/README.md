# 3371. 识别数组中的最大异常值

## 题目描述

<p>给你一个整数数组 <code>nums</code>。该数组包含 <code>n</code> 个元素，其中&nbsp;<strong>恰好&nbsp;</strong>有 <code>n - 2</code> 个元素是&nbsp;<strong>特殊数字&nbsp;</strong>。剩下的&nbsp;<strong>两个&nbsp;</strong>元素中，一个是所有&nbsp;<strong>特殊数字&nbsp;</strong>的 <strong>和</strong> ，另一个是&nbsp;<strong>异常值&nbsp;</strong>。</p>

<p><strong>异常值</strong> 的定义是：既不是原始特殊数字之一，也不是所有特殊数字的和。</p>

<p><strong>注意</strong>，特殊数字、和 以及 异常值 的下标必须&nbsp;<strong>不同&nbsp;</strong>，但可以共享&nbsp;<strong>相同</strong> 的值。</p>

<p>返回 <code>nums</code> 中可能的&nbsp;<strong>最大</strong><strong>异常值</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,5,10]</span></p>

<p><strong>输出：</strong> <span class="example-io">10</span></p>

<p><strong>解释：</strong></p>

<p>特殊数字可以是 2 和 3，因此和为 5，异常值为 10。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [-2,-1,-3,-6,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>特殊数字可以是 -2、-1 和 -3，因此和为 -6，异常值为 4。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,1,1,1,1,5,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>特殊数字可以是 1、1、1、1 和 1，因此和为 5，另一个 5 为异常值。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
	<li>输入保证 <code>nums</code> 中至少存在&nbsp;<strong>一个&nbsp;</strong>可能的异常值。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数
- 枚举

## 提示

1. What will be the value of array sum if we remove the outlier from it?
2. Use hashmap to find occurrence of an element quickly.

## 示例

```
[2,3,5,10]
[-2,-1,-3,-6,4]
[1,1,1,1,1,5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getLargestOutlier(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int getLargestOutlier(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        
```

### C

```c
int getLargestOutlier(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetLargestOutlier(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var getLargestOutlier = function(nums) {
    
};
```

### TypeScript

```typescript
function getLargestOutlier(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function getLargestOutlier($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getLargestOutlier(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getLargestOutlier(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getLargestOutlier(List<int> nums) {
    
  }
}
```

### Go

```golang
func getLargestOutlier(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def get_largest_outlier(nums)
    
end
```

### Scala

```scala
object Solution {
    def getLargestOutlier(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_largest_outlier(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-largest-outlier nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec get_largest_outlier(Nums :: [integer()]) -> integer().
get_largest_outlier(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_largest_outlier(nums :: [integer]) :: integer
  def get_largest_outlier(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getLargestOutlier(nums: Array<Int64>): Int64 {

    }
}
```

