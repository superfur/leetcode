# 2216. 美化数组的最少删除数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，如果满足下述条件，则认为数组 <code>nums</code> 是一个 <strong>美丽数组</strong> ：</p>

<ul>
	<li><code>nums.length</code> 为偶数</li>
	<li>对所有满足 <code>i % 2 == 0</code> 的下标 <code>i</code> ，<code>nums[i] != nums[i + 1]</code> 均成立</li>
</ul>

<p>注意，空数组同样认为是美丽数组。</p>

<p>你可以从 <code>nums</code> 中删除任意数量的元素。当你删除一个元素时，被删除元素右侧的所有元素将会向左移动一个单位以填补空缺，而左侧的元素将会保持 <strong>不变</strong> 。</p>

<p>返回使 <code>nums</code> 变为美丽数组所需删除的 <strong>最少</strong> 元素数目<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,2,3,5]
<strong>输出：</strong>1
<strong>解释：</strong>可以删除 <code>nums[0]</code> 或 <code>nums[1]</code> ，这样得到的 <code>nums</code> = [1,2,3,5] 是一个美丽数组。可以证明，要想使 nums 变为美丽数组，至少需要删除 1 个元素。</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [1,1,2,2,3,3]
<strong>输出：</strong>2
<strong>解释：</strong>可以删除 <code>nums[0]</code> 和 <code>nums[5]</code> ，这样得到的 nums = [1,2,2,3] 是一个美丽数组。可以证明，要想使 nums 变为美丽数组，至少需要删除 2 个元素。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组

## 提示

1. Delete as many adjacent equal elements as necessary.
2. If the length of nums is odd after the entire process, delete the last element.

## 示例

```
[1,1,2,3,5]
[1,1,2,2,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minDeletion(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minDeletion(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minDeletion(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        
```

### C

```c
int minDeletion(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinDeletion(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minDeletion = function(nums) {
    
};
```

### TypeScript

```typescript
function minDeletion(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minDeletion($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minDeletion(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minDeletion(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minDeletion(List<int> nums) {
    
  }
}
```

### Go

```golang
func minDeletion(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_deletion(nums)
    
end
```

### Scala

```scala
object Solution {
    def minDeletion(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_deletion(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-deletion nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_deletion(Nums :: [integer()]) -> integer().
min_deletion(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_deletion(nums :: [integer]) :: integer
  def min_deletion(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minDeletion(nums: Array<Int64>): Int64 {

    }
}
```

