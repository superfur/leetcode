# 1725. 可以形成最大正方形的矩形数目

## 题目描述

<p>给你一个数组 <code>rectangles</code> ，其中 <code>rectangles[i] = [l<sub>i</sub>, w<sub>i</sub>]</code> 表示第 <code>i</code> 个矩形的长度为 <code>l<sub>i</sub></code> 、宽度为 <code>w<sub>i</sub></code> 。</p>

<p>如果存在 <code>k</code> 同时满足 <code>k <= l<sub>i</sub></code> 和 <code>k <= w<sub>i</sub></code> ，就可以将第 <code>i</code> 个矩形切成边长为 <code>k</code> 的正方形。例如，矩形 <code>[4,6]</code> 可以切成边长最大为 <code>4</code> 的正方形。</p>

<p>设 <code>maxLen</code> 为可以从矩形数组 <code>rectangles</code> 切分得到的 <strong>最大正方形</strong> 的边长。</p>

<p>请你统计有多少个矩形能够切出边长为<em> </em><code>maxLen</code> 的正方形，并返回矩形 <strong>数目</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rectangles = [[5,8],[3,9],[5,12],[16,5]]
<strong>输出：</strong>3
<strong>解释：</strong>能从每个矩形中切出的最大正方形边长分别是 [5,3,5,5] 。
最大正方形的边长为 5 ，可以由 3 个矩形切分得到。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rectangles = [[2,3],[3,7],[4,3],[3,7]]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= rectangles.length <= 1000</code></li>
	<li><code>rectangles[i].length == 2</code></li>
	<li><code>1 <= l<sub>i</sub>, w<sub>i</sub> <= 10<sup>9</sup></code></li>
	<li><code>l<sub>i</sub> != w<sub>i</sub></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. What is the length of the largest square the can be cut out of some rectangle? It'll be equal to min(rectangle.length, rectangle.width). Replace each rectangle with this value.
2. Calculate maxSize by iterating over the given rectangles and maximizing the answer with their values denoted in the first hint.
3. Then iterate again on the rectangles and calculate the number whose values = maxSize.

## 示例

```
[[5,8],[3,9],[5,12],[16,5]]
[[2,3],[3,7],[4,3],[3,7]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        
    }
};
```

### Java

```java
class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
```

### C

```c
int countGoodRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountGoodRectangles(int[][] rectangles) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} rectangles
 * @return {number}
 */
var countGoodRectangles = function(rectangles) {
    
};
```

### TypeScript

```typescript
function countGoodRectangles(rectangles: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $rectangles
     * @return Integer
     */
    function countGoodRectangles($rectangles) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodRectangles(_ rectangles: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodRectangles(rectangles: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodRectangles(List<List<int>> rectangles) {
    
  }
}
```

### Go

```golang
func countGoodRectangles(rectangles [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} rectangles
# @return {Integer}
def count_good_rectangles(rectangles)
    
end
```

### Scala

```scala
object Solution {
    def countGoodRectangles(rectangles: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_rectangles(rectangles: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-rectangles rectangles)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_rectangles(Rectangles :: [[integer()]]) -> integer().
count_good_rectangles(Rectangles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_rectangles(rectangles :: [[integer]]) :: integer
  def count_good_rectangles(rectangles) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodRectangles(rectangles: Array<Array<Int64>>): Int64 {

    }
}
```

