# 2097. 合法重新排列数对

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>pairs</code>&nbsp;，其中&nbsp;<code>pairs[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;。如果 <code>pairs</code>&nbsp;的一个重新排列，满足对每一个下标 <code>i</code> （&nbsp;<code>1 &lt;= i &lt; pairs.length</code>&nbsp;）都有&nbsp;<code>end<sub>i-1</sub> == start<sub>i</sub></code><sub> </sub>，那么我们就认为这个重新排列是&nbsp;<code>pairs</code> 的一个 <strong>合法重新排列</strong> 。</p>

<p>请你返回 <strong>任意一个</strong>&nbsp;<code>pairs</code> 的合法重新排列。</p>

<p><b>注意：</b>数据保证至少存在一个 <code>pairs</code>&nbsp;的合法重新排列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>pairs = [[5,1],[4,5],[11,9],[9,4]]
<b>输出：</b>[[11,9],[9,4],[4,5],[5,1]]
<strong>解释：
</strong>输出的是一个合法重新排列，因为每一个 end<sub>i-1</sub> 都等于 start<sub>i</sub>&nbsp;。
end<sub>0</sub> = 9 == 9 = start<sub>1</sub> 
end<sub>1</sub> = 4 == 4 = start<sub>2</sub>
end<sub>2</sub> = 5 == 5 = start<sub>3</sub>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>pairs = [[1,3],[3,2],[2,1]]
<b>输出：</b>[[1,3],[3,2],[2,1]]
<strong>解释：</strong>
输出的是一个合法重新排列，因为每一个 end<sub>i-1</sub> 都等于 start<sub>i</sub>&nbsp;。
end<sub>0</sub> = 3 == 3 = start<sub>1</sub>
end<sub>1</sub> = 2 == 2 = start<sub>2</sub>
重新排列后的数组 [[2,1],[1,3],[3,2]] 和 [[3,2],[2,1],[1,3]] 都是合法的。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>pairs = [[1,2],[1,3],[2,1]]
<b>输出：</b>[[1,2],[2,1],[1,3]]
<strong>解释：</strong>
输出的是一个合法重新排列，因为每一个 end<sub>i-1</sub> 都等于 start<sub>i</sub>&nbsp;。
end<sub>0</sub> = 2 == 2 = start<sub>1</sub>
end<sub>1</sub> = 1 == 1 = start<sub>2</sub>
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= pairs.length &lt;= 10<sup>5</sup></code></li>
	<li><code>pairs[i].length == 2</code></li>
	<li><code>0 &lt;= start<sub>i</sub>, end<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>start<sub>i</sub> != end<sub>i</sub></code></li>
	<li><code>pairs</code>&nbsp;中不存在一模一样的数对。</li>
	<li>至少 <strong>存在</strong> 一个合法的&nbsp;<code>pairs</code>&nbsp;重新排列。</li>
</ul>


## 难度

Hard

## 标签

- 深度优先搜索
- 图
- 欧拉回路

## 提示

1. Could you convert this into a graph problem?
2. Consider the pairs as edges and each number as a node.
3. We have to find an Eulerian path of this graph. Hierholzer’s algorithm can be used.

## 示例

```
[[5,1],[4,5],[11,9],[9,4]]
[[1,3],[3,2],[2,1]]
[[1,2],[1,3],[2,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] validArrangement(int[][] pairs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** validArrangement(int** pairs, int pairsSize, int* pairsColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ValidArrangement(int[][] pairs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} pairs
 * @return {number[][]}
 */
var validArrangement = function(pairs) {
    
};
```

### TypeScript

```typescript
function validArrangement(pairs: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $pairs
     * @return Integer[][]
     */
    function validArrangement($pairs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validArrangement(_ pairs: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validArrangement(pairs: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> validArrangement(List<List<int>> pairs) {
    
  }
}
```

### Go

```golang
func validArrangement(pairs [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} pairs
# @return {Integer[][]}
def valid_arrangement(pairs)
    
end
```

### Scala

```scala
object Solution {
    def validArrangement(pairs: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_arrangement(pairs: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (valid-arrangement pairs)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec valid_arrangement(Pairs :: [[integer()]]) -> [[integer()]].
valid_arrangement(Pairs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_arrangement(pairs :: [[integer]]) :: [[integer]]
  def valid_arrangement(pairs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validArrangement(pairs: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

