# LCP 42. 玩具套圈

## 题目描述

「力扣挑战赛」场地外，小力组织了一个套玩具的游戏。所有的玩具摆在平地上，`toys[i]` 以 `[xi,yi,ri]` 的形式记录了第 `i` 个玩具的坐标 `(xi,yi)` 和半径 `ri`。小扣试玩了一下，他扔了若干个半径均为 `r` 的圈，`circles[j]` 记录了第 `j` 个圈的坐标 `(xj,yj)`。套圈的规则如下：
- 若一个玩具被某个圈完整覆盖了（即玩具的任意部分均在圈内或者圈上），则该玩具被套中。
- 若一个玩具被多个圈同时套中，最终仅计算为套中一个玩具

请帮助小扣计算，他成功套中了多少玩具。

**注意：**
- 输入数据保证任意两个玩具的圆心不会重合，但玩具之间可能存在重叠。


**示例 1：**

> 输入：`toys = [[3,3,1],[3,2,1]], circles = [[4,3]], r = 2`
>
> 输出：`1`
> 
> 解释： 如图所示，仅套中一个玩具
![image.png](https://pic.leetcode-cn.com/1629194140-ydKiGF-image.png)


**示例 2：**

> 输入：`toys = [[1,3,2],[4,3,1],[7,1,2]], circles = [[1,0],[3,3]], r = 4`
>
> 输出：`2`
> 
> 解释： 如图所示，套中两个玩具
![image.png](https://pic.leetcode-cn.com/1629194157-RiOAuy-image.png){:width="400px"}



**提示：** 
- `1 <= toys.length <= 10^4`
- `0 <= toys[i][0], toys[i][1] <= 10^9`
- `1 <= circles.length <= 10^4`
- `0 <= circles[i][0], circles[i][1] <= 10^9`
- `1 <= toys[i][2], r <= 10`


## 难度

Hard

## 标签

- 几何
- 数组
- 哈希表
- 数学
- 二分查找
- 排序

## 示例

```
[[1,3,2],[4,3,1]]
[[1,0],[3,3],[0,0],[3,4]]
4
[[3,4,5],[1,4,4],[4,4,1],[1,5,5]]
[[4,1],[4,2]]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int circleGame(vector<vector<int>>& toys, vector<vector<int>>& circles, int r) {

    }
};
```

### Java

```java
class Solution {
    public int circleGame(int[][] toys, int[][] circles, int r) {

    }
}
```

### Python

```python
class Solution(object):
    def circleGame(self, toys, circles, r):
        """
        :type toys: List[List[int]]
        :type circles: List[List[int]]
        :type r: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def circleGame(self, toys: List[List[int]], circles: List[List[int]], r: int) -> int:
```

### C

```c


int circleGame(int** toys, int toysSize, int* toysColSize, int** circles, int circlesSize, int* circlesColSize, int r){

}
```

### C#

```csharp
public class Solution {
    public int CircleGame(int[][] toys, int[][] circles, int r) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} toys
 * @param {number[][]} circles
 * @param {number} r
 * @return {number}
 */
var circleGame = function(toys, circles, r) {

};
```

### TypeScript

```typescript
function circleGame(toys: number[][], circles: number[][], r: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $toys
     * @param Integer[][] $circles
     * @param Integer $r
     * @return Integer
     */
    function circleGame($toys, $circles, $r) {

    }
}
```

### Swift

```swift
class Solution {
    func circleGame(_ toys: [[Int]], _ circles: [[Int]], _ r: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun circleGame(toys: Array<IntArray>, circles: Array<IntArray>, r: Int): Int {

    }
}
```

### Go

```golang
func circleGame(toys [][]int, circles [][]int, r int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} toys
# @param {Integer[][]} circles
# @param {Integer} r
# @return {Integer}
def circle_game(toys, circles, r)

end
```

### Scala

```scala
object Solution {
    def circleGame(toys: Array[Array[Int]], circles: Array[Array[Int]], r: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn circle_game(toys: Vec<Vec<i32>>, circles: Vec<Vec<i32>>, r: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (circle-game toys circles r)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec circle_game(Toys :: [[integer()]], Circles :: [[integer()]], R :: integer()) -> integer().
circle_game(Toys, Circles, R) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec circle_game(toys :: [[integer]], circles :: [[integer]], r :: integer) :: integer
  def circle_game(toys, circles, r) do

  end
end
```

