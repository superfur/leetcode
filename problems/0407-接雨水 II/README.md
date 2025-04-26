# 407. 接雨水 II

## 题目描述

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg" /></p>

<pre>
<strong>输入:</strong> heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
<strong>输出:</strong> 4
<strong>解释:</strong> 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg" /></p>

<pre>
<strong>输入:</strong> heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
<strong>输出:</strong> 10
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>m == heightMap.length</code></li>
	<li><code>n == heightMap[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 200</code></li>
	<li><code>0 &lt;= heightMap[i][j] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 矩阵
- 堆（优先队列）

## 示例

```
[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
[[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        
    }
};
```

### Java

```java
class Solution {
    public int trapRainWater(int[][] heightMap) {
        
    }
}
```

### Python

```python
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
```

### C

```c
int trapRainWater(int** heightMap, int heightMapSize, int* heightMapColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TrapRainWater(int[][] heightMap) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} heightMap
 * @return {number}
 */
var trapRainWater = function(heightMap) {
    
};
```

### TypeScript

```typescript
function trapRainWater(heightMap: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $heightMap
     * @return Integer
     */
    function trapRainWater($heightMap) {
        
    }
}
```

### Swift

```swift
class Solution {
    func trapRainWater(_ heightMap: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun trapRainWater(heightMap: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int trapRainWater(List<List<int>> heightMap) {
    
  }
}
```

### Go

```golang
func trapRainWater(heightMap [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} height_map
# @return {Integer}
def trap_rain_water(height_map)
    
end
```

### Scala

```scala
object Solution {
    def trapRainWater(heightMap: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn trap_rain_water(height_map: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (trap-rain-water heightMap)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec trap_rain_water(HeightMap :: [[integer()]]) -> integer().
trap_rain_water(HeightMap) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec trap_rain_water(height_map :: [[integer]]) :: integer
  def trap_rain_water(height_map) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func trapRainWater(heightMap: Array<Array<Int64>>): Int64 {

    }
}
```

