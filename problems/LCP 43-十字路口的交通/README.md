# LCP 43. 十字路口的交通

## 题目描述

前往「力扣挑战赛」场馆的道路上，有一个拥堵的十字路口，该十字路口由两条双向两车道的路交叉构成。由于信号灯故障，交警需要手动指挥拥堵车辆。假定路口没有新的来车且一辆车从一个车道驶入另一个车道所需的时间恰好为一秒钟，长度为 4 的一维字符串数组 `directions` 中按照 **东、南、西、北** 顺序记录了四个方向从最靠近路口到最远离路口的车辆计划开往的方向。其中：
- `"E"` 表示向东行驶；
- `"S"` 表示向南行驶；
- `"W"` 表示向西行驶；
- `"N"` 表示向北行驶。

交警每秒钟只能指挥各个车道距离路口最近的一辆车，且每次指挥需要满足如下规则：
- 同一秒钟内，一个方向的车道只允许驶出一辆车；
- 同一秒钟内，一个方向的车道只允许驶入一辆车；
- 同一秒钟内，车辆的行驶路线不可相交。

请返回最少需要几秒钟，该十字路口等候的车辆才能全部走完。

各个车道驶出的车辆可能的行驶路线如图所示：


![图片.png](https://pic.leetcode-cn.com/1630393755-gyPeMM-%E5%9B%BE%E7%89%87.png){:height="350px"}

**注意：**
- 测试数据保证不会出现掉头行驶指令，即某一方向的行驶车辆计划开往的方向不会是当前车辆所在的车道的方向;
- 表示堵塞车辆行驶方向的字符串仅用大写字母 `"E"`，`"N"`，`"W"`，`"S"` 表示。

**示例 1：**
>输入：`directions = ["W","N","ES","W"]`
>
>输出：`2`
>
>解释：
>第 1 秒：东西方向排在最前的车先行，剩余车辆状态 `["","N","S","W"]`；
>第 2 秒：南、西、北方向的车行驶，路口无等待车辆；
>因此最少需要 2 秒，返回 2。

**示例 2：**
>输入：`directions = ["NS","WE","SE","EW"]`
>
>输出：`3`
>
>解释：
>第 1 秒：四个方向排在最前的车均可驶出；
>第 2 秒：东南方向的车驶出，剩余车辆状态 `["","","E","W"]`；
>第 3 秒：西北方向的车驶出。


**提示：**
- `directions.length = 4`
- `0 <= directions[i].length <= 20`


## 难度

Hard

## 标签

- 数组
- 字符串
- 动态规划

## 示例

```
["W","N","ES","W"]
["NS","WE","SE","EW"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int trafficCommand(vector<string>& directions) {

    }
};
```

### Java

```java
class Solution {
    public int trafficCommand(String[] directions) {

    }
}
```

### Python

```python
class Solution(object):
    def trafficCommand(self, directions):
        """
        :type directions: List[str]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def trafficCommand(self, directions: List[str]) -> int:
```

### C

```c


int trafficCommand(char** directions, int directionsSize){

}
```

### C#

```csharp
public class Solution {
    public int TrafficCommand(string[] directions) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} directions
 * @return {number}
 */
var trafficCommand = function(directions) {

};
```

### TypeScript

```typescript
function trafficCommand(directions: string[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $directions
     * @return Integer
     */
    function trafficCommand($directions) {

    }
}
```

### Swift

```swift
class Solution {
    func trafficCommand(_ directions: [String]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun trafficCommand(directions: Array<String>): Int {

    }
}
```

### Go

```golang
func trafficCommand(directions []string) int {

}
```

### Ruby

```ruby
# @param {String[]} directions
# @return {Integer}
def traffic_command(directions)

end
```

### Scala

```scala
object Solution {
    def trafficCommand(directions: Array[String]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn traffic_command(directions: Vec<String>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (traffic-command directions)
  (-> (listof string?) exact-integer?)

  )
```

### Erlang

```erlang
-spec traffic_command(Directions :: [unicode:unicode_binary()]) -> integer().
traffic_command(Directions) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec traffic_command(directions :: [String.t]) :: integer
  def traffic_command(directions) do

  end
end
```

