# 1929. 数组串联

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> 。请你构建一个长度为 <code>2n</code> 的答案数组 <code>ans</code> ，数组下标<strong> 从 0 开始计数 </strong>，对于所有 <code>0 <= i < n</code> 的 <code>i</code> ，满足下述所有要求：</p>

<ul>
	<li><code>ans[i] == nums[i]</code></li>
	<li><code>ans[i + n] == nums[i]</code></li>
</ul>

<p>具体而言，<code>ans</code> 由两个 <code>nums</code> 数组 <strong>串联</strong> 形成。</p>

<p>返回数组<em> </em><code>ans</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,1]
<strong>输出：</strong>[1,2,1,1,2,1]
<strong>解释：</strong>数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,2,1]
<strong>输出：</strong>[1,3,2,1,1,3,2,1]
<strong>解释：</strong>数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 <= n <= 1000</code></li>
	<li><code>1 <= nums[i] <= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 模拟

## 提示

1. Build an array of size 2 * n and assign num[i] to ans[i] and ans[i + n]

## 示例

```
[1,2,1]
[1,3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] getConcatenation(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] GetConcatenation(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function(nums) {
    
};
```

### TypeScript

```typescript
function getConcatenation(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function getConcatenation($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getConcatenation(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getConcatenation(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> getConcatenation(List<int> nums) {
    
  }
}
```

### Go

```golang
func getConcatenation(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def get_concatenation(nums)
    
end
```

### Scala

```scala
object Solution {
    def getConcatenation(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (get-concatenation nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec get_concatenation(Nums :: [integer()]) -> [integer()].
get_concatenation(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_concatenation(nums :: [integer]) :: [integer]
  def get_concatenation(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getConcatenation(nums: Array<Int64>): Array<Int64> {

    }
}
```

