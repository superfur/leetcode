# 2170. 使数组变成交替数组的最少操作数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>nums</code> ，该数组由 <code>n</code> 个正整数组成。</p>

<p>如果满足下述条件，则数组 <code>nums</code> 是一个 <strong>交替数组</strong> ：</p>

<ul>
	<li><code>nums[i - 2] == nums[i]</code> ，其中 <code>2 &lt;= i &lt;= n - 1</code> 。</li>
	<li><code>nums[i - 1] != nums[i]</code> ，其中 <code>1 &lt;= i &lt;= n - 1</code> 。</li>
</ul>

<p>在一步 <strong>操作</strong> 中，你可以选择下标 <code>i</code> 并将 <code>nums[i]</code> <strong>更改</strong> 为 <strong>任一</strong> 正整数。</p>

<p>返回使数组变成交替数组的 <strong>最少操作数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,1,3,2,4,3]
<strong>输出：</strong>3
<strong>解释：</strong>
使数组变成交替数组的方法之一是将该数组转换为 [3,1,3,<em><strong>1</strong></em>,<em><strong>3</strong></em>,<em><strong>1</strong></em>] 。
在这种情况下，操作数为 3 。
可以证明，操作数少于 3 的情况下，无法使数组变成交替数组。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2,2,2]
<strong>输出：</strong>2
<strong>解释：</strong>
使数组变成交替数组的方法之一是将该数组转换为 [1,2,<em><strong>1</strong></em>,2,<em><strong>1</strong></em>].
在这种情况下，操作数为 2 。
注意，数组不能转换成 [<em><strong>2</strong></em>,2,2,2,2] 。因为在这种情况下，nums[0] == nums[1]，不满足交替数组的条件。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 计数

## 提示

1. Count the frequency of each element in odd positions in the array. Do the same for elements in even positions.
2. To minimize the number of operations we need to maximize the number of elements we keep from the original array.
3. What are the possible combinations of elements we can choose from odd indices and even indices so that the number of unchanged elements is maximized?

## 示例

```
[3,1,3,2,4,3]
[1,2,2,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumOperations(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
```

### C

```c
int minimumOperations(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumOperations(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    
};
```

### TypeScript

```typescript
function minimumOperations(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minimumOperations($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumOperations(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumOperations(List<int> nums) {
    
  }
}
```

### Go

```golang
func minimumOperations(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
    
end
```

### Scala

```scala
object Solution {
    def minimumOperations(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-operations nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_operations(Nums :: [integer()]) -> integer().
minimum_operations(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_operations(nums :: [integer]) :: integer
  def minimum_operations(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumOperations(nums: Array<Int64>): Int64 {

    }
}
```

