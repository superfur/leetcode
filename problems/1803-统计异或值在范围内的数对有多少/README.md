# 1803. 统计异或值在范围内的数对有多少

## 题目描述

<p>给你一个整数数组 <code>nums</code> （下标 <strong>从 0 开始</strong> 计数）以及两个整数：<code>low</code> 和 <code>high</code> ，请返回 <strong>漂亮数对</strong> 的数目。</p>

<p><strong>漂亮数对</strong> 是一个形如 <code>(i, j)</code> 的数对，其中 <code>0 &lt;= i &lt; j &lt; nums.length</code> 且 <code>low &lt;= (nums[i] XOR nums[j]) &lt;= high</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,4,2,7], low = 2, high = 6
<strong>输出：</strong>6
<strong>解释：</strong>所有漂亮数对 (i, j) 列出如下：
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [9,8,4,2,1], low = 5, high = 14
<strong>输出：</strong>8
<strong>解释：</strong>所有漂亮数对 (i, j) 列出如下：
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= low &lt;= high &lt;= 2 * 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 字典树
- 数组

## 提示

1. Let's note that we can count all pairs with XOR ≤ K, so the answer would be to subtract the number of pairs withs XOR < low from the number of pairs with XOR ≤ high.
2. For each value, find out the number of values when you XOR it with the result is  ≤ K using a trie.

## 示例

```
[1,4,2,7]
2
6
[9,8,4,2,1]
5
14
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPairs(vector<int>& nums, int low, int high) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPairs(int[] nums, int low, int high) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, nums, low, high):
        """
        :type nums: List[int]
        :type low: int
        :type high: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        
```

### C

```c
int countPairs(int* nums, int numsSize, int low, int high) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPairs(int[] nums, int low, int high) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countPairs = function(nums, low, high) {
    
};
```

### TypeScript

```typescript
function countPairs(nums: number[], low: number, high: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $low
     * @param Integer $high
     * @return Integer
     */
    function countPairs($nums, $low, $high) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ nums: [Int], _ low: Int, _ high: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(nums: IntArray, low: Int, high: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPairs(List<int> nums, int low, int high) {
    
  }
}
```

### Go

```golang
func countPairs(nums []int, low int, high int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def count_pairs(nums, low, high)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(nums: Array[Int], low: Int, high: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(nums: Vec<i32>, low: i32, high: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs nums low high)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pairs(Nums :: [integer()], Low :: integer(), High :: integer()) -> integer().
count_pairs(Nums, Low, High) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(nums :: [integer], low :: integer, high :: integer) :: integer
  def count_pairs(nums, low, high) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(nums: Array<Int64>, low: Int64, high: Int64): Int64 {

    }
}
```

