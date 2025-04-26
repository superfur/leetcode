# 477. 汉明距离总和

## 题目描述

<p>两个整数的&nbsp;<a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB/475174?fr=aladdin">汉明距离</a> 指的是这两个数字的二进制数对应位不同的数量。</p>

<p>给你一个整数数组 <code>nums</code>，请你计算并返回 <code>nums</code> 中任意两个数之间 <strong>汉明距离的总和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,14,2]
<strong>输出：</strong>6
<strong>解释：</strong>在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [4,14,4]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li>给定输入的对应答案符合 <strong>32-bit</strong> 整数范围</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 数学

## 示例

```
[4,14,2]
[4,14,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int totalHammingDistance(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int totalHammingDistance(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        
```

### C

```c
int totalHammingDistance(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TotalHammingDistance(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var totalHammingDistance = function(nums) {
    
};
```

### TypeScript

```typescript
function totalHammingDistance(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function totalHammingDistance($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func totalHammingDistance(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun totalHammingDistance(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int totalHammingDistance(List<int> nums) {
    
  }
}
```

### Go

```golang
func totalHammingDistance(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def total_hamming_distance(nums)
    
end
```

### Scala

```scala
object Solution {
    def totalHammingDistance(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn total_hamming_distance(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (total-hamming-distance nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec total_hamming_distance(Nums :: [integer()]) -> integer().
total_hamming_distance(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec total_hamming_distance(nums :: [integer]) :: integer
  def total_hamming_distance(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func totalHammingDistance(nums: Array<Int64>): Int64 {

    }
}
```

