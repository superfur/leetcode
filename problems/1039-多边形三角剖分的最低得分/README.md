# 1039. 多边形三角剖分的最低得分

## 题目描述

<p>你有一个凸的<meta charset="UTF-8" />&nbsp;<code>n</code>&nbsp;边形，其每个顶点都有一个整数值。给定一个整数数组<meta charset="UTF-8" />&nbsp;<code>values</code>&nbsp;，其中<meta charset="UTF-8" />&nbsp;<code>values[i]</code>&nbsp;是第 <code>i</code> 个顶点的值（即 <strong>顺时针顺序</strong> ）。</p>

<p>假设将多边形 <strong>剖分</strong>&nbsp;为 <code>n - 2</code>&nbsp;个三角形。对于每个三角形，该三角形的值是顶点标记的<strong>乘积</strong>，三角剖分的分数是进行三角剖分后所有 <code>n - 2</code>&nbsp;个三角形的值之和。</p>

<p>返回 <em>多边形进行三角剖分后可以得到的最低分</em> 。<br />
&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape1.jpg" /></p>

<pre>
<strong>输入：</strong>values = [1,2,3]
<strong>输出：</strong>6
<strong>解释：</strong>多边形已经三角化，唯一三角形的分数为 6。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape2.jpg" style="height: 163px; width: 446px;" /></p>

<pre>
<strong>输入：</strong>values = [3,7,4,5]
<strong>输出：</strong>144
<strong>解释：</strong>有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape3.jpg" /></p>

<pre>
<strong>输入：</strong>values = [1,3,1,4,1,5]
<strong>输出：</strong>13
<strong>解释：</strong>最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == values.length</code></li>
	<li><code>3 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= values[i] &lt;= 100</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划

## 提示

1. Without loss of generality, there is a triangle that uses adjacent vertices A[0] and A[N-1] (where N = A.length).  Depending on your choice K of it, this breaks down the triangulation into two subproblems A[1:K] and A[K+1:N-1].

## 示例

```
[1,2,3]
[3,7,4,5]
[1,3,1,4,1,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minScoreTriangulation(vector<int>& values) {
        
    }
};
```

### Java

```java
class Solution {
    public int minScoreTriangulation(int[] values) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minScoreTriangulation(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
```

### C

```c
int minScoreTriangulation(int* values, int valuesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinScoreTriangulation(int[] values) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} values
 * @return {number}
 */
var minScoreTriangulation = function(values) {
    
};
```

### TypeScript

```typescript
function minScoreTriangulation(values: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $values
     * @return Integer
     */
    function minScoreTriangulation($values) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minScoreTriangulation(_ values: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minScoreTriangulation(values: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minScoreTriangulation(List<int> values) {
    
  }
}
```

### Go

```golang
func minScoreTriangulation(values []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} values
# @return {Integer}
def min_score_triangulation(values)
    
end
```

### Scala

```scala
object Solution {
    def minScoreTriangulation(values: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_score_triangulation(values: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-score-triangulation values)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_score_triangulation(Values :: [integer()]) -> integer().
min_score_triangulation(Values) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_score_triangulation(values :: [integer]) :: integer
  def min_score_triangulation(values) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minScoreTriangulation(values: Array<Int64>): Int64 {

    }
}
```

