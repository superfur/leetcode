# LCR 100. 三角形最小路径和

## 题目描述

<p>给定一个三角形 <code>triangle</code> ，找出自顶向下的最小路径和。</p>

<p>每一步只能移动到下一行中相邻的结点上。<strong>相邻的结点 </strong>在这里指的是 <strong>下标</strong> 与 <strong>上一层结点下标</strong> 相同或者等于 <strong>上一层结点下标 + 1</strong> 的两个结点。也就是说，如果正位于当前行的下标 <code>i</code> ，那么下一步可以移动到下一行的下标 <code>i</code> 或 <code>i + 1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
<strong>输出：</strong>11
<strong>解释：</strong>如下面简图所示：
   <strong>2</strong>
  <strong>3</strong> 4
 6 <strong>5</strong> 7
4 <strong>1</strong> 8 3
自顶向下的最小路径和为&nbsp;11（即，2&nbsp;+&nbsp;3&nbsp;+&nbsp;5&nbsp;+&nbsp;1&nbsp;= 11）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>triangle = [[-10]]
<strong>输出：</strong>-10
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= triangle.length &lt;= 200</code></li>
	<li><code>triangle[0].length == 1</code></li>
	<li><code>triangle[i].length == triangle[i - 1].length + 1</code></li>
	<li><code>-10<sup>4</sup> &lt;= triangle[i][j] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以只使用 <code>O(n)</code>&nbsp;的额外空间（<code>n</code> 为三角形的总行数）来解决这个问题吗？</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 120&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/triangle/">https://leetcode-cn.com/problems/triangle/</a></p>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 示例

```
[[2],[3,4],[6,5,7],[4,1,8,3]]
[[-10]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {

    }
};
```

### Java

```java
class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {

    }
}
```

### Python

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
```

### C

```c


int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){

}
```

### C#

```csharp
public class Solution {
    public int MinimumTotal(IList<IList<int>> triangle) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {

};
```

### TypeScript

```typescript
function minimumTotal(triangle: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $triangle
     * @return Integer
     */
    function minimumTotal($triangle) {

    }
}
```

### Swift

```swift
class Solution {
    func minimumTotal(_ triangle: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTotal(triangle: List<List<Int>>): Int {

    }
}
```

### Go

```golang
func minimumTotal(triangle [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} triangle
# @return {Integer}
def minimum_total(triangle)

end
```

### Scala

```scala
object Solution {
    def minimumTotal(triangle: List[List[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_total(triangle: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (minimum-total triangle)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec minimum_total(Triangle :: [[integer()]]) -> integer().
minimum_total(Triangle) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_total(triangle :: [[integer]]) :: integer
  def minimum_total(triangle) do

  end
end
```

