# 945. 使数组唯一的最小增量

## 题目描述

<p>给你一个整数数组 <code>nums</code> 。每次 move 操作将会选择任意一个满足 <code>0 &lt;= i &lt; nums.length</code> 的下标 <code>i</code>，并将&nbsp;<code>nums[i]</code> 递增&nbsp;<code>1</code>。</p>

<p>返回使 <code>nums</code> 中的每个值都变成唯一的所需要的最少操作次数。</p>

<p>生成的测试用例保证答案在 32 位整数范围内。</p>

<div class="original__bRMd">
<div>
<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,2]
<strong>输出：</strong>1
<strong>解释：</strong>经过一次 <em>move</em> 操作，数组将变为 [1, 2, 3]。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [3,2,1,2,1,7]
<strong>输出：</strong>6
<strong>解释：</strong>经过 6 次 <em>move</em> 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 <em>move</em> 操作是不能让数组的每个值唯一的。</pre>
</div>
</div>

<p>&nbsp;</p>
<strong>提示：</strong>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 计数
- 排序

## 示例

```
[1,2,2]
[3,2,1,2,1,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minIncrementForUnique(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minIncrementForUnique(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
```

### C

```c
int minIncrementForUnique(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinIncrementForUnique(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minIncrementForUnique = function(nums) {
    
};
```

### TypeScript

```typescript
function minIncrementForUnique(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minIncrementForUnique($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minIncrementForUnique(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minIncrementForUnique(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minIncrementForUnique(List<int> nums) {
    
  }
}
```

### Go

```golang
func minIncrementForUnique(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_increment_for_unique(nums)
    
end
```

### Scala

```scala
object Solution {
    def minIncrementForUnique(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_increment_for_unique(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-increment-for-unique nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_increment_for_unique(Nums :: [integer()]) -> integer().
min_increment_for_unique(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_increment_for_unique(nums :: [integer]) :: integer
  def min_increment_for_unique(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minIncrementForUnique(nums: Array<Int64>): Int64 {

    }
}
```

