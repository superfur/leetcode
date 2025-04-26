# 554. 砖墙

## 题目描述

<p>你的面前有一堵矩形的、由 <code>n</code> 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和相等。</p>

<p>你现在要画一条 <strong>自顶向下 </strong>的、穿过 <strong>最少 </strong>砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。<strong>你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。</strong></p>

<p>给你一个二维数组 <code>wall</code> ，该数组包含这堵墙的相关信息。其中，<code>wall[i]</code> 是一个代表从左至右每块砖的宽度的数组。你需要找出怎样画才能使这条线 <strong>穿过的砖块数量最少</strong> ，并且返回 <strong>穿过的砖块数量</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/01/17/a.png" style="width: 400px; height: 384px;" />
<pre>
<strong>输入：</strong>wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>wall = [[1],[1],[1]]
<strong>输出：</strong>3
</pre>
&nbsp;

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == wall.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= wall[i].length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= sum(wall[i].length) &lt;= 2 * 10<sup>4</sup></code></li>
	<li>对于每一行 <code>i</code> ，<code>sum(wall[i])</code> 是相同的</li>
	<li><code>1 &lt;= wall[i][j] &lt;= 2<sup>31</sup> - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 示例

```
[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
[[1],[1],[1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int leastBricks(vector<vector<int>>& wall) {
        
    }
};
```

### Java

```java
class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        
    }
}
```

### Python

```python
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
```

### C

```c
int leastBricks(int** wall, int wallSize, int* wallColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LeastBricks(IList<IList<int>> wall) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} wall
 * @return {number}
 */
var leastBricks = function(wall) {
    
};
```

### TypeScript

```typescript
function leastBricks(wall: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $wall
     * @return Integer
     */
    function leastBricks($wall) {
        
    }
}
```

### Swift

```swift
class Solution {
    func leastBricks(_ wall: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun leastBricks(wall: List<List<Int>>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int leastBricks(List<List<int>> wall) {
    
  }
}
```

### Go

```golang
func leastBricks(wall [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} wall
# @return {Integer}
def least_bricks(wall)
    
end
```

### Scala

```scala
object Solution {
    def leastBricks(wall: List[List[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn least_bricks(wall: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (least-bricks wall)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec least_bricks(Wall :: [[integer()]]) -> integer().
least_bricks(Wall) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec least_bricks(wall :: [[integer]]) :: integer
  def least_bricks(wall) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func leastBricks(wall: ArrayList<ArrayList<Int64>>): Int64 {

    }
}
```

