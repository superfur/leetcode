# 2568. 最小无法得到的或值

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>如果存在一些整数满足&nbsp;<code>0 &lt;= index<sub>1</sub> &lt; index<sub>2</sub> &lt; ... &lt; index<sub>k</sub> &lt; nums.length</code>&nbsp;，得到&nbsp;<code>nums[index<sub>1</sub>] | nums[index<sub>2</sub>] | ... | nums[index<sub>k</sub>] = x</code>&nbsp;，那么我们说&nbsp;<code>x</code>&nbsp;是&nbsp;<strong>可表达的</strong>&nbsp;。换言之，如果一个整数能由&nbsp;<code>nums</code>&nbsp;的某个子序列的或运算得到，那么它就是可表达的。</p>

<p>请你返回 <code>nums</code>&nbsp;不可表达的 <strong>最小非零整数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [2,1]
<b>输出：</b>4
<b>解释：</b>1 和 2 已经在数组中，因为 nums[0] | nums[1] = 2 | 1 = 3 ，所以 3 是可表达的。由于 4 是不可表达的，所以我们返回 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [5,3,2]
<b>输出：</b>1
<b>解释：</b>1 是最小不可表达的数字。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 脑筋急转弯
- 数组

## 提示

1. Think about forming numbers in the powers of 2 using their bit representation.
2. The minimum power of 2 not present in the array will be the first number that could not be expressed using the given operation.

## 示例

```
[2,1]
[5,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minImpossibleOR(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int minImpossibleOR(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minImpossibleOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        
```

### C

```c
int minImpossibleOR(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinImpossibleOR(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var minImpossibleOR = function(nums) {
    
};
```

### TypeScript

```typescript
function minImpossibleOR(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minImpossibleOR($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minImpossibleOR(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minImpossibleOR(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minImpossibleOR(List<int> nums) {
    
  }
}
```

### Go

```golang
func minImpossibleOR(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def min_impossible_or(nums)
    
end
```

### Scala

```scala
object Solution {
    def minImpossibleOR(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_impossible_or(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-impossible-or nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_impossible_or(Nums :: [integer()]) -> integer().
min_impossible_or(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_impossible_or(nums :: [integer]) :: integer
  def min_impossible_or(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minImpossibleOR(nums: Array<Int64>): Int64 {

    }
}
```

