# LCP 45. 自行车炫技赛场

## 题目描述

「力扣挑战赛」中 `N*M` 大小的自行车炫技赛场的场地由一片连绵起伏的上下坡组成，场地的高度值记录于二维数组 `terrain` 中，场地的减速值记录于二维数组 `obstacle` 中。
- 若选手骑着自行车从高度为 `h1` 且减速值为 `o1` 的位置到高度为 `h2` 且减速值为 `o2` 的相邻位置（上下左右四个方向），速度变化值为 `h1-h2-o2`（负值减速，正值增速）。

选手初始位于坐标 `position` 处且初始速度为 1，请问选手可以刚好到其他哪些位置时速度依旧为 1。请以二维数组形式返回这些位置。若有多个位置则按行坐标升序排列，若有多个位置行坐标相同则按列坐标升序排列。

**注意：** 骑行过程中速度不能为零或负值

**示例 1：**
> 输入：`position = [0,0], terrain = [[0,0],[0,0]], obstacle = [[0,0],[0,0]]`
> 
> 输出：`[[0,1],[1,0],[1,1]]`
> 
> 解释：
> 由于当前场地属于平地，根据上面的规则，选手从`[0,0]`的位置出发都能刚好在其他处的位置速度为 1。

**示例 2：**
> 输入：`position = [1,1], terrain = [[5,0],[0,6]], obstacle = [[0,6],[7,0]]`
> 
> 输出：`[[0,1]]`
> 
> 解释：
> 选手从 `[1,1]` 处的位置出发，到 `[0,1]` 处的位置时恰好速度为 1。


**提示：**
- `n == terrain.length == obstacle.length`
- `m == terrain[i].length == obstacle[i].length`
- `1 <= n <= 100`
- `1 <= m <= 100`
- `0 <= terrain[i][j], obstacle[i][j] <= 100`
- `position.length == 2`
- `0 <= position[0] < n`
- `0 <= position[1] < m`

## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 记忆化搜索
- 数组
- 动态规划
- 矩阵

## 示例

```
[0,0]
[[0,0],[0,0]]
[[0,0],[0,0]]
[1,1]
[[5,0],[0,6]]
[[0,6],[7,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> bicycleYard(vector<int>& position, vector<vector<int>>& terrain, vector<vector<int>>& obstacle) {

    }
};
```

### Java

```java
class Solution {
    public int[][] bicycleYard(int[] position, int[][] terrain, int[][] obstacle) {

    }
}
```

### Python

```python
class Solution(object):
    def bicycleYard(self, position, terrain, obstacle):
        """
        :type position: List[int]
        :type terrain: List[List[int]]
        :type obstacle: List[List[int]]
        :rtype: List[List[int]]
        """
```

### Python3

```python3
class Solution:
    def bicycleYard(self, position: List[int], terrain: List[List[int]], obstacle: List[List[int]]) -> List[List[int]]:
```

### C

```c


/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** bicycleYard(int* position, int positionSize, int** terrain, int terrainSize, int* terrainColSize, int** obstacle, int obstacleSize, int* obstacleColSize, int* returnSize, int** returnColumnSizes){

}
```

### C#

```csharp
public class Solution {
    public int[][] BicycleYard(int[] position, int[][] terrain, int[][] obstacle) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} position
 * @param {number[][]} terrain
 * @param {number[][]} obstacle
 * @return {number[][]}
 */
var bicycleYard = function(position, terrain, obstacle) {

};
```

### TypeScript

```typescript
function bicycleYard(position: number[], terrain: number[][], obstacle: number[][]): number[][] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $position
     * @param Integer[][] $terrain
     * @param Integer[][] $obstacle
     * @return Integer[][]
     */
    function bicycleYard($position, $terrain, $obstacle) {

    }
}
```

### Swift

```swift
class Solution {
    func bicycleYard(_ position: [Int], _ terrain: [[Int]], _ obstacle: [[Int]]) -> [[Int]] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bicycleYard(position: IntArray, terrain: Array<IntArray>, obstacle: Array<IntArray>): Array<IntArray> {

    }
}
```

### Go

```golang
func bicycleYard(position []int, terrain [][]int, obstacle [][]int) [][]int {

}
```

### Ruby

```ruby
# @param {Integer[]} position
# @param {Integer[][]} terrain
# @param {Integer[][]} obstacle
# @return {Integer[][]}
def bicycle_yard(position, terrain, obstacle)

end
```

### Scala

```scala
object Solution {
    def bicycleYard(position: Array[Int], terrain: Array[Array[Int]], obstacle: Array[Array[Int]]): Array[Array[Int]] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn bicycle_yard(position: Vec<i32>, terrain: Vec<Vec<i32>>, obstacle: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

    }
}
```

### Racket

```racket
(define/contract (bicycle-yard position terrain obstacle)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof (listof exact-integer?)))

  )
```

