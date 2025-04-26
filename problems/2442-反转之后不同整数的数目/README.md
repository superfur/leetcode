# 2442. 反转之后不同整数的数目

## 题目描述

<p>给你一个由 <strong>正</strong> 整数组成的数组 <code>nums</code> 。</p>

<p>你必须取出数组中的每个整数，<strong>反转其中每个数位</strong>，并将反转后得到的数字添加到数组的末尾。这一操作只针对 <code>nums</code> 中原有的整数执行。</p>

<p>返回结果数组中 <strong>不同</strong> 整数的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,13,10,12,31]
<strong>输出：</strong>6
<strong>解释：</strong>反转每个数字后，结果数组是 [1,13,10,12,31,<em><strong>1,31,1,21,13</strong></em>] 。
反转后得到的数字添加到数组的末尾并按斜体加粗表示。注意对于整数 10 ，反转之后会变成 01 ，即 1 。
数组中不同整数的数目为 6（数字 1、10、12、13、21 和 31）。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,2,2]
<strong>输出：</strong>1
<strong>解释：</strong>反转每个数字后，结果数组是 [2,2,2,<em><strong>2,2,2</strong></em>] 。
数组中不同整数的数目为 1（数字 2）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 数学
- 计数

## 提示

1. What data structure allows us to insert numbers and find the number of distinct numbers in it?
2. Try using a set, insert all the numbers and their reverse into it, and return its size.

## 示例

```
[1,13,10,12,31]
[2,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countDistinctIntegers(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int countDistinctIntegers(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
```

### C

```c
int countDistinctIntegers(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountDistinctIntegers(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var countDistinctIntegers = function(nums) {
    
};
```

### TypeScript

```typescript
function countDistinctIntegers(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function countDistinctIntegers($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countDistinctIntegers(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countDistinctIntegers(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countDistinctIntegers(List<int> nums) {
    
  }
}
```

### Go

```golang
func countDistinctIntegers(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def count_distinct_integers(nums)
    
end
```

### Scala

```scala
object Solution {
    def countDistinctIntegers(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_distinct_integers(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-distinct-integers nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_distinct_integers(Nums :: [integer()]) -> integer().
count_distinct_integers(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_distinct_integers(nums :: [integer]) :: integer
  def count_distinct_integers(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countDistinctIntegers(nums: Array<Int64>): Int64 {

    }
}
```

