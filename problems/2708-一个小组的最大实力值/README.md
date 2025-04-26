# 2708. 一个小组的最大实力值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，它表示一个班级中所有学生在一次考试中的成绩。老师想选出一部分同学组成一个 <strong>非空</strong>&nbsp;小组，且这个小组的 <strong>实力值</strong>&nbsp;最大，如果这个小组里的学生下标为&nbsp;<code>i<sub>0</sub></code>, <code>i<sub>1</sub></code>, <code>i<sub>2</sub></code>, ... , <code>i<sub>k</sub></code>&nbsp;，那么这个小组的实力值定义为&nbsp;<code>nums[i<sub>0</sub>] * nums[i<sub>1</sub>] * nums[i<sub>2</sub>] * ... * nums[i<sub>k</sub>​]</code>&nbsp;。</p>

<p>请你返回老师创建的小组能得到的最大实力值为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [3,-1,-5,2,5,-9]
<strong>输出：</strong>1350
<b>解释：</b>一种构成最大实力值小组的方案是选择下标为 [0,2,3,4,5] 的学生。实力值为 3 * (-5) * 2 * 5 * (-9) = 1350 ，这是可以得到的最大实力值。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [-4,-5,-4]
<b>输出：</b>20
<b>解释：</b>选择下标为 [0, 1] 的学生。得到的实力值为 20 。我们没法得到更大的实力值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 13</code></li>
	<li><code>-9 &lt;= nums[i] &lt;= 9</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 位运算
- 数组
- 动态规划
- 回溯
- 枚举
- 排序

## 提示

1. Try to generate all pairs of subsets and check which group provides maximal strength.
2. It can also be solved in O(NlogN) by sorting the array and using all positive integers.
3. Use negative integers only in pairs such that their product becomes positive.

## 示例

```
[3,-1,-5,2,5,-9]
[-4,-5,-4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long maxStrength(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public long maxStrength(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        
```

### C

```c
long long maxStrength(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MaxStrength(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxStrength = function(nums) {
    
};
```

### TypeScript

```typescript
function maxStrength(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maxStrength($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxStrength(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxStrength(nums: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxStrength(List<int> nums) {
    
  }
}
```

### Go

```golang
func maxStrength(nums []int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def max_strength(nums)
    
end
```

### Scala

```scala
object Solution {
    def maxStrength(nums: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_strength(nums: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (max-strength nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_strength(Nums :: [integer()]) -> integer().
max_strength(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_strength(nums :: [integer]) :: integer
  def max_strength(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxStrength(nums: Array<Int64>): Int64 {

    }
}
```

