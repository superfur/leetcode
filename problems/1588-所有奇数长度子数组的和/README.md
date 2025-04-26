# 1588. 所有奇数长度子数组的和

## 题目描述

<p>给你一个正整数数组&nbsp;<code>arr</code>&nbsp;，请你计算所有可能的奇数长度子数组的和。</p>

<p><strong>子数组</strong> 定义为原数组中的一个连续子序列。</p>

<p>请你返回 <code>arr</code>&nbsp;中 <strong>所有奇数长度子数组的和</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,4,2,5,3]
<strong>输出：</strong>58
<strong>解释：</strong>所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2]
<strong>输出：</strong>3
<strong>解释：</strong>总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [10,11,12]
<strong>输出：</strong>66
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<p>你可以设计一个 O(n) 时间复杂度的算法解决此问题吗？</p>


## 难度

Easy

## 标签

- 数组
- 数学
- 前缀和

## 提示

1. You can brute force – try every (i,j) pair, and if the length is odd, go through and add the sum to the answer.

## 示例

```
[1,4,2,5,3]
[1,2]
[10,11,12]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int sumOddLengthSubarrays(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
```

### C

```c
int sumOddLengthSubarrays(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int SumOddLengthSubarrays(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    
};
```

### TypeScript

```typescript
function sumOddLengthSubarrays(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function sumOddLengthSubarrays($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func sumOddLengthSubarrays(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun sumOddLengthSubarrays(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int sumOddLengthSubarrays(List<int> arr) {
    
  }
}
```

### Go

```golang
func sumOddLengthSubarrays(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def sum_odd_length_subarrays(arr)
    
end
```

### Scala

```scala
object Solution {
    def sumOddLengthSubarrays(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn sum_odd_length_subarrays(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (sum-odd-length-subarrays arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec sum_odd_length_subarrays(Arr :: [integer()]) -> integer().
sum_odd_length_subarrays(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec sum_odd_length_subarrays(arr :: [integer]) :: integer
  def sum_odd_length_subarrays(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func sumOddLengthSubarrays(arr: Array<Int64>): Int64 {

    }
}
```

