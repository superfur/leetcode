# 1979. 找出数组的最大公约数

## 题目描述

<p>给你一个整数数组 <code>nums</code> ，返回数组中最大数和最小数的 <strong>最大公约数</strong> 。</p>

<p>两个数的&nbsp;<strong>最大公约数</strong> 是能够被两个数整除的最大正整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>nums = [2,5,6,9,10]
<strong>输出：</strong>2
<strong>解释：</strong>
nums 中最小的数是 2
nums 中最大的数是 10
2 和 10 的最大公约数是 2
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>nums = [7,5,6,8,3]
<strong>输出：</strong>1
<strong>解释：</strong>
nums 中最小的数是 3
nums 中最大的数是 8
3 和 8 的最大公约数是 1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>nums = [3,3]
<strong>输出：</strong>3
<strong>解释：</strong>
nums 中最小的数是 3
nums 中最大的数是 3
3 和 3 的最大公约数是 3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 数论

## 提示

1. Find the minimum and maximum in one iteration. Let them be mn and mx.
2. Try all the numbers in the range [1, mn] and check the largest number which divides both of them.

## 示例

```
[2,5,6,9,10]
[7,5,6,8,3]
[3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findGCD(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findGCD(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
```

### C

```c
int findGCD(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindGCD(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findGCD = function(nums) {
    
};
```

### TypeScript

```typescript
function findGCD(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findGCD($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findGCD(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findGCD(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findGCD(List<int> nums) {
    
  }
}
```

### Go

```golang
func findGCD(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_gcd(nums)
    
end
```

### Scala

```scala
object Solution {
    def findGCD(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_gcd(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-gcd nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_gcd(Nums :: [integer()]) -> integer().
find_gcd(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_gcd(nums :: [integer]) :: integer
  def find_gcd(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findGCD(nums: Array<Int64>): Int64 {

    }
}
```

