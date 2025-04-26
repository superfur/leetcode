# LCP 53. 守护太空城

## 题目描述

各位勇者请注意，力扣太空城发布陨石雨红色预警。

太空城中的一些舱室将要受到陨石雨的冲击，这些舱室按照编号 `0 ~ N` 的顺序依次排列。为了阻挡陨石损毁舱室，太空城可以使用能量展开防护屏障，具体消耗如下：

- 选择一个舱室开启屏障，能量消耗为 `2` 
- 选择相邻两个舱室开启联合屏障，能量消耗为 `3`
- 对于已开启的**一个**屏障，**多维持一时刻**，能量消耗为 `1`

已知陨石雨的影响范围和到达时刻，`time[i]` 和 `position[i]` 分别表示该陨石的到达时刻和冲击位置。请返回太空舱能够守护所有舱室所需要的最少能量。

**注意：** 
- 同一时间，一个舱室不能被多个屏障覆盖
- 陨石雨仅在到达时刻对冲击位置处的舱室有影响


**示例 1：**
>输入：`time = [1,2,1], position = [6,3,3]`
>
>输出：`5`
>
>解释：
> 时刻 1，分别开启编号 3、6 舱室的屏障，能量消耗 2*2 = 4
> 时刻 2，维持编号 3 舱室的屏障，能量消耗 1
> 因此，最少需要能量 5

**示例 2：**
>输入：`time = [1,1,1,2,2,3,5], position = [1,2,3,1,2,1,3]`
>
>输出：`9`
>
>解释：
> 时刻 1，开启编号 1、2 舱室的联合屏障，能量消耗 3
> 时刻 1，开启编号 3 舱室的屏障，能量消耗 2
> 时刻 2，维持编号 1、2 舱室的联合屏障，能量消耗 1
> 时刻 3，维持编号 1、2 舱室的联合屏障，能量消耗 1
> 时刻 5，重新开启编号 3 舱室的联合屏障，能量消耗 2
> 因此，最少需要能量 9

**提示：**
+ `1 <= time.length == position.length <= 500`
+ `1 <= time[i] <= 5`
+ `0 <= position[i] <= 100`


## 难度

Hard

## 标签

- 位运算
- 数组
- 动态规划
- 状态压缩

## 示例

```
[1,2,1]
[6,3,3]
[1,1,1,2,2,3,5]
[1,2,3,1,2,1,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int defendSpaceCity(vector<int>& time, vector<int>& position) {

    }
};
```

### Java

```java
class Solution {
    public int defendSpaceCity(int[] time, int[] position) {

    }
}
```

### Python

```python
class Solution(object):
    def defendSpaceCity(self, time, position):
        """
        :type time: List[int]
        :type position: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def defendSpaceCity(self, time: List[int], position: List[int]) -> int:
```

### C

```c


int defendSpaceCity(int* time, int timeSize, int* position, int positionSize){

}
```

### C#

```csharp
public class Solution {
    public int DefendSpaceCity(int[] time, int[] position) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number[]} position
 * @return {number}
 */
var defendSpaceCity = function(time, position) {

};
```

### TypeScript

```typescript
function defendSpaceCity(time: number[], position: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer[] $position
     * @return Integer
     */
    function defendSpaceCity($time, $position) {

    }
}
```

### Swift

```swift
class Solution {
    func defendSpaceCity(_ time: [Int], _ position: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun defendSpaceCity(time: IntArray, position: IntArray): Int {

    }
}
```

### Go

```golang
func defendSpaceCity(time []int, position []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} time
# @param {Integer[]} position
# @return {Integer}
def defend_space_city(time, position)

end
```

### Scala

```scala
object Solution {
    def defendSpaceCity(time: Array[Int], position: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn defend_space_city(time: Vec<i32>, position: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (defend-space-city time position)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

### Erlang

```erlang
-spec defend_space_city(Time :: [integer()], Position :: [integer()]) -> integer().
defend_space_city(Time, Position) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec defend_space_city(time :: [integer], position :: [integer]) :: integer
  def defend_space_city(time, position) do

  end
end
```

