# 1673. 找出最具竞争力的子序列

## 题目描述

<p>给你一个整数数组 <code>nums</code> 和一个正整数 <code>k</code> ，返回长度为 <code>k</code> 且最具 <strong>竞争力</strong> 的<em> </em><code>nums</code> 子序列。</p>

<p>数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。</p>

<p>在子序列 <code>a</code> 和子序列 <code>b</code> 第一个不相同的位置上，如果 <code>a</code> 中的数字小于 <code>b</code> 中对应的数字，那么我们称子序列 <code>a</code> 比子序列 <code>b</code>（相同长度下）更具 <strong>竞争力</strong> 。 例如，<code>[1,3,4]</code> 比 <code>[1,3,5]</code> 更具竞争力，在第一个不相同的位置，也就是最后一个位置上， <code>4</code> 小于 <code>5</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,5,2,6], k = 2
<strong>输出：</strong>[2,6]
<strong>解释：</strong>在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,4,3,3,5,4,9,6], k = 4
<strong>输出：</strong>[2,3,3,4]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>0 <= nums[i] <= 10<sup>9</sup></code></li>
	<li><code>1 <= k <= nums.length</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 单调栈

## 提示

1. In lexicographical order, the elements to the left have higher priority than those that come after. Can you think of a strategy that incrementally builds the answer from left to right?

## 示例

```
[3,5,2,6]
2
[2,4,3,3,5,4,9,6]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] mostCompetitive(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* mostCompetitive(int* nums, int numsSize, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MostCompetitive(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var mostCompetitive = function(nums, k) {
    
};
```

### TypeScript

```typescript
function mostCompetitive(nums: number[], k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer[]
     */
    function mostCompetitive($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostCompetitive(_ nums: [Int], _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostCompetitive(nums: IntArray, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> mostCompetitive(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func mostCompetitive(nums []int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def most_competitive(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def mostCompetitive(nums: Array[Int], k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_competitive(nums: Vec<i32>, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (most-competitive nums k)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec most_competitive(Nums :: [integer()], K :: integer()) -> [integer()].
most_competitive(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_competitive(nums :: [integer], k :: integer) :: [integer]
  def most_competitive(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostCompetitive(nums: Array<Int64>, k: Int64): Array<Int64> {

    }
}
```

