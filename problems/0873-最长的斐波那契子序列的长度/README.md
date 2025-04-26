# 873. 最长的斐波那契子序列的长度

## 题目描述

<p>如果序列 <code>X_1, X_2, ..., X_n</code> 满足下列条件，就说它是 <em>斐波那契式 </em>的：</p>

<ul>
	<li><code>n >= 3</code></li>
	<li>对于所有 <code>i + 2 <= n</code>，都有 <code>X_i + X_{i+1} = X_{i+2}</code></li>
</ul>

<p>给定一个<strong>严格递增</strong>的正整数数组形成序列 arr ，找到 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.600000381469727px"><span style="caret-color:#c7254e"><span style="background-color:#f9f2f4">arr</span></span></span></font></font> 中最长的斐波那契式的子序列的长度。如果一个不存在，返回  0 。</p>

<p><em>（回想一下，子序列是从原序列 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.600000381469727px"><span style="caret-color:#c7254e"><span style="background-color:#f9f2f4">arr</span></span></span></font></font> 中派生出来的，它从 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.600000381469727px"><span style="caret-color:#c7254e"><span style="background-color:#f9f2f4">arr</span></span></span></font></font> 中删掉任意数量的元素（也可以不删），而不改变其余元素的顺序。例如， <code>[3, 5, 8]</code> 是 <code>[3, 4, 5, 6, 7, 8]</code> 的一个子序列）</em></p>

<p> </p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入: </strong>arr =<strong> </strong>[1,2,3,4,5,6,7,8]
<strong>输出: </strong>5
<strong>解释: </strong>最长的斐波那契式子序列为 [1,2,3,5,8] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>arr =<strong> </strong>[1,3,7,11,12,14,18]
<strong>输出: </strong>3
<strong>解释</strong>: 最长的斐波那契式子序列有 [1,11,12]、[3,11,14] 以及 [7,11,18] 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= arr.length <= 1000</code></li>
	<li>
	<p><code>1 <= arr[i] < arr[i + 1] <= 10^9</code></p>
	</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 动态规划

## 提示

1. Can we use dynamic programming here?
2. Consider a sequence ending at index <code>i</code. The previous two elements must sum to <code>arr[i]</code>, which can be done in linear time per element.

## 示例

```
[1,2,3,4,5,6,7,8]
[1,3,7,11,12,14,18]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
```

### C

```c
int lenLongestFibSubseq(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LenLongestFibSubseq(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var lenLongestFibSubseq = function(arr) {
    
};
```

### TypeScript

```typescript
function lenLongestFibSubseq(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function lenLongestFibSubseq($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func lenLongestFibSubseq(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun lenLongestFibSubseq(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int lenLongestFibSubseq(List<int> arr) {
    
  }
}
```

### Go

```golang
func lenLongestFibSubseq(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def len_longest_fib_subseq(arr)
    
end
```

### Scala

```scala
object Solution {
    def lenLongestFibSubseq(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn len_longest_fib_subseq(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (len-longest-fib-subseq arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec len_longest_fib_subseq(Arr :: [integer()]) -> integer().
len_longest_fib_subseq(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec len_longest_fib_subseq(arr :: [integer]) :: integer
  def len_longest_fib_subseq(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func lenLongestFibSubseq(arr: Array<Int64>): Int64 {

    }
}
```

