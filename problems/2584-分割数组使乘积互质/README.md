# 2584. 分割数组使乘积互质

## 题目描述

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> ，下标从 <strong>0</strong> 开始。</p>

<p>如果在下标 <code>i</code> 处 <strong>分割</strong> 数组，其中 <code>0 &lt;= i &lt;= n - 2</code> ，使前 <code>i + 1</code> 个元素的乘积和剩余元素的乘积互质，则认为该分割 <strong>有效</strong> 。</p>

<ul>
	<li>例如，如果 <code>nums = [2, 3, 3]</code> ，那么在下标 <code>i = 0</code> 处的分割有效，因为 <code>2</code> 和 <code>9</code> 互质，而在下标 <code>i = 1</code> 处的分割无效，因为 <code>6</code> 和 <code>3</code> 不互质。在下标 <code>i = 2</code> 处的分割也无效，因为 <code>i == n - 1</code> 。</li>
</ul>

<p>返回可以有效分割数组的最小下标 <code>i</code> ，如果不存在有效分割，则返回 <code>-1</code> 。</p>

<p>当且仅当 <code>gcd(val1, val2) == 1</code> 成立时，<code>val1</code> 和 <code>val2</code> 这两个值才是互质的，其中 <code>gcd(val1, val2)</code> 表示 <code>val1</code> 和 <code>val2</code> 的最大公约数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/second.PNG" style="width: 450px; height: 211px;" /></p>

<pre>
<strong>输入：</strong>nums = [4,7,8,15,3,5]
<strong>输出：</strong>2
<strong>解释：</strong>上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
唯一一个有效分割位于下标 2 。</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/12/14/capture.PNG" style="width: 450px; height: 215px;" /></p>

<pre>
<strong>输入：</strong>nums = [4,7,15,8,3,5]
<strong>输出：</strong>-1
<strong>解释：</strong>上表展示了每个下标 i 处的前 i + 1 个元素的乘积、剩余元素的乘积和它们的最大公约数的值。
不存在有效分割。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 数学
- 数论

## 提示

1. Two numbers with GCD equal to 1 have no common prime divisor.
2. Find the prime factorization of the left and right sides and check if they share a prime divisor.

## 示例

```
[4,7,8,15,3,5]
[4,7,15,8,3,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findValidSplit(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findValidSplit(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findValidSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        
```

### C

```c
int findValidSplit(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindValidSplit(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findValidSplit = function(nums) {
    
};
```

### TypeScript

```typescript
function findValidSplit(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findValidSplit($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findValidSplit(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findValidSplit(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findValidSplit(List<int> nums) {
    
  }
}
```

### Go

```golang
func findValidSplit(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_valid_split(nums)
    
end
```

### Scala

```scala
object Solution {
    def findValidSplit(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_valid_split(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-valid-split nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_valid_split(Nums :: [integer()]) -> integer().
find_valid_split(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_valid_split(nums :: [integer]) :: integer
  def find_valid_split(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findValidSplit(nums: Array<Int64>): Int64 {

    }
}
```

