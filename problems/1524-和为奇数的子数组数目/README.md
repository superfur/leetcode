# 1524. 和为奇数的子数组数目

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;。请你返回和为 <strong>奇数</strong>&nbsp;的子数组数目。</p>

<p>由于答案可能会很大，请你将结果对&nbsp;<code>10^9 + 7</code>&nbsp;取余后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [1,3,5]
<strong>输出：</strong>4
<strong>解释：</strong>所有的子数组为 [[1],[1,3],[1,3,5],[3],[3,5],[5]] 。
所有子数组的和为 [1,4,9,3,8,5].
奇数和包括 [1,9,3,5] ，所以答案为 4 。
</pre>

<p><strong>示例 2 ：</strong></p>

<pre><strong>输入：</strong>arr = [2,4,6]
<strong>输出：</strong>0
<strong>解释：</strong>所有子数组为 [[2],[2,4],[2,4,6],[4],[4,6],[6]] 。
所有子数组和为 [2,6,12,4,10,6] 。
所有子数组和都是偶数，所以答案为 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,3,4,5,6,7]
<strong>输出：</strong>16
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [100,100,99,99]
<strong>输出：</strong>4
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [7]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 动态规划
- 前缀和

## 提示

1. Can we use the accumulative sum to keep track of all the odd-sum sub-arrays ?
2. if the current accu sum is odd, we care only about previous even accu sums and vice versa.

## 示例

```
[1,3,5]
[2,4,6]
[1,2,3,4,5,6,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int numOfSubarrays(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
```

### C

```c
int numOfSubarrays(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumOfSubarrays(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var numOfSubarrays = function(arr) {
    
};
```

### TypeScript

```typescript
function numOfSubarrays(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numOfSubarrays($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numOfSubarrays(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numOfSubarrays(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numOfSubarrays(List<int> arr) {
    
  }
}
```

### Go

```golang
func numOfSubarrays(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def num_of_subarrays(arr)
    
end
```

### Scala

```scala
object Solution {
    def numOfSubarrays(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-of-subarrays arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_of_subarrays(Arr :: [integer()]) -> integer().
num_of_subarrays(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_of_subarrays(arr :: [integer]) :: integer
  def num_of_subarrays(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numOfSubarrays(arr: Array<Int64>): Int64 {

    }
}
```

