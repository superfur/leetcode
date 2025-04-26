# 493. 翻转对

## 题目描述

<p>给定一个数组&nbsp;<code>nums</code>&nbsp;，如果&nbsp;<code>i &lt; j</code>&nbsp;且&nbsp;<code>nums[i] &gt; 2*nums[j]</code>&nbsp;我们就将&nbsp;<code>(i, j)</code>&nbsp;称作一个<strong><em>重要翻转对</em></strong>。</p>

<p>你需要返回给定数组中的重要翻转对的数量。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入</strong>: [1,3,2,3,1]
<strong>输出</strong>: 2
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入</strong>: [2,4,3,5,1]
<strong>输出</strong>: 3
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定数组的长度不会超过<code>50000</code>。</li>
	<li>输入数组中的所有数字都在32位整数的表示范围内。</li>
</ol>


## 难度

Hard

## 标签

- 树状数组
- 线段树
- 数组
- 二分查找
- 分治
- 有序集合
- 归并排序

## 提示

1. Use the merge-sort technique.
2. Divide the array into two parts and sort them.
3. For each integer in the first part, count the number of integers that satisfy the condition from the second part. Use the pointer to help you in the counting process.

## 示例

```
[1,3,2,3,1]
[2,4,3,5,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int reversePairs(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int reversePairs(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
```

### C

```c
int reversePairs(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ReversePairs(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var reversePairs = function(nums) {
    
};
```

### TypeScript

```typescript
function reversePairs(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function reversePairs($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reversePairs(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reversePairs(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int reversePairs(List<int> nums) {
    
  }
}
```

### Go

```golang
func reversePairs(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def reverse_pairs(nums)
    
end
```

### Scala

```scala
object Solution {
    def reversePairs(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reverse_pairs(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (reverse-pairs nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec reverse_pairs(Nums :: [integer()]) -> integer().
reverse_pairs(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reverse_pairs(nums :: [integer]) :: integer
  def reverse_pairs(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reversePairs(nums: Array<Int64>): Int64 {

    }
}
```

