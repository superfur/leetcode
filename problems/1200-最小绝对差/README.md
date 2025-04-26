# 1200. 最小绝对差

## 题目描述

<p>给你个整数数组&nbsp;<code>arr</code>，其中每个元素都 <strong>不相同</strong>。</p>

<p>请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。</p>

<p>每对元素对 <code>[a,b</code>] 如下：</p>

<ul>
	<li><code>a ,&nbsp;b</code>&nbsp;均为数组&nbsp;<code>arr</code>&nbsp;中的元素</li>
	<li><code>a &lt; b</code></li>
	<li><code>b - a</code>&nbsp;等于 <code>arr</code> 中任意两个元素的最小绝对差</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [4,2,1,3]
<strong>输出：</strong>[[1,2],[2,3],[3,4]]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,3,6,10,15]
<strong>输出：</strong>[[1,3]]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,8,-10,23,19,-4,-14,27]
<strong>输出：</strong>[[-14,-10],[19,23],[23,27]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>-10^6 &lt;= arr[i] &lt;= 10^6</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Find the minimum absolute difference between two elements in the array.
2. The minimum absolute difference must be a difference between two consecutive elements in the sorted array.

## 示例

```
[4,2,1,3]
[1,3,6,10,15]
[3,8,-10,23,19,-4,-14,27]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** minimumAbsDifference(int* arr, int arrSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> MinimumAbsDifference(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[][]}
 */
var minimumAbsDifference = function(arr) {
    
};
```

### TypeScript

```typescript
function minimumAbsDifference(arr: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[][]
     */
    function minimumAbsDifference($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumAbsDifference(_ arr: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumAbsDifference(arr: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> minimumAbsDifference(List<int> arr) {
    
  }
}
```

### Go

```golang
func minimumAbsDifference(arr []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[][]}
def minimum_abs_difference(arr)
    
end
```

### Scala

```scala
object Solution {
    def minimumAbsDifference(arr: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_abs_difference(arr: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-abs-difference arr)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec minimum_abs_difference(Arr :: [integer()]) -> [[integer()]].
minimum_abs_difference(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_abs_difference(arr :: [integer]) :: [[integer]]
  def minimum_abs_difference(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumAbsDifference(arr: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

