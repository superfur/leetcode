# 2239. 找到最接近 0 的数字

## 题目描述

<p>给你一个长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;，请你返回 <code>nums</code>&nbsp;中最 <strong>接近</strong>&nbsp;<code>0</code>&nbsp;的数字。如果有多个答案，请你返回它们中的 <strong>最大值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [-4,-2,1,4,8]
<b>输出：</b>1
<strong>解释：</strong>
-4 到 0 的距离为 |-4| = 4 。
-2 到 0 的距离为 |-2| = 2 。
1 到 0 的距离为 |1| = 1 。
4 到 0 的距离为 |4| = 4 。
8 到 0 的距离为 |8| = 8 。
所以，数组中距离 0 最近的数字为 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,-1,1]
<b>输出：</b>1
<b>解释：</b>1 和 -1 都是距离 0 最近的数字，所以返回较大值 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Keep track of the number closest to 0 as you iterate through the array.
2. Ensure that if multiple numbers are closest to 0, you store the one with the largest value.

## 示例

```
[-4,-2,1,4,8]
[2,-1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findClosestNumber(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
```

### C

```c
int findClosestNumber(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindClosestNumber(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findClosestNumber = function(nums) {
    
};
```

### TypeScript

```typescript
function findClosestNumber(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findClosestNumber($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findClosestNumber(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findClosestNumber(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findClosestNumber(List<int> nums) {
    
  }
}
```

### Go

```golang
func findClosestNumber(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_closest_number(nums)
    
end
```

### Scala

```scala
object Solution {
    def findClosestNumber(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_closest_number(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-closest-number nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_closest_number(Nums :: [integer()]) -> integer().
find_closest_number(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_closest_number(nums :: [integer]) :: integer
  def find_closest_number(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findClosestNumber(nums: Array<Int64>): Int64 {

    }
}
```

