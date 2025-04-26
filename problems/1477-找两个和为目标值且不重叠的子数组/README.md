# 1477. 找两个和为目标值且不重叠的子数组

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code> 和一个整数值&nbsp;<code>target</code>&nbsp;。</p>

<p>请你在 <code>arr</code>&nbsp;中找 <strong>两个互不重叠的子数组</strong>&nbsp;且它们的和都等于&nbsp;<code>target</code>&nbsp;。可能会有多种方案，请你返回满足要求的两个子数组长度和的 <strong>最小值</strong> 。</p>

<p>请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 <strong>-1</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [3,2,2,4,3], target = 3
<strong>输出：</strong>2
<strong>解释：</strong>只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [7,3,4,7], target = 7
<strong>输出：</strong>2
<strong>解释：</strong>尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [4,3,2,6,2,3,4], target = 6
<strong>输出：</strong>-1
<strong>解释：</strong>我们只有一个和为 6 的子数组。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [5,5,4,4,5], target = 3
<strong>输出：</strong>-1
<strong>解释：</strong>我们无法找到和为 3 的子数组。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [3,1,1,1,5,1,2,1], target = 3
<strong>输出：</strong>3
<strong>解释：</strong>注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>1 &lt;= target &lt;= 10^8</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 二分查找
- 动态规划
- 滑动窗口

## 提示

1. Let's create two arrays prefix and suffix where prefix[i] is the minimum length of sub-array ends before i and has sum = k, suffix[i] is the minimum length of sub-array starting at or after i and has sum = k.
2. The answer we are searching for is min(prefix[i] + suffix[i]) for all values of i from 0 to n-1 where n == arr.length.
3. If you are still stuck with how to build prefix and suffix, you can store for each index i the length of the sub-array starts at i and has sum = k or infinity otherwise, and you can use it to build both prefix and suffix.

## 示例

```
[3,2,2,4,3]
3
[7,3,4,7]
7
[4,3,2,6,2,3,4]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
```

### C

```c
int minSumOfLengths(int* arr, int arrSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinSumOfLengths(int[] arr, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var minSumOfLengths = function(arr, target) {
    
};
```

### TypeScript

```typescript
function minSumOfLengths(arr: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function minSumOfLengths($arr, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minSumOfLengths(_ arr: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minSumOfLengths(arr: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minSumOfLengths(List<int> arr, int target) {
    
  }
}
```

### Go

```golang
func minSumOfLengths(arr []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def min_sum_of_lengths(arr, target)
    
end
```

### Scala

```scala
object Solution {
    def minSumOfLengths(arr: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_sum_of_lengths(arr: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-sum-of-lengths arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_sum_of_lengths(Arr :: [integer()], Target :: integer()) -> integer().
min_sum_of_lengths(Arr, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_sum_of_lengths(arr :: [integer], target :: integer) :: integer
  def min_sum_of_lengths(arr, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minSumOfLengths(arr: Array<Int64>, target: Int64): Int64 {

    }
}
```

