# 1191. K 次串联后最大子数组之和

## 题目描述

<p>给定一个整数数组&nbsp;<code>arr</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，通过重复&nbsp;<code>k</code>&nbsp;次来修改数组。</p>

<p>例如，如果&nbsp;<code>arr = [1, 2]</code>&nbsp;，<meta charset="UTF-8" />&nbsp;<code>k = 3</code>&nbsp;，那么修改后的数组将是 <code>[1, 2, 1, 2, 1, 2]</code> 。</p>

<p>返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 <code>0</code>，在这种情况下它的总和也是 <code>0</code>。</p>

<p>由于&nbsp;<strong>结果可能会很大</strong>，需要返回的<meta charset="UTF-8" />&nbsp;<code>10<sup>9</sup>&nbsp;+ 7</code>&nbsp;的&nbsp;<strong>模</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2], k = 3
<strong>输出：</strong>9
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,-2,1], k = 5
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [-1,-2], k = 7
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. How to solve the problem for k=1 ?
2. Use Kadane's algorithm for k=1.
3. What are the possible cases for the answer ?
4. The answer is the maximum between, the answer for k=1, the sum of the whole array multiplied by k, or the maximum suffix sum plus the maximum prefix sum plus (k-2) multiplied by the whole array sum for k > 1.

## 示例

```
[1,2]
3
[1,-2,1]
5
[-1,-2]
7
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int kConcatenationMaxSum(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int kConcatenationMaxSum(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
```

### C

```c
int kConcatenationMaxSum(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int KConcatenationMaxSum(int[] arr, int k) {
        
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
var kConcatenationMaxSum = function(arr, k) {
    
};
```

### TypeScript

```typescript
function kConcatenationMaxSum(arr: number[], k: number): number {
    
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
    function kConcatenationMaxSum($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kConcatenationMaxSum(_ arr: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kConcatenationMaxSum(arr: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int kConcatenationMaxSum(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func kConcatenationMaxSum(arr []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def k_concatenation_max_sum(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def kConcatenationMaxSum(arr: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn k_concatenation_max_sum(arr: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (k-concatenation-max-sum arr k)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec k_concatenation_max_sum(Arr :: [integer()], K :: integer()) -> integer().
k_concatenation_max_sum(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec k_concatenation_max_sum(arr :: [integer], k :: integer) :: integer
  def k_concatenation_max_sum(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kConcatenationMaxSum(arr: Array<Int64>, k: Int64): Int64 {

    }
}
```

