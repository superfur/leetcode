# 2614. 对角线上的质数

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二维整数数组 <code>nums</code> 。</p>

<p>返回位于 <code>nums</code> 至少一条 <strong>对角线</strong> 上的最大 <strong>质数</strong> 。如果任一对角线上均不存在质数，返回<em> 0 。</em></p>

<p>注意：</p>

<ul>
	<li>如果某个整数大于 <code>1</code> ，且不存在除 <code>1</code> 和自身之外的正整数因子，则认为该整数是一个质数。</li>
	<li>如果存在整数 <code>i</code> ，使得&nbsp;<code>nums[i][i] = val</code> 或者&nbsp;<code>nums[i][nums.length - i - 1]= val</code> ，则认为整数 <code>val</code> 位于 <code>nums</code> 的一条对角线上。</li>
</ul>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/03/06/screenshot-2023-03-06-at-45648-pm.png" style="width: 181px; height: 121px;" /></p>

<p>在上图中，一条对角线是 <strong>[1,5,9]</strong> ，而另一条对角线是<strong> [3,5,7]</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[5,6,7],[9,10,11]]
<strong>输出：</strong>11
<strong>解释：</strong>数字 1、3、6、9 和 11 是所有 "位于至少一条对角线上" 的数字。由于 11 是最大的质数，故返回 11 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [[1,2,3],[5,17,7],[9,11,10]]
<strong>输出：</strong>17
<strong>解释：</strong>数字 1、3、9、10 和 17 是所有满足"位于至少一条对角线上"的数字。由于 17 是最大的质数，故返回 17 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 300</code></li>
	<li><code>nums.length == nums<sub>i</sub>.length</code></li>
	<li><code>1 &lt;= nums<span style="">[i][j]</span>&nbsp;&lt;= 4*10<sup>6</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 数学
- 矩阵
- 数论

## 提示

1. Iterate over the diagonals of the matrix and check for each element.
2. Check if the element is prime or not in O(sqrt(n)) time.

## 示例

```
[[1,2,3],[5,6,7],[9,10,11]]
[[1,2,3],[5,17,7],[9,11,10]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int diagonalPrime(vector<vector<int>>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int diagonalPrime(int[][] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def diagonalPrime(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
```

### C

```c
int diagonalPrime(int** nums, int numsSize, int* numsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int DiagonalPrime(int[][] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} nums
 * @return {number}
 */
var diagonalPrime = function(nums) {
    
};
```

### TypeScript

```typescript
function diagonalPrime(nums: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $nums
     * @return Integer
     */
    function diagonalPrime($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func diagonalPrime(_ nums: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun diagonalPrime(nums: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int diagonalPrime(List<List<int>> nums) {
    
  }
}
```

### Go

```golang
func diagonalPrime(nums [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} nums
# @return {Integer}
def diagonal_prime(nums)
    
end
```

### Scala

```scala
object Solution {
    def diagonalPrime(nums: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn diagonal_prime(nums: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (diagonal-prime nums)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec diagonal_prime(Nums :: [[integer()]]) -> integer().
diagonal_prime(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec diagonal_prime(nums :: [[integer]]) :: integer
  def diagonal_prime(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func diagonalPrime(nums: Array<Array<Int64>>): Int64 {

    }
}
```

