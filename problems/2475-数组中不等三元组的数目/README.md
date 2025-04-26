# 2475. 数组中不等三元组的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的正整数数组 <code>nums</code> 。请你找出并统计满足下述条件的三元组 <code>(i, j, k)</code> 的数目：</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; k &lt; nums.length</code></li>
	<li><code>nums[i]</code>、<code>nums[j]</code> 和 <code>nums[k]</code> <strong>两两不同</strong> 。
	<ul>
		<li>换句话说：<code>nums[i] != nums[j]</code>、<code>nums[i] != nums[k]</code> 且 <code>nums[j] != nums[k]</code> 。</li>
	</ul>
	</li>
</ul>

<p>返回满足上述条件三元组的数目<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,4,2,4,3]
<strong>输出：</strong>3
<strong>解释：</strong>下面列出的三元组均满足题目条件：
- (0, 2, 4) 因为 4 != 2 != 3
- (1, 2, 4) 因为 4 != 2 != 3
- (2, 3, 4) 因为 2 != 4 != 3
共计 3 个三元组，返回 3 。
注意 (2, 0, 4) 不是有效的三元组，因为 2 &gt; 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,1,1,1,1]
<strong>输出：</strong>0
<strong>解释：</strong>不存在满足条件的三元组，所以返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 排序

## 提示

1. The constraints are very small. Can we try every triplet?
2. Yes, we can. Use three loops to iterate through all the possible triplets, ensuring the condition i < j < k holds.

## 示例

```
[4,4,2,4,3]
[1,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int unequalTriplets(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int unequalTriplets(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        
```

### C

```c
int unequalTriplets(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int UnequalTriplets(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var unequalTriplets = function(nums) {
    
};
```

### TypeScript

```typescript
function unequalTriplets(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function unequalTriplets($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func unequalTriplets(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun unequalTriplets(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int unequalTriplets(List<int> nums) {
    
  }
}
```

### Go

```golang
func unequalTriplets(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def unequal_triplets(nums)
    
end
```

### Scala

```scala
object Solution {
    def unequalTriplets(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unequal_triplets(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (unequal-triplets nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec unequal_triplets(Nums :: [integer()]) -> integer().
unequal_triplets(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unequal_triplets(nums :: [integer]) :: integer
  def unequal_triplets(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func unequalTriplets(nums: Array<Int64>): Int64 {

    }
}
```

