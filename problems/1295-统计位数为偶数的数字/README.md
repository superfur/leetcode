# 1295. 统计位数为偶数的数字

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>，请你返回其中位数为&nbsp;<strong>偶数</strong>&nbsp;的数字的个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [12,345,2,6,7896]
<strong>输出：</strong>2
<strong>解释：
</strong>12 是 2 位数字（位数为偶数）&nbsp;
345 是 3 位数字（位数为奇数）&nbsp;&nbsp;
2 是 1 位数字（位数为奇数）&nbsp;
6 是 1 位数字 位数为奇数）&nbsp;
7896 是 4 位数字（位数为偶数）&nbsp;&nbsp;
因此只有 12 和 7896 是位数为偶数的数字
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [555,901,482,1771]
<strong>输出：</strong>1 
<strong>解释： </strong>
只有 1771 是位数为偶数的数字。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学

## 提示

1. How to compute the number of digits of a number ?
2. Divide the number by 10 again and again to get the number of digits.

## 示例

```
[12,345,2,6,7896]
[555,901,482,1771]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findNumbers(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findNumbers(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
```

### C

```c
int findNumbers(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindNumbers(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    
};
```

### TypeScript

```typescript
function findNumbers(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findNumbers($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findNumbers(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findNumbers(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findNumbers(List<int> nums) {
    
  }
}
```

### Go

```golang
func findNumbers(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_numbers(nums)
    
end
```

### Scala

```scala
object Solution {
    def findNumbers(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_numbers(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-numbers nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_numbers(Nums :: [integer()]) -> integer().
find_numbers(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_numbers(nums :: [integer]) :: integer
  def find_numbers(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findNumbers(nums: Array<Int64>): Int64 {

    }
}
```

