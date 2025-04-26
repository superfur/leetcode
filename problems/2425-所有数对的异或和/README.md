# 2425. 所有数对的异或和

## 题目描述

<p>给你两个下标从 <strong>0</strong>&nbsp;开始的数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>&nbsp;，两个数组都只包含非负整数。请你求出另外一个数组&nbsp;<code>nums3</code>&nbsp;，包含 <code>nums1</code>&nbsp;和 <code>nums2</code>&nbsp;中 <strong>所有数对</strong>&nbsp;的异或和（<code>nums1</code>&nbsp;中每个整数都跟 <code>nums2</code>&nbsp;中每个整数 <strong>恰好</strong>&nbsp;匹配一次）。</p>

<p>请你返回 <code>nums3</code>&nbsp;中所有整数的 <strong>异或和</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums1 = [2,1,3], nums2 = [10,2,5,0]
<b>输出：</b>13
<strong>解释：</strong>
一个可能的 nums3 数组是 [8,0,7,2,11,3,4,1,9,1,6,3] 。
所有这些数字的异或和是 13 ，所以我们返回 13 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums1 = [1,2], nums2 = [3,4]
<b>输出：</b>0
<strong>解释：</strong>
所有数对异或和的结果分别为 nums1[0] ^ nums2[0] ，nums1[0] ^ nums2[1] ，nums1[1] ^ nums2[0] 和 nums1[1] ^ nums2[1] 。
所以，一个可能的 nums3 数组是 [2,5,1,6] 。
2 ^ 5 ^ 1 ^ 6 = 0 ，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 脑筋急转弯
- 数组

## 提示

1. Think how the count of each individual integer affects the final answer.
2. If the length of nums1 is m and the length of nums2 is n, then each number in nums1 is repeated n times and each number in nums2 is repeated m times.

## 示例

```
[2,1,3]
[10,2,5,0]
[1,2]
[3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        
    }
};
```

### Java

```java
class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        
```

### C

```c
int xorAllNums(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int XorAllNums(int[] nums1, int[] nums2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var xorAllNums = function(nums1, nums2) {
    
};
```

### TypeScript

```typescript
function xorAllNums(nums1: number[], nums2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function xorAllNums($nums1, $nums2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func xorAllNums(_ nums1: [Int], _ nums2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun xorAllNums(nums1: IntArray, nums2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int xorAllNums(List<int> nums1, List<int> nums2) {
    
  }
}
```

### Go

```golang
func xorAllNums(nums1 []int, nums2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def xor_all_nums(nums1, nums2)
    
end
```

### Scala

```scala
object Solution {
    def xorAllNums(nums1: Array[Int], nums2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn xor_all_nums(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (xor-all-nums nums1 nums2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec xor_all_nums(Nums1 :: [integer()], Nums2 :: [integer()]) -> integer().
xor_all_nums(Nums1, Nums2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec xor_all_nums(nums1 :: [integer], nums2 :: [integer]) :: integer
  def xor_all_nums(nums1, nums2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func xorAllNums(nums1: Array<Int64>, nums2: Array<Int64>): Int64 {

    }
}
```

