# 面试题 16.14. 最佳直线

## 题目描述

<p>给定一个二维平面及平面上的 N 个点列表<code>Points</code>，其中第<code>i</code>个点的坐标为<code>Points[i]=[X<sub>i</sub>,Y<sub>i</sub>]</code>。请找出一条直线，其通过的点的数目最多。</p>
<p>设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为<code>S</code>，你仅需返回<code>[S[0],S[1]]</code>作为答案，若有多条直线穿过了相同数量的点，则选择<code>S[0]</code>值较小的直线返回，<code>S[0]</code>相同则选择<code>S[1]</code>值较小的直线返回。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong> [[0,0],[1,1],[1,0],[2,0]]
<strong>输出：</strong> [0,2]
<strong>解释：</strong> 所求直线穿过的3个点的编号为[0,2,3]
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>2 <= len(Points) <= 300</code></li>
<li><code>len(Points[i]) = 2</code></li>
</ul>


## 难度

Medium

## 标签

- 几何
- 数组
- 哈希表
- 数学

## 提示

1. 有时，蛮力解法是相当好的办法。你能试试所有可能的直线吗？
2. 你不能真的试遍世界上所有可能的无限长的线。但你知道一条“最好”的线必须至少相交两点。你能连接每对点吗？你可以检查每一条线是否是最优的吗？
3. 你应该能得到O(N²)的解法。
4. 你试过使用散列表吗?

## 示例

```
[[-38935,27124],[-39837,19604],[-7086,42194],[-11571,-23257],[115,-23257],[20229,5976],[24653,-18488],[11017,21043],[-9353,16550],[-47076,15237],[-36686,42194],[-17704,1104],[31067,7368],[-20882,42194],[-19107,-10597],[-14898,24506],[-20801,42194],[-52268,40727],[-14042,42194],[-23254,42194],[-30837,-53882],[1402,801],[-33961,-984],[-6411,42194],[-12210,22901],[-8213,-19441],[-26939,20810],[30656,-23257],[-27195,21649],[-33780,2717],[23617,27018],[12266,3608]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> bestLine(vector<vector<int>>& points) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] bestLine(int[][] points) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestLine(self, points):
        """
        :type points: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* bestLine(int** points, int pointsSize, int* pointsColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] BestLine(int[][] points) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} points
 * @return {number[]}
 */
var bestLine = function(points) {
    
};
```

### TypeScript

```typescript
function bestLine(points: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $points
     * @return Integer[]
     */
    function bestLine($points) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestLine(_ points: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestLine(points: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> bestLine(List<List<int>> points) {
    
  }
}
```

### Go

```golang
func bestLine(points [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} points
# @return {Integer[]}
def best_line(points)
    
end
```

### Scala

```scala
object Solution {
    def bestLine(points: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_line(points: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (best-line points)
  (-> (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec best_line(Points :: [[integer()]]) -> [integer()].
best_line(Points) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_line(points :: [[integer]]) :: [integer]
  def best_line(points) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestLine(points: Array<Array<Int64>>): Array<Int64> {

    }
}
```

