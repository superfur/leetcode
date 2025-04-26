# 2616. 最小化数对的最大差值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>p</code>&nbsp;。请你从&nbsp;<code>nums</code>&nbsp;中找到&nbsp;<code>p</code> 个下标对，每个下标对对应数值取差值，你需要使得这 <code>p</code> 个差值的&nbsp;<strong>最大值</strong>&nbsp;<strong>最小</strong>。同时，你需要确保每个下标在这&nbsp;<code>p</code>&nbsp;个下标对中最多出现一次。</p>

<p>对于一个下标对&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;，这一对的差值为&nbsp;<code>|nums[i] - nums[j]|</code>&nbsp;，其中&nbsp;<code>|x|</code>&nbsp;表示 <code>x</code>&nbsp;的 <strong>绝对值</strong>&nbsp;。</p>

<p>请你返回 <code>p</code>&nbsp;个下标对对应数值 <strong>最大差值</strong>&nbsp;的 <strong>最小值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [10,1,2,7,1,3], p = 2
<b>输出：</b>1
<b>解释：</b>第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [4,2,1,2], p = 1
<b>输出：</b>0
<b>解释：</b>选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= p &lt;= (nums.length)/2</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找

## 提示

1. Can we use dynamic programming here?
2. To minimize the answer, the array should be sorted first.
3. The recurrence relation is fn(i, x) = min(fn(i+1, x), max(abs(nums[i]-nums[i+1]), fn(i+2, p-1)), and fn(0,p) gives the desired answer.

## 示例

```
[10,1,2,7,1,3]
2
[4,2,1,2]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimizeMax(vector<int>& nums, int p) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimizeMax(int[] nums, int p) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimizeMax(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
```

### C

```c
int minimizeMax(int* nums, int numsSize, int p) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimizeMax(int[] nums, int p) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minimizeMax = function(nums, p) {
    
};
```

### TypeScript

```typescript
function minimizeMax(nums: number[], p: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $p
     * @return Integer
     */
    function minimizeMax($nums, $p) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimizeMax(_ nums: [Int], _ p: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimizeMax(nums: IntArray, p: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimizeMax(List<int> nums, int p) {
    
  }
}
```

### Go

```golang
func minimizeMax(nums []int, p int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} p
# @return {Integer}
def minimize_max(nums, p)
    
end
```

### Scala

```scala
object Solution {
    def minimizeMax(nums: Array[Int], p: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimize_max(nums: Vec<i32>, p: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimize-max nums p)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimize_max(Nums :: [integer()], P :: integer()) -> integer().
minimize_max(Nums, P) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimize_max(nums :: [integer], p :: integer) :: integer
  def minimize_max(nums, p) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimizeMax(nums: Array<Int64>, p: Int64): Int64 {

    }
}
```

