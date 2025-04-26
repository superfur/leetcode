# 2607. 使子数组元素和相等

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>arr</code> 和一个整数 <code>k</code> 。数组 <code>arr</code> 是一个循环数组。换句话说，数组中的最后一个元素的下一个元素是数组中的第一个元素，数组中第一个元素的前一个元素是数组中的最后一个元素。</p>

<p>你可以执行下述运算任意次：</p>

<ul>
	<li>选中 <code>arr</code> 中任意一个元素，并使其值加上 <code>1</code> 或减去 <code>1</code> 。</li>
</ul>

<p>执行运算使每个长度为 <code>k</code> 的 <strong>子数组</strong> 的元素总和都相等，返回所需要的最少运算次数。</p>

<p><strong>子数组</strong> 是数组的一个连续部分。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [1,4,1,3], k = 2
<strong>输出：</strong>1
<strong>解释：</strong>在下标为 1 的元素那里执行一次运算，使其等于 3 。
执行运算后，数组变为 [1,3,1,3] 。
- 0 处起始的子数组为 [1, 3] ，元素总和为 4 
- 1 处起始的子数组为 [3, 1] ，元素总和为 4 
- 2 处起始的子数组为 [1, 3] ，元素总和为 4 
- 3 处起始的子数组为 [3, 1] ，元素总和为 4 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [2,5,5,7], k = 3
<strong>输出：</strong>5
<strong>解释：</strong>在下标为 0 的元素那里执行三次运算，使其等于 5 。在下标为 3 的元素那里执行两次运算，使其等于 5 。
执行运算后，数组变为 [5,5,5,5] 。
- 0 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 1 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 2 处起始的子数组为 [5, 5, 5] ，元素总和为 15
- 3 处起始的子数组为 [5, 5, 5] ，元素总和为 15
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 数学
- 数论
- 排序

## 提示

1. Think about gcd(n, k). How will it help to calculate the answer?
2. indices i and j are in the same group if gcd(n, k) mod i = gcd(n, k) mod j. Each group should have equal elements. Think about the minimum number of operations for each group
3. The minimum number of operations for each group equals the summation of differences between the elements and the median of elements inside the group.

## 示例

```
[1,4,1,3]
2
[2,5,5,7]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long makeSubKSumEqual(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public long makeSubKSumEqual(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def makeSubKSumEqual(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        
```

### C

```c
long long makeSubKSumEqual(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public long MakeSubKSumEqual(int[] arr, int k) {
        
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
var makeSubKSumEqual = function(arr, k) {
    
};
```

### TypeScript

```typescript
function makeSubKSumEqual(arr: number[], k: number): number {
    
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
    function makeSubKSumEqual($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func makeSubKSumEqual(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun makeSubKSumEqual(arr: IntArray, k: Int): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int makeSubKSumEqual(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func makeSubKSumEqual(arr []int, k int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def make_sub_k_sum_equal(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def makeSubKSumEqual(arr: Array[Int], k: Int): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn make_sub_k_sum_equal(arr: Vec<i32>, k: i32) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (make-sub-k-sum-equal arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec make_sub_k_sum_equal(Arr :: [integer()], K :: integer()) -> integer().
make_sub_k_sum_equal(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec make_sub_k_sum_equal(arr :: [integer], k :: integer) :: integer
  def make_sub_k_sum_equal(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func makeSubKSumEqual(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

