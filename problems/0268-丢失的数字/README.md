# 268. 丢失的数字

## 题目描述

<p>给定一个包含 <code>[0, n]</code>&nbsp;中&nbsp;<code>n</code>&nbsp;个数的数组 <code>nums</code> ，找出 <code>[0, n]</code> 这个范围内没有出现在数组中的那个数。</p>

<ul>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [3,0,1]</p>

<p><strong>输出：</strong>2</p>

<p><b>解释：</b><code>n = 3</code>，因为有 3 个数字，所以所有的数字都在范围 <code>[0,3]</code> 内。2 是丢失的数字，因为它没有出现在 <code>nums</code> 中。</p>
</div>

<p><strong>示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [0,1]</p>

<p><strong>输出：</strong>2</p>

<p><b>解释：</b><code>n = 2</code>，因为有 2 个数字，所以所有的数字都在范围 <code>[0,2]</code> 内。2 是丢失的数字，因为它没有出现在 <code>nums</code> 中。</p>
</div>

<p><strong>示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>nums = [9,6,4,2,3,5,7,0,1]</p>

<p><strong>输出：</strong>8</p>

<p><b>解释：</b><code>n = 9</code>，因为有 9 个数字，所以所有的数字都在范围 <code>[0,9]</code> 内。8 是丢失的数字，因为它没有出现在 <code>nums</code> 中。</p>
</div>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li><code>nums</code> 中的所有数字都 <strong>独一无二</strong></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?</p>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表
- 数学
- 二分查找
- 排序

## 示例

```
[3,0,1]
[0,1]
[9,6,4,2,3,5,7,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int missingNumber(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
```

### C

```c
int missingNumber(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MissingNumber(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    
};
```

### TypeScript

```typescript
function missingNumber(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function missingNumber($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun missingNumber(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int missingNumber(List<int> nums) {
    
  }
}
```

### Go

```golang
func missingNumber(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def missing_number(nums)
    
end
```

### Scala

```scala
object Solution {
    def missingNumber(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (missing-number nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec missing_number(Nums :: [integer()]) -> integer().
missing_number(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec missing_number(nums :: [integer]) :: integer
  def missing_number(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func missingNumber(nums: Array<Int64>): Int64 {

    }
}
```

