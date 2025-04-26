# LCP 21. 追逐游戏

## 题目描述

秋游中的小力和小扣设计了一个追逐游戏。他们选了秋日市集景区中的 N 个景点，景点编号为 1~N。此外，他们还选择了 N 条小路，满足任意两个景点之间都可以通过小路互相到达，且不存在两条连接景点相同的小路。整个游戏场景可视作一个无向连通图，记作二维数组 `edges`，数组中以 `[a,b]` 形式表示景点 a 与景点 b 之间有一条小路连通。

小力和小扣只能沿景点间的小路移动。小力的目标是在最快时间内追到小扣，小扣的目标是尽可能延后被小力追到的时间。游戏开始前，两人分别站在两个不同的景点 `startA` 和 `startB`。每一回合，小力先行动，小扣观察到小力的行动后再行动。小力和小扣在每回合可选择以下行动之一：
- 移动至相邻景点
- 留在原地

如果小力追到小扣（即两人于某一时刻出现在同一位置），则游戏结束。若小力可以追到小扣，请返回最少需要多少回合；若小力无法追到小扣，请返回 -1。

注意：小力和小扣一定会采取最优移动策略。

**示例 1：**
>输入：`edges = [[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]], startA = 3, startB = 5`
>
>输出：`3`
>
>解释：
>![image.png](https://pic.leetcode-cn.com/1597991318-goeHHr-image.png){:height="250px"}
>
>第一回合，小力移动至 2 号点，小扣观察到小力的行动后移动至 6 号点；
>第二回合，小力移动至 5 号点，小扣无法移动，留在原地；
>第三回合，小力移动至 6 号点，小力追到小扣。返回 3。


**示例 2：**
>输入：`edges = [[1,2],[2,3],[3,4],[4,1]], startA = 1, startB = 3`
>
>输出：`-1`
>
>解释：
>![image.png](https://pic.leetcode-cn.com/1597991157-QfeakF-image.png){:height="250px"}
>
>小力如果不动，则小扣也不动；否则小扣移动到小力的对角线位置。这样小力无法追到小扣。

**提示：**
- `edges` 的长度等于图中节点个数
- `3 <= edges.length <= 10^5`
- `1 <= edges[i][0], edges[i][1] <= edges.length 且 edges[i][0] != edges[i][1]`
- `1 <= startA, startB <= edges.length 且 startA != startB`



## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 图
- 拓扑排序

## 示例

```
[[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]]
3
5
[[1,2],[2,3],[3,4],[4,1]]
1
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int chaseGame(vector<vector<int>>& edges, int startA, int startB) {

    }
};
```

### Java

```java
class Solution {
    public int chaseGame(int[][] edges, int startA, int startB) {

    }
}
```

### Python

```python
class Solution(object):
    def chaseGame(self, edges, startA, startB):
        """
        :type edges: List[List[int]]
        :type startA: int
        :type startB: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
```

### C

```c


int chaseGame(int** edges, int edgesSize, int* edgesColSize, int startA, int startB){

}
```

### C#

```csharp
public class Solution {
    public int ChaseGame(int[][] edges, int startA, int startB) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} edges
 * @param {number} startA
 * @param {number} startB
 * @return {number}
 */
var chaseGame = function(edges, startA, startB) {

};
```

### TypeScript

```typescript
function chaseGame(edges: number[][], startA: number, startB: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $edges
     * @param Integer $startA
     * @param Integer $startB
     * @return Integer
     */
    function chaseGame($edges, $startA, $startB) {

    }
}
```

### Swift

```swift
class Solution {
    func chaseGame(_ edges: [[Int]], _ startA: Int, _ startB: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun chaseGame(edges: Array<IntArray>, startA: Int, startB: Int): Int {

    }
}
```

### Go

```golang
func chaseGame(edges [][]int, startA int, startB int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} edges
# @param {Integer} start_a
# @param {Integer} start_b
# @return {Integer}
def chase_game(edges, start_a, start_b)

end
```

### Scala

```scala
object Solution {
    def chaseGame(edges: Array[Array[Int]], startA: Int, startB: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn chase_game(edges: Vec<Vec<i32>>, start_a: i32, start_b: i32) -> i32 {

    }
}
```

