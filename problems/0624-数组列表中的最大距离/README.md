# 624. 数组列表中的最大距离

## 题目描述

<p>给定&nbsp;<code>m</code>&nbsp;个数组，每个数组都已经按照升序排好序了。</p>

<p>现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数&nbsp;<code>a</code>&nbsp;和&nbsp;<code>b</code>&nbsp;之间的距离定义为它们差的绝对值&nbsp;<code>|a-b|</code>&nbsp;。</p>

<p>返回最大距离。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>[[1,2,3],[4,5],[1,2,3]]
<strong>输出：</strong>4
<strong>解释：</strong>
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>arrays = [[1],[1]]
<b>输出：</b>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == arrays.length</code></li>
	<li><code>2 &lt;= m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= arrays[i].length &lt;= 500</code></li>
	<li><code>-10<sup>4</sup> &lt;= arrays[i][j] &lt;= 10<sup>4</sup></code></li>
	<li><code>arrays[i]</code>&nbsp;以&nbsp;<strong>升序</strong>&nbsp;排序。</li>
	<li>所有数组中最多有&nbsp;<code>10<sup>5</sup></code> 个整数。</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 贪心
- 数组

## 示例

```
[[1,2,3],[4,5],[1,2,3]]
[[1],[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxDistance(List<List<Integer>> arrays) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
```

### C

```c
int maxDistance(int** arrays, int arraysSize, int* arraysColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxDistance(IList<IList<int>> arrays) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} arrays
 * @return {number}
 */
var maxDistance = function(arrays) {
    
};
```

### TypeScript

```typescript
function maxDistance(arrays: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $arrays
     * @return Integer
     */
    function maxDistance($arrays) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxDistance(_ arrays: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxDistance(arrays: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxDistance(List<List<int>> arrays) {
    
  }
}
```

### Go

```golang
func maxDistance(arrays [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} arrays
# @return {Integer}
def max_distance(arrays)
    
end
```

### Scala

```scala
object Solution {
    def maxDistance(arrays: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_distance(arrays: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-distance arrays)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_distance(Arrays :: [[integer()]]) -> integer().
max_distance(Arrays) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_distance(arrays :: [[integer]]) :: integer
  def max_distance(arrays) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxDistance(arrays: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

