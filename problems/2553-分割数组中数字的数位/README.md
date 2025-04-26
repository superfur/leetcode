# 2553. 分割数组中数字的数位

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>&nbsp;，请你返回一个数组<em>&nbsp;</em><code>answer</code> ，你需要将&nbsp;<code>nums</code>&nbsp;中每个整数进行数位分割后，按照&nbsp;<code>nums</code>&nbsp;中出现的&nbsp;<strong>相同顺序</strong>&nbsp;放入答案数组中。</p>

<p>对一个整数进行数位分割，指的是将整数各个数位按原本出现的顺序排列成数组。</p>

<ul>
	<li>比方说，整数&nbsp;<code>10921</code>&nbsp;，分割它的各个数位得到&nbsp;<code>[1,0,9,2,1]</code>&nbsp;。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [13,25,83,77]
<b>输出：</b>[1,3,2,5,8,3,7,7]
<b>解释：</b>
- 分割 13 得到 [1,3] 。
- 分割 25 得到 [2,5] 。
- 分割 83 得到 [8,3] 。
- 分割 77 得到 [7,7] 。
answer = [1,3,2,5,8,3,7,7] 。answer 中的数字分割结果按照原数字在数组中的相同顺序排列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [7,1,3,9]
<b>输出：</b>[7,1,3,9]
<b>解释：</b>nums 中每个整数的分割是它自己。
answer = [7,1,3,9] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Convert each number into a list and append that list to the answer.
2. You can convert the integer into a string to do that easily.

## 示例

```
[13,25,83,77]
[7,1,3,9]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> separateDigits(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] separateDigits(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* separateDigits(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] SeparateDigits(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var separateDigits = function(nums) {
    
};
```

### TypeScript

```typescript
function separateDigits(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function separateDigits($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func separateDigits(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun separateDigits(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> separateDigits(List<int> nums) {
    
  }
}
```

### Go

```golang
func separateDigits(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def separate_digits(nums)
    
end
```

### Scala

```scala
object Solution {
    def separateDigits(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn separate_digits(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (separate-digits nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec separate_digits(Nums :: [integer()]) -> [integer()].
separate_digits(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec separate_digits(nums :: [integer]) :: [integer]
  def separate_digits(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func separateDigits(nums: Array<Int64>): Array<Int64> {

    }
}
```

