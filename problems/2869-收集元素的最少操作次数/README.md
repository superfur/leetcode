# 2869. 收集元素的最少操作次数

## 题目描述

<p>给你一个正整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>一次操作中，你可以将数组的最后一个元素删除，将该元素添加到一个集合中。</p>

<p>请你返回收集元素&nbsp;<code>1, 2, ..., k</code>&nbsp;需要的&nbsp;<strong>最少操作次数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [3,1,5,4,2], k = 2
<b>输出：</b>4
<b>解释：</b>4 次操作后，集合中的元素依次添加了 2 ，4 ，5 和 1 。此时集合中包含元素 1 和 2 ，所以答案为 4 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [3,1,5,4,2], k = 5
<b>输出：</b>5
<b>解释：</b>5 次操作后，集合中的元素依次添加了 2 ，4 ，5 ，1 和 3 。此时集合中包含元素 1 到 5 ，所以答案为 5 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [3,2,5,3,1], k = 3
<b>输出：</b>4
<b>解释：</b>4 次操作后，集合中的元素依次添加了 1 ，3 ，5 和 2 。此时集合中包含元素 1 到 3  ，所以答案为 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
	<li><code>1 &lt;= k &lt;= nums.length</code></li>
	<li>输入保证你可以收集到元素&nbsp;<code>1, 2, ..., k</code> 。</li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组
- 哈希表

## 提示

1. Use an occurrence array.
2. Iterate over the elements in reverse order.
3. If the current element <code>nums[i]</code> is not marked in the occurrence array and <code>nums[i] &lt;= k</code>, mark <code>nums[i]</code>.
4. Keep track of how many integers you have marked.
5. Return the current index as soon as the number of marked integers becomes equal to <code>k</code>.

## 示例

```
[3,1,5,4,2]
2
[3,1,5,4,2]
5
[3,2,5,3,1]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(List<Integer> nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int minOperations(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(IList<int> nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minOperations = function(nums, k) {
    
};
```

### TypeScript

```typescript
function minOperations(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function minOperations($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(nums: List<Int>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func minOperations(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(nums: List[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Nums :: [integer()], K :: integer()) -> integer().
min_operations(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(nums :: [integer], k :: integer) :: integer
  def min_operations(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(nums: ArrayList<Int64>, k: Int64): Int64 {

    }
}
```

