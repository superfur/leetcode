# 3000. 对角线最长的矩形的面积

## 题目描述

<p>给你一个下标从<strong> 0</strong> 开始的二维整数数组 <code>dimensions</code>。</p>

<p>对于所有下标 <code>i</code>（<code>0 &lt;= i &lt; dimensions.length</code>），<code>dimensions[i][0]</code> 表示矩形 <span style="font-size: 13.3333px;"> <code>i</code></span> 的长度，而 <code>dimensions[i][1]</code> 表示矩形 <span style="font-size: 13.3333px;"> <code>i</code></span> 的宽度。</p>

<p>返回对角线最 <strong>长 </strong>的矩形的<strong> 面积 </strong>。如果存在多个对角线长度相同的矩形，返回面积最<strong> 大 </strong>的矩形的面积。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>dimensions = [[9,3],[8,6]]
<strong>输出：</strong>48
<strong>解释：</strong>
下标 = 0，长度 = 9，宽度 = 3。对角线长度 = sqrt(9 * 9 + 3 * 3) = sqrt(90) ≈<!-- notionvc: 882cf44c-3b17-428e-9c65-9940810216f1 --> 9.487。
下标 = 1，长度 = 8，宽度 = 6。对角线长度 = sqrt(8 * 8 + 6 * 6) = sqrt(100) = 10。
因此，下标为 1 的矩形对角线更长，所以返回面积 = 8 * 6 = 48。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>dimensions = [[3,4],[4,3]]
<strong>输出：</strong>12
<strong>解释：</strong>两个矩形的对角线长度相同，为 5，所以最大面积 = 12。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= dimensions.length &lt;= 100</code></li>
	<li><code>dimensions[i].length == 2</code></li>
	<li><code>1 &lt;= dimensions[i][0], dimensions[i][1] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. Diagonal of rectangle is <code>sqrt(length<sup>2</sup> + width<sup>2</sup>)</code>.

## 示例

```
[[9,3],[8,6]]
[[3,4],[4,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        
    }
};
```

### Java

```java
class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        
    }
}
```

### Python

```python
class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        
```

### C

```c
int areaOfMaxDiagonal(int** dimensions, int dimensionsSize, int* dimensionsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int AreaOfMaxDiagonal(int[][] dimensions) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function(dimensions) {
    
};
```

### TypeScript

```typescript
function areaOfMaxDiagonal(dimensions: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $dimensions
     * @return Integer
     */
    function areaOfMaxDiagonal($dimensions) {
        
    }
}
```

### Swift

```swift
class Solution {
    func areaOfMaxDiagonal(_ dimensions: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun areaOfMaxDiagonal(dimensions: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int areaOfMaxDiagonal(List<List<int>> dimensions) {
    
  }
}
```

### Go

```golang
func areaOfMaxDiagonal(dimensions [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} dimensions
# @return {Integer}
def area_of_max_diagonal(dimensions)
    
end
```

### Scala

```scala
object Solution {
    def areaOfMaxDiagonal(dimensions: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn area_of_max_diagonal(dimensions: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (area-of-max-diagonal dimensions)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec area_of_max_diagonal(Dimensions :: [[integer()]]) -> integer().
area_of_max_diagonal(Dimensions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec area_of_max_diagonal(dimensions :: [[integer]]) :: integer
  def area_of_max_diagonal(dimensions) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func areaOfMaxDiagonal(dimensions: Array<Array<Int64>>): Int64 {

    }
}
```

