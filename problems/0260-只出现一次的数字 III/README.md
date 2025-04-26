# 260. 只出现一次的数字 III

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 <strong>任意顺序</strong> 返回答案。</p>

<p>你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1,3,2,5]
<strong>输出：</strong>[3,5]
<strong>解释：</strong>[5, 3] 也是有效的答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [-1,0]
<strong>输出：</strong>[-1,0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,1]
<strong>输出：</strong>[1,0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>-2<sup>31</sup> &lt;= nums[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li>除两个只出现一次的整数外，<code>nums</code> 中的其他数字都出现两次</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组

## 示例

```
[1,2,1,3,2,5]
[-1,0]
[0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] singleNumber(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* singleNumber(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SingleNumber(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    
};
```

### TypeScript

```typescript
function singleNumber(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function singleNumber($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func singleNumber(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun singleNumber(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> singleNumber(List<int> nums) {
    
  }
}
```

### Go

```golang
func singleNumber(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def single_number(nums)
    
end
```

### Scala

```scala
object Solution {
    def singleNumber(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn single_number(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (single-number nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec single_number(Nums :: [integer()]) -> [integer()].
single_number(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec single_number(nums :: [integer]) :: [integer]
  def single_number(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func singleNumber(nums: Array<Int64>): Array<Int64> {

    }
}
```

