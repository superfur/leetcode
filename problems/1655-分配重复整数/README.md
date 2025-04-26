# 1655. 分配重复整数

## 题目描述

<p>给你一个长度为&nbsp;<code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;，这个数组中至多有&nbsp;<code>50</code>&nbsp;个不同的值。同时你有 <code>m</code>&nbsp;个顾客的订单 <code>quantity</code>&nbsp;，其中，整数&nbsp;<code>quantity[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;位顾客订单的数目。请你判断是否能将 <code>nums</code>&nbsp;中的整数分配给这些顾客，且满足：</p>

<ul>
	<li>第&nbsp;<code>i</code>&nbsp;位顾客 <strong>恰好&nbsp;</strong>有&nbsp;<code>quantity[i]</code>&nbsp;个整数。</li>
	<li>第&nbsp;<code>i</code>&nbsp;位顾客拿到的整数都是 <strong>相同的</strong>&nbsp;。</li>
	<li>每位顾客都满足上述两个要求。</li>
</ul>

<p>如果你可以分配 <code>nums</code>&nbsp;中的整数满足上面的要求，那么请返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,4], quantity = [2]
<b>输出：</b>false
<strong>解释：</strong>第 0 位顾客没办法得到两个相同的整数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,2,3,3], quantity = [2]
<b>输出：</b>true
<b>解释：</b>第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,1,2,2], quantity = [2,2]
<b>输出：</b>true
<b>解释：</b>第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li><code>m == quantity.length</code></li>
	<li><code>1 &lt;= m &lt;= 10</code></li>
	<li><code>1 &lt;= quantity[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums</code>&nbsp;中至多有&nbsp;<code>50</code>&nbsp;个不同的数字。</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 回溯
- 状态压缩

## 提示

1. Count the frequencies of each number. For example, if nums = [4,4,5,5,5], frequencies = [2,3].
2. Each customer wants all of their numbers to be the same. This means that each customer will be assigned to one number.
3. Use dynamic programming. Iterate through the numbers' frequencies, and choose some subset of customers to be assigned to this number.

## 示例

```
[1,2,3,4]
[2]
[1,2,3,3]
[2]
[1,1,2,2]
[2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canDistribute(vector<int>& nums, vector<int>& quantity) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canDistribute(int[] nums, int[] quantity) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canDistribute(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        
```

### C

```c
bool canDistribute(int* nums, int numsSize, int* quantity, int quantitySize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanDistribute(int[] nums, int[] quantity) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} quantity
 * @return {boolean}
 */
var canDistribute = function(nums, quantity) {
    
};
```

### TypeScript

```typescript
function canDistribute(nums: number[], quantity: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $quantity
     * @return Boolean
     */
    function canDistribute($nums, $quantity) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canDistribute(_ nums: [Int], _ quantity: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canDistribute(nums: IntArray, quantity: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canDistribute(List<int> nums, List<int> quantity) {
    
  }
}
```

### Go

```golang
func canDistribute(nums []int, quantity []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} quantity
# @return {Boolean}
def can_distribute(nums, quantity)
    
end
```

### Scala

```scala
object Solution {
    def canDistribute(nums: Array[Int], quantity: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_distribute(nums: Vec<i32>, quantity: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-distribute nums quantity)
  (-> (listof exact-integer?) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_distribute(Nums :: [integer()], Quantity :: [integer()]) -> boolean().
can_distribute(Nums, Quantity) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_distribute(nums :: [integer], quantity :: [integer]) :: boolean
  def can_distribute(nums, quantity) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canDistribute(nums: Array<Int64>, quantity: Array<Int64>): Bool {

    }
}
```

