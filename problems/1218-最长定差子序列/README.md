# 1218. 最长定差子序列

## 题目描述

<p>给你一个整数数组 <code>arr</code> 和一个整数 <code>difference</code>，请你找出并返回 <code>arr</code> 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 <code>difference</code> 。</p>

<p><strong>子序列</strong> 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 <code>arr</code> 派生出来的序列。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4], difference = 1
<strong>输出：</strong>4
<strong>解释：</strong>最长的等差子序列是 [1,2,3,4]。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,3,5,7], difference = 1
<strong>输出：</strong>1
<strong>解释：</strong>最长的等差子序列是任意单个元素。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,5,7,8,5,3,4,2,1], difference = -2
<strong>输出：</strong>4
<strong>解释：</strong>最长的等差子序列是 [7,5,3,1]。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= arr.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> <= arr[i], difference <= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 动态规划

## 提示

1. Use dynamic programming.
2. Let dp[i] be the maximum length of a subsequence of the given difference whose last element is i.
3. dp[i] = 1 + dp[i-k]

## 示例

```
[1,2,3,4]
1
[1,3,5,7]
1
[1,5,7,8,5,3,4,2,1]
-2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestSubsequence(int[] arr, int difference) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
```

### C

```c
int longestSubsequence(int* arr, int arrSize, int difference) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestSubsequence(int[] arr, int difference) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} difference
 * @return {number}
 */
var longestSubsequence = function(arr, difference) {
    
};
```

### TypeScript

```typescript
function longestSubsequence(arr: number[], difference: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $difference
     * @return Integer
     */
    function longestSubsequence($arr, $difference) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestSubsequence(_ arr: [Int], _ difference: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestSubsequence(arr: IntArray, difference: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestSubsequence(List<int> arr, int difference) {
    
  }
}
```

### Go

```golang
func longestSubsequence(arr []int, difference int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} difference
# @return {Integer}
def longest_subsequence(arr, difference)
    
end
```

### Scala

```scala
object Solution {
    def longestSubsequence(arr: Array[Int], difference: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-subsequence arr difference)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_subsequence(Arr :: [integer()], Difference :: integer()) -> integer().
longest_subsequence(Arr, Difference) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_subsequence(arr :: [integer], difference :: integer) :: integer
  def longest_subsequence(arr, difference) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestSubsequence(arr: Array<Int64>, difference: Int64): Int64 {

    }
}
```

