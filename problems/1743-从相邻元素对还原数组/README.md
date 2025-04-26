# 1743. 从相邻元素对还原数组

## 题目描述

<p>存在一个由 <code>n</code> 个不同元素组成的整数数组 <code>nums</code> ，但你已经记不清具体内容。好在你还记得 <code>nums</code> 中的每一对相邻元素。</p>

<p>给你一个二维整数数组 <code>adjacentPairs</code> ，大小为 <code>n - 1</code> ，其中每个 <code>adjacentPairs[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> 表示元素 <code>u<sub>i</sub></code> 和 <code>v<sub>i</sub></code> 在 <code>nums</code> 中相邻。</p>

<p>题目数据保证所有由元素 <code>nums[i]</code> 和 <code>nums[i+1]</code> 组成的相邻元素对都存在于 <code>adjacentPairs</code> 中，存在形式可能是 <code>[nums[i], nums[i+1]]</code> ，也可能是 <code>[nums[i+1], nums[i]]</code> 。这些相邻元素对可以 <strong>按任意顺序</strong> 出现。</p>

<p>返回 <strong>原始数组</strong><em> </em><code>nums</code><em> </em>。如果存在多种解答，返回 <strong>其中任意一个</strong> 即可。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>adjacentPairs = [[2,1],[3,4],[3,2]]
<strong>输出：</strong>[1,2,3,4]
<strong>解释：</strong>数组的所有相邻元素对都在 adjacentPairs 中。
特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>adjacentPairs = [[4,-2],[1,4],[-3,1]]
<strong>输出：</strong>[-2,4,1,-3]
<strong>解释：</strong>数组中可能存在负数。
另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>adjacentPairs = [[100000,-100000]]
<strong>输出：</strong>[100000,-100000]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>nums.length == n</code></li>
	<li><code>adjacentPairs.length == n - 1</code></li>
	<li><code>adjacentPairs[i].length == 2</code></li>
	<li><code>2 <= n <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> <= nums[i], u<sub>i</sub>, v<sub>i</sub> <= 10<sup>5</sup></code></li>
	<li>题目数据保证存在一些以 <code>adjacentPairs</code> 作为元素对的数组 <code>nums</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 数组
- 哈希表

## 提示

1. Find the first element of nums - it will only appear once in adjacentPairs.
2. The adjacent pairs are like edges of a graph. Perform a depth-first search from the first element.

## 示例

```
[[2,1],[3,4],[3,2]]
[[4,-2],[1,4],[-3,1]]
[[100000,-100000]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] restoreArray(int[][] adjacentPairs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* restoreArray(int** adjacentPairs, int adjacentPairsSize, int* adjacentPairsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RestoreArray(int[][] adjacentPairs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} adjacentPairs
 * @return {number[]}
 */
var restoreArray = function(adjacentPairs) {
    
};
```

### TypeScript

```typescript
function restoreArray(adjacentPairs: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $adjacentPairs
     * @return Integer[]
     */
    function restoreArray($adjacentPairs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func restoreArray(_ adjacentPairs: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun restoreArray(adjacentPairs: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> restoreArray(List<List<int>> adjacentPairs) {
    
  }
}
```

### Go

```golang
func restoreArray(adjacentPairs [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} adjacent_pairs
# @return {Integer[]}
def restore_array(adjacent_pairs)
    
end
```

### Scala

```scala
object Solution {
    def restoreArray(adjacentPairs: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn restore_array(adjacent_pairs: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (restore-array adjacentPairs)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec restore_array(AdjacentPairs :: [[integer()]]) -> [integer()].
restore_array(AdjacentPairs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec restore_array(adjacent_pairs :: [[integer]]) :: [integer]
  def restore_array(adjacent_pairs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func restoreArray(adjacentPairs: Array<Array<Int64>>): Array<Int64> {

    }
}
```

