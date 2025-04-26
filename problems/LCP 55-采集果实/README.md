# LCP 55. 采集果实

## 题目描述

欢迎各位勇者来到力扣新手村，本次训练内容为「采集果实」。

在新手村中，各位勇者需要采集一些果实来制作药剂。`time[i]` 表示勇者每次采集 `1～limit` 颗第 `i` 种类型的果实需要的时间（即每次最多可以采集 `limit` 颗果实）。

当前勇者需要完成「采集若干批果实」的任务， `fruits[j] = [type, num]` 表示第 `j` 批需要采集 `num` 颗 `type` 类型的果实。采集规则如下：
- 按 `fruits` 给定的顺序**依次**采集每一批次
- 采集完当前批次的果实才能开始采集下一批次
- 勇者完成当前批次的采集后将**清空背包**（即多余的果实将清空）

请计算并返回勇者完成采集任务最少需要的时间。


**示例 1：**
>输入：`time = [2,3,2], fruits = [[0,2],[1,4],[2,1]], limit = 3`
>
>输出：`10`
>
>解释：
>由于单次最多采集 3 颗
>第 0 批需要采集 2 颗第 0 类型果实，需要采集 1 次，耗时为 2\*1=2
>第 1 批需要采集 4 颗第 1 类型果实，需要采集 2 次，耗时为 3\*2=6
>第 2 批需要采集 1 颗第 2 类型果实，需要采集 1 次，耗时为 2\*1=2
>返回总耗时 2+6+2=10

**示例 2：**
>输入：`time = [1], fruits = [[0,3],[0,5]], limit = 2`
>
>输出：`5`
>
>解释：
>由于单次最多采集 2 颗
>第 0 批需要采集 3 颗第 0 类型果实，需要采集 2 次，耗时为 1\*2=2
>第 1 批需要采集 5 颗第 0 类型果实，需要采集 3 次，耗时为 1\*3=3
>需按照顺序依次采集，返回 2+3=5

**提示：**
- `1 <= time.length <= 100`
- `1 <= time[i] <= 100`
- `1 <= fruits.length <= 10^3`
- `0 <= fruits[i][0] < time.length`
- `1 <= fruits[i][1] < 10^3`
- `1 <= limit <= 100`

## 难度

Easy

## 标签

- 数组

## 示例

```
[2,3,2]
[[0,2],[1,4],[2,1]]
3
[1]
[[0,3],[0,5]]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getMinimumTime(vector<int>& time, vector<vector<int>>& fruits, int limit) {

    }
};
```

### Java

```java
class Solution {
    public int getMinimumTime(int[] time, int[][] fruits, int limit) {

    }
}
```

### Python

```python
class Solution(object):
    def getMinimumTime(self, time, fruits, limit):
        """
        :type time: List[int]
        :type fruits: List[List[int]]
        :type limit: int
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:
```

### C

```c


int getMinimumTime(int* time, int timeSize, int** fruits, int fruitsSize, int* fruitsColSize, int limit){

}
```

### C#

```csharp
public class Solution {
    public int GetMinimumTime(int[] time, int[][] fruits, int limit) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number[][]} fruits
 * @param {number} limit
 * @return {number}
 */
var getMinimumTime = function(time, fruits, limit) {

};
```

### TypeScript

```typescript
function getMinimumTime(time: number[], fruits: number[][], limit: number): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer[][] $fruits
     * @param Integer $limit
     * @return Integer
     */
    function getMinimumTime($time, $fruits, $limit) {

    }
}
```

### Swift

```swift
class Solution {
    func getMinimumTime(_ time: [Int], _ fruits: [[Int]], _ limit: Int) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getMinimumTime(time: IntArray, fruits: Array<IntArray>, limit: Int): Int {

    }
}
```

### Go

```golang
func getMinimumTime(time []int, fruits [][]int, limit int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} time
# @param {Integer[][]} fruits
# @param {Integer} limit
# @return {Integer}
def get_minimum_time(time, fruits, limit)

end
```

### Scala

```scala
object Solution {
    def getMinimumTime(time: Array[Int], fruits: Array[Array[Int]], limit: Int): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_minimum_time(time: Vec<i32>, fruits: Vec<Vec<i32>>, limit: i32) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (get-minimum-time time fruits limit)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) exact-integer? exact-integer?)

  )
```

### Erlang

```erlang
-spec get_minimum_time(Time :: [integer()], Fruits :: [[integer()]], Limit :: integer()) -> integer().
get_minimum_time(Time, Fruits, Limit) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_minimum_time(time :: [integer], fruits :: [[integer]], limit :: integer) :: integer
  def get_minimum_time(time, fruits, limit) do

  end
end
```

