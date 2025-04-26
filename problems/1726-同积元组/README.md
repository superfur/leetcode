# 1726. 同积元组

## 题目描述

<p>给你一个由 <strong>不同</strong> 正整数组成的数组 <code>nums</code> ，请你返回满足&nbsp;<code>a * b = c * d</code> 的元组<em> </em><code>(a, b, c, d)</code><em> </em>的数量。其中 <code>a</code>、<code>b</code>、<code>c</code> 和 <code>d</code> 都是 <code>nums</code> 中的元素，且 <code>a != b != c != d</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [2,3,4,6]
<strong>输出：</strong>8
<strong>解释：</strong>存在 8 个满足题意的元组：
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,2,4,5,10]
<strong>输出：</strong>16
<strong>解释：</strong>存在 16 个满足题意的元组：
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> 中的所有元素 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Note that all of the integers are distinct. This means that each time a product is formed it must be formed by two unique integers.
2. Count the frequency of each product of 2 distinct numbers. Then calculate the permutations formed.

## 示例

```
[2,3,4,6]
[1,2,4,5,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int tupleSameProduct(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
```

### C

```c
int tupleSameProduct(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TupleSameProduct(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var tupleSameProduct = function(nums) {
    
};
```

### TypeScript

```typescript
function tupleSameProduct(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function tupleSameProduct($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func tupleSameProduct(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun tupleSameProduct(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int tupleSameProduct(List<int> nums) {
    
  }
}
```

### Go

```golang
func tupleSameProduct(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def tuple_same_product(nums)
    
end
```

### Scala

```scala
object Solution {
    def tupleSameProduct(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (tuple-same-product nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec tuple_same_product(Nums :: [integer()]) -> integer().
tuple_same_product(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec tuple_same_product(nums :: [integer]) :: integer
  def tuple_same_product(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func tupleSameProduct(nums: Array<Int64>): Int64 {

    }
}
```

