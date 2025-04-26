# LCP 54. 夺回据点

## 题目描述

欢迎各位勇者来到力扣城，本次试炼主题为「夺回据点」。

魔物了占领若干据点，这些据点被若干条道路相连接，`roads[i] = [x, y]` 表示编号 `x`、`y` 的两个据点通过一条道路连接。

现在勇者要将按照以下原则将这些据点逐一夺回：

- 在开始的时候，勇者可以花费资源先夺回一些据点，初始夺回第 `j` 个据点所需消耗的资源数量为 `cost[j]` 

- 接下来，勇者在不消耗资源情况下，每次可以夺回**一个**和「已夺回据点」相连接的魔物据点，并对其进行夺回

> 注：为了防止魔物暴动，勇者在每一次夺回据点后（包括花费资源夺回据点后），需要保证剩余的所有魔物据点之间是相连通的（不经过「已夺回据点」）。

请返回勇者夺回所有据点需要消耗的最少资源数量。

**注意：**
- 输入保证初始所有据点都是连通的，且不存在重边和自环

**示例 1：**
>输入：
>`cost = [1,2,3,4,5,6]`
>`roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]`
>
>输出：`6`
>
>解释：
>勇者消耗资源 `6` 夺回据点 `0` 和 `4`，魔物据点 `1、2、3、5` 相连通；
>第一次夺回据点 `1`，魔物据点 `2、3、5` 相连通；
>第二次夺回据点 `3`，魔物据点 `2、5` 相连通；
>第三次夺回据点 `2`，剩余魔物据点 `5`；
>第四次夺回据点 `5`，无剩余魔物据点；
>因此最少需要消耗资源为 `6`，可占领所有据点。
![image.png](https://pic.leetcode-cn.com/1648706944-KJstUN-image.png){:height=170px}


**示例 2：**
>输入：
>`cost = [3,2,1,4]`
>`roads = [[0,2],[2,3],[3,1]]`
>
>输出：`2`
>
>解释：
>勇者消耗资源 `2` 夺回据点 `1`，魔物据点 `0、2、3` 相连通；
>第一次夺回据点 `3`，魔物据点 `2、0` 相连通；
>第二次夺回据点 `2`，剩余魔物据点 `0`；
>第三次夺回据点 `0`，无剩余魔物据点；
>因此最少需要消耗资源为 `2`，可占领所有据点。
![image.png](https://pic.leetcode-cn.com/1648707186-LJRwzU-image.png){:height=60px}


**提示：**
- `1 <= roads.length, cost.length <= 10^5`
- `0 <= roads[i][0], roads[i][1] < cost.length`
- `1 <= cost[i] <= 10^9`


## 难度

Hard

## 标签

- 图
- 数组
- 双连通分量

## 示例

```
[1,2,3,4,5,6]
[[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]
[3,2,1,4]
[[0,2],[2,3],[3,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumCost(vector<int>& cost, vector<vector<int>>& roads) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumCost(int[] cost, int[][] roads) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, cost, roads):
        """
        :type cost: List[int]
        :type roads: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        
```

### C

```c
long long minimumCost(int* cost, int costSize, int** roads, int roadsSize, int* roadsColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumCost(int[] cost, int[][] roads) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} cost
 * @param {number[][]} roads
 * @return {number}
 */
var minimumCost = function(cost, roads) {
    
};
```

### TypeScript

```typescript
function minimumCost(cost: number[], roads: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $cost
     * @param Integer[][] $roads
     * @return Integer
     */
    function minimumCost($cost, $roads) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ cost: [Int], _ roads: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(cost: IntArray, roads: Array<IntArray>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(List<int> cost, List<List<int>> roads) {
    
  }
}
```

### Go

```golang
func minimumCost(cost []int, roads [][]int) int64 {
    
}
```

### Ruby

```ruby
# @param {Integer[]} cost
# @param {Integer[][]} roads
# @return {Integer}
def minimum_cost(cost, roads)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(cost: Array[Int], roads: Array[Array[Int]]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(cost: Vec<i32>, roads: Vec<Vec<i32>>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost cost roads)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Cost :: [integer()], Roads :: [[integer()]]) -> integer().
minimum_cost(Cost, Roads) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(cost :: [integer], roads :: [[integer]]) :: integer
  def minimum_cost(cost, roads) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(cost: Array<Int64>, roads: Array<Array<Int64>>): Int64 {

    }
}
```

