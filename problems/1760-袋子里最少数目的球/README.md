# 1760. 袋子里最少数目的球

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，其中 <code>nums[i]</code> 表示第 <code>i</code> 个袋子里球的数目。同时给你一个整数 <code>maxOperations</code> 。</p>

<p>你可以进行如下操作至多 <code>maxOperations</code> 次：</p>

<ul>
	<li>选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 <strong>正整数</strong> 个球。

	<ul>
		<li>比方说，一个袋子里有 <code>5</code> 个球，你可以把它们分到两个新袋子里，分别有 <code>1</code> 个和 <code>4</code> 个球，或者分别有 <code>2</code> 个和 <code>3</code> 个球。</li>
	</ul>
	</li>
</ul>

<p>你的开销是单个袋子里球数目的 <strong>最大值</strong> ，你想要 <strong>最小化</strong> 开销。</p>

<p>请你返回进行上述操作后的最小开销。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [9], maxOperations = 2
<b>输出：</b>3
<b>解释：</b>
- 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[<strong>9</strong>] -> [6,3] 。
- 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[<strong>6</strong>,3] -> [3,3,3] 。
装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [2,4,8,2], maxOperations = 4
<b>输出：</b>2
<strong>解释：</strong>
- 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,<strong>8</strong>,2] -> [2,4,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,<strong>4</strong>,4,4,2] -> [2,2,2,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,<strong>4</strong>,4,2] -> [2,2,2,2,2,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,<strong>4</strong>,2] -> [2,2,2,2,2,2,2,2] 。
装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [7,17], maxOperations = 2
<b>输出：</b>7
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= maxOperations, nums[i] <= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 提示

1. Let's change the question if we know the maximum size of a bag what is the minimum number of bags you can make
2. note that as the maximum size increases the minimum number of bags decreases so we can binary search the maximum size

## 示例

```
[9]
2
[2,4,8,2]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumSize(vector<int>& nums, int maxOperations) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumSize(self, nums, maxOperations):
        """
        :type nums: List[int]
        :type maxOperations: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
```

### C

```c
int minimumSize(int* nums, int numsSize, int maxOperations) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumSize(int[] nums, int maxOperations) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} maxOperations
 * @return {number}
 */
var minimumSize = function(nums, maxOperations) {
    
};
```

### TypeScript

```typescript
function minimumSize(nums: number[], maxOperations: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $maxOperations
     * @return Integer
     */
    function minimumSize($nums, $maxOperations) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumSize(_ nums: [Int], _ maxOperations: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumSize(nums: IntArray, maxOperations: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumSize(List<int> nums, int maxOperations) {
    
  }
}
```

### Go

```golang
func minimumSize(nums []int, maxOperations int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} max_operations
# @return {Integer}
def minimum_size(nums, max_operations)
    
end
```

### Scala

```scala
object Solution {
    def minimumSize(nums: Array[Int], maxOperations: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_size(nums: Vec<i32>, max_operations: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-size nums maxOperations)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_size(Nums :: [integer()], MaxOperations :: integer()) -> integer().
minimum_size(Nums, MaxOperations) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_size(nums :: [integer], max_operations :: integer) :: integer
  def minimum_size(nums, max_operations) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumSize(nums: Array<Int64>, maxOperations: Int64): Int64 {

    }
}
```

