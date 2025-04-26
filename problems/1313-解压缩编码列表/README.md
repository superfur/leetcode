# 1313. 解压缩编码列表

## 题目描述

<p>给你一个以行程长度编码压缩的整数列表 <code>nums</code> 。</p>

<p>考虑每对相邻的两个元素 <code>[freq, val] = [nums[2*i], nums[2*i+1]]</code> （其中 <code>i >= 0</code> ），每一对都表示解压后子列表中有 <code>freq</code> 个值为 <code>val</code> 的元素，你需要从左到右连接所有子列表以生成解压后的列表。</p>

<p>请你返回解压后的列表。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,3,4]
<strong>输出：</strong>[2,4,4,4]
<strong>解释：</strong>第一对 [1,2] 代表着 2 的出现频次为 1，所以生成数组 [2]。
第二对 [3,4] 代表着 4 的出现频次为 3，所以生成数组 [4,4,4]。
最后将它们串联到一起 [2] + [4,4,4] = [2,4,4,4]。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,2,3]
<strong>输出：</strong>[1,3,3]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= nums.length <= 100</code></li>
	<li><code>nums.length % 2 == 0</code></li>
	<li><code>1 <= nums[i] <= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Decompress the given array by repeating nums[2*i+1] a number of times equal to nums[2*i].

## 示例

```
[1,2,3,4]
[1,1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] decompressRLElist(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decompressRLElist(int* nums, int numsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] DecompressRLElist(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    
};
```

### TypeScript

```typescript
function decompressRLElist(nums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer[]
     */
    function decompressRLElist($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func decompressRLElist(_ nums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun decompressRLElist(nums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> decompressRLElist(List<int> nums) {
    
  }
}
```

### Go

```golang
func decompressRLElist(nums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer[]}
def decompress_rl_elist(nums)
    
end
```

### Scala

```scala
object Solution {
    def decompressRLElist(nums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn decompress_rl_elist(nums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (decompress-rl-elist nums)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec decompress_rl_elist(Nums :: [integer()]) -> [integer()].
decompress_rl_elist(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec decompress_rl_elist(nums :: [integer]) :: [integer]
  def decompress_rl_elist(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func decompressRLElist(nums: Array<Int64>): Array<Int64> {

    }
}
```

