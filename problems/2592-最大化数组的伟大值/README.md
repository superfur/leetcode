# 2592. 最大化数组的伟大值

## 题目描述

<p>给你一个下标从 0 开始的整数数组&nbsp;<code>nums</code>&nbsp;。你需要将&nbsp;<code>nums</code>&nbsp;重新排列成一个新的数组&nbsp;<code>perm</code>&nbsp;。</p>

<p>定义 <code>nums</code>&nbsp;的 <strong>伟大值</strong>&nbsp;为满足&nbsp;<code>0 &lt;= i &lt; nums.length</code>&nbsp;且&nbsp;<code>perm[i] &gt; nums[i]</code>&nbsp;的下标数目。</p>

<p>请你返回重新排列 <code>nums</code>&nbsp;后的 <strong>最大</strong>&nbsp;伟大值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,3,5,2,1,3,1]
<b>输出：</b>4
<b>解释：</b>一个最优安排方案为 perm = [2,5,1,3,3,1,1] 。
在下标为 0, 1, 3 和 4 处，都有 perm[i] &gt; nums[i] 。因此我们返回 4 。</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [1,2,3,4]
<b>输出：</b>3
<b>解释：</b>最优排列为 [2,3,4,1] 。
在下标为 0, 1 和 2 处，都有 perm[i] &gt; nums[i] 。因此我们返回 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 提示

1. Can we use sorting and two pointers here?
2. Assign every element the next bigger unused element as many times as possible.

## 示例

```
[1,3,5,2,1,3,1]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximizeGreatness(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximizeGreatness(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximizeGreatness(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        
```

### C

```c
int maximizeGreatness(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximizeGreatness(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximizeGreatness = function(nums) {
    
};
```

### TypeScript

```typescript
function maximizeGreatness(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function maximizeGreatness($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximizeGreatness(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximizeGreatness(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximizeGreatness(List<int> nums) {
    
  }
}
```

### Go

```golang
func maximizeGreatness(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def maximize_greatness(nums)
    
end
```

### Scala

```scala
object Solution {
    def maximizeGreatness(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximize_greatness(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximize-greatness nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec maximize_greatness(Nums :: [integer()]) -> integer().
maximize_greatness(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximize_greatness(nums :: [integer]) :: integer
  def maximize_greatness(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximizeGreatness(nums: Array<Int64>): Int64 {

    }
}
```

