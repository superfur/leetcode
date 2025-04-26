# 1043. 分隔数组以得到最大和

## 题目描述

<p>给你一个整数数组 <code>arr</code>，请你将该数组分隔为长度 <strong>最多 </strong>为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。</p>

<p>返回将数组分隔变换后能够得到的元素最大和。本题所用到的测试用例会确保答案是一个 32 位整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,15,7,9,2,5,10], k = 3
<strong>输出：</strong>84
<strong>解释：</strong>数组变为 [15,15,15,9,10,10,10]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
<strong>输出：</strong>83
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [1], k = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 500</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Think dynamic programming:  dp[i] will be the answer for array A[0], ..., A[i-1].
2. For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .

## 示例

```
[1,15,7,9,2,5,10]
3
[1,4,1,5,7,3,6,1,9,9,3]
4
[1]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
```

### C

```c
int maxSumAfterPartitioning(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxSumAfterPartitioning(int[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var maxSumAfterPartitioning = function(arr, k) {
    
};
```

### TypeScript

```typescript
function maxSumAfterPartitioning(arr: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function maxSumAfterPartitioning($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxSumAfterPartitioning(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxSumAfterPartitioning(arr: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxSumAfterPartitioning(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func maxSumAfterPartitioning(arr []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def max_sum_after_partitioning(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def maxSumAfterPartitioning(arr: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_sum_after_partitioning(arr: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-sum-after-partitioning arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_sum_after_partitioning(Arr :: [integer()], K :: integer()) -> integer().
max_sum_after_partitioning(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_sum_after_partitioning(arr :: [integer], k :: integer) :: integer
  def max_sum_after_partitioning(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxSumAfterPartitioning(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

