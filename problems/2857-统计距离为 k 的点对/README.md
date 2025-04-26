# 2857. 统计距离为 k 的点对

## 题目描述

<p>给你一个 <strong>二维</strong>&nbsp;整数数组&nbsp;<code>coordinates</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;，其中&nbsp;<code>coordinates[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>&nbsp;是第 <code>i</code>&nbsp;个点在二维平面里的坐标。</p>

<p>我们定义两个点&nbsp;<code>(x<sub>1</sub>, y<sub>1</sub>)</code>&nbsp;和&nbsp;<code>(x<sub>2</sub>, y<sub>2</sub>)</code>&nbsp;的 <strong>距离</strong>&nbsp;为&nbsp;<code>(x1 XOR x2) + (y1 XOR y2)</code> ，<code>XOR</code>&nbsp;指的是按位异或运算。</p>

<p>请你返回满足<em>&nbsp;</em><code>i &lt; j</code><em>&nbsp;</em>且点<em>&nbsp;</em><code>i</code><em> </em>和点<em>&nbsp;</em><code>j</code>之间距离为<em>&nbsp;</em><code>k</code>&nbsp;的点对数目。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>coordinates = [[1,2],[4,2],[1,3],[5,2]], k = 5
<b>输出：</b>2
<b>解释：</b>以下点对距离为 k ：
- (0, 1)：(1 XOR 4) + (2 XOR 2) = 5 。
- (2, 3)：(1 XOR 5) + (3 XOR 2) = 5 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>coordinates = [[1,3],[1,3],[1,3],[1,3],[1,3]], k = 0
<b>输出：</b>10
<b>解释：</b>任何两个点之间的距离都为 0 ，所以总共有 10 组点对。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= coordinates.length &lt;= 50000</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组
- 哈希表

## 提示

1. <div class="_1l1MA">Suppose that <code>x = x<sub>1</sub> XOR x<sub>2</sub></code> and y = y<sub>1</sub> XOR y<sub>2</sub> then we can get <code>x<sub>2</sub> = x XOR x<sub>1</sub></code> and <code>y<sub>2</sub> = y XOR y<sub>1</sub></code>.</div>
2. <div class="_1l1MA">We are supposed to have k = x + y so we can get <code>x<sub>2</sub> = x XOR x<sub>1</sub></code> and <code>y<sub>2</sub> = (k - x) XOR y<sub>1</sub></code>.</div>
3. <div class="_1l1MA">We can iterate over all possible values of <code>x</code> and count the number of points <code>(x<sub>1</sub>, x<sub>2</sub>)</code> and <code>(x<sub>2</sub>, y<sub>2</sub>)</code>.</div>

## 示例

```
[[1,2],[4,2],[1,3],[5,2]]
5
[[1,3],[1,3],[1,3],[1,3],[1,3]]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countPairs(vector<vector<int>>& coordinates, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int countPairs(List<List<Integer>> coordinates, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countPairs(self, coordinates, k):
        """
        :type coordinates: List[List[int]]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        
```

### C

```c
int countPairs(int** coordinates, int coordinatesSize, int* coordinatesColSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountPairs(IList<IList<int>> coordinates, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} coordinates
 * @param {number} k
 * @return {number}
 */
var countPairs = function(coordinates, k) {
    
};
```

### TypeScript

```typescript
function countPairs(coordinates: number[][], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $coordinates
     * @param Integer $k
     * @return Integer
     */
    function countPairs($coordinates, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countPairs(_ coordinates: [[Int]], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countPairs(coordinates: List<List<Int>>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countPairs(List<List<int>> coordinates, int k) {
    
  }
}
```

### Go

```golang
func countPairs(coordinates [][]int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} coordinates
# @param {Integer} k
# @return {Integer}
def count_pairs(coordinates, k)
    
end
```

### Scala

```scala
object Solution {
    def countPairs(coordinates: List[List[Int]], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_pairs(coordinates: Vec<Vec<i32>>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-pairs coordinates k)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_pairs(Coordinates :: [[integer()]], K :: integer()) -> integer().
count_pairs(Coordinates, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_pairs(coordinates :: [[integer]], k :: integer) :: integer
  def count_pairs(coordinates, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countPairs(coordinates: ArrayList<ArrayList<Int64>>, k: Int64): Int64 {

    }
}
```

