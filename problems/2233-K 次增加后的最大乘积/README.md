# 2233. K 次增加后的最大乘积

## 题目描述

<p>给你一个非负整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。每次操作，你可以选择&nbsp;<code>nums</code>&nbsp;中 <strong>任一</strong>&nbsp;元素并将它 <strong>增加</strong>&nbsp;<code>1</code>&nbsp;。</p>

<p>请你返回 <strong>至多</strong>&nbsp;<code>k</code>&nbsp;次操作后，能得到的<em>&nbsp;</em><code>nums</code>的&nbsp;<strong>最大乘积</strong>&nbsp;。由于答案可能很大，请你将答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;取余后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [0,4], k = 5
<b>输出：</b>20
<b>解释：</b>将第一个数增加 5 次。
得到 nums = [5, 4] ，乘积为 5 * 4 = 20 。
可以证明 20 是能得到的最大乘积，所以我们返回 20 。
存在其他增加 nums 的方法，也能得到最大乘积。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [6,3,3,2], k = 2
<b>输出：</b>216
<b>解释：</b>将第二个数增加 1 次，将第四个数增加 1 次。
得到 nums = [6, 4, 3, 3] ，乘积为 6 * 4 * 3 * 3 = 216 。
可以证明 216 是能得到的最大乘积，所以我们返回 216 。
存在其他增加 nums 的方法，也能得到最大乘积。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, k &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. If you can increment only once, which number should you increment?
2. We should always prioritize the smallest number. What kind of data structure could we use?
3. Use a min heap to hold all the numbers. Each time we do an operation, replace the top of the heap x by x + 1.

## 示例

```
[0,4]
5
[6,3,3,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maximumProduct(vector<int>& nums, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maximumProduct(int[] nums, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        
```

### C

```c
int maximumProduct(int* nums, int numsSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaximumProduct(int[] nums, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maximumProduct = function(nums, k) {
    
};
```

### TypeScript

```typescript
function maximumProduct(nums: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $k
     * @return Integer
     */
    function maximumProduct($nums, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumProduct(_ nums: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumProduct(nums: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maximumProduct(List<int> nums, int k) {
    
  }
}
```

### Go

```golang
func maximumProduct(nums []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_product(nums, k)
    
end
```

### Scala

```scala
object Solution {
    def maximumProduct(nums: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_product(nums: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-product nums k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec maximum_product(Nums :: [integer()], K :: integer()) -> integer().
maximum_product(Nums, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_product(nums :: [integer], k :: integer) :: integer
  def maximum_product(nums, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumProduct(nums: Array<Int64>, k: Int64): Int64 {

    }
}
```

