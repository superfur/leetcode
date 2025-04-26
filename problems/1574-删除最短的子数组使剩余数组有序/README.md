# 1574. 删除最短的子数组使剩余数组有序

## 题目描述

<p>给你一个整数数组 <code>arr</code>&nbsp;，请你删除一个子数组（可以为空），使得 <code>arr</code>&nbsp;中剩下的元素是 <strong>非递减</strong> 的。</p>

<p>一个子数组指的是原数组中连续的一个子序列。</p>

<p>请你返回满足题目要求的最短子数组的长度。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,10,4,2,3,5]
<strong>输出：</strong>3
<strong>解释：</strong>我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [5,4,3,2,1]
<strong>输出：</strong>4
<strong>解释：</strong>由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3]
<strong>输出：</strong>0
<strong>解释：</strong>数组已经是非递减的了，我们不需要删除任何元素。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>arr = [1]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10^9</code></li>
</ul>


## 难度

Medium

## 标签

- 栈
- 数组
- 双指针
- 二分查找
- 单调栈

## 提示

1. The key is to find the longest non-decreasing subarray starting with the first element or ending with the last element, respectively.
2. After removing some subarray, the result is the concatenation of a sorted prefix and a sorted suffix, where the last element of the prefix is smaller than the first element of the suffix.

## 示例

```
[1,2,3,10,4,2,3,5]
[5,4,3,2,1]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
```

### C

```c
int findLengthOfShortestSubarray(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindLengthOfShortestSubarray(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var findLengthOfShortestSubarray = function(arr) {
    
};
```

### TypeScript

```typescript
function findLengthOfShortestSubarray(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findLengthOfShortestSubarray($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findLengthOfShortestSubarray(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findLengthOfShortestSubarray(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findLengthOfShortestSubarray(List<int> arr) {
    
  }
}
```

### Go

```golang
func findLengthOfShortestSubarray(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def find_length_of_shortest_subarray(arr)
    
end
```

### Scala

```scala
object Solution {
    def findLengthOfShortestSubarray(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_length_of_shortest_subarray(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-length-of-shortest-subarray arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_length_of_shortest_subarray(Arr :: [integer()]) -> integer().
find_length_of_shortest_subarray(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_length_of_shortest_subarray(arr :: [integer]) :: integer
  def find_length_of_shortest_subarray(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findLengthOfShortestSubarray(arr: Array<Int64>): Int64 {

    }
}
```

