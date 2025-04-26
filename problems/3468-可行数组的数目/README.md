# 3468. 可行数组的数目

## 题目描述

<p>给你一个长度为 <code>n</code> 的数组 <code>original</code> 和一个长度为 <code>n x 2</code> 的二维数组 <code>bounds</code>，其中 <code>bounds[i] = [u<sub>i</sub>, v<sub>i</sub>]</code>。</p>

<p>你需要找到长度为 <code>n</code>&nbsp;且满足以下条件的&nbsp;<strong>可能的&nbsp;</strong>数组 <code>copy</code> 的数量：</p>

<ol>
	<li>对于 <code>1 &lt;= i &lt;= n - 1</code>&nbsp;，都有&nbsp;<code>(copy[i] - copy[i - 1]) == (original[i] - original[i - 1])</code>&nbsp;。</li>
	<li>对于 <code>0 &lt;= i &lt;= n - 1</code>&nbsp;，都有&nbsp;<code>u<sub>i</sub> &lt;= copy[i] &lt;= v<sub>i</sub></code><sub>&nbsp;</sub>。</li>
</ol>

<p>返回满足这些条件的数组数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>可能的数组为：</p>

<ul>
	<li><code>[1, 2, 3, 4]</code></li>
	<li><code>[2, 3, 4, 5]</code></li>
</ul>
</div>

<p><strong class="example">示例 2</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]</span></p>

<p><strong>输出：</strong><span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>可能的数组为：</p>

<ul>
	<li><code>[1, 2, 3, 4]</code></li>
	<li><code>[2, 3, 4, 5]</code></li>
	<li><code>[3, 4, 5, 6]</code></li>
	<li><code>[4, 5, 6, 7]</code></li>
</ul>
</div>

<p><strong class="example">示例 3</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>没有可行的数组。</p>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>2 &lt;= n == original.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= original[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>bounds.length == n</code></li>
	<li><code>bounds[i].length == 2</code></li>
	<li><code>1 &lt;= bounds[i][0] &lt;= bounds[i][1] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. <code>copy[0]</code> uniquely determines all other values.
2. Possible values for <code>copy[0]</code> are in <code>[u[0], v[0]]</code>.
3. From left to right, compute valid ranges for each index by intersecting bounds with the previous range.
4. The answer is the size of the valid range for the last index.

## 示例

```
[1,2,3,4]
[[1,2],[2,3],[3,4],[4,5]]
[1,2,3,4]
[[1,10],[2,9],[3,8],[4,7]]
[1,2,1,2]
[[1,1],[2,3],[3,3],[2,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countArrays(vector<int>& original, vector<vector<int>>& bounds) {
        
    }
};
```

### Java

```java
class Solution {
    public int countArrays(int[] original, int[][] bounds) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countArrays(self, original, bounds):
        """
        :type original: List[int]
        :type bounds: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        
```

### C

```c
int countArrays(int* original, int originalSize, int** bounds, int boundsSize, int* boundsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountArrays(int[] original, int[][] bounds) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} original
 * @param {number[][]} bounds
 * @return {number}
 */
var countArrays = function(original, bounds) {
    
};
```

### TypeScript

```typescript
function countArrays(original: number[], bounds: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $original
     * @param Integer[][] $bounds
     * @return Integer
     */
    function countArrays($original, $bounds) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countArrays(_ original: [Int], _ bounds: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countArrays(original: IntArray, bounds: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countArrays(List<int> original, List<List<int>> bounds) {
    
  }
}
```

### Go

```golang
func countArrays(original []int, bounds [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} original
# @param {Integer[][]} bounds
# @return {Integer}
def count_arrays(original, bounds)
    
end
```

### Scala

```scala
object Solution {
    def countArrays(original: Array[Int], bounds: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_arrays(original: Vec<i32>, bounds: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-arrays original bounds)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_arrays(Original :: [integer()], Bounds :: [[integer()]]) -> integer().
count_arrays(Original, Bounds) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_arrays(original :: [integer], bounds :: [[integer]]) :: integer
  def count_arrays(original, bounds) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countArrays(original: Array<Int64>, bounds: Array<Array<Int64>>): Int64 {

    }
}
```

