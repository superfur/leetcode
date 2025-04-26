# LCP 59. 搭桥过河

## 题目描述

欢迎各位勇者来到力扣城，本次试炼主题为「搭桥过河」。

勇者面前有一段长度为 `num` 的河流，河流可以划分为若干河道。每条河道上恰有一块浮木，`wood[i]` 记录了第 `i` 条河道上的浮木初始的覆盖范围。

- 当且仅当浮木与相邻河道的浮木覆盖范围有重叠时，勇者才可以在两条浮木间移动
- 勇者 **仅能在岸上** 通过花费一点「自然之力」，使任意一条浮木沿着河流移动一个单位距离

请问勇者跨越这条河流，最少需要花费多少「自然之力」。


**示例 1：**
> 输入： `num = 10, wood = [[1,2],[4,7],[8,9]]`
> 输出： `3`
> 解释：如下图所示，
> 将 [1,2] 浮木移动至 [3,4]，花费 2「自然之力」，
> 将 [8,9] 浮木移动至 [7,8]，花费 1「自然之力」，
> 此时勇者可以顺着 [3,4]->[4,7]->[7,8] 跨越河流，
> 因此，勇者最少需要花费 3 点「自然之力」跨越这条河流
![wood (2).gif](https://pic.leetcode-cn.com/1648196478-ophADL-wood%20\(2\).gif){:width=650px}


**示例 2：**
> 输入： `num = 10, wood = [[1,5],[1,1],[10,10],[6,7],[7,8]]`
> 输出： `10`
> 解释：
> 将 [1,5] 浮木移动至 [2,6]，花费 1「自然之力」，
> 将 [1,1] 浮木移动至 [6,6]，花费 5「自然之力」，
> 将 [10,10] 浮木移动至 [6,6]，花费 4「自然之力」，
> 此时勇者可以顺着 [2,6]->[6,6]->[6,6]->[6,7]->[7,8] 跨越河流，
> 因此，勇者最少需要花费 10 点「自然之力」跨越这条河流


**示例 3：**
> 输入： `num = 5, wood = [[1,2],[2,4]]`
> 输出： `0`
> 解释：勇者不需要移动浮木，仍可以跨越这条河流

**提示:**
- `1 <= num <= 10^9`
- `1 <= wood.length <= 10^5`
- `wood[i].length == 2`
- `1 <= wood[i][0] <= wood[i][1] <= num`



## 难度

Hard

## 标签

- 数组
- 动态规划

## 示例

```
10
[[1,2],[4,7],[8,9]]
10
[[1,5],[1,1],[10,10],[6,7],[7,8]]
5
[[1,2],[2,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long buildBridge(int num, vector<vector<int>>& wood) {

    }
};
```

### Java

```java
class Solution {
    public long buildBridge(int num, int[][] wood) {

    }
}
```

### Python

```python
class Solution(object):
    def buildBridge(self, num, wood):
        """
        :type num: int
        :type wood: List[List[int]]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def buildBridge(self, num: int, wood: List[List[int]]) -> int:
```

### C

```c


long long buildBridge(int num, int** wood, int woodSize, int* woodColSize){

}
```

### C#

```csharp
public class Solution {
    public long BuildBridge(int num, int[][] wood) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @param {number[][]} wood
 * @return {number}
 */
var buildBridge = function(num, wood) {

};
```

### TypeScript

```typescript
function buildBridge(num: number, wood: number[][]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @param Integer[][] $wood
     * @return Integer
     */
    function buildBridge($num, $wood) {

    }
}
```

### Swift

```swift
class Solution {
    func buildBridge(_ num: Int, _ wood: [[Int]]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun buildBridge(num: Int, wood: Array<IntArray>): Long {

    }
}
```

### Go

```golang
func buildBridge(num int, wood [][]int) int64 {

}
```

### Ruby

```ruby
# @param {Integer} num
# @param {Integer[][]} wood
# @return {Integer}
def build_bridge(num, wood)

end
```

### Scala

```scala
object Solution {
    def buildBridge(num: Int, wood: Array[Array[Int]]): Long = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn build_bridge(num: i32, wood: Vec<Vec<i32>>) -> i64 {

    }
}
```

### Racket

```racket
(define/contract (build-bridge num wood)
  (-> exact-integer? (listof (listof exact-integer?)) exact-integer?)

  )
```

### Erlang

```erlang
-spec build_bridge(Num :: integer(), Wood :: [[integer()]]) -> integer().
build_bridge(Num, Wood) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec build_bridge(num :: integer, wood :: [[integer]]) :: integer
  def build_bridge(num, wood) do

  end
end
```

