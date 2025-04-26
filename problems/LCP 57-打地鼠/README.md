# LCP 57. 打地鼠

## 题目描述

欢迎各位勇者来到力扣城，本次试炼主题为「打地鼠」。
![middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png](https://pic.leetcode-cn.com/1650273183-nZIijm-middle_img_v2_d5d09656-0616-4a80-845e-ece461c5ba9g.png){:height="200px"}
勇者面前有一个大小为 `3*3` 的打地鼠游戏机，地鼠将随机出现在各个位置，`moles[i] = [t,x,y]` 表示在第 `t` 秒会有地鼠出现在 `(x,y)` 位置上，并于第 `t+1` 秒该地鼠消失。

勇者有一把可敲打地鼠的锤子，初始时刻（即第 `0` 秒）锤子位于正中间的格子 `(1,1)`，锤子的使用规则如下：
- 锤子每经过 `1` 秒可以往上、下、左、右中的一个方向移动一格，也可以不移动
- 锤子只可敲击所在格子的地鼠，**敲击不耗时**

请返回勇者**最多**能够敲击多少只地鼠。

**注意：** 
- 输入用例保证在相同时间相同位置最多仅有一只地鼠


**示例 1：**
>输入： `moles = [[1,1,0],[2,0,1],[4,2,2]]`
>
>输出： `2`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (1,0) 并敲击地鼠
>第 2 秒，锤子移动至 (2,0)
>第 3 秒，锤子移动至 (2,1)
>第 4 秒，锤子移动至 (2,2) 并敲击地鼠
>因此勇者最多可敲击 2 只地鼠


**示例 2：**
>输入：`moles = [[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]`
>
>输出：`3`
>
>解释：
>第 0 秒，锤子位于 (1,1)
>第 1 秒，锤子移动至 (2,1) 并敲击地鼠
>第 2 秒，锤子移动至 (1,1)
>第 3 秒，锤子移动至 (1,0)
>第 4 秒，锤子在 (1,0) 不移动并敲击地鼠
>第 5 秒，锤子移动至 (2,0) 并敲击地鼠
>因此勇者最多可敲击 3 只地鼠


**示例 3：**
>输入：`moles = [[0,1,0],[0,0,1]]`
>
>输出：`0`
>
>解释：
>第 0 秒，锤子初始位于 (1,1)，此时并不能敲击 (1,0)、(0,1) 位置处的地鼠


**提示：**
+ `1 <= moles.length <= 10^5`
+ `moles[i].length == 3`
+ `0 <= moles[i][0] <= 10^9`
+ `0 <= moles[i][1], moles[i][2] < 3`


## 难度

Hard

## 标签

- 数组
- 动态规划
- 矩阵
- 排序

## 示例

```
[[1,1,0],[2,0,1],[4,2,2]]
[[2,0,2],[5,2,0],[4,1,0],[1,2,1],[3,0,2]]
[[2,0,2],[6,2,0],[4,1,0],[2,2,2],[3,0,2]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMaximumNumber(vector<vector<int>>& moles) {

    }
};
```

### Java

```java
class Solution {
    public int getMaximumNumber(int[][] moles) {

    }
}
```

### Python

```python
class Solution(object):
    def getMaximumNumber(self, moles):
        """
        :type moles: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def getMaximumNumber(self, moles: List[List[int]]) -> int:
```

### C

```c


int getMaximumNumber(int** moles, int molesSize, int* molesColSize){

}
```

### C#

```csharp
public class Solution {
    public int GetMaximumNumber(int[][] moles) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} moles
 * @return {number}
 */
var getMaximumNumber = function(moles) {

};
```

### TypeScript

```typescript
function getMaximumNumber(moles: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $moles
     * @return Integer
     */
    function getMaximumNumber($moles) {

    }
}
```

### Swift

```swift
class Solution {
    func getMaximumNumber(_ moles: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMaximumNumber(moles: Array<IntArray>): Int {

    }
}
```

### Go

```golang
func getMaximumNumber(moles [][]int) int {

}
```

### Ruby

```ruby
# @param {Integer[][]} moles
# @return {Integer}
def get_maximum_number(moles)

end
```

### Scala

```scala
object Solution {
    def getMaximumNumber(moles: Array[Array[Int]]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_maximum_number(moles: Vec<Vec<i32>>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (get-maximum-number moles)
  (-> (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec get_maximum_number(Moles :: [[integer()]]) -> integer().
get_maximum_number(Moles) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_maximum_number(moles :: [[integer]]) :: integer
  def get_maximum_number(moles) do

  end
end
```

