# 1343. 大小为 K 且平均值大于等于阈值的子数组数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;和两个整数 <code>k</code>&nbsp;和 <code>threshold</code>&nbsp;。</p>

<p>请你返回长度为 <code>k</code>&nbsp;且平均值大于等于&nbsp;<code>threshold</code>&nbsp;的子数组数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
<strong>输出：</strong>3
<strong>解释：</strong>子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
<strong>输出：</strong>6
<strong>解释：</strong>前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>0 &lt;= threshold &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 滑动窗口

## 提示

1. Start with a window of size K and test its average against the threshold.
2. Keep moving the window by one element maintaining its size k until you cover the whole array. Count the number of windows that have an average greater than or equal to the threshold.

## 示例

```
[2,2,2,2,5,5,5,8]
3
4
[11,13,17,23,29,31,7,5,2,3]
3
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
```

### C

```c
int numOfSubarrays(int* arr, int arrSize, int k, int threshold) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfSubarrays(int[] arr, int k, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @param {number} threshold
 * @return {number}
 */
var numOfSubarrays = function(arr, k, threshold) {
    
};
```

### TypeScript

```typescript
function numOfSubarrays(arr: number[], k: number, threshold: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @param Integer $threshold
     * @return Integer
     */
    function numOfSubarrays($arr, $k, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfSubarrays(_ arr: [Int], _ k: Int, _ threshold: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfSubarrays(arr: IntArray, k: Int, threshold: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfSubarrays(List<int> arr, int k, int threshold) {
    
  }
}
```

### Go

```golang
func numOfSubarrays(arr []int, k int, threshold int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @param {Integer} threshold
# @return {Integer}
def num_of_subarrays(arr, k, threshold)
    
end
```

### Scala

```scala
object Solution {
    def numOfSubarrays(arr: Array[Int], k: Int, threshold: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>, k: i32, threshold: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-subarrays arr k threshold)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_subarrays(Arr :: [integer()], K :: integer(), Threshold :: integer()) -> integer().
num_of_subarrays(Arr, K, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_subarrays(arr :: [integer], k :: integer, threshold :: integer) :: integer
  def num_of_subarrays(arr, k, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfSubarrays(arr: Array<Int64>, k: Int64, threshold: Int64): Int64 {

    }
}
```

