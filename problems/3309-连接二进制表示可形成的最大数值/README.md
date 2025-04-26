# 3309. 连接二进制表示可形成的最大数值

## 题目描述

<p>给你一个长度为 <code>3</code> 的整数数组 <code>nums</code>。</p>

<p>现以某种顺序<strong> 连接 </strong>数组 <code>nums</code> 中所有元素的 <strong>二进制表示</strong> ，请你返回可以由这种方法形成的 <strong>最大 </strong>数值。</p>

<p><strong>注意</strong> 任何数字的二进制表示<em> </em><strong>不含</strong><em> </em>前导零。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>输出:</strong> 30</p>

<p><strong>解释:</strong></p>

<p>按照顺序 <code>[3, 1, 2]</code> 连接数字的二进制表示，得到结果 <code>"11110"</code>，这是 30 的二进制表示。</p>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [2,8,16]</span></p>

<p><strong>输出:</strong> 1296</p>

<p><strong>解释:</strong></p>

<p>按照顺序 <code>[2, 8, 16]</code> 连接数字的二进制表述，得到结果 <code>"10100010000"</code>，这是 1296 的二进制表示。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>nums.length == 3</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 127</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 枚举

## 提示

1. How many possible concatenation orders are there?

## 示例

```
[1,2,3]
[2,8,16]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxGoodNumber(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxGoodNumber(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxGoodNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        
```

### C

```c
int maxGoodNumber(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxGoodNumber(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxGoodNumber = function(nums) {
    
};
```

### TypeScript

```typescript
function maxGoodNumber(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxGoodNumber($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxGoodNumber(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxGoodNumber(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxGoodNumber(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxGoodNumber(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_good_number(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxGoodNumber(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_good_number(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-good-number nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_good_number(Nums :: [integer()]) -> integer().
max_good_number(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_good_number(nums :: [integer]) :: integer
  def max_good_number(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxGoodNumber(nums: Array<Int64>): Int64 {

    }
}
```

