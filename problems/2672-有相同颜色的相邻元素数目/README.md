# 2672. 有相同颜色的相邻元素数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始、长度为 <code>n</code>&nbsp;的数组&nbsp;<code>nums</code>&nbsp;。一开始，所有元素都是 <strong>未染色</strong>&nbsp;（值为 <code>0</code>&nbsp;）的。</p>

<p>给你一个二维整数数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [index<sub>i</sub>, color<sub>i</sub>]</code>&nbsp;。</p>

<p>对于每个操作，你需要将数组 <code>nums</code>&nbsp;中下标为&nbsp;<code>index<sub>i</sub></code>&nbsp;的格子染色为&nbsp;<code>color<sub>i</sub></code>&nbsp;。</p>

<p>请你返回一个长度与 <code>queries</code>&nbsp;相等的数组<em>&nbsp;</em><code>answer</code><em>&nbsp;</em>，其中<em>&nbsp;</em><code>answer[i]</code>是前 <code>i</code>&nbsp;个操作&nbsp;<strong>之后</strong>&nbsp;，相邻元素颜色相同的数目。</p>

<p>更正式的，<code>answer[i]</code>&nbsp;是执行完前 <code>i</code>&nbsp;个操作后，<code>0 &lt;= j &lt; n - 1</code>&nbsp;的下标 <code>j</code>&nbsp;中，满足&nbsp;<code>nums[j] == nums[j + 1]</code> 且&nbsp;<code>nums[j] != 0</code>&nbsp;的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>n = 4, queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]
<b>输出：</b>[0,1,1,0,2]
<b>解释：</b>一开始数组 nums = [0,0,0,0] ，0 表示数组中还没染色的元素。
- 第 1 个操作后，nums = [2,0,0,0] 。相邻元素颜色相同的数目为 0 。
- 第 2 个操作后，nums = [2,2,0,0] 。相邻元素颜色相同的数目为 1 。
- 第 3 个操作后，nums = [2,2,0,1] 。相邻元素颜色相同的数目为 1 。
- 第 4 个操作后，nums = [2,1,0,1] 。相邻元素颜色相同的数目为 0 。
- 第 5 个操作后，nums = [2,1,1,1] 。相邻元素颜色相同的数目为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>n = 1, queries = [[0,100000]]
<b>输出：</b>[0]
<b>解释：</b>一开始数组 nums = [0] ，0 表示数组中还没染色的元素。
- 第 1 个操作后，nums = [100000] 。相邻元素颜色相同的数目为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length&nbsp;== 2</code></li>
	<li><code>0 &lt;= index<sub>i</sub>&nbsp;&lt;= n - 1</code></li>
	<li><code>1 &lt;=&nbsp; color<sub>i</sub>&nbsp;&lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组

## 提示

1. Since at each query, only one element is being recolored, we just need to focus on its neighbors.
2. If an element that is changed on the i-th query had the same color as its right element answer decreases by 1. Similarly contributes its left element too.
3. After changing the color, if the element has the same color as its right element answer increases by 1. Similarly contributes its left element too.

## 示例

```
4
[[0,2],[1,2],[3,1],[1,1],[2,1]]
1
[[0,100000]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] colorTheArray(int n, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* colorTheArray(int n, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ColorTheArray(int n, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var colorTheArray = function(n, queries) {
    
};
```

### TypeScript

```typescript
function colorTheArray(n: number, queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function colorTheArray($n, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func colorTheArray(_ n: Int, _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun colorTheArray(n: Int, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> colorTheArray(int n, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func colorTheArray(n int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def color_the_array(n, queries)
    
end
```

### Scala

```scala
object Solution {
    def colorTheArray(n: Int, queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn color_the_array(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (color-the-array n queries)
  (-> exact-integer? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec color_the_array(N :: integer(), Queries :: [[integer()]]) -> [integer()].
color_the_array(N, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec color_the_array(n :: integer, queries :: [[integer]]) :: [integer]
  def color_the_array(n, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func colorTheArray(n: Int64, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

